import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def 아이스크림_판매량_모델만들기():
    df = pd.read_csv('csvs/icecream_sales.csv')
    X = df[['기온']]
    y = df['판매량']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")
    # 추후 날짜별 기온을 조회하여 기온별로 판매량 예측
    # 편의점, 아이스크림 가게를 운영하는 사장님들에게 일자별 기온과 예상 판매량 예상 오더수량
    with open(f'models/icecream_{r2_score(y_test, y_pred):.4f}.pkl', 'wb') as f:
        pickle.dump(model, f)
    print(f'models/icecream_{r2_score(y_test, y_pred):.4f}.pkl 저장 완료')


def 운동칼로리_모델만들기():
    df = pd.read_csv('csvs/exercise_calories.csv')
    X = df[['운동시간(분)']]
    y = df['칼로리소모']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")
    # 운동어플, 헬스장 고객별 평균 운동시간으로 소모 칼로리 예측
    # 식단관리 어플, 식단을 기준으로 평균 칼로리 예측
    # 한 달 후, 체지방 근육량을 예측할 수 있다.
    with open(f'models/exercise_calories_{r2_score(y_test, y_pred):.4f}.pkl', 'wb') as f:
        pickle.dump(model, f)
    print(f'models/exercise_calories_{r2_score(y_test, y_pred):.4f}.pkl 저장 완료')


def 광고매출_모델만들기():
    df = pd.read_csv('csvs/ad_sales.csv')
    X = df[['광고비용(만원)']]
    y = df['매출액(만원)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"R² : {r2_score(y_test, y_pred):.4f}")
    # 광고 비용으로 매출 예측
    # 소셜에 광고비용 basic ~ premium basic 예상 기대효과 예상 기대효과 수익 예측 추천
    with open(f'models/ad_sales{r2_score(y_test, y_pred):.4f}.pkl', 'wb') as f:
        pickle.dump(model, f)
    print(f'models/ad_sales{r2_score(y_test, y_pred):.4f}.pkl 저장 완료')

아이스크림_판매량_모델만들기()
운동칼로리_모델만들기()
광고매출_모델만들기()
