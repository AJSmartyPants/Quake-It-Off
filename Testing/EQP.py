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

model = pickle.load(open('REGModel.pkl', 'rb'))
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
#print(odf)
#print((odf['Latitude'], odf['Longitude']))
#print('fromheritstatts')
#print(odf['Latitude'])
#print(odf['Longitude'])
#print(odf['Latitude', 'Longitude'])
#print(odf['Latitude'], odf['Longitude'])
#print(odf['Latitude'].values)
#print(odf['Longitude'].values)
#print(odf['Latitude'].values, odf['Longitude'].values)
#print(odf['Latitude'].values.tolist())
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
#st.map(data=ydf, zoom=None, use_container_width=True, color='red')
























minfo = st.selectbox("Please choose what you would like to learn about: ",
['None selected','Earthquakes', 'Hurricanes', 'Spotting Natural Disasters', 'Safety Tips', 'Relevant First Aid'], index = 0)

if(minfo == 'Earthquakes'):
    #print('Earthquakes chosen')
    eqbns = st.radio("What subtopic do you want to learn about?", ('Responding to Earthquakes', 'Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen', 'Terminology'))
    st.success(eqbns)

    if(eqbns == 'Responding to Earthquakes'):
        st.subheader("What to Do Before an Earthquake")
        st.info("\
                \n• Make sure you have a fire extinguisher, first aid kit, a battery-powered radio, a flashlight, and extra batteries at home.\
                \n• Learn first aid.\
                \n• Learn how to turn off the gas, water, and electricity.\
                \n• Make up a plan of where to meet your family after an earthquake.\
                \n• Don't leave heavy objects on shelves (they'll fall during a quake).\
                \n• Anchor heavy furniture, cupboards, and appliances to the walls or floor.\
                \n• Learn the earthquake plan at your school or workplace.\
                \n• Identify earthquake-safe places in your home that have furniture to protect you, have less glass or less heavy objects on shelves, and don't have other dangerous objects.\
                \n• Keep closed-toe shoes in an accessible location at your home.\
                \n• Organize disaster supplies.\
                \n• Minimize financial hardships by ensuring objects are in safe locations.\
                Keep in mind that a few of these tips are specifically for earthquake-prone regions. If you live somewhere where earthquakes don't happen very frequently, just be sure to have knowledge about earthquakes and be prepared.")
        st.subheader("What to Do During an Earthquake")
        st.info("\
                \n• Stay calm! If you're indoors, stay inside. If you're outside, stay outside.\
                \n• If you're indoors, stand against a wall near the center of the building, stand in a doorway, or crawl under heavy furniture (a desk or table). Stay away from windows and outside doors.\
                \n• If you're outdoors, stay in the open away from power lines or anything that might fall. Stay away from buildings (stuff might fall off the building or the building could fall on you).\
                \n• Don't use matches, candles, or any flame. Broken gas lines and fire don't mix.\
                \n• If you're in a car, stop the car and stay inside the car until the earthquake stops. Make sure your car is away from anything that might fall on top of it.\
                \n• Don't use elevators (they may shut down).")
        st.subheader("What to Do After an Earthquake")
        st.info("\
            \n• Check yourself and others for injuries. Provide first aid for anyone who needs it.\
            \n• Check water, gas, and electric lines for damage. If any are damaged, shut off the valves. Check for the smell of gas. If you smell it, open all the windows and doors, leave immediately, and report it to the authorities (use someone else's phone).\
            \n• Turn on the radio. Don't use the phone unless it's an emergency.\
            \n• Stay out of damaged buildings.\
            \n• Be careful around broken glass and debris. Wear boots or sturdy shoes to keep from cutting your feet.\
            \n• Be careful of chimneys (they may fall on you).\
            \n• Stay away from beaches. Tsunamis and seiches sometimes hit after the ground has stopped shaking.\
            \n• Stay away from damaged areas.\
            \n• If you're at school or work, follow the emergency plan or the instructions of the person in charge.\
            \n• Expect aftershocks.")
    elif(eqbns == 'Predicting Earthquakes'):
        st.subheader("Can you predict an earthquake?")
        st.info("No. We have never really predicted a major earthquake. We do not know how, and we do not expect to know how any time soon. We can only calculate the probability that a significant earthquake will occur (thanks to hazard mapping) in a specific area within a certain number of years. This application estimates")
    elif(eqbns == 'Why & How Earthquakes Happen'):
        print('hi')

