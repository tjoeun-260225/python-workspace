import pickle
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 주의할점 : 캘리포니아 집값에서만 LinearRegression 사용할 수 있는게 아니고,
# 당뇨병 예측에서만Ridge를 사용하는 것이 아니라
# 보통 회귀를 배울 때 처음 소개하는 데이터 = 집값 예측 처음 배우는 회귀 모델 = LinearRegression 일 뿐이다.
# 두번째로 배울 때  당뇨병 예측에서 사용하는 모델이 Ridge 일 뿐 두번째로 사용하는 모델과 데이터일 뿐
# 캘리포니아 집값에서 Ridge 사용하기도 하고, 당뇨병 모델에서 LinearRegression을 사용하기도 한다.

# 1. 데이터 불러오기
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