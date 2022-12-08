import streamlit as st
st.title("Testing Stremlit")

user = st.text_area("Enter Anything: ")
if len(user) < 1:
    st.write("  ")
