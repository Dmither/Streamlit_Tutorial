import streamlit as st

with st.form('my_form'):
    name = st.text_input('Name')
    surname = st.text_input('Surname')
    age = st.slider('How old are you?', 0, 130, 18)
    start_day = st.date_input('Start date')

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f'Name: {name} Surname: {surname} Age: {age} Start date: {start_day}')

if submitted:
    st.write(f'Name: {name} Surname: {surname} Age: {age} Start date: {start_day}')
