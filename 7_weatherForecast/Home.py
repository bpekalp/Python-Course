import streamlit as st
import plotly.express as px

st.header("Best Weather Forecast App!")

location = st.text_input("Location", key="tb_Location")
day = st.slider("Forecast Days", min_value=1, max_value=5, step=1, key="sl_Days")
weatherOpt = st.selectbox(
    "Select Weather Data To View", options=("Temperature", "Sky"), key="dl_WeatherOpt"
)

if location and day and weatherOpt:
    message = f"{weatherOpt} For Next {day} Days In {location}"
    st.subheader(message)

    dates = ("2022-25-10", "2022-26-10", "2022-27-10")
    temps = (14, 27, 34)
    if weatherOpt == "Temperature":
        plot = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(plot)

    elif weatherOpt == "Sky":
        pass


st.session_state
