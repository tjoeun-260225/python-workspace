"""
데이터는 존재하고 데이터에 어떤 모델을 사용하여 학습시키는가
붓꽃 은 대부분의 모델에서 활용 가능한 데이터셋
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.datasets import load_iris, load_wine, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
import numpy as np


def 붓꽃데이터실습():
    X, y = load_iris(return_X_y=True)
    feature_names = load_iris().feature_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf.fit(X_train, y_train)
    pred = rf.predict(X_test)
    print(f"정확도 : {accuracy_score(y_test, pred):.4f}")
    print(classification_report(y_test, pred, target_names=['세토사', '버시컬러', '버지니카']))
    print("=" * 30)
    # 피처 = 컬럼 중요도 순으로 정렬해서 어떤 피처를 중요하게 생각하는지 조회
    중요도 = pd.DataFrame({
        '특성': feature_names,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)
    print(중요도)


def 와인데이터실습():
    # TODO 1: load_wine() 으로 X, y 와 feature_names 불러오기
    X, y = load_wine(return_X_y=True)
    feature_names = load_wine().feature_names

    # TODO 2: train_test_split 으로 훈련/테스트 나누기
    #          test_size=0.2, random_state=42
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    # TODO 3: RandomForestClassifier 모델 만들기
    #          n_estimators=100, max_features='sqrt', random_state=42
    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    # TODO 4: 모델 학습 후 예측하기

    pred = None

    print(f"와인 정확도 : {accuracy_score(y_test, pred):.4f}")
    print(classification_report(y_test, pred, target_names=['와인1', '와인2', '와인3']))
    print("=" * 30)

    # TODO 5: 붓꽃과 똑같은 방식으로 피처 중요도 출력하기
    중요도 = pd.DataFrame({
        '특성': feature_names,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)
    print(중요도)


def 집값데이터실습():
    X, y = fetch_california_housing(return_X_y=True)
    feature_names = fetch_california_housing().feature_names

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(n_estimators=100, max_features=None, random_state=42)
    rf.fit(X_train, y_train)

    pred = rf.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))
    print(f"집값 RMSE (오차) : {rmse:.4f}")
    print("=" * 30)

    중요도 = pd.DataFrame({
        '특성': feature_names,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)
    print(중요도)


# ===== 실행 =====
붓꽃데이터실습()
print("=" * 50)
와인데이터실습()
print("=" * 50)
집값데이터실습()
