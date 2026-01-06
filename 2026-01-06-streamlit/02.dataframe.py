import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'First Column': [1, 2, 3, 4], 
    'Second Column': [10, 20, 30, 40]
})

st.write("### Here's our first attempt at using dataframes in Streamlit:")
st.write(df)