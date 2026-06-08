import streamlit as st

st.title("✍️ Grammar Fixer")

text = st.text_area("Write a sentence:")

if st.button("Correct Grammar"):
    if "very very" in text:
        st.warning("Avoid repetition like 'very very'")
    elif "goed" in text:
        st.error("Incorrect! Use 'went' instead of 'goed'")
    elif text:
        st.success("Grammar looks okay 👍 Try improving vocabulary next time.")
