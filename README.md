# Streamlit cheat-sheet

From YouTube lessons on:
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

## Display elements

Tables:

```python
table = ({'Column 1': [1, 2, 3, 4, 5],
          'Column 2': [6, 7, 8, 9, 0]})
st.table(table)
st.dataframe(table)
```

Metrics:
```python
st.metric(label='Win Speed',
          value='70ms', delta='5.7')
```
