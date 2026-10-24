import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Summarizer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Text Summarizer")
st.write("Convert long paragraphs into short summaries.")

@st.cache_resource
def get_summarizer():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

text = st.text_area(
    "Enter your paragraph:",
    placeholder="Type or paste your text here...",
    height=200
)

summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)

if st.button("Summarize Text"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif len(text.split()) < 30:
        st.warning("Please enter at least 30 words.")

    else:
        with st.spinner("Creating summary..."):

            summarizer = get_summarizer()

            lengths = {
                "Short": (40, 15),
                "Medium": (80, 30),
                "Long": (120, 50)
            }

            max_len, min_len = lengths[summary_length]

            result = summarizer(
                text,
                max_length=max_len,
                min_length=min_len,
                do_sample=False,
                truncation=True
            )

        st.subheader("✨ Summary")
        st.success(result[0]["summary_text"])

        st.caption("Original word count: " + str(len(text.split())))
        st.caption(
            "Summary word count: " +
            str(len(result[0]["summary_text"].split()))
        )
