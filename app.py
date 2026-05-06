
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Seoul Cafe Dashboard", layout="wide")

st.title("☕ Seoul Cafe Data Dashboard")

# Sample data
data = {
    "Cafe": ["Cafe A", "Cafe B", "Cafe C", "Cafe D", "Cafe E"],
    "Location": ["Gangnam", "Hongdae", "Itaewon", "Jamsil", "Seongsu"],
    "Rating": [4.5, 4.2, 4.7, 4.0, 4.6],
    "Price": [5, 4, 6, 3, 5]
}

df = pd.DataFrame(data)

st.subheader("📊 Cafe Data Table")
st.dataframe(df)

# Bar chart
fig = px.bar(df, x="Cafe", y="Rating", color="Location", title="Cafe Ratings")
st.plotly_chart(fig)

# Pie chart
fig2 = px.pie(df, names="Location", title="Location Distribution")
st.plotly_chart(fig2)

# Metric
st.subheader("⭐ Average Rating")
st.metric(label="Avg Rating", value=round(df["Rating"].mean(), 2))
