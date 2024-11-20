import requests
import json


def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, json=body, headers=headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    response_dict = json.loads(response.text)

    emotion_data = response_dict["emotionPredictions"][0]["emotion"]

    anger_score = emotion_data["anger"]
    disgust_score = emotion_data["disgust"]
    fear_score = emotion_data["fear"]
    joy_score = emotion_data["joy"]
    sadness_score = emotion_data["sadness"]

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(scores, key=scores.get)

    scores["dominant_emotion"] = dominant_emotion

    return scores
