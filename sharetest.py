import streamlit as st
import base64
import webbrowser
import urllib.parse
import geocoder

share_text = "Hello, this is a test message!"

wa_button = st.button("Share on WhatsApp")

if wa_button:
    sharetext = urllib.parse.quote(share_text.encode('utf-8'))
    wa_url = f"https://web.whatsapp.com/send?text={sharetext}"
    webbrowser.open(wa_url)
lat = 12.974572442070121 
lon = 77.75744541199099

results = geocoder.osm([lat, lon], method='reverse')
print(results)
print(results.raw)
print(results.raw.get('address'))
print(results.raw.get('address', {}).get('country_code'))
#print(results[0]['country'])