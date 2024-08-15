import requests

def analyze_emotion(text):
    # Define the URL and headers based on the provided information
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Prepare the JSON payload with the text to analyze
    payload = {
        "raw_document": {
            "text": text
        }
    }
    
    # Make the POST request to the API
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        emotions = response_data['emotion']['document']['emotion']
        
        # Format the output
        formatted_output = (f"Joy: {emotions['joy']}, Sadness: {emotions['sadness']}, "
                            f"Anger: {emotions['anger']}, Disgust: {emotions['disgust']}, "
                            f"Fear: {emotions['fear']}")
        return formatted_output
    else:
        # Handle the error if the request was not successful
        return f"Error: {response.status_code} - {response.text}"

