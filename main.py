import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Enerlytics Demo", layout="wide")

st.sidebar.title("Enerlytics Dashboard")
page = st.sidebar.radio("Go to", ["Overview", "Solar"])

df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=10),
    "AC_power": [20,22,25,21,27,30,32,29,31,33],
    "Expected": [25]*10
})

if page == "Overview":
    st.title("Executive Overview")
    st.metric("Energy Savings (OMR)", "2,310", "+15% vs last month")
    fig = px.line(df, x="Date", y=["AC_power","Expected"], title="PV Output vs Expected")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Solar":
    st.title("Solar System Details")
    st.dataframe(df)
