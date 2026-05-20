import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

house_data = fetch_california_housing()
X, y = house_data.data, house_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()  # KNeighborClassification LinearRegression 이외에도 모델은 정말 많다.
# 모델을 외운다기 보다는 AI 학습을 공부할 때 제일 먼저 배우는 기초 모델이구나~
# 모델은 굉장히 많고, 대표적으로 분류 / 회귀로 나뉘는구나.
# 앞으로도 많은 모델이 나올 것이고, 모델에 종류가 수천 수만가지 이지만 내가 필요한 모델 찾기!
model.fit(X_train, y_train)  # 수많은 모델중에서 개발자가 선택한 모델로 훈련하기
y_pred = model.predict(X_test)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 실제값 vs 예측값 산점도
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.3, color='steelblue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # 'r--' =빨간색 -- 점선 정답선
plt.xlabel("실제 집값")
plt.ylabel("예측 집값")
plt.title("실제값 vs 예측값 (캘리포니아 집값")
plt.tight_layout()
plt.show()
