# 💬 Sentiment Classification Using Hugging Face Transformers

An NLP project that compares multiple pretrained transformer models for sentiment analysis. The application allows users to classify text sentiment in real time through an interactive Streamlit interface.

---

## 📌 Overview

This project evaluates different transformer-based models for sentiment classification using Hugging Face Transformers.

Users can enter any text and receive:

- Sentiment prediction
- Confidence score
- Results from different pretrained models

The goal is to compare model performance while providing an easy-to-use web application.

---

## ✨ Features

- Real-time sentiment prediction
- Multiple pretrained transformer models
- Interactive Streamlit interface
- Confidence score for every prediction
- Easy model comparison

---

## 🛠️ Tech Stack

- Python
- Hugging Face Transformers
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- PyTorch

---

## 📂 Project Structure

```
sentiment-classification-huggingface/
│
├── app.py
├── evaluate_models.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ragadsalharbi/sentiment-classification-huggingface.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 Example

**Input**

```
I really enjoyed this movie.
```

**Prediction**

```
Positive
Confidence: 99%
```

---

## 🔮 Future Improvements

- Add support for Arabic sentiment analysis
- Compare additional transformer models
- Deploy the application online
- Improve visualization of model performance

---

## 👩‍💻 Author

**Raghad Alharbi**

- GitHub: https://github.com/ragadsalharbi
- LinkedIn: https://www.linkedin.com/in/raghad-alharbi-38a61b326
