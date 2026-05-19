from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def 손글씨숫자분류():
    # 1. sklearn 에서 미리 수집하여 신입 개발자들에게 제공하는 손글씨 데이터 가져오기
    data_load = load_digits()  # 나중에는 개발자가 원하는 결과에 맞춰 데이터 수집하고 수집한 데이터 가져오기
    X = data_load.data  # 8x8 픽셀 이미지를 1줄로 편 숫자 64개 저장
    y = data_load.target  # 정답 (0~9)

    # 2. 학습용 / 테스트용 나누기 load_digits() = 총 1797개 에서 8:2 로 나눈 기준
    # X_train = 손     글     씨     데     이     터 1437개
    # X_test  = 각 손글씨 이미지에 해당하는 숫자  번호 1437개 정답으로 들어감
    # y_train = 손글씨 학습이 제대로 되었는지 확인용   데이터 360개
    # y_test  = 손글시 학습이 제대로 되었는지 채점용 숫자번호 360개
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. 모델 학습
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # 4. 예측 & 정확도
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"정확도 : {acc * 100:1.f}%")
