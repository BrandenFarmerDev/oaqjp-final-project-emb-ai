"""Call the Watson NLP service and normalize emotion predictions."""

import json

import requests

EMOTION_PREDICT_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and dominant emotion for input text."""
    response = requests.post(
        EMOTION_PREDICT_URL,
        headers={"grpc-metadata-mm-model-id": MODEL_ID},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    if response.status_code == 400:
        return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}
    response.raise_for_status()

    response_text = response.text
    payload = json.loads(response_text) if response_text else response.json()
    emotion_scores = payload["emotionPredictions"][0]["emotion"]
    scores = {name: emotion_scores[name] for name in EMOTION_NAMES}
    scores["dominant_emotion"] = max(EMOTION_NAMES, key=scores.get)
    return scores
