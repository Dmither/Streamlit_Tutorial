import streamlit as st

if 'visibility' not in st.session_state:
    st.session_state.visibility = False

st.session_state.visibility = not st.checkbox('Visibility', value=st.session_state.visibility)

radio_button = st.radio('Choose you course',
                        ['HTML, CSS :rainbow:',
                         'Linux :penguin:',
                         'Python :snake:'],
                        index=None,
                        # key='visibility',
                        disabled=st.session_state.visibility
                        )
if radio_button:
    st.subheader(f'You chose {radio_button}')
