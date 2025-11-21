import streamlit as st

st.header('Welcome to the Main page')

with st.sidebar:
    add_selectbox = st.selectbox(
        "How would you like to be contacted?",
        ['Mobile phone', 'Email']
    )

    add_input = st.text_input('Info')

    add_radio = st.radio(
        'Choose a shipping method',
        ['Standard (5-15 days)', 'Express (2-5 days)']
    )

    send_button = st.button('Send')

if send_button:
    st.sidebar.write('Send button clicked!')