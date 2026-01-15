from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from modules.gemini_handler import ask_gemini_with_image
from logger import logger

router = APIRouter()

@router.post("/ask_with_image", tags=["Q&A"])
async def handle_ask_with_image(
    question: str = Form(...),
    image: UploadFile = File(...)
):
    """
    Receives image and text, and uses Google Gemini to answer.
    """
    try:
        logger.info("Receiving image for Gemini analysis...")
        image_bytes = await image.read()
        
        # Use Gemini Module
        answer_text = ask_gemini_with_image(image_bytes, question)
        
        logger.info("Successfully answered query with image via Gemini.")
        
        # Return in the format expected by the frontend
        # (The frontend likely expects a dict with 'result' or similar, but let's check app.py response handling if needed.
        #  Looking at previous code, it returned 'answer' dict. Let's mimic a simple result.)
        return {"answer": answer_text}

    except Exception as e:
        logger.exception("Error in /ask_with_image endpoint")
        return JSONResponse(status_code=500, content={"error": str(e)})
