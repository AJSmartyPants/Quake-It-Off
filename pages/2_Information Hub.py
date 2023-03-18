# import module
import streamlit as st

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
        print('x')
    elif(eqbns == 'Preventing Earthquakes'):
        print('x')
    elif(eqbns == 'Where Earthquakes Happen'):
        print('x')
    elif(eqbns == 'When Earthquakes Happen'):
        print('x')
    elif(eqbns == 'Terminology'):
        print('x')
elif(minfo == 'Spotting Natural Disasters'):
    print('Spotting Natural Disasters')
    #sndbns = st.radio("What subtopic do you want to learn about?: ", ('Predicting Earthquakes', 'Why & How Earthquakes Happen', 'Preventing Earthquakes', 'Responding to Earthquakes', 'Where Earthquakes Happen', 'When Earthquakes Happen'))
elif(minfo == 'Safety Tips'):
    print('Safety Tips Selected')
else:
    print('Relevant First Aid chosen')
