from input_handler import extract_video_id, fetch_video_metadata

if __name__ == "__main__":
    youtube_url = input("Enter a YouTube video URL or ID: ")
    
    try:
        video_id = extract_video_id(youtube_url)
        print(f"✅ Extracted Video ID: {video_id}")

        metadata = fetch_video_metadata(video_id)
        print("✅ Video Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"❌ Error: {e}")
