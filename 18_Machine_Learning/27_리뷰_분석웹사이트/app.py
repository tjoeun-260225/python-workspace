# 만들어놓은 모델을 웹사이트에 장작해서 사용하기
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# ======================
# 모델 불러오기
# ※ train_model.py 실행 후 생성된 파일이름으로 맞춰주세요.
# ======================
with open('review_model_0.1_42_86.6.pkl', 'rb') as f:
    저장된모델 = pickle.load(f)

model = 저장된모델['model']
vectorizer = 저장된모델['vectorizer']


@app.route("/")
def 메인페이지():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def 예측하기():
    review = request.form.get('review')  # HTML 폼에서 name=review 라는 태그 를 가져온다.

    vec = vectorizer.transform([review]) # 가져온 리뷰를 글자 -> 숫자 변환처리 transform 을 하고 있다.
    결과 = model.predict(vec)[0]         # positive negative
    확률 = model.predict_proba(vec)[0]   # positive negative 의 확률
    확률값 = round(max(확률) * 100, 1)   # 더 높은쪽의 확률로 가져오겠다.

    return render_template('index.html', 결과=결과, 확률=확률값, 리뷰=review)


if __name__ == "__main__":
    app.run(debug=True)  # 개발모드
