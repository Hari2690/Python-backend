# Module to handle Google GPT API key

def get_google_gpt_api_key():
    """Retrieve the Google GPT API key from a secure location or environment variable."""
    import os
    return os.getenv("GOOGLE_GPT_API_KEY", "")
