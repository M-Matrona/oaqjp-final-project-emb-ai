import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotions(self):
        # List of test cases with statements and expected emotions
        test_cases = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]

        # Loop through each test case
        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement):
                emotions_dict = emotion_detector(statement)
                self.assertEqual(emotions_dict.get('dominant_emotion'), expected_emotion)

if __name__ == '__main__':
    unittest.main()