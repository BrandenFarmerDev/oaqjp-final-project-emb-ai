"""Flask web application for the EmotionDetection package."""

from flask import Flask, render_template, request
import requests

from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder="../templates", static_folder="../static")


@app.get("/")
def home():
    """Render the supplied sentiment-analysis interface."""
    return render_template("index.html")


@app.get("/emotionDetector")
def emotion_detector_route():
    """Analyze query text and return a readable summary or input error."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyze)
    except requests.exceptions.RequestException:
        return (
            "The emotion analysis service is temporarily unavailable. "
            "Please try again later."
        ), 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
