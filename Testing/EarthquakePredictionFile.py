# import module
import streamlit as st
import geocoder
import pandas as pd
import pickle
import numpy as np
import time
from streamlit_folium import st_folium
import folium
import json
import urllib.request
import requests
from array import *

# display the latitude and longitude
# Title
st.title("Live and Future Predictions")
# Header
#st.header("Welcome to the Info Hub!")
#def header(url):
#st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;src: url(https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap);font-family: Oswald, sans-serif;">{"Welcome to the Info Hub!"}</p>', unsafe_allow_html=True)
#blue["You may have to scroll down to see the information"])#, '#AA00FF')#["You may have to scroll down to see the information."])
# Subheader
st.subheader("View the current earthquakes happening (or recently happened) across the world and near you. See the current and future prediction of any earthquake that might occur near where you are.")
st.markdown("We use your location for prediction, so if this feature is not working, please enable access to location. Your data is safe and deleted when unrequired, so don't worry!")
st.markdown("You may have to scroll down to see all the information.")

location_div = st.empty()
location_div.markdown("<div id='location'></div>", unsafe_allow_html=True)
latitude = ''
longitude = ''
g = geocoder.ip('me')
latitude = g.latlng[0]
longitude = g.latlng[1]
print(latitude, longitude)
if st.button("Refresh Location"):
    latitude = g.latlng[0]
    longitude = g.latlng[1]
    print(latitude, longitude)
    print(time.time())
ydf = pd.DataFrame({'LATITUDE': [latitude], 'LONGITUDE': [longitude]})

model = pickle.load(open('REGModel2.pkl', 'rb'))
print(time.time())
inputx = np.reshape([latitude, longitude, time.time()], (1, -1))
predictions = model.predict(inputx)
preds = pd.DataFrame(predictions, columns=['Depth', 'Magnitude'], index = None)
print(predictions, preds)

st.subheader("Current predictions:")
st.write("Depth: ",str(preds.iloc[0]['Depth']))
st.write("Magnitude: ",str(round(preds.iloc[0]['Magnitude']/10, 1)))
#hide_table_row_index = """
#            <style>
#            thead tr th:first-child {display:none}
#            tbody th {display:none}
#            </style>
#           """
#st.markdown(hide_table_row_index, unsafe_allow_html=True)
#st.write("Current predictions:")#, index = False)
#st.table(preds)
st.subheader("Current earthquakes near you:")
m = folium.Map(location = ydf, zoom_start = 3)
yi = folium.Icon(icon = 'star', prefix='fa', color='darkpurple', icon_color='#00FFFF', border_color='#FFFFFF')

folium.Marker(
    ydf,
    popup = "Latitude: "+str(latitude)+" Longitude: "+str(longitude),
    tooltip = "This is you",
    icon = yi
).add_to(m)
#st_folium(m, width = 725)#, height = 725)

oi = folium.Icon(icon = 'circle', prefix = 'fa', color='orange', icon_color='red')
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"

odf = pd.DataFrame({
                    'Latitude':[],
                    'Longitude' :[],
                    'PlaceName':[]
                    })
#print(odf)
response = urllib.request.urlopen(url)
data = json.loads(response.read())
features = data["features"]
for feature in features:
    place = feature["properties"]["place"]
    lat = feature["geometry"]["coordinates"][1]
    lon = feature["geometry"]["coordinates"][0]
    #print("Place: ", place)
    #print("Latitude: ", latitude)
    #print("Longitude: ", longitude)
    newrow = [lat, lon, place]
    odf.loc[len(odf.index)] = newrow

for lats, lons, plcs, in zip(odf['Latitude'].values.tolist(), odf['Longitude'].values.tolist(), odf['PlaceName'].values.tolist()):
    #print(lats, lons, plcs)
    folium.Marker(
        location= (lats, lons),
        popup="Latitude: "+str(lats)+" Longitude: "+str(lons),
        tooltip=plcs,
        #icon=oi
    ).add_to(m)

url2 = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset=significant-earthquake-database&q=&rows=10000&facet=country&facet=state&facet=location_name&facet=region_code&facet=deaths_description&facet=missing_description&facet=injuries_description&facet=damage_description&facet=houses_destroyed_description&facet=houses_damaged_description&facet=total_deaths_description&facet=total_missing_description&facet=total_injuries_description&facet=total_damage_description&facet=total_houses_destroyed_description")
u2d = url2.json()
countries = [record["fields"]["country"] for record in u2d["records"]]
ctydf = pd.DataFrame(countries, columns=["Country"])
counts = ctydf["Country"].value_counts().reset_index()
counts.columns = ["Country", "Count"]
#print(ctydf)
#print(counts)
cgj = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"
folium.Choropleth(
    geo_data = cgj,
    data=counts,
    columns=["Country", "Count"],
    key_on="feature.properties.name",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Frequency of Large-Scale Earthquakes"
).add_to(m)

st_folium(m, width = 725, height = 1000)