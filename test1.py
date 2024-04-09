import streamlit as st
import pandas as pd



# Title of the webpage
st.title('My Interactive Streamlit App')

# Create a static DataFrame
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the DataFrame
st.write("Here's a simple table:")
st.table(dataframe)

# User text input
user_name = st.text_input('Enter your name', '')

# Greet the user
if st.button('Greet'):
    st.write(f'Hello, {user_name}!')

# Checkbox to show/hide the DataFrame
if st.checkbox('Show DataFrame'):
    st.subheader('DataFrame')
    st.write(dataframe)

