import sys
import os

# Add root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from app.modules.module1_input.input_handler import extract_video_id
from app.modules.module2_transcript.transcript_extractor import fetch_transcript
from app.modules.module3_chunking.chunker import chunk_transcript
from app.modules.module5_summary.summary_generator import generate_summary_from_chunks

if __name__ == "__main__":
    url = input("Enter a YouTube video URL or ID: ")

    try:
        video_id = extract_video_id(url)
        transcript = fetch_transcript(video_id)
        chunks = chunk_transcript(transcript)
        summary = generate_summary_from_chunks(chunks)

        print("\n✅ Video Summary:\n")
        print(summary)

        # Optional: Save output
        with open("sample_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)

    except Exception as e:
        print(f"❌ Error: {e}")
