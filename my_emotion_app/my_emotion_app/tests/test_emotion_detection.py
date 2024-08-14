import unittest
from my_emotion_app.emotion_detection import analyze_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_analyze_emotion_success(self):
        text = "I am very happy today!"
        result = analyze_emotion(text)
        self.assertIn("Joy:", result)
        self.assertIn("Sadness:", result)
        self.assertIn("Anger:", result)
        self.assertIn("Disgust:", result)
        self.assertIn("Fear:", result)
    
    def test_analyze_emotion_failure(self):
        text = ""
        result = analyze_emotion(text)
        self.assertTrue(result.startswith("Error:"))

if __name__ == '__main__':
    unittest.main()
