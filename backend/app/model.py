# backend/app/model.py
import os, joblib
from typing import Optional

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODEL_NAME = os.environ.get("MODEL_NAME", "document_classifier.pkl")
MODEL_PATH = os.path.join(ROOT, MODEL_NAME)

_model = None

def load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Place {MODEL_NAME} in repo root.")
        _model = joblib.load(MODEL_PATH)
    return _model

def predict(text: str) -> dict:
    """
    returns {label: str, confidence: float, proba: dict}
    """
    model = load_model()
    pred = model.predict([text])[0]
    probs = model.predict_proba([text])[0]
    # map class->prob
    classes = model.classes_
    proba_map = {classes[i]: float(probs[i]) for i in range(len(classes))}
    return {"label": pred, "confidence": float(max(probs)), "proba": proba_map}
