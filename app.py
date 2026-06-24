import streamlit as st
import pandas as pd

df = pd.read_csv("../data/clean_churn.csv")


st.title(
    "European Bank Customer Churn Dashboard"
)


# KPI Cards

col1, col2 = st.columns(2)

churn = round(
    df["Exited"].mean()*100,
    2
)

customers = len(df)


col1.metric(
    "Churn Rate",
    f"{churn}%"
)

col2.metric(
    "Total Customers",
    customers
)


# Filter

country = st.selectbox(
    "Select Country",
    df["Geography"].unique()
)

filtered_df = df[
    df["Geography"] == country
]

st.write(filtered_df.head())


# Churn Chart

chart = (
    filtered_df
    .groupby("Gender")
    ["Exited"]
    .mean()
)

st.bar_chart(chart)