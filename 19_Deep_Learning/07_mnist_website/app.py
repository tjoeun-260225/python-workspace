from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
import base64
from PIL import Image
import io

app = Flask(__name__)
model = load_model('mnist_model.keras')  # 저장된 모델 불러오기

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 프론트에서 보낸 이미지 받기
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])

    # 이미지 전처리 (28x28 흑백으로 변환)
    image = Image.open(io.BytesIO(image_data)).convert('L').resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28)

    # 예측
    pred = model.predict(image)
    result = int(np.argmax(pred))
    confidence = float(np.max(pred)) * 100

    return jsonify({'result': result, 'confidence': f'{confidence:.1f}%'})

if __name__ == '__main__':
    app.run(debug=True)