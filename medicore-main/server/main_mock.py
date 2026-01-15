import os
import time
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Medical Assistant API (MOCK)", description="Mock API for testing UI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["healthcheck"])
async def root():
    return {"message": "Hello World (Mock Mode)"}

@app.post("/ask_with_image", tags=["Q&A"])
async def handle_ask_with_image(
    question: str = Form(...),
    image: UploadFile = File(...)
):
    # Simulate processing time
    time.sleep(2)
    return {
        "result": "This is a MOCK response. The AI models are still installing in the background. Please wait for the full installation to complete for real answers.",
        "image_description": "Mock image description: A medical image.",
        "source_documents": []
    }

@app.post("/ask", tags=["Q&A"])
async def ask_question(
    question: str = Form(...), # or json body depending on original implementation, let's assume form for consistency or check
):
     return {
        "result": "This is a MOCK response.",
        "source_documents": []
    }
