# Streamlit tutorial

https://www.youtube.com/watch?v=rMLwiVrK3Fw&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=2

## Creating App with Python Streamlit

Install and import streamlit

```python
import streamlit as st
```

Streamlit label methods:

```python
st.title('This is a title')
st.header('And a header')
st.subheader('And a smaller subheader')
st.text('Lorem ipsum dolor sit amet.')
```

## Markdown elements

It supports markdown features:

```python
st.markdown('# Title 1')
st.markdown('> blockquote section')
```

Also, it has own method for code blocks:

```python
st.code('print(\'Hello, World!\')')
```

And for json blocks:

```python
person1 = {"name": "John", "surname": "Doe"}
st.json(person1)
```
