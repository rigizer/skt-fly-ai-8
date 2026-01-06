import streamlit as st

x = st.slider('x', 0, 100, 25)
st.write(x, 'squared is', x * x)