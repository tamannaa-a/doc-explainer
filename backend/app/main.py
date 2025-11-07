# backend/app/main.py
from fastapi import FastAPI
from .api import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DocExplainer Enterprise API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
