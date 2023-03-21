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
['None selected','Earthquakes', 'Spotting Earthquakes', 'Safety Tips', 'Relevant First Aid'], index = 0)
weqhi = pd.DataFrame(columns=['Type of Earthquake', 'Cause'])
weqhi['Type of Earthquake'] = ['Tectonic Earthquake', 'Volcanic Earthquake', 'Collapse Earthquake', 'Explosion Earthquake']
weqhi['Cause'] = ["The movement of tectonic plates is a geological fault that causes the earth's crust to break, resulting in an earthquake.", "Volcanic activities can cause disruptions on the earth's surface, causing shifts in the tectonic plates, and resulting in earthquakes.", "Human activities such as mining, tunnel, construction, etc. can produce seismic waves, which can cause earthquakes.", "The force that releases when a nuclear or chemical device is launched can cause earthquakes."]
terminology = pd.DataFrame(columns=['Term', 'Meaning'])
terminology['Term'] = ['Earthquake', 'Magnitude', 'Intensity', 'Focus or hypocenter', 'Epicenter', 'Body Waves', 'P wave & S wave', 'Shallow Focus Earthquake', 'Teleseism', 'Microseism', 'Micro earthquake', 'Accelogram', 'Accelograph', 'Focal Distance', 'Intermediate Focus Earthquake', 'Epicentral Distance', 'Foreshocks', 'Aftershocks', 'Benioff Zone', 'Destructive boundary', 'Fault', 'Active fault', 'Liquefaction', 'Magnitude/frequency relationship', 'Richter Scale', 'Rossi-Forrel Scale', 'Seismometer', 'Seismograph', 'Tsunami']
terminology['Meaning'] = [
    "It is a transient violent movement of the Earth's surface that follows a release of energy in the Earth's crust.",
    "It is a measure of the amount of energy released during an earthquake and expressed by Richter scale.",
    "Intensity is a qualitative measure of the actual shaking at a location during an Earthquake, and is assigned in Roman Capital Numerical. It refers to the effects of earthquakes. Modified Mercalli scale is the standard measurement. The intensity scale is based on the features of shaking, perception by people and animals, performance of buildings, and changes to natural surroundings.",
    "It is the point within the earth where an earthquake rupture starts",
    "It is the point on the earth's surface vertically above the hypocenter, point in the crust.",
    "They move through the interior of the earth, as opposed to surface waves that ravel near the earth's surface.",
    "A P wave, or compressional wave, shakes the ground back and forth in the same direction and the opposite direction in the direction the wave is moving. An S wave, or shear wave, shakes the ground back and forth perpendicular to the direction the wave is moving. S wave can travel only through solids.",
    "Earthquakes of focus less than 70 km deep from ground surface are called shallow focus earthquakes.",
    "A teleseism is an earthquake recorded by a seismograph at a distance. By international convention the distance is over 1000 Kilometers from the epicenter.",
    "These are more or less continuous disturbances in the ground recorded by seismographs.",
    "A very small earthquake having a magnitude measurable less than three on Richter scale is called a Micro-earthquake.",
    "The ground acceleration record produced by Accelerograph is called Accelerogram.",
    "This is an earthquake-recording device designed to measure the ground motion in terms of acceleration in the epicentral region of strong shaking.",
    "The straight-line distance between the places of recording/observation to the hypocenter is called the focal distance.",
    "When the focus of an Earthquake is between 70 to 300 km deep it is termed as Intermediate Focus Earthquake.",
    "Distance between epicenter and recording station(in km) is termed as Epicentral Distance.",
    "Smaller earthquakes preceding the main earthquake results in the generation of Foreshocks.",
    "Smaller earthquakes following the main earthquake results in the development of aftershocks.",
    "A region of earthquake activity inclined at an angle underneath a destructive boundary.",
    "A part of the earth's crust where tectonic plates move towards one another, resulting in the seduction of one below the other.",
    "A fracture in the rocks along which strain is occasionally released as an earthquake.",
    "Faults considered to be active if they have moved one or more time in the last 10000 years.",
    "The process by which sediments and soil collapse, behaving like a thick liquid when shaken by earthquake waves.",
    "The observed relationship (with most hazards) that bigger scale events occur less frequently while smaller scale events are relatively common.",
    "A measure of earthquake magnitude allowing an estimate of energy levels involved.",
    "An observational scale for measuring earthquake intensity. This was improved and expanded by Mercalli to produce the 'Modified Mercalli Scale'.",
    "An instrument for detecting and recording earthquake waves.",
    "A printout from a seismometer. Studies of seismograph traces can be used to pinpoint both the epicenter of an earthquake and the nature of the fault movement.",
    "An earthquake generated sea wave. Can travel thousands of miles and reach many metres in height when approaching shallow water."
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
        st.table(terminology)
elif(minfo == 'Spotting Earthquakes'):
    st.info("There are sometimes signs that a large earthquake is coming. There may be small quakes, called foreshocks. These can occur a few seconds to a few weeks before a major quake. Unfortunately, foreshocks are not very useful for predicting large earthquakes. Many quakes do not have foreshocks. Also, small earthquakes are not necessarily followed by a large earthquake.")
    st.info("There are other possible signs before an earthquake. The ground may tilt. Ground tilting is caused by the buildup of stress in the rocks. This may happen before a large earthquake, but it doesn't always. Water levels in wells may fluctuate. This is because water may move into or out of fractures before an earthquake. This is also an uncertain way to predict an earthquake. The difference in arrival times of P-waves and S-waves may decrease just before an earthquake occurs.")
    st.info("Folklore tells of animals behaving strangely just before an earthquake. Most people tell stories of these behaviors after the earthquake. Chinese scientists have actively studied the behavior of animals before earthquakes to see if there is a connection. So far nothing concrete has come of these studies.")
    st.info("Actions can reduce the damage once an earthquake has started. Seismometers can detect P-waves a few seconds before more damaging S-waves and surface waves arrive. In this time computers can shut down gas mains and electrical transmission lines. They can initiate protective measures in chemical plants, nuclear power plants, mass transit systems, airports, and roadways. Just a few seconds can be tremendously valuable.")
elif(minfo == 'Safety Tips'):
    st.info("Check the 'Responding to Earthquakes' subtopic under the 'Earthquakes' topic! That has all the safety tips you need.")
else:
    st.info("If you are trapped by falling items or a collapse, protect your mouth, nose, and eyes from dust. If you are bleeding, put pressure on the wound and elevate the injured part. Signal for help with your emergency whistle, a cell phone, or knock loudly on solid pieces of the building, three times every few minutes. Rescue personnel will be listening for such sounds.")
    st.warning("If a person is bleeding, put direct pressure on the wound. Use clean gauze or cloth, if available.\
                \nIf a person is not breathing, administer rescue breathing.\
                \nIf a person has no pulse, begin CPR (cardiopulmonary resuscitation).\
                \nDo not move seriously injured persons unless they are in immediate danger of further injury.\
                \nCover injured persons with blankets or additional clothing to keep them warm.\
                \nGet medical help for serious injuries.\
                \nCarefully check children or others needing special assistance.")
