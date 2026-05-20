from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('digits_model_0.2_42_3_98.3.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route("/")
def 메인페이지():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def 예측하기():
    pixels = request.form.get('pixels')
    pixel_list = list(map(float, pixels.split(',')))
    입력 = np.array(pixel_list).reshape(1, -1)
    결과 = model.predict(입력)[0]
    return render_template('index.html', 결과=결과)


if __name__ == "__main__":
    app.run(debug=True)
