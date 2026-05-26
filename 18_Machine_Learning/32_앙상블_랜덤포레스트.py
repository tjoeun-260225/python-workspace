from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# 유방암 데이터 준비
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 모델
rf = RandomForestClassifier(
    n_estimators=100,  # 트리개수
    max_depth=None,  # 트리 깊이 제한 없음
    max_features='sqrt',  # 각 분기에서 사용할 피처수
    random_state=42
)

rf.fit(X_train, y_train)
pred = rf.predict(X_test)
print(f"랜덤 포레스트 정확도 : {accuracy_score(y_test, pred):.4f}")
print()
print(classification_report(y_test, pred, target_names=['악성','양성']))
