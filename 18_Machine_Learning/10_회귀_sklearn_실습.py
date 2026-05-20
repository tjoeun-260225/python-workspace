from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1. 데이터 불러오기
data = fetch_california_housing()
X, y = data.data, data.target
# X=data.data
# y=data.target
# print("fetch_california_housing() 에 존재하는 속성들 : ",dir(data))
#   설명서    데이터   세부설정이름     표형태   정답번호   정답이름
# ['DESCR', 'data', 'feature_names', 'frame', 'target', 'target_names']

# 2. 학습 / 테스트 분리작업
# X = 훈         련            용  _train = 데이터  _test = 정답
# y = 훈련 제대로 되었는지 확인용  _train = 데이터  _test = 정답
#  test_size=0.2, random_state=42 이 숫자가 100% 좋은 수는 아니다.
#  단순히 초반에 시작할 때 많이 설정하는 숫자값
#  숫자값은 변경이 계속 된다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 학습용과 학습제대로 되었는지 확인하기 위한 데이터 분리를 바탕으로
#    모델 학습
#   모델을 학습하기 위해서 모델을 선택하고 선택한 모델로 학습을 시킨다.
# 3-1. 모델 선택해서 model 변수공간에 저장하기
model = LinearRegression()
model.fit(X_train, y_train)

# 3-2. 선택한 모델로 훈련시키기
model.fit(X_train, y_train)

# 4. 예측하기
# 예측을 할 때 X_test 만 사용하는 이유
# fit 으로 만들어진 임시 모델을 컴퓨터에서 잠시 보유
# 임시 모델을 이용해서 X_test 데이터 정답을 제대로 맞추고 있는지 확인
y_pred = model.predict(X_test)

# 5. 평가
# Root Mean Squared Error = 오차의 크기
#  - numpy 에 존재하는 sqrt() 기능과 mean_squared_error(y_test, y_pred) 기능 사용
#  -- mean_squared_error(y_test, y_pred)
#  -- 실제값이랑 예측값의 차이를 계산하는 기능
#  -- y_test = 실제 집값
#  -- y_pred = 모델이 예측한 집값
#  -- np.sqrt() 제곱근 함수
#     mean_squared_error 평균의 제곱근형태로 결과 반환
#     그것을 원래대로 되돌려 놓는 것 0과 -1 처럼 잘못된 데이터로 추출되는것을 방지하기 위하여 제곱근 형태로 반환
# R²(R-Squared)           = 내 모델이 데이터를 얼마나 잘 표현하고 있는가
# - r2_score(y_test, y_pred)
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"R² : {r2_score(y_test, y_pred):.4f}")
"""
(X, y, test_size=0.2, random_state=42)
RMSE : 0.7456 *10만 = 평균적으로 예측이 7만 4천 달러 정도 빗나간다.
R² : 0.5758         = 내 모델이 57% 정확하다

R² 기준으로
0.9 이상  → 매우 좋음
0.7 ~ 0.9 → 좋음
0.5 ~ 0.7 → 보통
0.5 이하  → 별로

LinearRegression(OLS)은 단순 직선 모델이라 한계가 있다.
0.5 0.9로 만들기 위해서 모델 교체 데이터 나누는 것도 다시 세팅 피처 넣어보고 다양한 방법 존재하기 시작
"""