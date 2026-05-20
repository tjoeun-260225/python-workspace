import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 0. 한글 깨짐 환경설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1. csv 데이터 불러오기
df = pd.read_csv('csvs/icecream_sales.csv')
X = df[['기온']]  # 결과가 표 형태로 나옴 sklearn 모델은 X를 표 형태로 무조건 받아야 한다.
y = df['판매량']  # 결과가 목록 리스트 형태로 나옴 정답같은 경우 하나만 필요하기 때문에 1개

# 2. 학습 / 테스트 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 예측
y_pred = model.predict(X_test)

# 5. 평가
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"R² : {r2_score(y_test, y_pred):.4f}")

# 6. 시각화
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='steelblue', label="실제데이터")
plt.plot(X, model.predict(X), color='red', label="예측 직선")
plt.xlabel("기온")
plt.ylabel("판매량")
plt.title("기온에 따른 아이스크림 판매량 예측")
plt.legend()
plt.tight_layout()
plt.show()
