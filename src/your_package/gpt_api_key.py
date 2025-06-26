# This module has been renamed. Please use 'google_gpt.py' instead.

# Module to handle GPT API key

def get_gpt_api_key():
    """Retrieve the GPT API key from a secure location or environment variable."""
    import os
    return os.getenv("GPT_API_KEY", "")
