# **Quake It Off**

By Anika Jha

We used to say that tornadoes couldn't be predicted, but then came the Doppler radar, and other ways to forecast them. So, what if we could predict earthquakes?

Because of an earthquake, millions of people suffer, property is wrecked, and whole nations can be destroyed. Just because of a lack of preparedness, knowledge, and evacuation plans. But what if we had hours or days of warning? And all the resources for learning about earthquakes, earthquakes around us, and expert route recommendation for evacuation, was at our fingertips?

Between 1998-2017, earthquakes caused nearly 750,000 deaths globally, more than half of all deaths related to natural disasters. More than 125 million people were affected by earthquakes during this time period, meaning they were injured, made homeless, displaced or evacuated during the emergency phase of the disaster.

In February this year, devastating earthquakes in Turkey and Syria have resulted in over 45000 deaths in Turkey, and over 6000 in Syria. At least 1.5 million people are now homeless, and it's unclear how long it will take to find them proper shelter.

The problem is NOW. And we must act. Quake It Off: Predict, Analyze, Learn, Prepare, and Prevent

Quake It Off currently runs as a web application and will soon be implemented in other devices. It is an app that uses machine learning and data analysis to help predict and analyze earthquakes, learn about earthquakes and safety, prepare for earthquakes, and prevent catastrophic damage thanks to all of its features.

Quake It Off has 5 main features:

1. Predicts earthquakes and their impact

2. Provides ways for the user to know if they are in danger zones of an earthquake, and provides reliable donation centers for the user to contribute

3. Recommends the most effective routes and strategies for shelter and responding to a disaster

4. Analyzes and lets the user analyze the areas affected by earthquakes in real-time, and in the past

5. Educates the user about earthquakes, safety, first aid, and more

Quake It Off uses the Random Forest Regressor machine learning algorithm to find a connection between the factors and results, helping us predict earthquakes based on the factors.

The model is trained on 3 factors: Latitude, Longitude, and Time. The model then estimates the probability of an earthquake happening at the user's location, and the magnitude and depth if an earthquake does occur.

The factors are totally independent parameters, and I recognize that: Quake It Off is built to provide preparedness and guidance for when the predictions DO come true, and it is a great way to keep track of current and past earthquakes across the globe as well.

It's better to have false alarms when an earthquake is predicted but one doesn't occur, than to have no idea for when an earthquake is not predicted, but one occurs. Like we always say, better safe than sorry.

The best part is: Our predictions are catered to those with anxiety and stress as well. On the app, I clarify that these predictions mean to warn.
The predictions go up to a week from the current day, and also provide current predictions.
![Home Page Image 1](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/HomePage1.png?raw=true)
![Home Page Image 2](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/HomePage2.png?raw=true)

The user can either view real-time and constantly updated earthquakes occurring across the globe (they can choose whether they want to view earthquakes that have happened in the past hour, day, week, or month), OR they can use a double-ended slider to choose a range of years to see the earthquakes that have occurred in that range. The user can choose whether they want to see the map of earthquakes in 2D or 3D. The color of the scatter points on the map represents the magnitude of the earthquake: The legend on the right shows what magnitude scale the colors represent. The size of the scatter points represents the depth of the earthquake. When you hover over a scatter point, you can see the earthquake's exact magnitude, depth, latitude, longitude, and place name/year based on the options you have chosen.

Everything is customizable, accessible, and easy to interpret! 
![Map Example 1](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/Map1.png?raw=true)
![Map Example 2](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/Map2.png?raw=true)

The Information Hub provides lots of vital information about earthquakes, safety, how to do first aid, terminology, and more. A drop-down allows you to choose a main topic, and subtopic in some cases. The information is presented as multimedia, with helpful infographics and images alongside readable and concise textual knowledge. Additionally, you can easily share content with your family members and friends with the share feature at the top right. The screenshots below were taken back when the share feature wasn't added, but it's there now!

![InfoHub1](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/InfoHub1.png?raw=true) 
![InfoHub2](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/InfoHub2.png?raw=true)
![InfoHub3](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/InfoHub3.png?raw=true)

The Route Recommendation section uses Artificial Intelligence, along with real-time earthquake data, to determine and recommend the safest routes to evacuate an earthquake-affected or earthquake-prone area.

