from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('fashion_model.keras')

labels = ['티셔츠', '바지', '스웨터', '드레스', '코트',
          '샌들', '셔츠', '스니커즈', '가방', '부츠']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read())).convert('L').resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28)

    pred = model.predict(image)
    result = labels[int(np.argmax(pred))]
    confidence = float(np.max(pred)) * 100

    return jsonify({'result': result, 'confidence': f'{confidence:.1f}%'})

if __name__ == '__main__':
    app.run(debug=True)