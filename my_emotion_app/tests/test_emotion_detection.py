# my_emotion_app/tests/test_emotion_detection.py

import unittest
from emotion_detection import analyze_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_analyze_emotion_success(self):
        # Mock the analyze_emotion function response for testing
        text = "I am very happy today!"
        result = analyze_emotion(text)
        self.assertIn("Joy:", result)
        self.assertIn("Sadness:", result)
        self.assertIn("Anger:", result)
        self.assertIn("Disgust:", result)
        self.assertIn("Fear:", result)
    
    def test_analyze_emotion_failure(self):
        # Test with invalid data
        text = ""
        result = analyze_emotion(text)
        self.assertTrue(result.startswith("Error:"))

if __name__ == '__main__':
    unittest.main()