![Route Selection Map](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/Route1.png?raw=true)
![Route Output Map](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/Route2.png?raw=true)

Finally, the Share & Donate page provides the user with trustworthy donation sites and centers for earthquake relief, along with a map that plots the best donation centers. This feature helps build a community!

![Share & Donate page Top 10 Donation Sites](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/ShareDonate1.png?raw=true)
![Donation Map](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/ShareDonate2.png?raw=true)

Notifications are coming soon!

Speaking of which, here are the top 3 future plans for this highly applicable app:
 - Improve model accuracy and include better factors: This will be done in many ways. Firstly, we will need more factors, rather than the unrelated 3 factors of latitude, longitude, and time, and more data. Seismic interactions, and live seismic wave data will be vital to predict an actual earthquake or alert the user. Connecting with initiatives, organizations, and scientists can help achieve this. Additionally, using a better, stronger, and more neural-network based machine learning algorithm could also help.

- Notification system: I need to develop a notification system for Quake It Off to alert the user during an earthquake at or nearby their location. This will only be possible once the app is published.

- Improve the Route Recommendation feature and make it akin to Google Maps

Here is a brief competitor analysis that clearly shows that Quake It Off uses brand-new technologies and novel ideas to solve this real-world problem:

![Brief Competitor Analysis Table](https://github.com/AJSmartyPants/Quake-It-Off/blob/main/Images/CompetitorAnalysis.png?raw=true)

Creating this application was no easy feat, to say the least. I spent long days and nights, working around the clock, and racing against the universe, to finish it in time! That too, with NO PRIOR KNOWLEDGE about machine learning! My Clevered mentor, Ms. Shivani, who was the instructor of the course I did before starting the creation of this app, was the one who brought me into the deep, intense, intricate, and infinite-possibility world of AI and ML. It was like stepping onto the tip of the iceberg, only to notice that under the water, the iceberg never ended!
My Technovation mentor, Mr. Vivek, helped me a lot with the entrepreneurship and feature-refining of the app! I couldn't have made it without him.

A huge shoutout to Dr. Ken Kahn for his irreplaceable and valuable insights into my project.

I am so proud of Quake It Off, and I hope my efforts can greatly contribute to the world of earthquake prediction and efficient disaster response.

Quake It Off is published as a web application! Start using it today:
[Quake It Off - A Web App that runs on all devices with geolocation in their browser](https://quakeitoff.streamlit.app/)

Please check out the GitHub repository for my project:
[https://github.com/AJSmartyPants/Quake-It-Off](https://github.com/AJSmartyPants/Quake-It-Off)

The requirements.txt file specifies all the libraries you will need to run the project.

The user manual has all the details of the project, and how to use it:

[https://www.canva.com/design/DAFdi\_mfC9E/Vf3fc1s5hpsr8OMTfVygUw/view?utm\_content=DAFdi\_mfC9E&utm\_campaign=designshare&utm\_medium=link&utm\_source=publishsharelink](https://www.canva.com/design/DAFdi_mfC9E/Vf3fc1s5hpsr8OMTfVygUw/view?utm_content=DAFdi_mfC9E&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

Be sure to go through it!

*I'm Anika, a 13-year-old learning enthusiast and a female philomath. I work in an NGO (Distressed Children and Infants International). My main commendable titles and laurels are below. I love learning, and my fields of interest lie in physics, chemistry, math, programming, and literature! I am a confident self-learner. People have told me that I have incredible leadership skills and quality cognitive ability. I enjoy reading, swimming, and ice-skating in my free time.*

*• Developer of the Grand Prize Winner app: cHHange - It's Normal*

*• International winner in the OakCodeFest 24-hour hackathon twice*

*• International winner in the TISBHacks hackathon*

*• Ted-ED speaker: [https://youtu.be/MPZkbC9kM8A](https://youtu.be/MPZkbC9kM8A)*

*• 3-time Best Delegate of Model United Nations*

*• Author of 2 books*

*• India's Top Young Problem Solver (HCL Jigsaw)*

*• Honorary mention title holder in the Johns Hopkins University SCAT math test*

*• National winner in the SpALLENthon Spell Bee*
