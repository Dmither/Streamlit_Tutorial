import streamlit as st

st.image('./python-streamlit-files-main/image.jpg', caption='image.jpg')
file_name = st.text_input('Enter the file name:')
st.write(file_name)
with open('./python-streamlit-files-main/image.jpg', 'rb') as file:
    btn = st.download_button(
        label='Download Image',
        data=file,
        file_name=file_name,
        mime='image/file'
    )