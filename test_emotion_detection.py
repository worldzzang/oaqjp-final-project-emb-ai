import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = emotion_detector("I am so angry!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = emotion_detector("I feel disgusted right now")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_fear(self):
        result = emotion_detector("I am so scared")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_sadness(self):
        result = emotion_detector("I feel so sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
