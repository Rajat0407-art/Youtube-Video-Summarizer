import google.generativeai as genai
import os
from dotenv import load_dotenv
from googletrans import Translator

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
translator = Translator()

# Supported language codes
LANGUAGE_CODES = {
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Telugu": "te",
    "Tamil": "ta",
    "English": "en"
}

def get_gemini_pro():
    return genai.GenerativeModel("gemini-1.5-flash")

def generate_summary_from_chapters(chapters, language="English"):
    """
    Generates a 2–3 paragraph natural language summary of the video using its chapters.
    Optionally translates the summary into the selected language.
    """
    if not chapters:
        return "⚠️ No chapters provided for summary."

    # Prepare input
    chapter_text = "\n".join(
        f"{chapter['timestamp']} - {chapter['title']}" for chapter in chapters
    )

    prompt = f"""
You are a helpful assistant that summarizes YouTube videos.

Based on the following list of video chapters with timestamps and titles, write a 2–3 paragraph natural-language summary of the video content. 
Do not list bullet points. Instead, write fluid, coherent paragraphs that summarize the narrative or explanation in the video.

Chapters:
{chapter_text}

Keep it concise but informative.
"""

    model = get_gemini_pro()
    try:
        response = model.generate_content(prompt)
        summary = response.text.strip()
    except Exception as e:
        return f"⚠️ Gemini API error: {str(e)}"

    # Translate if requested
    if language != "English":
        lang_code = LANGUAGE_CODES.get(language, "en")
        try:
            translated = translator.translate(summary, dest=lang_code)
            return translated.text
        except Exception as e:
            return f"{summary}\n\n⚠️ Translation failed: {str(e)}"

    return summary
