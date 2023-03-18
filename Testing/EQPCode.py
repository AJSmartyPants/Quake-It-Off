# import module
import streamlit as st
from streamlit.components.v1 import html
from streamlit.script_runner import RerunException

# define the JavaScript code to request geolocation permission and send the location data to Python
js_code = """
<script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            console.log(latitude);
            console.log(longitude);
            const event = new CustomEvent("locationChanged", {detail: {latitude: latitude, longitude: longitude}});
            document.dispatchEvent(event);
        },
        function(error) {
            console.log(error);
        }
    );
</script>
"""

# display the latitude and longitude
location_div = st.empty()
location_div.markdown("<div id='location'></div>", unsafe_allow_html=True)

# execute the JavaScript code to request geolocation and send the location data to Python
result_div = st.empty()  # create an empty div with ID "result"

if st.button("Get Location"):
    try:
        # write the JavaScript code to the div
        result_div.write(html(js_code))
        
        # define a function to handle the custom "locationChanged" event in JavaScript
        # and send the location data to Python using Streamlit's st.experimental_rerun()
        def handle_location_changed(event):
            latitude = event.detail.latitude
            longitude = event.detail.longitude
            location_div.write("Your location: Latitude: " + str(latitude) + ", Longitude: " + str(longitude))
            # send the location data to Python using Streamlit's st.experimental_rerun()
            st.experimental_rerun(message={"latitude": latitude, "longitude": longitude})
        
        # add an event listener in JavaScript to listen for the "locationChanged" event
        # and call the handle_location_changed function
        result_div.write(html("""
        <script>
            document.addEventListener("locationChanged", function(event) {
                console.log("locationChanged event received");
                console.log(event.detail);
                const data = {latitude: event.detail.latitude, longitude: event.detail.longitude};
                const jsonString = JSON.stringify(data);
                const command = "handle_location_changed(" + jsonString + ")";
                Streamlit.setComponentValue(command);
            });
        </script>
        """))
        
        # define the handle_location_changed function in Python
        @st.cache(allow_output_mutation=True)
        def handle_location_changed(latitude, longitude):
            print("latitude:", latitude)
            print("longitude:", longitude)
            # do something with the location data
            
    except RerunException as e:
        if e.rerun_data is not None:
            # handle the location data sent from JavaScript
            location_data = e.rerun_data.message
            latitude = location_data.get("latitude")
            longitude = location_data.get("longitude")
            handle_location_changed(latitude, longitude)
            
    except:
        st.write("Error getting location.")












url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

headers = {
	"X-RapidAPI-Key": "55588fff42msh38648ac92f61898p1bc6a2jsnea83869aa07a",
	"X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
}

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

# Title
st.title("Live and Future Predictions")
# Header
#st.header("Welcome to the Info Hub!")
#def header(url):
#st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;src: url(https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap);font-family: Oswald, sans-serif;">{"Welcome to the Info Hub!"}</p>', unsafe_allow_html=True)
#blue["You may have to scroll down to see the information"])#, '#AA00FF')#["You may have to scroll down to see the information."])
# Subheader
st.header("Get information about natural disasters, how to recognize them, what to do when one occurs, first aid, safety tips, and more!")
st.markdown("You may have to scroll down to see the information")

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