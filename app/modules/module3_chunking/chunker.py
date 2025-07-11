def chunk_transcript(transcript, max_chunk_length=1000, overlap=200):
    """
    Chunks the transcript into overlapping segments of specified character length.

    Parameters:
        transcript (list): List of transcript segments with 'text' and 'start'.
        max_chunk_length (int): Max number of characters per chunk.
        overlap (int): Number of overlapping characters between chunks.

    Returns:
        list: List of chunked transcript strings.
    """
    if not transcript:
        return []

    full_text = " ".join([segment["text"] for segment in transcript])
    chunks = []

    start = 0
    while start < len(full_text):
        end = start + max_chunk_length
        chunk = full_text[start:end]
        chunks.append(chunk.strip())
        start += max_chunk_length - overlap

    return chunks
