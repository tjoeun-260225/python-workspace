# app.py
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# .keras 포맷으로 로드
model = load_model('sentiment_model.keras')
with open('word_index.pkl', 'rb') as f:
    word_index = pickle.load(f)

MAX_LEN = 200
NUM_WORDS = 10000

def preprocess(text):
    words = text.lower().split()
    encoded = []
    for word in words:
        idx = word_index.get(word, 2) + 3
        if idx < NUM_WORDS:
            encoded.append(idx)
        else:
            encoded.append(2)
    padded = pad_sequences([encoded], maxlen=MAX_LEN)
    return padded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'error': '텍스트를 입력해주세요'}), 400

    processed = preprocess(text)
    score = model.predict(processed)[0][0]

    result = {
        'score': float(score),
        'label': '긍정' if score >= 0.5 else '부정',
        'confidence': f"{max(score, 1-score)*100:.1f}%"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)