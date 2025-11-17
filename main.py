import streamlit as st

car = st.text_input('Type a car')
button = st.button('Check Availability')
st.write(car, button)