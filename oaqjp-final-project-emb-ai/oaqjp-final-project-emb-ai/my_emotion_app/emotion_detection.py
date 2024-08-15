import requests

def analyze_emotion(text):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_data = response.json()
        emotions = response_data["emotion"]["document"]["emotion"]
        formatted_output = (f"Joy: {emotions["joy"]}, Sadness: {emotions["sadness"]}, "
                            f"Anger: {emotions["anger"]}, Disgust: {emotions["disgust"]}, "
                            f"Fear: {emotions["fear"]}")
        return formatted_output
    else:
        return f"Error: {response.status_code} - {response.text}"
