# 🎥 YouTube Video Summarizer & Chapterizer

A powerful AI-driven tool to automatically generate chapters and concise summaries from YouTube videos. Just paste a YouTube URL — get structured chapters, a clean summary, and key insights instantly!

---

## 🚀 Features

✅ Extract video transcripts directly from YouTube  
✅ Automatically chunk long transcripts intelligently  
✅ Generate meaningful chapters with titles and timestamps (using Gemini API)  
✅ Create concise, high-level summaries of the entire video  
✅ Supports multi-language transcripts (e.g., English, Hindi, etc.)  
✅ Interactive and user-friendly Streamlit frontend  
✅ Display video metadata (title, description, duration, thumbnail)

---

## 🛠️ Tech Stack

- **Python** (backend and orchestration)
- **YouTube Data API v3** (fetch video metadata and transcripts)
- **Gemini API** (for chapter and summary generation)
- **LangChain** (chunking logic and prompt templates)
- **Streamlit** (frontend UI)
- **tqdm** (progress visualization during chunking)

---

GEMINI_API_KEY=your_gemini_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
