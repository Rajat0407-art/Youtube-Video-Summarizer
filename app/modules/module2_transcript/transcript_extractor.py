from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api._errors import VideoUnavailable

def fetch_transcript(video_id: str) -> list:
    """
    Fetches the transcript for the given video ID.
    Returns a list of segments with 'text', 'start', and 'duration'.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript

    except VideoUnavailable:
        raise ValueError("The video is unavailable.")

    except TranscriptsDisabled:
        raise ValueError("The video has transcripts disabled.")

    except NoTranscriptFound:
        raise ValueError("No transcript available for this video.")

    except Exception as e:
        raise ValueError(f"Failed to fetch transcript: {str(e)}")
