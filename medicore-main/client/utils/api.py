import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import io

# Load environment variables (for local development)
load_dotenv()

def configure_genai():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return False
    genai.configure(api_key=api_key)
    return True

def upload_pdfs_api(files):
    # RAG feature disabled for Streamlit Cloud free tier
    # Returning a mock response to prevent errors if called
    class MockResponse:
        status_code = 200
        text = "PDF upload disabled in this demo version."
        def json(self):
            return {"message": self.text}
    return MockResponse()

def ask_question(question):
    if not configure_genai():
        class ErrorResponse:
            status_code = 500
            text = "GOOGLE_API_KEY not found in environment variables."
            def json(self): return {"response": self.text}
        return ErrorResponse()

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(question)
        
        # Mimic the previous API response structure for compatibility
        class SuccessResponse:
            status_code = 200
            def json(self):
                return {"response": response.text}
        return SuccessResponse()

    except Exception as e:
        class ExceptionResponse:
            status_code = 500
            text = str(e)
            def json(self): return {"error": str(e)}
        return ExceptionResponse()

def get_answer_with_image(question: str, image_file):
    """Sends a question and an image to Google Gemini."""
    if not configure_genai():
        class ErrorResponse:
            status_code = 500
            text = "GOOGLE_API_KEY not found in environment variables."
            def json(self): return {"answer": self.text}
        return ErrorResponse()

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Convert uploaded file to PIL Image
        image = Image.open(image_file)
        
        response = model.generate_content([question, image])
        
        # Mimic the previous API response structure
        class SuccessResponse:
            status_code = 200
            def json(self):
                return {"answer": response.text, "image_description": "Processed by Gemini 1.5 Flash"}
        return SuccessResponse()

    except Exception as e:
        class ExceptionResponse:
            status_code = 500
            text = str(e)
            def json(self): return {"error": str(e)}
        return ExceptionResponse()
