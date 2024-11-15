import streamlit as st
from glob import glob
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

diaryFiles = glob("bonus/diaryMood/datas/*.txt")

dates = [os.path.basename(diaryFile).strip(".txt") for diaryFile in diaryFiles]

diaryEntries = []
for diaryFile in diaryFiles:
    with open(diaryFile) as file:
        content = file.read()

    diaryEntries.append(content)

analyzer = SentimentIntensityAnalyzer()
moods = [analyzer.polarity_scores(diaryEntry) for diaryEntry in diaryEntries]
pos = [mood["pos"] for mood in moods]
neu = [mood["neu"] for mood in moods]
neg = [mood["neg"] for mood in moods]

st.header("Diary Mood Visualizer App")
st.write("You can find each diary entry at the end of the page.")

st.subheader("Positivity Scores By Dates")
plot = px.line(x=dates, y=pos, labels={"x": "Dates", "y": "Positivity Score"})
st.plotly_chart(plot, key="line_PosByDate")

st.subheader("Neutrality Scores By Dates")
plot = px.line(x=dates, y=neu, labels={"x": "Dates", "y": "Neutrality Score"})
st.plotly_chart(plot, key="line_NeuByDate")

st.subheader("Negativity Scores By Dates")
plot = px.line(x=dates, y=neg, labels={"x": "Dates", "y": "Negativity Score"})
st.plotly_chart(plot, key="line_NegByDate")

dateEntries = dict(zip(dates, diaryEntries))

st.header("Entries")
for entry in dateEntries:
    st.subheader(entry)
    st.write(dateEntries[entry])
