"""This module is the main module for defining routes and instantiating the flask app"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def analyzer():
    """Analyze the response and return the emotion of the feeling and the dominant emotion"""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, \
        'joy': {response['joy']}, and 'sadness': {response['sadness']}. \
        The dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """Render the index.html file"""
    return render_template("index.html")


if __name__ == "__main__":
    # Host on the 5000 port
    app.run(host="0.0.0.0", port=5000)
