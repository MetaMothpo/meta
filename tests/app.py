import streamlit as st
from test_scripts import testloginPage
import pandas as pd
# Title of the app
st.title("Test Runner")

# Button to trigger the test script
if st.button("Run Tests"):
    # Run the test script and capture the results
    result = testloginPage()

    # Display the results in the app
    st.text_area("Test Results", result)
    #data = pd.read_csv('test_results.csv')
    #st.dataframe(data)

    st.image("screenshot1.png", caption="Login Screen")
    st.image("screenshot2.png", caption="Home Screen")



