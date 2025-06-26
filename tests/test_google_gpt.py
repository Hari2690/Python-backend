import os
import requests
import json
from pymongo import MongoClient
import nltk
from transformers import pipeline

nltk.download('punkt')

# Initialize emotion classifier once (global)
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def test_google_gpt_api(text):
    detect_and_store_emotion(text)  # Detect and store emotion before API call
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyD41Dv4rg7RaWJO3Nq_XpW9o_NoxaZ21oQ"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": text}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    assert response.status_code == 200, f"API call failed: {response.status_code} {response.text}"
    try:
        candidates = response.json().get("candidates", [])
        text = candidates[0]["content"]["parts"][0]["text"] if candidates else "No response text found."
    except (KeyError, IndexError, TypeError):
        text = "No response text found."
    print("Response:", text)
    # Detect and print emotion for the response text
    # emotions = te.get_emotion(text)
    # dominant_emotion = max(emotions, key=emotions.get) if emotions else "unknown"
    # print(f"Detected emotion: {dominant_emotion}")
    return text

def detect_and_store_emotion(text, mongo_uri="mongodb://localhost:27017/", db_name="emotion_db", collection_name="emotions"):
    # Advanced emotion detection using transformers
    results = emotion_classifier(text)
    # Get the most probable emotion
    if results and isinstance(results, list):
        sorted_results = sorted(results[0], key=lambda x: x['score'], reverse=True)
        dominant_emotion = sorted_results[0]['label'] if sorted_results else "unknown"
        emotions = {item['label']: float(item['score']) for item in sorted_results}
    else:
        dominant_emotion = "unknown"
        emotions = {}
    print(f"Detected emotion: {dominant_emotion}")

    # Store in MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]
    doc = {"text": text, "emotion": dominant_emotion, "emotions": emotions}
    result = collection.insert_one(doc)
    print(f"Stored in MongoDB with id: {result.inserted_id}")
    return dominant_emotion

if __name__ == "__main__":
    response_text, _ = test_google_gpt_api("How are you today?")
    detect_and_store_emotion(response_text)
