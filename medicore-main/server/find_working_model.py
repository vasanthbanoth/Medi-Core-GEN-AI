
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "gemini-2.0-flash-lite-preview-02-05",
    "gemini-flash-latest",
    "gemini-2.0-flash-lite-preview",
    "gemini-pro-latest",
    "gemini-2.0-flash", 
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash" # Trying again just in case
]

print(f"Testing models with API Key: {api_key[:10]}...")

for model_name in models_to_test:
    print(f"\nTesting: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello, simple test.")
        print(f"SUCCESS: {model_name}")
        print(f"Response: {response.text}")
        break # Found a working one!
    except Exception as e:
        print(f"FAILED: {model_name}")
        print(f"Error: {e}")
        time.sleep(1) # Avoid hammering the API
