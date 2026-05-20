import pickle
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# 주의할점 : 캘리포니아 집값에서만 LinearRegression 사용할 수 있는게 아니고,
# 당뇨병 예측에서만Ridge를 사용하는 것이 아니라
# 보통 회귀를 배울 때 처음 소개하는 데이터 = 집값 예측 처음 배우는 회귀 모델 = LinearRegression 일 뿐이다.
# 두번째로 배울 때  당뇨병 예측에서 사용하는 모델이 Ridge 일 뿐 두번째로 사용하는 모델과 데이터일 뿐
# 캘리포니아 집값에서 Ridge 사용하기도 하고, 당뇨병 모델에서 LinearRegression을 사용하기도 한다.

# 1. 데이터 불러오기

def 캘리포니아_집값_모델():
    data = fetch_california_housing()
    X, y = data.data, data.target

    # 2. 학습 / 테스트 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 모델 선택 후 학습
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. 평가 모델이 제대로 만들어졌는가
    y_pred = model.predict(X_test)
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred))}:.4f")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")

    # 5. pkl 저장
    # f = model.open(f"캘리포니아_집값_예측_{r2_score(y_test, y_pred):.4f)},"wb")
    with open(f'캘리포니아_집값_예측_{r2_score(y_test, y_pred):.4f}', 'wb') as f:
        pickle.dump(model, f)
    print(f'캘리포니아_집값_예측_{r2_score(y_test, y_pred):.4f} 저장 완료')


def 당뇨병_모델():
    data = load_diabetes()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TODO 1. Ridge 모델 학습시키기 (alpha=1.0)
    """
    Ridge 모델의 논문에 작성되어 있다. 데이터 분석가 논문 보는 방법도 추후 익히면 좋다.
    alpha=1.0
    Ridge 에 있는 수식 정규화 강도 모델한테 얼마나 제약을 걸지 조절하는 숫자
    alph 0.01 제약 약함 -> OLS 랑 거의 같은 상태
    alph  1.0 제약 중간 -> 중간 단계
    alph 100  제약 강함 -> 계수가 거의 0에 가까워짐
    """
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")

    # TODO 2. diabetes_model.pkl 로 저장하기
    with open("diabetes_model.pkl", "wb") as f:
        pickle.dump(model, f)

    # TODO 3. 저장한 pkl 불러오기
    with open('diabetes_model', 'rb') as f:
        load_model = pickle.load(f)

    # TODO 4. 불러온 모델로 X_test[0] 예측해서 출력하기
    print(f"불러온 모델로 예측해보기(사이트 만들기 전 체크) : {load_model.predict([X_test[0]])}")
def 당뇨병_모델_알파데이터다수비교():
    data = load_diabetes()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    for a in [0.01, 0.1, 1.0, 10.0, 100.0]:
        model = Ridge(alpha=a)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print(f"alpha={a} → R² : {r2_score(y_test, y_pred):.4f}")
        # 각 알파값마다 어떻게 정확도가 나오는지 확인할 수 있다.
        # 제일 높은 숫자가 그 데이터에 맞는 근사값 알파숫자
        # 실제 모델을 만들 때는 이런식으로 하나하나 찾지 않고 RidgeCV 자동으로 찾아줌
        
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")

    with open("diabetes_model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open('diabetes_model', 'rb') as f:
        load_model = pickle.load(f)

    print(f"불러온 모델로 예측해보기(사이트 만들기 전 체크) : {load_model.predict([X_test[0]])}")
