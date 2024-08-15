# oaqjp-final-project-emb-ai/app.py

from flask import Flask, request, jsonify
from my_emotion_app.emotion_detection import analyze_emotion

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text')
        if not text:
            return jsonify({"error": "No text provided"}), 400
        result = analyze_emotion(text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
