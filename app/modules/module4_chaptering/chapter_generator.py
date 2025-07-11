import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_model():
    return genai.GenerativeModel("gemini-1.5-flash")

def generate_chapters_from_chunks(chunks):
    if not chunks:
        return []

    # Prepare prompt
    prompt = """
You are a helpful assistant that creates structured YouTube video chapters from transcript chunks.

Based on the following transcript chunks, generate a list of chapters in JSON format like:
[
  {"timestamp": "00:00", "title": "Introduction"},
  {"timestamp": "01:35", "title": "Main Concept"},
  ...
]

Only return valid JSON, nothing else.

Transcript Chunks:
"""

    for chunk in chunks:
        prompt += f"\n{chunk}"

    try:
        model = get_gemini_model()
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Chapter generation error: {str(e)}"
