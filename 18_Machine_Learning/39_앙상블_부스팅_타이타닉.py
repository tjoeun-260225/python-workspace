"""
타이타닉 - 머신러닝을 배우고, 캐글대회를 참가할 때
가장 먼저 만나는 대회 문제
https://www.kaggle.com/competitions/titanic/data
타이타닉 승객 생존 여부 예측

나이/티켓 등급/성별 같은 피처(=컬럼)로 생존자를 예측하자
Pclass    → 1등석/2등석/3등석 부자일수록 먼저 구조되었을까? → YES
Sex       → 여성 / 어린이 먼저 구조 원칙이 있었다.          → YES
Age       → 어린이는 먼저 구조되었을까?                     → YES
Fare      → 비싼 티켓 = 1등석 =구조 우선?                   → YES
SibSp     → 형제/배우자 수, 혼자면 더 빨리 탈출             → 애매
Parch     → 부모/자녀 수, 가족이 있으면 도움?              → 애매
Embarked  → 탑승 항구, 생존과 관계가 있을까?               → 약함

버릴 컬럼
PassengerId → 번호 생존과 무관
Name        → 이름이 생존에 영향? 없음
Ticket      → 티켓 번호, 의미 없다.
Cabin       → 객실 번호, 결측값이 너무 많아 쓰기 어렵다.

데이터를 확인하고 데이터 분석을 하며 위와 같은 상황 조회하며 판단

머릿속 흐름
1. 생존에 영향을 줄 컬럼 고르기
2. 버릴 컬럼 정리
3. 결측치를 어떻게 채울지 결정
4. 문자 → 숫자 변환 과 같은 작업이 필요한지 확인

자주 사용되는 속성이나 기능
columns        → 컬럼 이름 목록 확인
shape          → 데이터가 몇 행 몇 열 인지
head()         → 실제 데이터 눈으로 확인
info()         → 타입이 문자인지 숫자인지 + 결측값 있는지
isnull().sum() → 결측값 몇 개인지 정확히 보기
describe()     → 숫자 컬럼 평균/최소/최대 한눈에 보기
value_counts() → 문자 컬럼에 어떤 값들이 있는지 보기
"""
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import lightgbm as lgb

import xgboost as xgb  # 이와 같은 형태로 많이 사용

# from xgboost import XGBClassifier 이렇게도 사용 가능하나

# ===========================
# 1. 데이터 불러오기
# 캐글에서 train.csv = 모델을 만들기 위한 데이터 들어있다.
# test.csv 는 train에서 만든 모델을 가지고 test.csv 에서
#             얼마나 예측을 잘하는지 확인하기 위한 시험 문제
# ===========================
train = pd.read_csv("csvs/titanic/train.csv")
test = pd.read_csv("csvs/titanic/test.csv")

# ===========================
# 2. 데이터 분석 pandas 이용해서 데이터 확인
# ===========================


# ===========================
# 3. 전처리 (부스팅 실습에 집중하기 위해 최소한의 작업만 진행)
# ===========================
# Pclass    → 1등석/2등석/3등석 부자일수록 먼저 구조되었을까? → YES
# Sex       → 여성 / 어린이 먼저 구조 원칙이 있었다.          → YES
# Age       → 어린이는 먼저 구조되었을까?                     → YES
# Fare      → 비싼 티켓 = 1등석 =구조 우선?                   → YES
# SibSp     → 형제/배우자 수, 혼자면 더 빨리 탈출             → 애매
# Parch     → 부모/자녀 수, 가족이 있으면 도움?              → 애매
# Embarked  → 탑승 항구, 생존과 관계가 있을까?               → 약함
컬럼들 = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Embarked']

# .map() = 컬럼의 값을 다른값으로 변경
# 기본구조
# df = pd.read_csv("csv파일.csv")
# df['컬럼'] = df['컬럼'].map({'바꾸기전':'바꾼후'})

# 성별을 숫자로 변환(male = 0, female=1)
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
test['Sex'] = test['Sex'].map({'male': 0, 'female': 1})

# 탑승항구 숫자로 변환(S=0, C=1, Q=2)
# Embarked
train['Embarked'] = train['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
test['Embarked'] = test['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# 빈칸(결측값) 평균으로 채우기
# ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
# inplace=True == 방식이 pandas 최신 버전에서 사용하지 않는 방식
# train['Age'].fillna(train['Age'].mean(), inplace=True)  오래된 버전 방식
train['Age']      = train['Age'].fillna(train['Age'].mean())
test['Age']       = test['Age'].fillna(train['Age'].mean())
test['Fare']      = test['Fare'].fillna(train['Fare'].mean())
train['Embarked'] = train['Embarked'].fillna(0)

# X(입력) y(정답)분리
X = train[컬럼들]
y = train['Survived']  # 생존 유무 컬럼을 정답으로 사용해서 훈련시키겠다.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===========================
# 4. 부스팅 모델 4개 학습 & 결과 비교
# ===========================

# AdaBoost n_estimators=100, random_state=42
ada_model = AdaBoostClassifier(n_estimators=100, random_state=42)
ada_model.fit(X_train, y_train)
print(f"AdaBoost : {ada_model.score(X_test, y_test):0.4f}")
# GBM n_estimators=100, random_state=42
gbm_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gbm_model.fit(X_train, y_train)
print(f"gbmBoost : {gbm_model.score(X_test, y_test):0.4f}")
# XGBoost n_estimators=100, eval_metric='logloss', random_state=42
xgb_model = xgb.XGBClassifier(n_estimators=100, eval_metric='logloss', random_state=42)
xgb_model.fit(X_train, y_train)
print(f"xgbBoost : {xgb_model.score(X_test, y_test):0.4f}")
# LightGBM n_estimators=100, random_state=42
lgb_model = lgb.LGBMClassifier(n_estimators=100, random_state=42)
lgb_model.fit(X_train, y_train)
print(f"lbmBoost : {lgb_model.score(X_test, y_test):0.4f}")
"""
AdaBoost : 0.7933
gbmBoost : 0.8156
xgbBoost : 0.8101
lbmBoost : 0.8380


[LightGBM] [Info] Number of positive: 268, number of negative: 444
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000125 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 195
[LightGBM] [Info] Number of data points in the train set: 712, number of used features: 7
[LightGBM] [Info] [binary:BoostFromScore]: pavg=0.376404 -> initscore=-0.504838
[LightGBM] [Info] Start training from score -0.504838
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
lbmBoost : 0.8380


"""


# ===========================
# 5. 가장 좋은 모델로 캐글 제출 파일 만들기
# ===========================
test_x = test[컬럼들]
predictions = lgb_model.predict(test_x)

submission = pd.DataFrame({
    'PassengerId':test['PassengerId'],
    'Survived':predictions
})
submission.to_csv('csvs/titanic/submission.csv',index=False)
print(f"캐글 제출 파일 생성 완료 ▶ submission.csv")
# 나중에 만들어진 submission.csv 파일을 캐글에 업로드