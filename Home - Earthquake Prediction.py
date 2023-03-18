# import module
import streamlit as st
import geocoder
import pandas as pd
import pickle
import numpy as np
import time
#from streamlit_folium import st_folium
#import folium
import json
import urllib.request
#import requests
#import plotly.graph_objects as go
from array import *
#from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration, VideoProcessorBase

st.set_page_config(
    page_title="Quake It Off - Home",
    page_icon='🌎'
)

st.sidebar.subheader("Select page above")
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
country = g.country
print(country)
print(latitude, longitude)
if st.button("Refresh Location"):
    latitude = g.latlng[0]
    longitude = g.latlng[1]
    print(latitude, longitude)
    print(time.time())
ydf = pd.DataFrame({'LATITUDE': [latitude], 'LONGITUDE': [longitude]})

model = pickle.load(open("EQPModel.pkl", 'rb'))
print(time.time())
inputx = np.reshape([latitude, longitude, time.time()], (1, -1))
predictions = model.predict(inputx)
preds = pd.DataFrame(predictions, columns=['Depth', 'Magnitude'], index = None)
print(predictions, preds)

st.subheader("Current predictions:")
eqpdepth = preds.iloc[0]['Depth']
eqpmag = round(preds.iloc[0]['Magnitude'], 1)
if(g.country == 'IN' or 'QA' or 'SA' or 'AD' or 'SE' or 'NO' or 'FI' or 'MT' or 'BB'):
    st.success("Low chance of earthquake happening at your location at the current time. If one does occur, here is the prediction: ")
st.write("Depth: ",str(eqpdepth))
st.write("Magnitude: ",str(eqpmag))
if(eqpmag<=2):
    st.success("Low chance of feeling the earthquake, or of the earthquake happening.")
    st.info("Earthquake type: Minor/Light")
elif(eqpmag<5 and eqpmag>2):
    st.warning("Medium chance of feeling the earthquake, or of the earthquake happening at your location.")
    st.info("Earthquake type: Light/Moderate")
else:
    st.error("If the predicted earthquake occurs, high chance of you feeling it. Be safe and prepared!")
    st.info("Earthquake type: Strong/Major/Great")


st.subheader("Current earthquakes near you:")

import plotly.express as px
global df
global fig
global fmap
eqmap = st.radio("Do you want to see a map of recent earthquakes, or choose a range of years? ", ("Recent Earthquakes", "Choose the Range"))
mapview = st.radio("Select the view of the map you would like to see: ", ("2D", "3D"))

def getcoords(url, odf):
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    features = data["features"]
    #geometry = data["geometry"]
    for feature in features:
        place = feature["properties"]["place"]
        lat = feature["geometry"]["coordinates"][1]
        lon = feature["geometry"]["coordinates"][0]
        mag = feature["properties"]["mag"]
        depth = feature["geometry"]["coordinates"][2]
        depth = abs(depth)
        #print("Place: ", place)
        #print("Latitude: ", latitude)
        #print("Longitude: ", longitude)
        #print("Magnitude: ", mag)
        #print("Depth: ", depth)
        newrow = [lat, lon, place, mag, depth]
        odf.loc[len(odf.index)] = newrow
    global fig
    fig = px.scatter_geo(odf,
                    lat='Latitude',
                    lon='Longitude',
                    color='Magnitude',
                    size='Depth',
                    hover_name='PlaceName')#,
                    #size_max=30, size_min=5)
    
    fig.add_scattergeo(lat=[latitude], lon=[longitude], hovertext="Your Location", name="Your Location", marker=dict(color='black'), showlegend=False)
    #fig.update_layout(geo=dict(lataxis=dict(range=[-90, 90]), lonaxis=dict(range=[-180, 180])))
    fig.update_geos(
        showcountries=True, 
        bgcolor="#ece6ff",
        #mode='lines+markers+text',
        #center_lat=latitude,
        #center_lon=longitude,
        coastlinewidth=0.3,
        countrywidth=0.4,
        showsubunits=True,
        subunitcolor="#160152",
        subunitwidth=0.3,
        #projection_scale=14,
        showcoastlines=True, coastlinecolor="RebeccaPurple",
        showland=True, landcolor="LightGreen",
        showocean=True, oceancolor="Blue",
        showlakes=True, lakecolor="LightBlue",
        showrivers=True, rivercolor="LightBlue")

