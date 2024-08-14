import unittest
from emotion_detection import analyze_emotion

class TestEmotionDetection(unittest.TestCase):
    def test_analyze_emotion(self):
        # Example text to analyze
        text = "I am very happy today!"
        
        # Call the function
        result = analyze_emotion(text)
        
        # Check that 'joy' is in the result string
        self.assertIn('Joy:', result)
        
        # Extract the joy value from the result string and assert it's greater than 0
        joy_score = float(result.split('Joy: ')[1].split(',')[0])
        self.assertGreater(joy_score, 0)

if __name__ == '__main__':
    unittest.main()
