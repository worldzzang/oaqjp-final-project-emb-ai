import requests
import json

def emotion_detector(text_to_analyse):

    if text_to_analyse.strip() == "":
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    x = requests.post(url, json = myobj, headers=header)

    if x.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    formatted_response = json.loads(x.text)
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotions_dict = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}

def emotion_predictor(text_to_analyse):
    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    output = "For the given statement, the system response is 'anger': " + str(anger) + ", 'disgust': " + str(disgust) + ", 'fear': " + str(fear) + ", 'joy': " + str(joy) + " and 'sadness': " + str(sadness) + ". The dominant emotion is " + dominant_emotion + "."
    return output
