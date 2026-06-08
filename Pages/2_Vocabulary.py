import streamlit as st

st.title("📚 Vocabulary Builder")

words = {
    "happy": "delighted / joyful / thrilled",
    "angry": "furious / irritated",
    "big": "enormous / massive",
    "smart": "intelligent / brilliant",
    "important": "crucial / essential"
}

word = st.selectbox("Choose a word:", list(words.keys()))

st.write("🔁 Better alternatives:")
st.info(words[word])

sentence = st.text_input("Make a sentence using this word:")

if st.button("Check Sentence"):
    if word in sentence.lower():
        st.success("Good job using the word correctly 👍")
    else:
        st.warning("Try to include the word in your sentence.")
