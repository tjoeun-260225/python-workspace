from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# 힌트: 'models/weather_model.keras'
model = load_model('models/weather_model.keras')

# 날씨 클래스 순서 (폴더 알파벳 순서)
날씨목록 = ['cloudy', 'fogsmog', 'frost', 'lightning',
        'rain', 'rainbow', 'sandstorm', 'shine',
        'snow', 'thunder', 'tornado']

날씨이모지 = {
    'cloudy'   : '🌥️',
    'fogsmog'  : '🌫️',
    'frost'    : '🧊',
    'lightning': '🌩️',
    'rain'     : '🌧️',
    'rainbow'  : '🌈',
    'sandstorm': '🌊',
    'shine'    : '🌞',
    'snow'     : '❄️',
    'thunder'  : '⛈️',
    'tornado'  : '🌪️'
}

날씨한국어 = {
    'cloudy'   : '흐림',
    'fogsmog'  : '안개',
    'frost'    : '서리',
    'lightning': '번개',
    'rain'     : '비',
    'rainbow'  : '무지개',
    'sandstorm': '모래폭풍',
    'shine'    : '맑음',
    'snow'     : '눈',
    'thunder'  : '천둥',
    'tornado'  : '토네이도'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']

    # TODO 2: 이미지 크기를 채우세요
    # 힌트: 모델 훈련할 때 150x150 으로 했어요
    image = Image.open(io.BytesIO(file.read())).convert('RGB').resize((150, 150))
    image = np.array(image) / 255.0
    image = image.reshape(1, 150, 150, 3)

    pred = model.predict(image)[0]   # 11개 확률 배열

    # TODO 3: 가장 높은 확률의 인덱스를 구하세요
    # 힌트: np.argmax(pred)
    최고인덱스 = np.argmax(pred)
    최고확률   = pred[최고인덱스] * 100

    # TODO 4: 신뢰도 기준점 설정
    # 확률이 50% 미만이면 "알 수 없는 날씨" 처리
    신뢰도기준 = 50   # 힌트: 50

    if 최고확률 >= 신뢰도기준:
        날씨영어 = 날씨목록[최고인덱스]
        result   = 날씨한국어[날씨영어]
        emoji    = 날씨이모지[날씨영어]
        confidence = 최고확률
    else:
        result     = '알 수 없는 날씨'
        emoji      = '❓'
        confidence = 0

    # TODO 5: jsonify 로 결과를 반환하세요
    # 반환 기준 js 에 작성한 반환 변수이름 기준
    return jsonify({
        'result': result,
        'confidence': f'{confidence:.1f}%',
        'emoji': emoji
    })

if __name__ == '__main__':
    app.run(debug=True)