import streamlit 
import joblib
import numpy as np
streamlit.set_page_config(page_title="salary prediction",layout="centered")
model=joblib.load("salary_training_model.pkl")
streamlit.title("Salary Prediction App")
streamlit.write("Predict salary based on years of prefessional experiance")
streamlit.sidebar.header("Employee Information")
exp=streamlit.sidebar.number_input("years of experiance",min_value=20,max_value=60,step=1)
if streamlit.button("Predict salary"):
    input=np.array([[exp]])
    pred=model.predict(input)
    # to display result
    streamlit
    streamlit.success(f"Predicted salary={pred}")
