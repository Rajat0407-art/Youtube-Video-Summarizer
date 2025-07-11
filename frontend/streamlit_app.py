import sys
import os
import json
from pathlib import Path
import streamlit as st

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Module imports
from app.modules.module1_input.input_handler import extract_video_id, fetch_video_metadata
from app.modules.module2_transcript.transcript_extractor import fetch_transcript
from app.modules.module3_chunking.chunker import chunk_transcript
from app.modules.module4_chaptering.chapter_generator import generate_chapters_from_chunks
from app.modules.module5_summary.summary_generator import generate_summary_from_chapters  # <- Multi-language version

# Streamlit UI setup
st.set_page_config(page_title="YouTube Chapterizer + Summarizer", layout="centered", page_icon="🎬")
st.title("🎬 YouTube Chapterizer + Summarizer")

# User input
video_input = st.text_input("Enter a YouTube video URL or ID:")

# Language selection
language = st.selectbox(
    "Choose summary language:",
    ["English", "Hindi", "Spanish", "French", "German", "Marathi", "Bengali", "Gujarati", "Telugu", "Tamil"]
)

if video_input:
    try:
        # Extract video ID and metadata
        video_id = extract_video_id(video_input)
        metadata = fetch_video_metadata(video_id)
        st.subheader("📺 Video Metadata")
        st.markdown(f"**Title:** {metadata['title']}")
        st.markdown(f"**Duration:** {metadata['duration']}")

        # Try fetching transcript
        try:
            transcript = fetch_transcript(video_id)
            st.success(f"✅ Transcript for video ID: {video_id} fetched successfully.")
        except ValueError:
            transcript = ""
            st.error("❌ No transcript available for this video.")

        # Manual transcript input
        if not transcript:
            st.warning("⚠️ Transcript not available. You can paste a manual transcript below:")
            manual_transcript = st.text_area("Paste transcript here (with timestamps if possible):")
            if manual_transcript.strip():
                transcript = manual_transcript.strip()

        if transcript:
            # Chunking
            chunks = chunk_transcript(transcript)
            st.success(f"✅ Created {len(chunks)} transcript chunks.")

            # Chapter Generation
            raw_chapters = generate_chapters_from_chunks(chunks)

            # Ensure chapters are parsed JSON list
            if isinstance(raw_chapters, str):
                try:
                    json_start = raw_chapters.find('[')
                    json_end = raw_chapters.rfind(']') + 1
                    raw_chapters = raw_chapters[json_start:json_end]
                    chapters = json.loads(raw_chapters)
                except json.JSONDecodeError:
                    st.error("❌ Failed to parse chapter response.")
                    chapters = []
            else:
                chapters = raw_chapters

            # Display chapters
            if chapters:
                st.subheader("📌 Chapter Suggestions:")
                for chapter in chapters:
                    if isinstance(chapter, dict) and 'timestamp' in chapter and 'title' in chapter:
                        st.markdown(f"**{chapter['timestamp']}** — {chapter['title']}")
                    else:
                        st.warning("⚠️ Invalid chapter format detected.")

                # Generate and show summary
                summary_paragraph = generate_summary_from_chapters(chapters, language=language)
                if summary_paragraph:
                    st.subheader(f"📝 Video Summary ({language}):")
                    st.markdown(summary_paragraph)
                else:
                    st.warning("⚠️ Could not generate summary from chapters.")
            else:
                st.error("❌ No valid chapters to display or summarize.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
