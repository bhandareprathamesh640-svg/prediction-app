import streamlit as st
import joblib
import numpy as np
st.set_page_config(page_title="salary prediction",layout="centered")
model=joblib.load("salary_traning_model.pkl")
st.title("Salary Prediction App")
st.write("Predict salary based on years of prefessional experiance")
st.sidebar.header("Employee Information")
exp=st.sidebar.number_input("years of experiance",min_value=20,max_value=60,step=1)
if st.button("Predict salary"):
    input=np.array([[exp]])
    pred=model.predict(input)
    # to display result
    st.success(f"Predicted salary={pred}")