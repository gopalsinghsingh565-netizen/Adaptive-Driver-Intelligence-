import streamlit as st
import numpy as np
import pandas as pd
import random
import cv2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(page_title="Driver Intelligence", layout="wide")

# ============================================
# DATA COLLECTION
# ============================================
def collect_driver_data(samples=300):
    data = []
    for _ in range(samples):
        speed = random.randint(20, 140)
        acceleration = round(random.uniform(0.5, 6.0), 2)
        braking = random.randint(1, 5)
        steering = round(random.uniform(0.1, 2.5), 2)

        if speed > 100 and acceleration > 4:
            behavior = 2
        elif speed < 60 and acceleration < 2:
            behavior = 0
        else:
            behavior = 1

        data.append([speed, acceleration, braking, steering, behavior])

    return pd.DataFrame(data, columns=['speed', 'acceleration', 'braking', 'steering', 'behavior'])

# ============================================
# TRAIN MODEL
# ============================================
@st.cache_resource
def train_model():
    df = collect_driver_data()
    X = df[['speed', 'acceleration', 'braking', 'steering']]
    y = df['behavior']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    return model, df

# ============================================
# PREDICTION
# ============================================
def predict_driver(model, input_data):
    pred = model.predict([input_data])[0]
    return ["Calm", "Normal", "Aggressive"][pred]

# ============================================
# PERSONALIZATION
# ============================================
def personalize(driver):
    if driver == "Aggressive":
        return "⚠️ Safety Mode Activated"
    elif driver == "Calm":
        return "💡 Eco Mode Activated"
    else:
        return "✅ Normal Mode Activated"

# ============================================
# GPS TRACKING
# ============================================
def generate_gps():
    lat = round(13.0827 + random.uniform(-0.01, 0.01), 6)
    lon = round(80.2707 + random.uniform(-0.01, 0.01), 6)
    return lat, lon

def track_route():
    if "route" not in st.session_state:
        st.session_state["route"] = []

    lat, lon = generate_gps()
    st.session_state["route"].append({"lat": lat, "lon": lon})

    return st.session_state["route"]

# ============================================
# CAMERA FUNCTION
# ============================================
def start_camera():
    cap = cv2.VideoCapture(0)
    st.warning("Press ESC to close camera window")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Driver Camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# ============================================
# DROWSINESS DETECTION
# ============================================
def detect_drowsiness():
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            roi = gray[y:y+h, x:x+w]
            eyes = eye.detectMultiScale(roi)

            if len(eyes) == 0:
                count += 1
            else:
                count = 0

            if count > 15:
                cv2.putText(frame, "DROWSINESS ALERT!", (50,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# ============================================
# LOAD MODEL
# ============================================
model, df = train_model()

# ============================================
# UI
# ============================================
st.title("🚗 Adaptive Driver Intelligence System")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Driving Data")

    speed = st.slider("Speed", 20, 140, 60)
    acceleration = st.slider("Acceleration", 0.5, 6.0, 2.0)
    braking = st.slider("Braking", 1, 5, 2)
    steering = st.slider("Steering", 0.1, 2.5, 1.0)

    if st.button("Analyze Driver"):
        driver = predict_driver(model, [speed, acceleration, braking, steering])
        result = personalize(driver)

        st.session_state["driver"] = driver
        st.session_state["result"] = result

with col2:
    st.subheader("📊 Output")

    if "driver" in st.session_state:
        st.success(f"Driver: {st.session_state['driver']}")
        st.info(st.session_state["result"])

# ============================================
# GRAPH
# ============================================
st.subheader("📈 Driving Trends")
st.line_chart(df[['speed','acceleration','braking']])

# ============================================
# GPS MAP
# ============================================
st.subheader("📍 GPS Tracking")
route = track_route()
st.map(pd.DataFrame(route))

# ============================================
# CAMERA + DROWSINESS
# ============================================
st.subheader("🎥 Driver Monitoring")

if st.button("Start Camera"):
    start_camera()

if st.button("Check Drowsiness"):
    detect_drowsiness()