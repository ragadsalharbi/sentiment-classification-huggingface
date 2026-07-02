from transformers import pipeline

models = {
    "DistilBERT": "distilbert-base-uncased-finetuned-sst-2-english",
    "RoBERTa": "cardiffnlp/twitter-roberta-base-sentiment-latest"
}

texts = [
    "I love this product. It is amazing!",
    "The service was terrible and disappointing.",
    "The experience was okay, nothing special."
]

for model_name, model_id in models.items():
    print(f"\n{'='*50}")
    print(f"Model: {model_name}")
    print(f"{'='*50}")

    classifier = pipeline("sentiment-analysis", model=model_id)

    for text in texts:
        result = classifier(text)[0]

        print(f"Text: {text}")
        print(f"Prediction: {result['label']}")
        print(f"Confidence: {result['score']:.2%}")
        print("-" * 50)
