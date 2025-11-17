# Streamlit cheat-sheet

From YouTube lessons on:
https://www.youtube.com/watch?v=rMLwiVrK3Fw&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=2

## Creating App with Python Streamlit

```commandline
pip install streamlit
streamlit run ./main.py
```

```python
import streamlit as st
```

## Display text

```python
st.title('This is a title')
st.header('And a header')
st.subheader('And a smaller subheader')
st.text('Lorem ipsum dolor sit amet.')
```

## Markdown, code and json

```python
st.markdown('# Title 1')
st.markdown('> blockquote section')
st.code('print(\'Hello, World!\')')
person1 = {"name": "John", "surname": "Doe"}
st.json(person1)
```

## Tables, dataframes and metrics

```python
table = ({'Column 1': [1, 2, 3, 4, 5],
          'Column 2': [6, 7, 8, 9, 0]})
st.table(table)
st.dataframe(table)
st.metric(label='Win Speed',
          value='70ms', delta='5.7')
```

## Media elements:

```python
st.image('./python-streamlit-files-main/image.jpg')
image_list = ['./python-streamlit-files-main/google.png',
    './python-streamlit-files-main/youtube.png']
caption_list = ['Google','Youtube']
st.image(image=image_list, caption=caption_list, width=100)
st.audio('./python-streamlit-files-main/audio.oga')
st.video('./python-streamlit-files-main/video.mp4')
```

## Text input, button, download button and link button

A `text_input` widget creates a text line and reads it with Enter pressing.

A `button` widget has False/True conditions if pressed, it sets False if confirming new value in text_input.

```python
car = st.text_input('Type a car')
button = st.button('Check Availability')
st.write(car, button)
```

A `download_button` allows to download a file with a specific name, and returns error if file is not found.

```python
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
```

A `link_button` adds link to the page.

```python
st.link_button('Go to Google start page', 'https://www.google.com/')
```