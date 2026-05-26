import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
X = digits.data
y = digits.target

model_split_size = 0.2
model_random_state = 42
neighbors = 3

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=model_split_size,
    random_state=model_random_state
)

model = KNeighborsClassifier(n_neighbors=neighbors)
model.fit(X_train, y_train)  # 데이터와 정답 각각 80% 데이터로 fit 훈련한다

acc = accuracy_score(y_test, model.predict(X_test))

with open(f'digits_model_{model_split_size}_{model_random_state}_{neighbors}_{acc * 100:.1f}.pkl', "wb") as f:
    pickle.dump(model, f)

print(f'모델 저장 완료 / 정확도 : {acc * 100:.1f}')