#    elif(eqbns == 'Preventing Earthquakes'):

#    elif(eqbns == 'Where Earthquakes Happen'):

#    elif(eqbns == 'When Earthquakes Happen'):

#    elif(eqbns == 'Terminology'):

#elif(minfo == 'Hurricanes'):
    print('Hurricanes chosen')
    hubns = st.radio("What subtopic do you want to learn about?: ", ('Predicting Hurricanes', 'Why & How Hurricanes Happen', 'Preventing Hurricanes', 'Responding to Hurricanes', 'Where Hurricanes Happen', 'When Hurricanes Happen', 'Terminology'))
    st.success(hubns)
#elif(minfo == 'Spotting Natural Disasters'):
    print('Spotting Natural Disasters')
    #sndbns = st.radio("What subtopic do you want to learn about?: ", ('Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Responding to Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen'))
#elif(minfo == 'Safety Tips'):
    print('Safety Tips Selected')
    stbns = st.radio("What safety tips do you want to learn about?: ", ('Earthquake Safety Tips', 'Hurricane Safety Tips'))
    st.success(stbns)
else:
    print('Relevant First Aid chosen')


#try:
# get the latitude and longitude using geocoder

# update the HTML element with the location
#location_div.write("Your location: Latitude: " + str(latitude) + ", Longitude: " + str(longitude))
#except:
#st.write("Error getting location.")

#url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

#headers = {
#	"X-RapidAPI-Key": "55588fff42msh38648ac92f61898p1bc6a2jsnea83869aa07a",
#	"X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
#}

#if st.button("Get Location"):
#    if not st.session_state.get("location_permission"):
#        st.session_state["location_permission"] = st.browser_request_permission(
#        permission_name="geolocation",  # request permission for geolocation
#        fullscreen=False)  # don't show permission dialog in full-screen mode
#        if st.session_state["location_permission"]:
#            try:
#                response = requests.request("GET", url, headers=headers)#, params=navigator.geolocation.getCurrentPosition())
#                st.write("Your location:")
#                st.write(response)
#            except:
#                    st.write("Error getting location.")
#        else:
#            st.write("Location permission denied.")











# success
st.info("Information")
# success
st.warning("Warning")
# success
st.error("Error")
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
# Write text
st.write("Text with write")
# Writing python inbuilt function range()
st.write(range(10))
# Display Images

# import Image from pillow to open images
from PIL import Image
#img = Image.open("https://i.pinimg.com/originals/b4/40/fe/b440fe8b087416820258b711b91ca18a.gif")

# display image using streamlit
# width is used to set the width of an image
st.image("https://i.pinimg.com/originals/b4/40/fe/b440fe8b087416820258b711b91ca18a.gif", width=200)
# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
# display the text if the checkbox returns True value
    st.text("Showing the widget")
# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
    #fabns = st.radio("What subtopic do you want to learn about?: ", ('Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Responding to Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen'))
# print the selected hobby
#st.write("Your hobby is: ", hobby)

# multi select box

# first argument takes the box title
# second argument takes the options to show
#hobbies = st.multiselect("Hobbies: ",
#['Dancing', 'Reading', 'Sports'])

# write the selected options
#st.write("You selected", len(hobbies), 'hobbies')
# Create a simple button that does nothing
#x = st.button("Click me for no reason")
#if(x):
#    print('bruh')
#y = st.button("About")
#z = st.text("")
# Create a button, that when clicked, shows a text
#if(y):
#    z.text("CLIcked")
# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
#name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
#if(st.button('Submit')):
#    result = name.title()
#    st.success(result)