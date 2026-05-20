import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

"""
파이썬 모델
- 데이터 학습을 완료하고, 예측을 할 수 있는 상태가 된 것
모델 파일 
- 학습과 결과를 파일로 저장한 형태

저장할 모델이름은 최대한 어떤 전처리와 어떤숫자값을 넣었을 때 나온 결과인지
상세히 작성해주는 것이 좋다.

데이터이름_모델이름_{random_state}_이외숫자세팅값_{acc * 100:.1f}.pkl
--> 회사에서 연구원일 때는 길게 작성

다른 사람들에게 내가 만든 모델에 대하여 오픈하여 모두 다운로드로 사용할 수 있도록 할 때는
프로젝트이름.모델확장자 만 작성해서 공유

1. pickle(.pkl)
- 파이썬 기본 내장 도구
- 가장 많이 사용하는 방식
- 파이썬에서만 열 수 있다.
- 아무 모델이나 저장 가능

2. joblib(.pkl or .joblib)
- scikit-learn 공식 추천 방식
- pickle 보다 큰 데이터를 저장할 때 빠름
- scikit-learn 모델에는 이게 적합
- 실무에서 pickle 보다 많이 사용됨

3. ONNX(.onnx)
- 파이썬 말고 다른 언어에서도 열 수 있는 모델
- 자바, C++, 자바스크립트 등에서 사용 가능
- 앱이나 다른 서버에 모델을 올릴 때 사용
- 입문 단계에서는 난이도 있다.

4. h5/keras (.h5)
- 딥러닝(tensorflow, keras) 전용
- scikit-learn 모델엔 사용 안 함
- 나중에 딥러닝 배울 때 배울 모델

웹사이트 확장자에 .jsp .html 이 존재하고, 
엑셀 파일 .xlsx .csv  이미지 파일 .jpg, .png 등
존재하는 것처럼 
모델에도 다양한 확장자가 사용 상황에 따라 존재할 뿐 동일한 상태이다.
"""

import pickle
import joblib # sklearn 설치할 때 자동으로 같이 설치가 된다.


def pkl사용하기():
    붓꽃 = load_iris()
    model = KNeighborsClassifier(n_neighbors=3)

    # 모델로 저장하기
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)  # 반드시 어떤 머신러닝 / 딥러닝 을 활용해서 저장할 것인가 모델이 존재해야한다.

    # 만들어져 있는 모델 호출하여 웹사이트나 부품에서 사용하기
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

def joblib사용하기():
    model = KNeighborsClassifier(n_neighbors=3)
    # 모델로 저장하기
    joblib.dump(model, "model.pkl")  # 반드시 어떤 머신러닝 / 딥러닝 을 활용해서 저장할 것인가 모델이 존재해야한다.
    joblib.dump(model, "model.joblib")  # 반드시 어떤 머신러닝 / 딥러닝 을 활용해서 저장할 것인가 모델이 존재해야한다.

    # 만들어져 있는 모델 호출하여 웹사이트나 부품에서 사용하기
    model = joblib.load("model.pkl")    # png jpg 처럼 확장자만 다름
    model = joblib.load("model.joblib") # pkl 보다 크고 무거운 모델에서 빠르다.

def onnx사용하기():
    print("onnx")
    # # pip install skl2onnx
    #
    # from skl2onnx import convert_sklearn
    #
    # # 저장
    # onnx_model = convert_sklearn(model, ...)
    #
    # # 불러오기
    # import onnxruntime
    # sess = onnxruntime.InferenceSession('model.onnx')

def h5_keras_사용하기():
    print("h5 keras")
    # pip install tensorflow

    # # 모델 저장하기
    # model.save("model.h5")

    # # 만들어져 있는 모델 호출하여 웹사이트나 부품에서 사용하기
    # model = tf.keras.models.load_model("model.h5")