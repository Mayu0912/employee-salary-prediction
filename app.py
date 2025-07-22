import streamlit as st

# Title
st.title("💼 Employee Salary Prediction Demo App")

# Inputs
st.header("Enter Employee Details")
experience = st.number_input("Years of Experience", min_value=0.0)
education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
position_level = st.selectbox("Position Level", ["Junior", "Mid-Level", "Senior", "Manager"])

# Dummy logic to simulate prediction
def fake_predict(exp, edu, pos):
    edu_score = {"High School": 1, "Bachelor's": 2, "Master's": 3, "PhD": 4}[edu]
    pos_score = {"Junior": 1, "Mid-Level": 2, "Senior": 3, "Manager": 4}[pos]
    salary = 20000 + (exp * 5000) + (edu_score * 3000) + (pos_score * 4000)
    return salary

# Predict button
if st.button("Predict Salary"):
    prediction = fake_predict(experience, education_level, position_level)
    st.success(f"Predicted Salary: ₹{prediction:,.2f}")
