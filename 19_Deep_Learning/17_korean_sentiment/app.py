from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# 서버 시작할 때 모델 한 번만 로드 (자동 다운로드)
classifier = pipeline(
    "sentiment-analysis",
    model="monologg/koelectra-base-finetuned-sentiment"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'error': '텍스트를 입력해주세요'}), 400

    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    return jsonify({
        'label': '긍정' if label == 'positive' else '부정',
        'confidence': f"{score * 100:.1f}%",
        'score': score
    })

if __name__ == '__main__':
    app.run(debug=True)