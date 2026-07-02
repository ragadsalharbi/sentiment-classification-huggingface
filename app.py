import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Sentiment Analysis")
st.write("Analyze the sentiment of any text using pretrained Hugging Face transformer models.")

model_name = st.selectbox(
    "Select Model",
    (
        "distilbert-base-uncased-finetuned-sst-2-english",
        "cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
)

text = st.text_area(
    "Enter your text",
    placeholder="Example: I really enjoyed this movie!"
)

if st.button("Analyze"):
    if text.strip():
        classifier = pipeline("sentiment-analysis", model=model_name)
        result = classifier(text)[0]

        st.success(f"Prediction: {result['label']}")
        st.info(f"Confidence: {result['score']:.2%}")
    else:
        st.warning("Please enter some text.")
