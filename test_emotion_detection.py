from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotions(unittest.TestCase):
    def test_emotion(self):
        joy_text = 'I am glad this happened'
        joy_emotion = emotion_detector(joy_text)['dominant_emotion']
        self.assertEqual(joy_emotion,'joy')
        ###
        anger_text = 'I am really mad about this'
        anger_emotion = emotion_detector(anger_text)['dominant_emotion']
        self.assertEqual(anger_emotion,'anger')
        ###
        disgust_text = 'I feel disgusted just hearing about this'
        disgust_emotion = emotion_detector(disgust_text)['dominant_emotion']
        self.assertEqual(disgust_emotion,'disgust')
        ###
        sadness_text = 'I am so sad about this'
        sadness_emotion = emotion_detector(sadness_text)['dominant_emotion']
        self.assertEqual(sadness_emotion,'sadness')
        ###
        fear_text = 'I am really afraid that this will happen'
        fear_emotion = emotion_detector(fear_text)['dominant_emotion']
        self.assertEqual(fear_emotion,'fear')
unittest.main()