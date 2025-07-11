import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from app.modules.module1_input.input_handler import extract_video_id
from app.modules.module2_transcript.transcript_extractor import fetch_transcript

if __name__ == "__main__":
    url = input("Enter a YouTube video URL or ID: ")

    try:
        video_id = extract_video_id(url)
        transcript = fetch_transcript(video_id)

        print(f"\n✅ Transcript for video ID: {video_id}\n")
        for segment in transcript[:5]:  # Show first 5 segments
            print(f"[{segment['start']:.2f}s - {segment['start'] + segment['duration']:.2f}s]: {segment['text']}")

    except Exception as e:
        print(f"❌ Error: {e}")
