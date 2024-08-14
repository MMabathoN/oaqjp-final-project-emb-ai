# my_emotion_app/app.py

from flask import Flask, request, jsonify
from my_emotion_app.emotion_detection import analyze_emotion


app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = analyze_emotion(text)
    return jsonify({'emotions': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
