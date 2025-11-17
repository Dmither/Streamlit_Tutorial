import streamlit as st

image_list = [
    './python-streamlit-files-main/google.png',
    './python-streamlit-files-main/youtube.png'
]
caption_list = ['Google','Youtube']
st.image(
    image=image_list,
    caption=caption_list,
    width=100
)
st.link_button('Go to Google start page', 'https://www.google.com/')
