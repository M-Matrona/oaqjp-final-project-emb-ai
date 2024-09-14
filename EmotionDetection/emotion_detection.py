"""
This module provides a function for emotion detection 
using the Watson NLP service.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the provided text using Watson's NLP EmotionPredict service.

    Args:
        text_to_analyse (str): The text for which emotions need to be detected.

    Returns:
        str: The text attribute of the response containing emotion analysis results.
        If an error occurs, returns an error message with status code.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=60)

        if response.status_code == 200:
            emotions=response.json()['emotionPredictions'][0]['emotion']

            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            dominant_emotion = max(emotions, key=emotions.get)

            return {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }

        if response.status_code==400:

            return {
                        'anger': None,
                        'disgust': None,
                        'fear': None,
                        'joy': None,
                        'sadness': None,
                        'dominant_emotion': None
                    }

        return f"Error: {response.status_code}, {response.text}"    
        
    except requests.Timeout:
        return "Error: Request timed out"

