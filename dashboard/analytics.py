
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Churn Analytics Dashboard")

df = pd.read_csv("sample_data.csv")

st.subheader("Churn Distribution")
plt.figure(figsize=(5,3))
df['churn'].value_counts().plot(kind='bar')
st.pyplot(plt)

st.subheader("Spend vs Churn")
plt.figure(figsize=(5,3))
df.groupby('churn')['avg_monthly_spend'].mean().plot(kind='bar')
st.pyplot(plt)

st.subheader("Support Tickets vs Churn")
plt.figure(figsize=(5,3))
df.groupby('churn')['support_tickets'].mean().plot(kind='bar')
st.pyplot(plt)
