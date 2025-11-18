import streamlit as st
import datetime

date = st.date_input('Date:', min_value=datetime.date.today())
time = st.time_input('Time:', None)