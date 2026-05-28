import xgboost as xgb
import lightgbm as lgb
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression

import pandas as pd
from sklearn.model_selection import train_test_split

# ================================
# 데이터 불러오기
# ================================
df = pd.read_csv('../csvs/seoulBike/SeoulBikeData.csv', encoding='latin1')

# 미션 1 - 데이터 파악
# df.shape, df.info(), df.isnull().sum() 으로
# 데이터 크기 / 타입 / 결측값 확인하기
print("df.shape =", df.shape)
print("df.info() =", df.info())
print("df.isnull().sum() =", df.isnull().sum())

# 미션 2 - 전처리
# 1) Date 컬럼 제거
df = df.drop(columns=['Date'])
# 2) Seasons / Holiday / Functioning Day 문자 → 숫자 변환
# 힌트 : .map() 사용
df['Seasons'] = df['Seasons'].map(
    {
        'Spring': 0,
        'Summer': 1,
        'Autumn': 2,
        'Winter': 3
    }
)
df['Holiday'] = df['Holiday'].map(
    {
        'No Holiday': 0,
        'Holiday': 1
    }
)
df['Functioning Day'] = df['Functioning Day'].map(
    {
        'Yes': 0,
        'No': 1
    }
)
# 3) X(입력), y(정답) 분리
# y → Rented Bike Count
# X → 나머지 전부
X = df.drop(columns=['Rented Bike Count'])
y = df['Rented Bike Count']

# 4) train_test_split 으로 학습/검증 데이터 나누기

# test_size=0.2, random_state=42
# 캐글처럼 train.csv test.csv 로 파일이 나뉘어져있을 때는
# X_test 대신에 X_val y_test 대신에 y_val 로 표기하기도 한다
# test_X 라는 이름으로 test.csv 를 사용하기도 한다.
# 표기 방식은 개발자의 자유
# X_train,X_val,y_train,y_val =train_test_split(X,y ,test_size=0.2,random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 미션 3 - 모델 학습
# 아래 모델 중 최소 2개 이상 골라서 학습시키기
# ① LinearRegression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
print(f"LinearRegression R²:{lr_model.score(X_test, y_test):.4f}")

# ② GradientBoostingRegressor
gbm_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gbm_model.fit(X_train, y_train)
print(f"GradientBoostingRegressor R²:{gbm_model.score(X_test, y_test):.4f}")

# ③ XGBRegressor
xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)
print(f"XGBoost R²:{xgb_model.score(X_test, y_test):.4f}")

# ④ LGBMRegressor
lgb_model = lgb.LGBMRegressor(n_estimators=100, random_state=42)
lgb_model.fit(X_train, y_train)
print(f"LGBBoost R²:{lgb_model.score(X_test, y_test):.4f}")
"""
LinearRegression R²:0.5128
GradientBoostingRegressor R²:0.8311
XGBoost R²:0.8644
[LightGBM] [Warning] Found whitespace in feature_names, replace with underlines
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.000298 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 1251
[LightGBM] [Info] Number of data points in the train set: 7008, number of used features: 12
[LightGBM] [Info] Start training from score 704.767837
LGBBoost R²:0.8746


"""

