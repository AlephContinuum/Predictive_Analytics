
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📈 Advanced Analytics Dashboard")

df = pd.read_csv("sample_data.csv")

st.subheader("Correlation Heatmap")
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
st.pyplot(plt)

st.subheader("Distribution of Monthly Spend")
plt.figure(figsize=(8,4))
sns.histplot(df['avg_monthly_spend'], kde=True)
st.pyplot(plt)

st.subheader("Age vs Spend Scatter Plot")
plt.figure(figsize=(8,4))
sns.scatterplot(data=df, x="age", y="avg_monthly_spend", hue="churn")
st.pyplot(plt)

st.subheader("Tickets vs Spend Boxplot")
plt.figure(figsize=(8,4))
sns.boxplot(data=df, x="support_tickets", y="avg_monthly_spend")
st.pyplot(plt)
