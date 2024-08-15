import unittest
from my_emotion_app.emotion_detection import analyze_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_analyze_emotion(self):
        text = "I am very happy today!"
        result = analyze_emotion(text)
        self.assertIn("Joy", result)

if __name__ == "__main__":
    unittest.main()
