"""Unit tests for the EmotionDetection package."""

import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector
from EmotionDetection.emotion_detection import EMOTION_PREDICT_URL, MODEL_ID


class EmotionDetectorTests(unittest.TestCase):
    """Verify service calls, normalized results, and HTTP 400 handling."""

    def make_response(self, scores, status_code=200):
        """Build a small Watson-compatible response object for a test."""
        response = Mock()
        response.status_code = status_code
        response.text = json.dumps(
            {"emotionPredictions": [{"emotion": scores}]}
        )
        response.json.return_value = json.loads(response.text)
        response.raise_for_status.return_value = None
        return response

    def test_emotion_detector_returns_all_scores_and_joy(self):
        """A high joy score is returned with the expected complete schema."""
        scores = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.91,
            "sadness": 0.04,
        }
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=self.make_response(scores),
        ) as post:
            result = emotion_detector("I am glad this happened")

        self.assertEqual(result, {**scores, "dominant_emotion": "joy"})
        post.assert_called_once()
        self.assertEqual(post.call_args.args[0], EMOTION_PREDICT_URL)
        self.assertEqual(
            post.call_args.kwargs["headers"]["grpc-metadata-mm-model-id"],
            MODEL_ID,
        )
        self.assertEqual(
            post.call_args.kwargs["json"],
            {"raw_document": {"text": "I am glad this happened"}},
        )

    def test_required_dominant_emotions(self):
        """Each course-required statement maps to its expected emotion."""
        cases = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )
        for statement, dominant in cases:
            scores = {name: 0.01 for name in
                      ("anger", "disgust", "fear", "joy", "sadness")}
            scores[dominant] = 0.9
            with self.subTest(statement=statement), patch(
                "EmotionDetection.emotion_detection.requests.post",
                return_value=self.make_response(scores),
            ):
                self.assertEqual(
                    emotion_detector(statement)["dominant_emotion"], dominant
                )

    def test_http_400_returns_none_for_every_result(self):
        """Invalid blank input returns all six required keys with None values."""
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=self.make_response({}, status_code=400),
        ):
            self.assertEqual(
                emotion_detector(""),
                {
                    "anger": None,
                    "disgust": None,
                    "fear": None,
                    "joy": None,
                    "sadness": None,
                    "dominant_emotion": None,
                },
            )

    def test_non_400_http_errors_are_raised(self):
        """Unexpected service errors are surfaced to the caller."""
        response = self.make_response({}, status_code=503)
        response.raise_for_status.side_effect = RuntimeError("service unavailable")
        with patch(
            "EmotionDetection.emotion_detection.requests.post",
            return_value=response,
        ), self.assertRaises(RuntimeError):
            emotion_detector("test")


if __name__ == "__main__":
    unittest.main()
