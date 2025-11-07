# backend/app/ocr_utils.py
import io, os
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import tempfile

def extract_text_from_pdf(path: str) -> str:
    """
    Try text extraction using pdfminer. If empty, fallback to OCR on pages.
    """
    try:
        text = extract_text(path)
        if text and text.strip():
            return text
    except Exception:
        pass
    # fallback OCR
    return ocr_pdf_images(path)

def ocr_pdf_images(path: str) -> str:
    pages_text = []
    # convert pages to images (requires poppler)
    pages = convert_from_path(path, dpi=200)
    for page in pages:
        text = pytesseract.image_to_string(page)
        pages_text.append(text)
    return "\n\n".join(pages_text)

def save_upload_tmp(upload_file) -> str:
    suffix = os.path.splitext(upload_file.filename)[1] or ".pdf"
    fd, tmp_path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    with open(tmp_path, "wb") as f:
        f.write(upload_file.file.read())
    return tmp_path
