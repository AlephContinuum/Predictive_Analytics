
import streamlit as st
import numpy as np
import joblib
from openai import OpenAI
import config.secrets as secrets
from ui.components import card, gradient_button

st.set_page_config(page_title="AI Churn Predictor", page_icon="🤖", layout="wide")

with open("ui/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🤖 AI-Powered Churn Prediction</h1>", unsafe_allow_html=True)

model = joblib.load("model.pkl")

with card("Customer Information"):
    col1, col2, col3, col4 = st.columns(4)
    age = col1.number_input("Age", 18, 100, 30)
    months = col2.number_input("Months Active", 1, 60, 12)
    spend = col3.number_input("Avg Monthly Spend", 1.0, 5000.0, 120.0)
    tickets = col4.number_input("Support Tickets", 0, 20, 2)

if gradient_button("Predict Churn"):
    X = np.array([[age, months, spend, tickets]])
    pred = int(model.predict(X)[0])

    st.markdown("<h2 class='subheader'>Prediction Result</h2>", unsafe_allow_html=True)
    st.success("🟥 Customer Will Churn" if pred==1 else "🟩 Customer Will Stay")

    st.markdown("<h2 class='subheader'>AI Explanation</h2>", unsafe_allow_html=True)

    client = OpenAI(api_key=secrets.OPENAI_API_KEY)
    prompt = f"""
    Explain why the model predicted {'churn' if pred==1 else 'stay'} for:
    Age: {age}, Months Active: {months}, Spend: {spend}, Support Tickets: {tickets}
    """

    resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
    st.info(resp.choices[0].message["content"])
