# train/train_model_colab.py
!pip install scikit-learn joblib pdfplumber

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# small synthetic dataset — replace with your real data or extracted pdf text
texts = [
    "Claim form: vehicle hit a pole, policy 123, loss details included.",
    "Settlement letter: approved payment of $1200 after deductible.",
    "Invoice: parts and labour for repair, total due $450.",
    "Mechanic invoice: replaced bumper and headlight.",
    "Inspection report: roof damage from hail observed and photographed.",
    "Inspection report: water leakage in basement, recommended repair.",
    "Customer query about premium renewal and policy terms.",
]
labels = [
    "Claim Document",
    "Claim Document",
    "Invoice",
    "Invoice",
    "Inspection Report",
    "Inspection Report",
    "Other",
]

model = make_pipeline(TfidfVectorizer(ngram_range=(1,2), max_features=5000), LogisticRegression(max_iter=1000))
model.fit(texts, labels)
joblib.dump(model, "document_classifier.pkl")
print("Saved model: document_classifier.pkl")
