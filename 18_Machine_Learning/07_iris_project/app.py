from flask import Flask, request, render_template
import pickle

app = Flask(__name__)  # 현재 app.py 에서 실행하지 않을 경우 실행하는 py 의 경로를 넣어줄 수 있다.
# 1. 만들어놓은 모델 불러오기
# with 자동으로 파일을 열었다가 닫았다 해주는 좋은 도구
# f : iris_model100.0.pkl 을 f 라는 이름에 담겠다.
# f = open("iris_model100.0.pkl",rb")
# 이렇게 작성하면  with open('iris_model100.0.pkl', 'rb') as f:
# 같은 구문 이지만 with 의 경우 오픈과 동시에 사용이 다되면 자동으로 닫기 처리가 된다.
with open('iris_model100.0.pkl', 'rb') as f:
    model = pickle.load(f)
종류 = ['setosa', 'versicolor', 'virginica']


@app.route("/")
def 메인페이지():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def 예측하기():
    # 입력값을 html에서 가져오기
    꽃받침길이 = float(request.form['꽃받침길이'])
    꽃받침너비 = float(request.form['꽃받침너비'])
    꽃잎길이 = float(request.form['꽃잎길이'])
    꽃잎너비 = float(request.form['꽃잎너비'])

    # 예측
    입력 = [[꽃받침길이, 꽃받침너비, 꽃잎길이, 꽃잎너비]]
    결과 = model.predict(입력)[0]
    꽃이름 = 종류[결과]

    return render_template('index.html', 결과=꽃이름)

if __name__ == "__main__":
    app.run(debug=True)
