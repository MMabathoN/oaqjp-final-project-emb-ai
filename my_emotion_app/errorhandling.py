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
    
    try:
        # Make the POST request to the API
        response = requests.post(url, headers=headers, json=payload)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        response_data = response.json()
        emotions = response_data['emotion']['document']['emotion']
        
        # Format the output
        formatted_output = (f"Joy: {emotions.get('joy', 'N/A')}, Sadness: {emotions.get('sadness', 'N/A')}, "
                            f"Anger: {emotions.get('anger', 'N/A')}, Disgust: {emotions.get('disgust', 'N/A')}, "
                            f"Fear: {emotions.get('fear', 'N/A')}")
        return formatted_output
    
    except requests.exceptions.RequestException as e:
        # Handle the error if the request was not successful
        return f"Error: {str(e)}"

# Example usage
text = "I'm feeling very happy today!"
print(analyze_emotion(text))
