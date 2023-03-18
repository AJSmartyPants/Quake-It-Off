import streamlit as st
import geocoder
import pandas as pd
import plotly.express as px
import urllib.request

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

st.subheader("Current earthquakes near you:")

global fig
eqmap = st.radio("Do you want to see a map of recent earthquakes, or choose a range of years? ", ("Recent Earthquakes", "Choose the Range"))
mapview = st.radio("Select the view of the map you would like to see: ", ("2D", "3D"))

def getcoords(url):
    response = urllib.request.urlopen(url)
    data = pd.read_json(response)
    data['depth'] = data['geometry'].apply(lambda x: abs(x['coordinates'][2]))
    data['place'] = data['properties']['place']
    data = data[['place', 'geometry', 'properties', 'depth']]
    data[['latitude', 'longitude']] = pd.DataFrame(data['geometry'].tolist(), index=data.index)
    data = data[['latitude', 'longitude', 'place', 'properties', 'depth']]
    data = data.rename(columns={'properties': 'properties', 'depth': 'magnitude'})
    return data

if (eqmap == "Recent Earthquakes"):
    roptions = ['Past hour', 'Past day', 'Past week', 'Past month']
    rrange = st.select_slider("Do you want to see earthquakes in the past hour, day, week, or month?", options = roptions, value = 'Past day')
    if(rrange == 'Past hour'):
        url = 'https
