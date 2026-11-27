import streamlit as st
import joblib
import numpy as np
st.set_page_config(page_title="salary prediction",layout="centered")
model=joblib.load("salary_traning_model.pkl")
st.title("Salary Prediction App")