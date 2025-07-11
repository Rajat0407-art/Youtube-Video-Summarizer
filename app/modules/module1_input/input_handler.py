import re
from urllib.parse import urlparse, parse_qs
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(youtube_url_or_id: str) -> str:
    """
    Extracts YouTube video ID from a full URL or returns it if already an ID.
    """
    # If it's already a valid video ID (11 characters)
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", youtube_url_or_id):
        return youtube_url_or_id

    # Parse from full URL
    parsed_url = urlparse(youtube_url_or_id)
    query_params = parse_qs(parsed_url.query)
    if "v" in query_params:
        return query_params["v"][0]

    # Short URL format
    if parsed_url.netloc == "youtu.be":
        return parsed_url.path[1:]

    raise ValueError("Invalid YouTube URL or video ID.")

def fetch_video_metadata(video_id: str) -> dict:
    """
    Fetch video metadata using YouTube Data API.
    """
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )
    response = request.execute()

    items = response.get("items", [])
    if not items:
        raise ValueError("No video found with the given ID.")

    video = items[0]
    metadata = {
        "video_id": video_id,
        "title": video["snippet"]["title"],
        "channel": video["snippet"]["channelTitle"],
        "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
        "description": video["snippet"]["description"],
        "duration": video["contentDetails"]["duration"]  # ISO 8601 format
    }
    return metadata
