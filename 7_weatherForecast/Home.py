import streamlit as st
import plotly.express as px
import func.weatherData as wd
from datetime import datetime

st.header("Best Weather Forecast App!")

location = st.text_input("Location", key="tb_Location")
day = st.slider("Forecast Days", min_value=1, max_value=5, step=1, key="sl_Days")
weatherOpt = st.selectbox(
    "Select Weather Data To View", options=("Temperature", "Sky"), key="dl_WeatherOpt"
)

if location and day and weatherOpt:
    message = (
        f"{weatherOpt} for next {day} days in {location} for every 3 hours".title()
    )
    st.subheader(message)
    try:
        forecast = wd.getData(location, day, weatherOpt)
        dates = [element["dt_txt"] for element in forecast]
        formattedDates = [
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%b %d, %Y - %H:%M")
            for date in dates
        ]

        if weatherOpt == "Temperature":
            temperatures = [element["main"]["temp"] - 273.15 for element in forecast]

            plot = px.line(
                x=formattedDates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (C)"},
            )
            st.plotly_chart(plot)

        elif weatherOpt == "Sky":
            sky = [element["weather"][0]["main"] for element in forecast]
            imagePath = "7_weatherForecast/weatherImages"
            skyToImg = {
                "Clear": f"{imagePath}/Clear.png",
                "Clouds": f"{imagePath}/Clouds.png",
                "Rain": f"{imagePath}/Rain.png",
                "Snow": f"{imagePath}/Snow.png",
            }
            images = [skyToImg[condition] for condition in sky]

            st.image(images, formattedDates, width=128)

    except KeyError:
        st.error("Please enter a valid location.")
