"""Tests for emotion detector."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test different emotions."""

    def test_emotions(self):
        """Check returned dominant emotions."""
        tests = {
            "I am happy": "joy",
            "I am angry": "anger",
            "I feel disgusted": "disgust",
            "I am sad": "sadness",
            "I am afraid": "fear",
        }
        for text, expected in tests.items():
            result = emotion_detector(text)
            self.assertEqual(result["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
