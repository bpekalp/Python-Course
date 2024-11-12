import streamlit as st
import plotly.express as px
import pandas as pd

columns = (
    "Country",
    "Happiness",
    "Income Per Capita (GDP)",
    "Social Support",
    "Life Expectancy",
    "Freedom",
    "Generosity",
    "Corruption",
)
st.header("Student Happiness Data")
xAxis = st.selectbox("Select Data For X Axis", options=columns[1:])
yAxis = st.selectbox("Select Data For Y Axis", options=columns[1:])

df = pd.read_csv("bonus/studentHappiness/datas/happy.csv")
df.columns = columns

plotX = df[xAxis]
plotY = df[yAxis]

labels = {"x": xAxis, "y": yAxis}

message = f"{yAxis} by {xAxis}"
st.subheader(message)
plot = px.scatter(df, x=plotX, y=plotY, color="Country", labels=labels)
st.plotly_chart(plot)
