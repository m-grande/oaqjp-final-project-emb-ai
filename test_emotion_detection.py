from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy_result = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(joy_result, "joy")

        anger_result = emotion_detector("I am really mad about this")[
            "dominant_emotion"
        ]
        self.assertEqual(anger_result, "anger")

        disgust_result = emotion_detector("I feel disgusted just hearing about this")[
            "dominant_emotion"
        ]
        self.assertEqual(disgust_result, "disgust")

        sadness_result = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(sadness_result, "sadness")

        fear_result = emotion_detector("I am really afraid that this will happen")[
            "dominant_emotion"
        ]
        self.assertEqual(fear_result, "fear")


unittest.main()
