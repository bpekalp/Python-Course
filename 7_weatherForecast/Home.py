import streamlit as st

st.header("Best Weather Forecast App!")

st.text_input("Location", key="tb_Location")
st.slider("Forecast Days", min_value=1, max_value=5, step=1, key="sl_Days")
st.selectbox(
    "Select Weather Data To View", options=("Temperature", "Sky"), key="dl_SubData"
)

location = st.session_state["tb_Location"]
day = st.session_state["sl_Days"]
subData = st.session_state["dl_SubData"]

if location and day and subData:
    message = f"{subData} For Next {day} Days In {location}"
    st.subheader(message)