# 미션 5 (도전)
# R² 0.90 이상 달성해보기
# 힌트 : n_estimators, learning_rate, max_depth 조절
lgb_tuned = lgb.LGBMRegressor(
    n_estimators=500,  # 트리를 더 심오하고 많게 설정
    learning_rate=0.05,  # 학습률 낮게, 더 정교하게
    max_depth=7,  # 트리 깊이 늘리기
    random_state=42
)
'''
n_estimators
- 만약 작성하지 않으면 기본값으로 100 설정
- 생성할 결정 트리의 개수 (부스팅 반복 횟수)
- 숫자가 클수록 학습을 더 많이 → 성능 향상 가능, 하지만 과적합 속도 저하 위험
- 보통 100 ~ 1000 사이 많이 사용

- * 과적합 : 훈련데이터에만 적합되어 있어서 새로운 데이터는 틀리는 현상 
-            응용이 안된다
-    지나칠   과 
-    딱맞을   적 
-    들어맞을 합          지나치게 훈련에만 딱 맞아버리는 결과



learning_rate
- 기본값 0.1
- 각 트리가 이전 트리의 오차를 얼마나 빠르게 교정할지 결정
- 낮을수록 → 천천히 꼼꼼하게 학습(과적합 방지)
- 높을수록 → 빠르게 학습하지만 제대로 살펴보지 않아 불안정할 수 있다.
- 일반적으로 learning_rate가 낮으면 n_estimators 를 늘려서 사용
--  세부적으로 보고보고 또 보면서 제대로 꼼꼼하게 학습하자!



max_depth
- 기본값 -1(제한없음)
- 개별 트리의 최대 깊이(가지를 몇 단계 까지 뻗을 수 있는가)
- 깊을수록 → 복잡한 패턴 학습 가능, 하지만 과적합 위험
- 얕을수록 → 단순하지만 과소적합 위험
- LightGBM 은 max_depth 설정제한을 어떻게 하느냐가 많이 중요


random_state=42
- 기본값 None(매번 다른 결과 발생)
- 기본값을 세팅한 후, 정확도가 높은 시작을 기준으로 고정하여 사용
- 어떤 시작 숫자가 좋은지는 아무도 모른다.
- 그것을 각 데이터와 모델별로 찾는 것이 일
- 시작을 42에서 출발하겠다.

트리 : 나무처럼 위에서 아래로 뻗어가는 구조
머신러닝에서 결정 트리 : 질문을 던지면서 답을 찾아가는 구조
루트 노드 : 맨 위 첫번째 질문
가지      : 질문의 Yes/No 경로
잎 노드   : 최종 답(더 이상 질문 없음)
깊이      : 질문이 몇 단꼐까지 이어지는가

max_depth=7
예를 들어 집값 예측 데이터 -> 머신러닝에서 우선 데이터를 쭉~ 살펴본다.
depth 1:            [면적 > 80m²?]
depth 2:           [예]                [아니오]
depth 3:     [층수 > 5층?]           [역까지 < 500m?]
depth 4:   [예]      [아니오]      [예]         [아니오]
depth 5: [복층]
depth 6: []
depth 7: [더이상 질문 금지 끝]
'''


lgb_tuned.fit(X_train, y_train)
print(f"LightGBM 튜닝 R² :{lgb_tuned.score(X_test, y_test):.4f} ")

"""
==============================================
서울 따릉이 대여량 예측 프로젝트
==============================================

목표
시간대, 날씨, 계절 등의 데이터를 보고
따릉이 대여 횟수를 예측하는 모델 만들기

컬럼 정리
Date                      → 날짜          (버리기)
Rented Bike Count         → 대여횟수      (← 정답 y)
Hour                      → 시간
Temperature(°C)           → 기온
Humidity(%)               → 습도
Wind speed (m/s)          → 풍속
Visibility (10m)          → 가시거리
Dew point temperature(°C) → 이슬점
Solar Radiation           → 태양복사량
Rainfall(mm)              → 강우량
Snowfall (cm)             → 강설량
Seasons                   → 계절         (문자 → 숫자 변환 필요)
Holiday                   → 공휴일 여부  (문자 → 숫자 변환 필요)
Functioning Day           → 운영여부     (문자 → 숫자 변환 필요)

미션 1 - 데이터 파악
  df.shape, df.info(), df.isnull().sum() 으로
  데이터 크기 / 타입 / 결측값 확인하기

미션 2 - 전처리
  1) Date 컬럼 제거
  2) Seasons / Holiday / Functioning Day 문자 → 숫자 변환
     힌트 : .map() 사용
  3) X(입력), y(정답) 분리
     y → Rented Bike Count
     X → 나머지 전부
  4) train_test_split 으로 학습/검증 데이터 나누기
     test_size=0.2, random_state=42

미션 3 - 모델 학습
  아래 모델 중 최소 2개 이상 골라서 학습시키기
  ① LinearRegression
  ② GradientBoostingRegressor
  ③ XGBRegressor
  ④ LGBMRegressor

  주의 : 대여횟수는 숫자 예측 = 회귀 문제
         Classifier 쓰면 안 됨

미션 4 - 성능 비교
  .score() 로 R² 점수 출력
  0.8 이상 → 잘 된 것
  0.9 이상 → 매우 잘 된 것

미션 5 (도전)
  R² 0.90 이상 달성해보기
  힌트 : n_estimators, learning_rate, max_depth 조절
==============================================
"""


