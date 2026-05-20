import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing, load_diabetes
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def 캘리포니아집값예측시각화():
    house_data = fetch_california_housing()
    X, y = house_data.data, house_data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()  # KNeighborClassification LinearRegression 이외에도 모델은 정말 많다.
    # 모델을 외운다기 보다는 AI 학습을 공부할 때 제일 먼저 배우는 기초 모델이구나~
    # 모델은 굉장히 많고, 대표적으로 분류 / 회귀로 나뉘는구나.
    # 앞으로도 많은 모델이 나올 것이고, 모델에 종류가 수천 수만가지 이지만 내가 필요한 모델 찾기!
    model.fit(X_train, y_train)  # 수많은 모델중에서 개발자가 선택한 모델로 훈련하기
    y_pred = model.predict(X_test)
    # 실제값 vs 예측값 산점도
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.3, color='steelblue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 'r--' =빨간색 -- 점선 정답선
    plt.xlabel("실제 집값")
    plt.ylabel("예측 집값")
    plt.title("실제값 vs 예측값 (캘리포니아 집값")
    plt.tight_layout()
    plt.show()


def 당뇨병데이터시각화():
    data = load_diabetes()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # TODO 1. 그래프 2개 나란히 배치 (1행 2열, 가로 14 세로 5)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # TODO 2. 그래프 1 — 실제값 vs 예측값 산점도
    axes[0].scatter(y_test, y_pred, alpha=0.5, color='steelblue')  # x=실제값, y=예측값

    # TODO 3. 정답선 그리기 (빨간 점선)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')

    # TODO 4. 축 이름이랑 타이틀 설정
    axes[0].set_xlabel("실제값")
    axes[0].set_ylabel("예측값")
    axes[0].set_title("실제값 vs 예측값")

    # TODO 5. 피처 이름이랑 계수 꺼내기
    features = data.feature_names
    coefs = model.coef_

    # TODO 6. 계수가 음수면 red, 양수면 steelblue 로 색 지정
    colors = ['red' if c < 0 else 'steelblue' for c in coefs]

    # TODO 7. 그래프 2 — 가로 막대그래프
    axes[1].barh(features, coefs, color=colors)

    # TODO 8. 기준선 (x=0 에 검은 세로선)
    axes[1].axvline(x=0, color='black', linewidth=0.8)

    # TODO 9. 타이틀이랑 x축 이름 설정
    axes[1].set_title("피처별 계수 (영향력)")
    axes[1].set_xlabel("계수값")

    # TODO 10. 레이아웃 정리 후 출력
    plt.tight_layout()
    plt.show()


당뇨병데이터시각화()
