# import module
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Quake It Off - Info Hub",
    page_icon='🌏'
)
# Title
st.title("Info Hub")
# Header
#st.header("Welcome to the Info Hub!")
#def header(url):
#st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;src: url(https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap);font-family: Oswald, sans-serif;">{"Welcome to the Info Hub!"}</p>', unsafe_allow_html=True)
#blue["You may have to scroll down to see the information"])#, '#AA00FF')#["You may have to scroll down to see the information."])
# Subheader
st.header("Get information about natural disasters, how to recognize them, what to do when one occurs, first aid, safety tips, and more!")
st.markdown("You may have to scroll down to see the information")

minfo = st.selectbox("Please choose what you would like to learn about: ",
['None selected','Earthquakes', 'Spotting Natural Disasters', 'Safety Tips', 'Relevant First Aid'], index = 0)
weqhi = pd.DataFrame(columns=['Type of Earthquake', 'Cause'])
weqhi['Type of Earthquake'] = ['Tectonic Earthquake', 'Volcanic Earthquake', 'Collapse Earthquake', 'Explosion Earthquake']
weqhi['Cause'] = ["The movement of tectonic plates is a geological fault that causes the earth's crust to break, resulting in an earthquake.", "Volcanic activities can cause disruptions on the earth's surface, causing shifts in the tectonic plates, and resulting in earthquakes.", "Human activities such as mining, tunnel, construction, etc. can produce seismic waves, which can cause earthquakes.", "The force that releases when a nuclear or chemical device is launched can cause earthquakes."]
terminology = pd.DataFrame(columns=['Term', 'Meaning'])
terminology['Term'] = ['Earthquake', 'Magnitude', 'Intensity', 'Focus or hypocenter', 'Epicenter', 'Body Waves', 'P wave & S wave', 'Shallow Focus Earthquake', 'Teleseism', 'Microseism', 'Micro earthquake', 'Accelogram', 'Accelograph', 'Focal Distance', 'Intermediate Focus Earthquake', 'Epicentral Distance', 'Foreshocks', 'Aftershocks', 'Benioff Zone', 'Destructive boundary', 'Fault', 'Active fault', 'Liquefaction', 'Magnitude/frequency relationship', 'Richter Scale', 'Rossi-Forrel Scale', 'Seismometer', 'Seismograph', 'Tsunami']
terminology['Meaning'] = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]
#print(weqhi)
if(minfo == 'Earthquakes'):
    #print('Earthquakes chosen')
    eqbns = st.radio("What subtopic do you want to learn about?", ('Preparing for and Responding to Earthquakes', 'Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen', 'Terminology'))
    st.success(eqbns)
    st.image("https://www.ready.gov/sites/default/files/styles/large/public/2021-03/illustration_earthquake_drop-cover-hold-on_0.png?itok=a_x6XtRz", caption='How to drop, cover, and hold on')
    if(eqbns == 'Preparing for and Responding to Earthquakes'):
        st.image("https://www.earthquakecountry.org/library/ECA_Seven_Steps_Earthquake_Safety-EN.png", caption='7 Steps to Earthquake Safety')
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
        st.image("https://dug.com/wp-content/uploads/2022/04/Webp.net-resizeimage-81.jpg", caption="Predicting earthquakes will soon be possible thanks to machine learning")
        st.subheader("Can you predict an earthquake?")
        st.info("No. We have never really predicted a major earthquake. We do not know how, and we do not expect to know how any time soon. We can only calculate the probability that a significant earthquake will occur (thanks to hazard mapping) in a specific area within a certain number of years. \
                \nThis application estimates the probability of an earthquake happening based on your location, and the magnitude and depth if an earthquake does occur. Our machine learning model is trained on the latitudes, longitudes, and times of when an earthquake has occured. These are totally independent parameters, and we recognize that: Our app is to provide preparedness and guidance for when our predictions DO come true, and it is a great way to keep track of current and past earthquakes across the globe as well.")
        st.subheader("What About Everything that People Who Predict the Future Say?")
    elif(eqbns == 'Why & How Earthquakes Happen'):
        st.image("https://caltechsites-prod.s3.amazonaws.com/scienceexchange/images/what-happens-earthquake-diagram_.original.png", caption="How an earthquake happens")
        st.image("https://www.aljazeera.com/wp-content/uploads/2023/02/INTERACTIVE-How-do-earthquakes-happen.png?w=770&resize=770%2C769", caption="How an earthquake happens with explanation")
        st.info("Earthquakes can occur in any intensity, which is so weak that they cannot be felt, that are violent enough to carry objects and people into the air and wreak havoc on entire cities. It is the movement of the Earth's surface that produces seismic waves as a result of the sudden release of energy in the Earth's lithosphere.")
        st.table(weqhi)
    elif(eqbns == 'Preventing Earthquakes'):
        st.subheader("Can we prevent earthquakes?")
        st.warning("No one can prevent an earthquake from happening: It's a natural disaster that occurs due to the movement of Earth's tectonic plates. And we have no control over that.\
                   \nBut what we can do is PREPARE before the next one hits. The following earthquake preparation tips take a few hours to create a plan and organize supplies that will keep you safer.")
        st.subheader("What and how should we prepare for earthquakes?")
        st.info("Step 1: Secure Your Space\
                \n• Secure your space by identifying hazards and securing moveable items.\
                \nStep 2: Plan to be Safe\
                \n• Plan to be safe by creating a disaster plan and deciding how you will communicate in an emergency.\
                \nStep 3: Organize Disaster Supplies\
                \n• Organize disaster supplies in convenient locations that can be accessed before, during, and after an earthquake\
                \nStep 4: Minimize Financial Hardship\
                \n• Minimize financial hardship by organizing important documents, strengthening your property, and considering insurance\
                \n\nRefer to the 'Responding to Earthquakes' subtopic, and 'What to Do Before an Earthquake' section there for more tips.")
    elif(eqbns == 'Where Earthquakes Happen'):
        st.image("https://quantectum.com/Blogs/8_Ring_of_Fire.png", caption="Ring of Fire")
        st.info("Earthquakes can occur anywhere, but they occur mainly along fault lines (planar or curved fractures in the rocks of Earth's crust), where compressional or tensional forces move rocks on opposite sides of a fracture. Faults extend from a few centimetres to many hundreds of kilometres. In addition, most of the world's earthquakes occur within the Ring of Fire, a long horseshoe-shaped belt of earthquake epicentres, volcanoes, and tectonic plate boundaries fringing the Pacific basin.")
        st.success("Check out the maps on the home page and alter the settings to see if you can spot a pattern where most earthquakes occur!")
        st.info("Some of the most earthquake-prone countries are: Indonesia is in a very active seismic zone, also, but by virtue of its larger size than Japan, it has more total earthquakes. Which country has the most earthquakes per unit area? This would probably be Tonga, Fiji, or Indonesia since they are all in extremely active seismic areas along subduction zones. Both China and Iran are in seismically active areas, have very long historical records, and have had many catastrophic earthquakes. Turkey is also worth mentioning in this category.")
    elif(eqbns == 'When Earthquakes Happen'):
        st.info("Earthquakes occur when tectonic plates struggle against each other, or due to other reasons that you can refer to in the 'Why & How Earthquakes Happen' subtopic. They can happen anytime, day or night, and are not yet scientifically proved to be affected by weather or time of day.")
        st.info("How long earthquakes last varies depending on the size of the earthquake. Earthquakes may last seconds to minutes. While the shaking of small earthquakes typically lasts only a few seconds, strong shaking during moderate to large earthquakes, such as the 2004 Sumatra earthquake, can lasts couple minutes.")
    elif(eqbns == 'Terminology'):
        
elif(minfo == 'Spotting Natural Disasters'):
    print('Spotting Natural Disasters')
    #sndbns = st.radio("What subtopic do you want to learn about?: ", ('Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Responding to Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen'))
elif(minfo == 'Safety Tips'):
    print('Safety Tips Selected')
else:
    print('Relevant First Aid chosen')
