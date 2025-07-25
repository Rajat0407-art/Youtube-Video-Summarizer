import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_pro():
    """
    Initializes and returns a Gemini Pro model instance using API key.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")
