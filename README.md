# Adaptive-Driver-Intelligence System For Personalized Vehicle Safety
The Adaptive Driver Intelligence System is an advanced smart vehicle solution designed to enhance driver safety, comfort, and personalization. The system uses machine learning and real-time data analysis to monitor driver behavior, detect drowsiness, and adapt vehicle settings accordingly. It integrates technologies such as computer vision for driver monitoring, GPS for route tracking, and intelligent algorithms to learn user preferences. This project demonstrates the application of AI in improving driving experience and reducing road accidents.

# Abstract

The rapid increase in road accidents due to human error has highlighted the need for more intelligent and adaptive vehicle safety systems. Most modern vehicles are equipped with Advanced Driver Assistance Systems (ADAS), but these systems largely operate on predefined rules and do not consider the unique driving behavior of individual users. As a result, many alerts are either ignored or fail to provide meaningful assistance in real-world scenarios. This project presents the design andimplementation of an Adaptive Driver Intelligence System, a software-based solution that focuses on learning and adapting to the driving patterns of individual users. The system continuously monitors driver behavior such as braking timing, steering smoothness, acceleration habits, and reaction patterns. By analyzing this data, it builds a personalized driving profile for each user and uses it to predict potential risks before they occur. The proposed system is developed using Python and computer vision techniques, where pre-recorded driving videos are used as input. These videos are processed frame-by-frame, and relevant information is overlaid in real time, including driver identification, behavior analysis, risk level prediction, and intelligent alerts.

# Features
- Drowsiness Detection using Computer Vision
-  Driver Behavior Analysis
-  GPS Tracking and Route Learning
- Personalized Vehicle Settings
-  Real-time Monitoring System

  # Technologies Used
- Python
- Machine Learning
- OpenCV
- NumPy
- GPS Integration

  # SOFTWARE REQUIREMENTS

   Python (version 3.8 – 3.12 recommended)
Internet (for installing libraries)
Webcam for camera + drowsiness part

# REQUIRED LIBRARIES

* Run this ONE command in terminal:

pip install streamlit numpy pandas scikit-learn opencv-python

#  PROJECT SETUP
Step 1: Save your file as:
app.py

Open terminal in that folder
 RUN THE PROJECT
 Step 2: Bash streamlit run app.py

 Then open:
http://localhost:8501

# HOW TO TEST EACH FEATURE
 1. Driver Prediction
Move sliders
Click Analyze Driver
You should see:
Driver type (Calm / Normal / Aggressive)
Mode (Eco / Normal / Safety)
2. Graph

 You should see line chart automatically

 3. GPS Map
    Map should appear with points

4. Camera

Click:
 Start Camera

 Opens webcam window
 Press ESC to close

 5. Drowsiness Detection

Click:
 Check Drowsiness
If eyes closed → shows alert

# How It Works
Collects driving data (speed, acceleration, braking, steering)
Trains a machine learning model
Predicts driver behavior
Adapts vehicle settings
Monitors driver using camera and detects drowsiness
Tracks GPS route in real-time
