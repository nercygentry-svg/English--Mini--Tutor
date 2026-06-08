import streamlit as st

st.title("🗣️ Speaking Practice")

prompt = st.selectbox("Choose a speaking topic:", [
    "Introduce yourself",
    "Describe your daily routine",
    "Talk about your future goals",
    "Describe your best friend",
    "Talk about your favorite food"
])

response = st.text_area("Speak (type your answer here):")

if st.button("Check Speaking"):
    if len(response.split()) < 10:
        st.warning("Try to speak more. Add details and examples.")
    else:
        st.success("Good effort 👍 Try to use more advanced vocabulary next time.")
