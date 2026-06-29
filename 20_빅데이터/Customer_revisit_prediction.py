"""
Customer   Churn   Prediction - 고객 이탈 예측
Customer Retention Prediction - 고객 유지 예측
Repeat   Purchase  Prediction - 재구매 예측
Customer Comeback  Prediction - 재방문 예측

실제로는 DB나 CSV로 수집한 데이터 로드
가상 고객 데이터 생성
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# 1. 가상으로 데이터 로드
np.random.seed(42)
개수 = 1000

데이터 = pd.DataFrame({
    'age': np.random.randint(20, 65, 개수),
    'total_spent': np.random.randint(10000, 500000, 개수),  # 총 결제 금액
    'visit_count': np.random.randint(1, 50, 개수),  # 방문 횟수
    'days_since_last': np.random.randint(1, 365, 개수),  # 마지막 방문 후 경과일
    'avg_per_visit': np.random.randint(5000, 50000, 개수),  # 방문당 평균 결제
    'gender': np.random.choice(['M', 'F'], 개수),
    'membership': np.random.choice(['일반', '실버', '골드'], 개수)
})

# 재방문여부(목표값) - 실제로는 DB CSV 수집한 곳에서 가져옴
데이터['revisit'] = (
        (데이터['visit_count'] > 10) &
        (데이터['days_since_last'] < 90) &
        (데이터['total_spent'] > 100000)
).astype(int)

print("재방문 비율 : ", 데이터['revisit'].mean().round(2))

# 2. 데이터 전처리
le = LabelEncoder()
데이터['gender_enc'] = le.fit_transform(데이터['gender'])
데이터['membership_enc'] = le.fit_transform(데이터['membership'])

features = ['age', 'total_spent',
            'visit_count', 'days_since_last',
            'avg_per_visit', 'gender_enc',
            'membership_enc']

X = 데이터[features]
y = 데이터['revisit']

# 3. 데이터 분리(80% 학습 / 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"학습데이터 : {len(X_train)} 건 / 테스트 : {len(X_test)} 건")

# 4. 모델 학습 - 머신러닝 / 딥러닝 / 허깅페이스 / pytorch 등
#                로봇뇌를 어떤 형태로 만들지 개발자가 선택
로봇뇌 = RandomForestClassifier(n_estimators=100, random_state=42)
로봇뇌.fit(X_train, y_train)

# 5. 평가
y_pred = 로봇뇌.predict(X_test)
print(f"모델 성능")
print(classification_report(y_test, y_pred, target_names=['재방문 안 함', '재방문 함']))

# 6. 중요 변수 확인 - 어떤 요소가 재방문에 영향을 주는가?
중요도 = pd.Series(로봇뇌.feature_importances_, index=features)
print("=== 재방문에 영향을 주는 요소(중요도 순) ===")
print(중요도.sort_values(ascending=False).round(3))

# 7. 실제 예측 - 특정 고객이 재방문할까?
new_customer = pd.DataFrame([{
    'age': 35,
    'total_spent': 250000,
    'visit_count': 15,
    'days_since_last': 30,
    'avg_per_visit': 16000,
    'gender_enc': 1,
    'membership_enc': 2
}])
prob = 로봇뇌.predict_proba(new_customer)[0][1]
print(f"고객의 재방문 확률:{prob * 100:.1f}%")
print("재방문 가능성", "높음" if prob > 0.5 else "낮음")
