"""Emotion Detector Flask Application"""
from flask import Flask, request, render_template
from emotion_detection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Route for emotion detection"""
    text = request.args.get('textToAnalyse')
    result = emotion_predictor(text)
    if result == "Invalid text! Please try again.":
        return result, 400
    return result

@app.route("/")
def index():
    """Route for index page"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
