import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from app.modules.module1_input.input_handler import extract_video_id
from app.modules.module2_transcript.transcript_extractor import fetch_transcript
from app.modules.module3_chunking.chunker import chunk_transcript

if __name__ == "__main__":
    url = input("Enter a YouTube video URL or ID: ")

    try:
        video_id = extract_video_id(url)
        transcript = fetch_transcript(video_id)
        chunks = chunk_transcript(transcript, max_chars=1000)

        print(f"\n✅ Created {len(chunks)} transcript chunks:\n")
        for i, chunk in enumerate(chunks[:3]):  # show only first 3
            print(f"\n--- Chunk {i+1} ---")
            print(f"[{chunk['start']:.2f}s - {chunk['end']:.2f}s]")
            print(chunk['text'][:300])  # preview first 300 chars

    except Exception as e:
        print(f"❌ Error: {e}")
