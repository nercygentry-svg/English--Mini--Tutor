import streamlit as st

st.title("🧪 Practice Test")

questions = [
    "Describe your last holiday",
    "Talk about your dream job",
    "Explain your daily routine",
    "Describe your hometown"
]

q = st.selectbox("Question:", questions)

answer = st.text_area("Your answer:")

if st.button("Submit"):
    if len(answer.split()) < 15:
        st.warning("Add more detail to improve fluency.")
    else:
        st.success("Great effort! Try using more advanced vocabulary next time.")
