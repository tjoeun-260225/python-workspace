import pickle
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. 수집한 데이터 가져오기
iris = load_iris()
# 2. 데이터만 X 에 담아두기
X = iris.data
# 3. 데이터의 정답만 y에 담아두기
y = iris.target

# 4. X, y에 저장된 데이터를 8:2 기준으로 train 과 test에 각각 나눠서 저장하기

# 반드시 train 에 오는 데이터는 학습용 데이터 - 정답으로 8~6에 준수하는 데이터와 정답 보유
# X_train = 데이터 80% y_train = 정답 80%

# 반드시 test 에 오는 데이터는  학습이 잘되었는지 확인용 데이터 - 2~4에 준수하는 데이터와 정답 보유
# X_test = 데이터 20% y_test = 정답 20%

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 5. 위 데이터를 훈련시킬 모델 선택해서 model 공간에 담아두기
model = KNeighborsClassifier(n_neighbors=3)
# 6. 학습시키기
model.fit(X_train, y_train)

# 7. 학습 결과 예측 조회하기
y_pred = model.predict(X_test)  # 시험결과 갖고오기
acc = accuracy_score(y_test, y_pred)
# 8. 학습 결과 모델 pkl 로 저장하기
# 모델을 저장할 때 데이터를 나눈 기준 , 데이터 전처리, 정답률을 포함하여 파일이름 저장
with open(f"iris_model{acc * 100:.1f}.pkl", "wb") as f:
    pickle.dump(model, f)

print("모델 저장 완료")
