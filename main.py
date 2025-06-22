import streamlit as st

st.title("Hello from Streamlit & Jenkins!")
st.write("This app was launched from a Jenkins pipeline.")
if st.button("Click Me"):
    st.success("Button Clicked!")
