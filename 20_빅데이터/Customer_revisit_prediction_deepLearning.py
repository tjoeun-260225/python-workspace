"""
Customer Comeback  Prediction - 재방문 예측
딥러닝 버전(TensorFlow / Keras)
sklearn RandomForest → TensorFlow 신경망으로 업그레이드
"""
import keras
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler

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

X = 데이터[features].values  # 넘파이 배열로 변환하여 좀 더 빠르게 계산
y = 데이터['revisit'].values

# 3. 데이터 분리(80% 학습 / 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ★ sklearn 과 가장 큰 차이 : 정규화
# - 결제금액(500000)과 성별 (0/1) 숫자 범위가 너무 달라서 학습이 잘 안됨
# - StandardScaler : 평균 0 표준편차 1로 맞춰줌
스케일도구 = StandardScaler()
X_train = 스케일도구.fit_transform(X_train)  # 학습 데이터로 기준 생성 + 변환
X_test = 스케일도구.transform(X_test)  # 위와 같은 기준으로 테스트 데이터만 변환

print(f"학습데이터 : {len(X_train)} 건 / 테스트 : {len(X_test)} 건")

# 4. 모델 학습 - 머신러닝 / 딥러닝 / 허깅페이스 / pytorch 등
#                로봇뇌를 어떤 형태로 만들지 개발자가 선택
# 인공지능 = 노트북
# 머신러닝 = 삼성 / LG / 애플 / HP / 레노버 / 아수스 / MSI ...
#             컴퓨터 종류에 따라 사양과 용량이 천차만별이지만
#             모든 컴퓨터가 100% 사람이 원하는대로 존재하지 않는다.
#             레노버 = 150만원 슬롯추가 기본 8GB + 32GB 40GB 2kg
#             아수스 = 200만원 슬롯추가불가 32GB 1.3kg
#             삼  성 = 220만원 슬롯추가불가 20GB 1.1kg
# 딥 러닝 = 조립식 노트북
#             개발자가 직접 커스텀한 노트북 = 70만원 슬롯추가무제한
#                                             무게 개발자가 고르는 것에 따라 다름
# RAM 삼성 제품 구매 SSD oo사 제품 HDD ㅁㅁ사 제품을 장착
# 몇가지는 개발자가 조립하여 장착
# 머신러닝에 존재하는 만들어진 로봇뇌 중에서 RandomForestClassifier을 선택했던 것일 뿐
#           신경망 만들기 시작
로봇뇌 = keras.Sequential([
    # 입력층 의 경우 피쳐 개수와 동일하게 세팅
    layers.Input(shape=(len(features),)),

    # 은닉층 1-64개 뉴런
    # Dense : 모든 뉴런이 연결된 완전 연결층
    # activation = 'relu' : 음수 → 0, 양수 → 그대로 (가장 많이 쓰는 활성화 함수)
    layers.Dense(64, activation='relu'),

    # Dropout : 학습 중 30% 뉴런을 랜덤으로 끔 → 과적합 방지
    # 사람의 뇌 신경망을 100% 860억개의 신경망을 모두다 사용하지 않는 것처럼
    # 로봇뇌 또한 100% 활용하지 않는 것
    layers.Dropout(0.3),

    # 은닉층 2 - 32 개 뉴런
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.2),

    # 은닉층 3 - 16 개 뉴런
    layers.Dense(16, activation='relu'),

    # 출력층 - 1개 뉴런
    # activation = 'sigmoid' : 결과를 0~1 사이 확률로 변환
    # 0.5 이상 → 재방문 함 / 미만 → 재방문 안 함
    layers.Dense(1, activation='sigmoid')
] ) #, name="재방문_예측_신경망")
# name="재방문_예측_신경망" 한국어 사용 불가하며,
# 만약 모델에 이름을 붙이고 싶다면 영어로 표기
# 제대로 만들어졌는지 만들어진 로봇뇌 상태 확인
로봇뇌.summary()

# 로봇뇌를 만들기 전에 추가적인 세팅작업 진행
로봇뇌.compile(
    # optimizer : 오답을 어떻게 수정할 것인지 전략 선택
    # Adam      : 가장 많이 쓰는 최적화 알고리즘(학습률 자동 조절)
    optimizer='adam',

    # loss : 정답과 예측의 차이를 계산하는 방식
    # binary_crossentropy = 이진분류(0/1)에 표준으로 쓰는 손실함수
    loss='binary_crossentropy',

    # metrics : 학습 중 출력할 성능 지표
    metrics=['accuracy']
)

# 로봇뇌 만들기 시작
# epochs : 전체 데이터를 몇 번 반복 학습할지
# batch_size : 한 번에 몇 개씩 묶어서 학습할지
# validation_split : 학습 데이터 중 20% 검증용으로 사용
로봇뇌.fit(X_train,
        y_train,
        epochs=50,
        batch_size=32,
        validation_split=0.2,
        verbose=1)

# 5. 평가
손실, 정확도 = 로봇뇌.evaluate(X_test, y_test, verbose=0)
print(f"테스트 정확도 :{정확도 * 100:.1f}%")
print(f"테스트 손  실 :{손실:.4f}")

# sklearn 의 predict 과 달리 딥러닝을 확률값을 (0.0 ~ 1.0)을 반환하기 때문에
# 0.5 기준으로 잘라서 0 또는 1 반환
y_pred_prob = 로봇뇌.predict(X_test)
y_pred = (y_pred_prob >= 0.5).astype(int).flatten()
print(f"모델 성능")
print(classification_report(y_test, y_pred, target_names=['재방문 안 함', '재방문 함']))

# 7. 실제 예측 - 특정 고객이 재방문할까?
# new_customer = pd.DataFrame([{ 이 형태로 사용해도 되나 np.array가 더 빠르기 때문에
# 이번에는 pd.DataFrame 를 np.array 로 교체
new_customer = np.array([[
    35,
    250000,
    15,
    30,
    16000,
    1,
    2
]])
# 스탠다드스케일로 설정한 값을 다시 원상복구
원상복구 = 스케일도구.transform(new_customer)
prob = 로봇뇌.predict(원상복구)[0][0] # 출력층 구조 차이
print(f"고객의 재방문 확률:{prob * 100:.1f}%")
print("재방문 가능성", "높음" if prob > 0.5 else "낮음")
"""
현재 예제 sklearn              머신러닝
다음 예제 tensorflow + cuda    딥러닝 신경망
응용 예제 huggingFace          리뷰 감성분석, 고객 문의 자동 분류
"""
