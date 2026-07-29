import joblib
import streamlit as st
import pandas as pd

## Load trained model
model = joblib.load("student_grade_model.pkl")

## Streamlit app
st.title("Student Final Grade Prediction")

st.write("This app predicts a student's final grade based on student information.")

## User inputs
school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["F", "M"])
age = st.slider("Age", 15, 22, 17)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["LE3", "GT3"])
Pstatus = st.selectbox("Parent Cohabitation Status", ["T", "A"])

Medu = st.slider("Mother Education Level", 0, 4, 2)
Fedu = st.slider("Father Education Level", 0, 4, 2)

Mjob = st.selectbox("Mother Job", ["teacher", "health", "services", "at_home", "other"])
Fjob = st.selectbox("Father Job", ["teacher", "health", "services", "at_home", "other"])

reason = st.selectbox("Reason for Choosing School", ["home", "reputation", "course", "other"])
guardian = st.selectbox("Guardian", ["mother", "father", "other"])

traveltime = st.slider("Travel Time", 1, 4, 1)
studytime = st.slider("Study Time", 1, 4, 2)
failures = st.slider("Number of Past Class Failures", 0, 4, 0)

schoolsup = st.selectbox("Extra Educational Support", ["yes", "no"])
famsup = st.selectbox("Family Educational Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra-curricular Activities", ["yes", "no"])
nursery = st.selectbox("Attended Nursery School", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access at Home", ["yes", "no"])
romantic = st.selectbox("In Romantic Relationship", ["yes", "no"])

famrel = st.slider("Family Relationship Quality", 1, 5, 4)
freetime = st.slider("Free Time After School", 1, 5, 3)
goout = st.slider("Going Out With Friends", 1, 5, 3)
Dalc = st.slider("Workday Alcohol Consumption", 1, 5, 1)
Walc = st.slider("Weekend Alcohol Consumption", 1, 5, 2)
health = st.slider("Current Health Status", 1, 5, 3)
absences = st.slider("Number of School Absences", 0, 100, 4)

G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

## Predict button
if st.button("Predict Final Grade"):

    ## Create input data
    df_input = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],
        "famsize": [famsize],
        "Pstatus": [Pstatus],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "Mjob": [Mjob],
        "Fjob": [Fjob],
        "reason": [reason],
        "guardian": [guardian],
        "traveltime": [traveltime],
        "studytime": [studytime],
        "failures": [failures],
        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "nursery": [nursery],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "Dalc": [Dalc],
        "Walc": [Walc],
        "health": [health],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    ## One-hot encoding
    df_input = pd.get_dummies(df_input)

    ## Match training columns
    df_input = df_input.reindex(columns=model.feature_names_in_, fill_value=0)

    ## Predict
    predicted_grade = model.predict(df_input)[0]

    ## Display prediction
    st.success(f"Predicted Final Grade: {predicted_grade:.2f} / 20")