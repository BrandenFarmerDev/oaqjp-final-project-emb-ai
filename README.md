# Final project

An emotion-detection web application built with Python, Flask, and the IBM Watson NLP Emotion Predict service. It scores anger, disgust, fear, joy, and sadness, then reports the dominant emotion. The project includes the `EmotionDetection` package, unit tests, a small browser interface, validation for empty text, and static-analysis evidence.

## Run locally

Use Python 3.10 or newer. From the repository root, install the dependencies and start the Flask server:

```powershell
python -m pip install -r requirements.txt
python final_project/server.py
```

Open http://localhost:5000 and enter a sentence. The application calls the Watson NLP endpoint, so the service must be reachable from your environment. Run the deterministic unit tests with:

```powershell
python -m unittest discover -s final_project -p "test_*.py" -v
```

The HTTP response schema and error handling are tested with mocked network responses; tests do not require a live NLP endpoint.