#data = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/silver.csv")
#data['date']= pd.to_datetime(data['date'])
#data['year']=data['date'].dt.year
#data = data.drop(['date'], axis = 1)

if (eqmap == "Recent Earthquakes"):
    roptions = ['Past hour', 'Past day', 'Past week', 'Past month']
    rrange = st.select_slider("Do you want to see earthquakes in the past hour, day, week, or month?", options = roptions, value = 'Past day')
    if(rrange == 'Past hour'):
        odf = pd.DataFrame({
                            'Latitude':[],
                            'Longitude' :[],
                            'PlaceName':[],
                            'Magnitude':[],
                            'Depth':[]
                            })
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
        getcoords(url, odf)
        if(mapview == '2D'):
            fig.update_geos(projection_scale = 4, center_lat = latitude, center_lon = longitude)
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
        elif(mapview == '3D'):
            fig.update_geos(
                projection_type="orthographic", 
                projection_scale=4,
                projection_rotation=dict(
                    lon=longitude,
                    lat=latitude,
                    roll=0
                ))
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
    elif(rrange == 'Past day'):
        odf = pd.DataFrame({
                            'Latitude':[],
                            'Longitude' :[],
                            'PlaceName':[],
                            'Magnitude':[],
                            'Depth':[]
                            })
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
        getcoords(url, odf)
        if(mapview == '2D'):
            fig.update_geos(projection_scale = 4, center_lat = latitude, center_lon = longitude)
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
        elif(mapview == '3D'):
            fig.update_geos(
                projection_type="orthographic", 
                projection_scale=4,
                projection_rotation=dict(
                    lon=longitude,
                    lat=latitude,
                    roll=0
                ))
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
    elif(rrange == 'Past week'):
        odf = pd.DataFrame({
                            'Latitude':[],
                            'Longitude' :[],
                            'PlaceName':[],
                            'Magnitude':[],
                            'Depth':[]
                            })
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
        getcoords(url, odf)
        if(mapview == '2D'):
            fig.update_geos(projection_scale = 4, center_lat = latitude, center_lon = longitude)
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
        elif(mapview == '3D'):
            fig.update_geos(
                projection_type="orthographic", 
                projection_scale=4,
                projection_rotation=dict(
                    lon=longitude,
                    lat=latitude,
                    roll=0
                ))
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
    else:
        odf = pd.DataFrame({
                            'Latitude':[],
                            'Longitude' :[],
                            'PlaceName':[],
                            'Magnitude':[],
                            'Depth':[]
                            })
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
        getcoords(url, odf)
        if(mapview == '2D'):
            fig.update_geos(projection_scale = 4, center_lat = latitude, center_lon = longitude)
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
        elif(mapview == '3D'):
            fig.update_geos(
                projection_type="orthographic", 
                projection_scale=4,
                projection_rotation=dict(
                    lon=longitude,
                    lat=latitude,
                    roll=0
                ))
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
data = pd.read_csv("https://data.humdata.org/dataset/4881d82b-ba63-4515-b748-c364f3d05b42/resource/10ac8776-5141-494b-b3cd-bf7764b2f964/download/earthquakes1970-2014.csv")
#data = data[:1000000]
data['DateTime']= pd.to_datetime(data['DateTime'])
data['year']=data['DateTime'].dt.year
#def placename(lat, lon):
#    location = geocoder.reverse((latitude, longitude))
#    return location
#data['place'] = data.apply(lambda row: placename(row['latitude'], row['longitude']), axis=1)
#print(data.head(10))
print(data.shape)

def cusmap(minyear, maxyear):
    df = data[(data['year'] >= minyear) & (data['year'] <= maxyear)]
    #print(df.head(10))
    #lons = df["longitude"].tolist()
    #lats = df["latitude"].tolist()
    global fig
    fig = px.scatter_geo(df,
                    lat='Latitude',
                    lon='Longitude',
                    color='Magnitude',
                    size='Depth',
                    hover_name='year')#,
                    #size_max=30, size_min=5)
    
    fig.add_scattergeo(lat=[latitude], lon=[longitude], hovertext="Your Location", name="Your Location", marker=dict(color='black'), showlegend=False)
    #fig.update_layout(geo=dict(lataxis=dict(range=[-90, 90]), lonaxis=dict(range=[-180, 180])))
    fig.update_geos(
        showcountries=True, 
        bgcolor="#ece6ff",
        #mode='lines+markers+text',
        #center_lat=latitude,
        #center_lon=longitude,
        coastlinewidth=0.3,
        countrywidth=0.4,
        showsubunits=True,
        subunitcolor="#160152",
        subunitwidth=0.3,
        #projection_scale=14,
        showcoastlines=True, coastlinecolor="RebeccaPurple",
        showland=True, landcolor="LightGreen",
        showocean=True, oceancolor="Blue",
        showlakes=True, lakecolor="LightBlue",
        showrivers=True, rivercolor="LightBlue")