# 여기서부터 작성


def 데이터분석하기():
    df = pd.read_csv('../csvs/seoulBike/SeoulBikeData.csv', encoding='latin1')

    # =====================
    # 1. 데이터 분석하는 메서드와 속성을 이용해서
    #   행 열 개수 컬럼 이름 목록 각 컬럼 타입 결측값 개수 컬럼별 결측값 정확히 보기
    #   평균 최소최대 표준편차
    #   문자 커럼 어떤 값들이 들어있는지
    #   그룹변 평균 비교
    # =====================
    print("=" * 10, "행 열의 개수", "=" * 10)
    print(df.shape)
    print("=" * 10, "컬럼 목록", "=" * 10)
    print(df.columns.tolist())
    print("=" * 10, "상위 5개의 행", "=" * 10)
    print(df.head())
    print("=" * 10, "타입 + 결측 값", "=" * 10)
    print(df.info())
    print("=" * 10, "결측 값 개수", "=" * 10)
    print(df.isnull().sum())


# 데이터분석하기()
"""
========== 행 열의 개수 ==========
(8760, 14)
========== 컬럼 목록 ==========
['Date', 'Rented Bike Count', 'Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)', 'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Seasons', 'Holiday', 'Functioning Day']
========== 상위 5개의 행 ==========
         Date  Rented Bike Count  Hour  ...  Seasons     Holiday  Functioning Day
0  01/12/2017                254     0  ...   Winter  No Holiday              Yes
1  01/12/2017                204     1  ...   Winter  No Holiday              Yes
2  01/12/2017                173     2  ...   Winter  No Holiday              Yes
3  01/12/2017                107     3  ...   Winter  No Holiday              Yes
4  01/12/2017                 78     4  ...   Winter  No Holiday              Yes

[5 rows x 14 columns]
========== 타입 + 결측 값 ==========
<class 'pandas.DataFrame'>
RangeIndex: 8760 entries, 0 to 8759
Data columns (total 14 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   Date                       8760 non-null   str    
 1   Rented Bike Count          8760 non-null   int64  
 2   Hour                       8760 non-null   int64  
 3   Temperature(°C)            8760 non-null   float64
 4   Humidity(%)                8760 non-null   int64  
 5   Wind speed (m/s)           8760 non-null   float64
 6   Visibility (10m)           8760 non-null   int64  
 7   Dew point temperature(°C)  8760 non-null   float64
 8   Solar Radiation (MJ/m2)    8760 non-null   float64
 9   Rainfall(mm)               8760 non-null   float64
 10  Snowfall (cm)              8760 non-null   float64
 11  Seasons                    8760 non-null   str    
 12  Holiday                    8760 non-null   str    
 13  Functioning Day            8760 non-null   str    
dtypes: float64(6), int64(4), str(4)
memory usage: 958.3 KB
None
========== 결측 값 개수 ==========
Date                         0
Rented Bike Count            0
Hour                         0
Temperature(°C)              0
Humidity(%)                  0
Wind speed (m/s)             0
Visibility (10m)             0
Dew point temperature(°C)    0
Solar Radiation (MJ/m2)      0
Rainfall(mm)                 0
Snowfall (cm)                0
Seasons                      0
Holiday                      0
Functioning Day              0
dtype: int64
"""
# 남이 만들어놓은 데이터를 이용해서 문제를 풀려 하기 때문에
# 데이터 분석 → 데이터 전처리 가 어려운 것

# 개발자나 분석가가 수집할 데이터의 기준을 정하고, 어떻게 사용하겠다
# 목표를 확실하게 정하면 분석과 전처리는 굉장히 쉬울 것이다.
# 강아지 고양이 돼지 수집 컬럼하나에 분류 강아지 고양이 돼지 작성

# 내가 목표로한 데이터가 아니고 남이 만든 데이터에 남이 만든 가정을 따라서
# 결과를 도달하려 하기 때문에 힘들다.
