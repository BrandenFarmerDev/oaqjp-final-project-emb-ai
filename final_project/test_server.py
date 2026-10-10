"""Tests for the Flask interface without calling the hosted Watson service."""

import unittest
from unittest.mock import patch

import requests

from server import app


class EmotionDetectorRouteTests(unittest.TestCase):
    """Verify page routing, readable results, and blank-input feedback."""

    def setUp(self):
        """Create a Flask test client for each test case."""
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_renders_provided_interface(self):
        """The landing page serves the supplied HTML template."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NLP - Emotion Detection", response.data)

    @patch("server.emotion_detector")
    def test_emotion_route_formats_scores(self, detector):
        """A valid analysis is rendered as the course-requested summary."""
        detector.return_value = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.9,
            "sadness": 0.04,
            "dominant_emotion": "joy",
        }
        response = self.client.get("/emotionDetector?textToAnalyze=hello")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"dominant emotion is joy", response.data)
        detector.assert_called_once_with("hello")

    def test_blank_analysis_returns_error_without_calling_watson(self):
        """Blank input uses the real route and does not need Watson access."""
        response = self.client.get("/emotionDetector?textToAnalyze=")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True),
                         "Invalid text! Please try again!")

    def test_whitespace_analysis_returns_invalid_text(self):
        """Whitespace-only input is treated as blank before the service call."""
        response = self.client.get("/emotionDetector?textToAnalyze=%20%20%20")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True),
                         "Invalid text! Please try again!")

    @patch(
        "server.emotion_detector",
        side_effect=requests.exceptions.Timeout("unavailable"),
    )
    def test_watson_timeout_returns_service_unavailable(self, detector):
        """Service timeouts return 503 without made-up emotion scores."""
        response = self.client.get("/emotionDetector?textToAnalyze=hello")
        self.assertEqual(response.status_code, 503)
        self.assertIn(b"service is temporarily unavailable", response.data)
        self.assertNotIn(b"dominant emotion", response.data)
        detector.assert_called_once_with("hello")


if __name__ == "__main__":
    unittest.main()