if (eqmap == "Choose the Range"):
    yrange = st.slider("Choose which time period of earthquakes you want to see", min_value = 1970, max_value = 2016, value=(1973, 1985))
    cusmap(yrange[0], yrange[1])
    if(mapview == '2D'):
            fig.update_geos(projection_scale = 4, center_lat = latitude, center_lon = longitude)
            fmap = st.plotly_chart(fig, theme=None, use_container_width=True)
    elif(mapview == '3D'):
        fig.update_geos(
            projection_type="orthographic", 
            projection_scale=4,
            projection_rotation=dict(
            lon=longitude,
            lat=latitude,
            roll=0
            ))
        fmap = st.plotly_chart(fig, theme=None, use_container_width=True)

#hide_table_row_index = """
#            <style>
#            thead tr th:first-child {display:none}
#            tbody th {display:none}
#            </style>
#           """
#st.markdown(hide_table_row_index, unsafe_allow_html=True)
#st.write("Current predictions:")#, index = False)
#st.table(preds)

#df=data[data['year']==1973]
#df.head()






#m = folium.Map(location = ydf, zoom_start = 3)
#yi = folium.Icon(icon = 'star', prefix='fa', color='darkpurple', icon_color='#00FFFF', border_color='#FFFFFF')

#folium.Marker(
#    ydf,
#    popup = "Latitude: "+str(latitude)+" Longitude: "+str(longitude),
#    tooltip = "This is you",
#    icon = yi
#).add_to(m)
##st_folium(m, width = 725)#, height = 725)

#oi = folium.Icon(icon = 'circle', prefix = 'fa', color='orange', icon_color='red')
#url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"

#odf = pd.DataFrame({
#                    'Latitude':[],
#                    'Longitude' :[],
#                    'PlaceName':[]
#                    })
#print(odf)
#response = urllib.request.urlopen(url)
#data = json.loads(response.read())
#features = data["features"]
#for feature in features:
#    place = feature["properties"]["place"]
#    lat = feature["geometry"]["coordinates"][1]
#    lon = feature["geometry"]["coordinates"][0]
#    #print("Place: ", place)
#    #print("Latitude: ", latitude)
#    #print("Longitude: ", longitude)
#    newrow = [lat, lon, place]
#    odf.loc[len(odf.index)] = newrow

#for lats, lons, plcs, in zip(odf['Latitude'].values.tolist(), odf['Longitude'].values.tolist(), odf['PlaceName'].values.tolist()):
    #print(lats, lons, plcs)
#    folium.Marker(
#        location= (lats, lons),
#        popup="Latitude: "+str(lats)+" Longitude: "+str(lons),
#        tooltip=plcs,
#        #icon=oi
#    ).add_to(m)

#url2 = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset=significant-earthquake-database&q=&rows=10000&facet=country&facet=state&facet=location_name&facet=region_code&facet=deaths_description&facet=missing_description&facet=injuries_description&facet=damage_description&facet=houses_destroyed_description&facet=houses_damaged_description&facet=total_deaths_description&facet=total_missing_description&facet=total_injuries_description&facet=total_damage_description&facet=total_houses_destroyed_description")
#u2d = url2.json()
#countries = [record["fields"]["country"] for record in u2d["records"]]
#ctydf = pd.DataFrame(countries, columns=["Country"])
#counts = ctydf["Country"].value_counts().reset_index()
#counts.columns = ["Country", "Count"]
#print(ctydf)
#print(counts)
#cgj = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"
#folium.Choropleth(
#    geo_data = cgj,
#    data=counts,
#    columns=["Country", "Count"],
#    key_on="feature.properties.name",
#    fill_color="YlGn",
#    fill_opacity=0.7,
#    line_opacity=.1,
#    legend_name="Frequency of Large-Scale Earthquakes"
#).add_to(m)
#m.drawmapboundary()
#m.drawcountries()
#st_folium(m, width = 725, height = 1000)