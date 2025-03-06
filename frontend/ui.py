import streamlit as st
import requests

st.title("🔥 AI Debate Agent")

topic = st.text_input("Enter a debate topic:")

if st.button("Start Debate"):
    response = requests.post("http://127.0.0.1:8000/debate/", json={"topic": topic})
    if response.status_code == 200:
        data = response.json()
        st.subheader("🔹 Argument FOR:")
        st.write(data["for"])
        st.subheader("🔹 Argument AGAINST:")
        st.write(data["against"])
    else:
        st.error("Error: Could not fetch debate arguments.")
