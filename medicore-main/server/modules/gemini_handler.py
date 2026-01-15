

import os
from PIL import Image
import io
from logger import logger

def ask_gemini_with_image(image_bytes, user_question):
    """
    Sends an image and a question to Google Gemini 1.5 Flash.
    """
    try:
        try:
            import google.generativeai as genai
        except ImportError:
            raise ImportError("The 'google-generativeai' library is still installing. Please wait a moment and try again.")

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

        genai.configure(api_key=api_key)

        # Use Gemini 1.5 Flash for speed and multimodal capabilities
        model = genai.GenerativeModel('gemini-flash-latest')

        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        logger.info(f"Sending request to Gemini: {user_question}")
        
        response = model.generate_content([user_question, image])
        
        logger.info("Received response from Gemini")
        return response.text

    except Exception as e:
        logger.exception("Error in ask_gemini_with_image")
        raise e
