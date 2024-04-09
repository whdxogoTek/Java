import streamlit as st
import pandas as pd

print("dd")

# Title of the webpage
st.title('My Simple Streamlit App')

# Write a dataframe
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
