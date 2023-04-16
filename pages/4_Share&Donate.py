import streamlit as st
import folium
import streamlit_folium as stf
import pandas as pd
#import requests, json
import streamlit_js_eval
from PIL import Image
import requests

appicon = Image.open(requests.get("https://github.com/AJSmartyPants/Quake-It-Off/raw/main/Images/QuakeItOffFinalLogo.png", stream=True).raw)
st.set_page_config(
    page_title="Quake It Off - Share & Donate",
    page_icon=appicon
)
col1, col2 = st.columns([1, 1])
col1.title("Share & Donate")
sharex = col2.expander(label='➦\n(Share)')
with sharex:
    sharetext = "PLEASE%20check%20out%20the%20Quake%20It%20Off%20app%20and%20start%20using%20it%20today%21%20https%3A%2F%2Fquakeitoff.streamlit.app%2F%0A%0AI%27m%20sharing%20the%20Share%20%26%20Donate%20page%20of%20the%20app.%20With%20Share%20%26%20Donate%2C%20you%20can%20join%20a%20community%20of%20people%20who%20want%20to%20share%20knowledge%20about%20earthquakes%2C%20spread%20awareness%2C%20warn%20each%20other%2C%20and%20end%20up%20saving%20lives%21%20You%20can%20also%20view%2C%20go%20to%2C%20and%20interact%20with%20the%20sites%20that%20help%20earthquake-affected%20areas.%20These%20sites%20include%20places%20to%20donate%2C%20volunteer%2C%20or%20support%20in%20some%20other%20way%20to%20help%20provide%20humanitarian%20aid%2C%20necessities%2C%20and%20efficient%2C%20effective%20response%20to%20earthquakes."
    sharetext2 = "PLEASE%20check%20out%20the%20Quake%20It%20Off%20app%20and%20start%20using%20it%20today%21%20https%3A%2F%2Fquakeitoff.streamlit.app%2F%0A%0AI%27m%20sharing%20the%20Share%20%26%20Donate%20page%20of%20the%20app.%20https%3A%2F%2Fquakeitoff.streamlit.app%2FShare%26Donate%0A%0AWith%20Share%20%26%20Donate%2C%20you%20can%20join%20a%20community%20of%20people%20who%20want%20to%20share%20knowledge%20about%20earthquakes%2C%20spread%20awareness%2C%20warn%20each%20other%2C%20and%20end%20up%20saving%20lives%21%20You%20can%20also%20view%2C%20go%20to%2C%20and%20interact%20with%20the%20sites%20that%20help%20earthquake-affected%20areas.%20These%20sites%20include%20places%20to%20donate%2C%20volunteer%2C%20or%20support%20in%20some%20other%20way%20to%20help%20provide%20humanitarian%20aid%2C%20necessities%2C%20and%20efficient%2C%20effective%20response%20to%20earthquakes."
    wurl = f"https://twitter.com/share?url=https://quakeitoff.streamlit.app/Share&Donate&text={sharetext}"
    wa = f'<a href="{wurl}" target="_blank"><img src="https://img.icons8.com/color/48/twitter--v1.png"/></a>'
    st.markdown(wa, unsafe_allow_html=True)
    turl = f"https://www.facebook.com/sharer/sharer.php?u=https://quakeitoff.streamlit.app/Share&Donate&quote={sharetext}"
    tw = f'<a href="{turl}" target="_blank"><img src="https://img.icons8.com/office/48/facebook-new.png"/></a>'
    st.markdown(tw, unsafe_allow_html=True)
    furl = f"https://web.whatsapp.com/send?text={sharetext2}"
    fb = f'<a href="{furl}" target="_blank"><img src="https://img.icons8.com/color/48/000000/whatsapp.png"/></a>'
    st.markdown(fb, unsafe_allow_html=True)
    gurl = f"https://mail.google.com/mail/u/0/?view=cm&su=Important%20Info%20from%20an%20App%20Quake%20It%20Off&body={sharetext2}"
    gm = f'<a href="{gurl}" target="_blank"><img src="https://img.icons8.com/color/48/gmail--v1.png"/></a>'
    st.markdown(gm, unsafe_allow_html=True)
st.header("Join a community, donate, spread awareness, and share knowledge and resources.")
st.markdown("Here, you can join a community of people who want to share knowledge about earthquakes, spread awareness, warn each other, and end up saving lives! You can also view, go to, and interact with the sites that help earthquake-affected areas. These sites include places to donate, volunteer, or support in some other way to help provide humanitarian aid, necessities, and efficient, effective response to earthquakes.")
st.markdown("You may have to scroll down to see everything.")
st.info("PLEASE NOTE: If you want to share some information from this app's Information Hub, press the share button at the top right of the screen of the Information Hub after opening the information you want to share.")

location = streamlit_js_eval.get_geolocation()
global ulatitude
global ulongitude
if st.button("Refresh Location", key="refresh_location_button"):
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

st.subheader("Top 10 Donation Sites Across the Globe: ")
st.markdown("[**UNHRC Donation Page**](https://donate.unhcr.org/in/en-in/turkiye-syria-earthquake)")
st.markdown("[**UN Crisis Relief**](https://crisisrelief.un.org/turkiye-syria-earthquake-appeal?gclid=CjwKCAjwrdmhBhBBEiwA4Hx5gx0cbMnGED4bLAuOfVS1rv-W1vPuVhgpWYbFJ2kdCDWWSlmkQjueSRoCbIQQAvD_BwE)")
st.markdown("[**Syrian American Medical Society Foundation**](https://www.sams-usa.net/)")
st.markdown("[**Center for Disaster Philanthropy**](https://disasterphilanthropy.org/)")
st.markdown("[**Plan International Inc.**](https://plan-international.org/)")
st.markdown("[**Direct Relief**](https://www.directrelief.org/)")
st.markdown("[**The White Helmets (Syria Civil Defense)**](https://www.whitehelmets.org/en/)")
st.markdown("[**Lions Club International**](https://www.lionsclubs.org/en/donate?utm_source=intruder-banner&utm_medium=link&utm_campaign=turkey-syria-earthquake-relief)")
st.markdown("[**American Red Cross**](https://www.redcross.org/donate/disaster-relief.html/?donamt=0)")
st.markdown("[**Global Giving**](https://www.globalgiving.org/projects/turkey-earthquake-relief-fund/)")

st.subheader("Donation Map:")

ddata = pd.read_excel("https://github.com/AJSmartyPants/EarthquakeDonationSitesDataset/raw/main/EarthquakeDonationSiteDataset.xlsx")
ddata.dropna(inplace=True)
ddata = ddata.drop_duplicates()
#print(ddata)

m = folium.Map(location = (ulatitude, ulongitude), zoom_start = 10)
yi = folium.Icon(icon = 'star', prefix='fa', color='darkpurple', icon_color='#00FFFF', border_color='#FFFFFF')

folium.Marker(
    (ulatitude, ulongitude),
    popup = "Latitude: "+str(ulatitude)+" Longitude: "+str(ulongitude),
    tooltip = "Your location",
    icon = yi
).add_to(m)

#oi = folium.Icon(icon = 'circle', prefix = 'fa', color='orange', icon_color='red')

for lats, lons, plcs in zip(ddata['Latitude'].values.tolist(), ddata['Longitude'].values.tolist(), ddata['Organization'].values.tolist()):
    folium.Marker(
        location= (lats, lons),
        popup= plcs + "\nLatitude: "+str(lats)+"\nLongitude: "+str(lons),
        tooltip=plcs,
        #icon = oi
    ).add_to(m)

dmap = stf.folium_static(m, height=725, width=725)