# 💳 Credit Card Fraud Detection

A machine learning web application that detects fraudulent credit card transactions in real time.

## 🔍 About
Built as a Capstone Project using a real-world anonymized dataset of 284,807 transactions 
with only 492 fraud cases — a highly imbalanced classification problem.

## ⚙️ Tech Stack
- **Model**: Logistic Regression (Scikit-learn)
- **Backend**: FastAPI
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Language**: Python

## 📊 Model Performance
| Metric    | Score  |
|-----------|--------|
| Accuracy  | 93.40% |
| Precision | 98.90% |
| Recall    | 88.24% |
| F1 Score  | 93.26% |

## 🚀 How to Run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your `fraud_model.pkl` file to the root folder
4. Run: `python -m uvicorn main:app --reload`
5. Open: `http://127.0.0.1:8000`

## 👨‍💻 Author
Azhar Mahmood
