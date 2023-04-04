import streamlit as st
import pandas as pd
import urllib.request
import json
import folium
import streamlit_folium as st_folium
import requests
import streamlit_js_eval

st.set_page_config(
    page_title="Quake It Off - Recommended Evacuation Routes",
    page_icon='🌍'
)
st.header("Recommended Evacuation Routes")
st.markdown("Connected with TrueWay Directions to provide fast and safe routes for evacuation")

location = streamlit_js_eval.get_geolocation()
global ulatitude
global ulongitude
if st.button("Refresh Location/Prediction", key="refresh_location_button"):
        #streamlit_js_eval.get_geolocation()
        try:
            ulatitude = float(location['coords']['latitude'])
            ulongitude = float(location['coords']['longitude'])
        except:
            st.warning("Loading")
try:
    ulatitude = float(location['coords']['latitude'])
    ulongitude = float(location['coords']['longitude'])
except:
    st.warning("Loading")
print(ulatitude, ulongitude)

if st.button("Refresh Location"):
    ulatitude = float(location['coords']['latitude'])
    ulongitude = float(location['coords']['longitude'])

st.write("Click a point on the map where you want to evacuate. A blue line will be drawn, showing you the most convenient route possible. Stay clear of earthquakes highlighted with pointers! 📌🗺️")
st.write("When you click on the point, a second map will be generated below. That is where the route will be visible.")
st.write("If you want to choose another point, just refresh the page and go again!")
odf = pd.DataFrame({
                    'latitude':[],
                    'longitude' :[],
                    'placeName':[],
                    'magnitude':[],
                    'depth':[]
                    })
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
response = urllib.request.urlopen(url)
data = json.loads(response.read())
features = data["features"]
for feature in features:
    place = feature["properties"]["place"]
    lat = feature["geometry"]["coordinates"][1]
    lon = feature["geometry"]["coordinates"][0]
    mag = feature["properties"]["mag"]
    depth = feature["geometry"]["coordinates"][2]
    depth = abs(depth)
    newrow = [lat, lon, place, mag, depth]
    odf.loc[len(odf.index)] = newrow
#print(odf)

m = folium.Map(location = (ulatitude, ulongitude), zoom_start = 10)
yi = folium.Icon(icon = 'star', prefix='fa', color='darkpurple', icon_color='#00FFFF', border_color='#FFFFFF')

folium.Marker(
    (ulatitude, ulongitude),
    popup = "Latitude: "+str(ulatitude)+" Longitude: "+str(ulongitude),
    tooltip = "Your location",
    icon = yi
).add_to(m)
#st_folium(m, width = 725)#, height = 725)

oi = folium.Icon(icon = 'circle', prefix = 'fa', color='orange', icon_color='red')
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"

for lats, lons, plcs, in zip(odf['latitude'].values.tolist(), odf['longitude'].values.tolist(), odf['placeName'].values.tolist()):
    #print(lats, lons, plcs)
    folium.Marker(
        location= (lats, lons),
        popup="Latitude: "+str(lats)+" Longitude: "+str(lons),
        tooltip=plcs,
        #icon=oi
    ).add_to(m)
#st_folium.st_folium(m, width = 725, height = 1000)
def get_pos(lat,lng):
    return lat,lng
m.add_child(folium.LatLngPopup())
#mapcomp = st.empty()
#with mapcomp:
mappp = st_folium.st_folium(m, height=725, width=725)
try:
    data = get_pos(mappp['last_clicked']['lat'],mappp['last_clicked']['lng'])
except:
    st.error("Please click the place you want to evacuate to on the map.")
    st.stop()

#if data is not None:
#    st.write(data)
folium.Marker(
    location = data,
    popup = "Latitude: "+str(data[0])+" Longitude: "+str(data[1])
).add_to(m)

apiurl = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"
urlparams = (str((str(ulatitude)+','+str(ulongitude))))+';'+str(data)[1:-1]
#print(urlparams)
querystring = {"stops":urlparams,"optimize":"true","avoid_ferries":"true","avoid_tolls":"true"}

headers = {
	"X-RapidAPI-Key": "55588fff42msh38648ac92f61898p1bc6a2jsnea83869aa07a",
	"X-RapidAPI-Host": "trueway-directions2.p.rapidapi.com"
}

response = requests.request("GET", apiurl, headers=headers, params=querystring)
#print(response.text)
datatouse = json.loads(response.text)
route = datatouse["route"]
#steps = route["legs"][0]["steps"]

# Create Folium map centered on start location
start_coords = (ulatitude, ulongitude)
route_coordinates = []
#print(route['geometry'])
route_coordinates.append([ulatitude, ulongitude])
for item in route['geometry']['coordinates']:
    route_coordinates.append(item)
    #print(item)
route_coordinates.append(data)
# Add a PolyLine to the map

m.add_child(folium.PolyLine(
    locations=route_coordinates,
    color='blue',
    weight=5,
    opacity=1
))
mappp = st_folium.st_folium(m, height=725, width=725)