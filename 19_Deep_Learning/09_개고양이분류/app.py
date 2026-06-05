from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('models/dog_cat_model.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read())).convert('RGB').resize((64, 64))
    image = np.array(image) / 255.0
    image = image.reshape(1, 64, 64, 3)

    pred = model.predict(image)[0][0]


    고양이기준 = 0.7
    개기준     = 0.3

    if pred > 고양이기준:
        result     = '고양이'
        confidence = pred * 100
        emoji      = '🐱'
    elif pred < 개기준:
        result     = '개'
        confidence = (1 - pred) * 100
        emoji      = '🐶'
    else:
        result     = '개/고양이가 아닙니다'
        confidence = 0
        emoji      = '❓'

    return jsonify({
        'result': result,
        'confidence': f'{confidence:.1f}%',
        'emoji': emoji
    })

if __name__ == '__main__':
    app.run(debug=True)