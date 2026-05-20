from flask import Flask, request, render_template
import pickle # 머신러닝 모델 파일을 저장하고 불러올 때 사용하는 라이브러리

app = Flask(__name__)  # 현재 app.py 에서 실행하지 않을 경우 실행하는 py 의 경로를 넣어줄 수 있다.
# 1. 만들어놓은 모델 불러오기
# with 자동으로 파일을 열었다가 닫았다 해주는 좋은 도구
# f : iris_model100.0.pkl 을 f 라는 이름에 담겠다.
# f = open("iris_model100.0.pkl",rb")
# 이렇게 작성하면  with open('iris_model100.0.pkl', 'rb') as f:
# 같은 구문 이지만 with 의 경우 오픈과 동시에 사용이 다되면 자동으로 닫기 처리가 된다.
with open('iris_model100.0.pkl', 'rb') as f: # 우리가 학습한 데이터를 기준으로 만들어놓은 모델 가져와서 사용할 준비
    model = pickle.load(f)
종류 = ['setosa', 'versicolor', 'virginica'] # 모델이 예측하는 숫자(0,1,2)를 실제 꽃 이름으로 바꿔줄 리스트


@app.route("/") # 소비자가 메인페이지로 접속했을 때 보여줄 화면
def 메인페이지():
    return render_template('index.html')


@app.route("/predict", methods=['POST']) # /predict 주소로 POST 방식 요청이 오면 이 함수를 실행
def 예측하기():
    # 입력값을 html에서 가져오기
    # request.form['키이름'] = HTML form 태그에서 사용자가 입력한 값을 가져온다
    # html name ="키이름" 으로 되어있는 태그의 값을 가져온다.
    # input 의 경우 기본으로 전달받는 데이터는 모두다 string 문자열 형태로
    # iris 데이터는 실수 형태로 pkl 모델에 내장되어 있기 때문에 float()을 이용해서 문자열 → 실수 변환
    꽃받침길이 = float(request.form['꽃받침길이'])
    꽃받침너비 = float(request.form['꽃받침너비'])
    꽃잎길이 = float(request.form['꽃잎길이'])
    꽃잎너비 = float(request.form['꽃잎너비'])

    # 예측
    입력 = [[꽃받침길이, 꽃받침너비, 꽃잎길이, 꽃잎너비]]
    결과 = model.predict(입력)[0]
    # model.predict(입력) : 모델이 예측한 결과를 반환하는데,
    # 보통 예측의 경우 다수가 될 수 있으므로, 맨 첫번째 예측 결과 값만 가져오는 형태로 많이 사용
    꽃이름 = 종류[결과] # 결과에서 가져온 숫자 데이터를 종류 list 안에 있는 index 번호로 존재하는
    # 문자 데이터로 변환하여 꽃이름으로 저장하고,
    # 꽃이름에 저장된 데이터를 결과라는 이름으로 index.html 반환


    # if 문에서 숫자 index가 0 일 경우 False 로 처리되어 데이터가 보이지 않는 이슈 발생
    # 개발자는 0,1,2 처럼 나오는 데이터를 소비자가 알 수 있는 형태로 변환하여
    # 소비자에게 보여줄 의무가 있다.
    # 소비자가 불편한 사이트는 개발자가 개발할 때 편했던 사이트
    # 개발자가 개발할 때 힘들었던 사이트는 소비자가 이용할 때 편리한 사이트

    #return render_template('index.html', 결과=결과)
    return render_template('index.html', 결과=꽃이름)

if __name__ == "__main__":
    app.run(debug=True)
