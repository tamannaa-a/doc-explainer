# backend/app/api.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .ocr_utils import extract_text_from_pdf, save_upload_tmp
from .model import predict
from .explain import explain_text
import os

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    # accept only pdf for now
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    tmp_path = save_upload_tmp(file)
    try:
        text = extract_text_from_pdf(tmp_path)
    finally:
        # keep safe: remove temp file
        try: os.remove(tmp_path)
        except Exception: pass

    if not text or not text.strip():
        return JSONResponse({"error":"No extractable text found (try higher-quality PDF or scanned OCR)."}, status_code=400)

    pred = predict(text)
    explanation = explain_text(pred["label"], text)
    return {
        "document_type": pred["label"],
        "confidence": pred["confidence"],
        "proba": pred["proba"],
        "explanation": explanation,
        "preview": text[:3000]
    }
