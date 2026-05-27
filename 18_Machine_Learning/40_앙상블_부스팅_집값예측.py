import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import lightgbm as lgb
from sqlalchemy.dialects.mssql.information_schema import columns


# ================================
# 1. 데이터 불러오기
# ================================
def load_data():
    train = pd.read_csv('csvs/house_prices/train.csv')
    test = pd.read_csv('csvs/house_prices/test.csv')
    return train, test


# ================================
# 2. 전처리
# ================================
def preprocess(train, test):
    # 결측값 너무 많은 컬럼 제거
    drop_cols = ['Alley', 'PoolQC', 'Fence', 'MiscFeature', 'FireplaceQu']
    train = train.drop(columns=drop_cols)
    test = test.drop(columns=drop_cols)

    # 숫자 컬럼 결측값 → 평균으로 채우기
    num_cols = train.drop(columns=['SalePrice']).select_dtypes(include='number').columns
    train[num_cols] = train[num_cols].fillna(train[num_cols].mean())
    test[num_cols] = test[num_cols].fillna(train[num_cols].mean())

    # 문자 컬럼 결측값 → 'None' 으로 채우기
    # Pandas4Warning: For backward compatibility, 'str' dtypes are included by
    # 판다스에서 최신버전 업데이트를 하며
    # cat_cols = train.select_dtypes(include='object').columns
    cat_cols = train.select_dtypes(include=['object', 'str']).columns
    train[cat_cols] = train[cat_cols].fillna('None')
    test[cat_cols] = test[cat_cols].fillna('None')

    # 문자 → 숫자 변환
    train = pd.get_dummies(train)
    test = pd.get_dummies(test)

    # train/test 컬럼 개수 맞추기
    #train, test = train.align(test, join='left', axis=1, fill_value=0)

    # X, y 분리
    X = train.drop(columns=['SalePrice'])
    y = train['SalePrice']
    X, test = X.align(test, join='left', axis=1, fill_value=0)

    return X, y, test


# ================================
# 3. 모델 학습 & 평가
# ================================
def train_models(X_train, X_val, y_train, y_val):
    # 과제 1. GBM 모델 채우기
    gbm_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    gbm_model.fit(X_train, y_train)
    print(f"GBM     : {gbm_model.score(X_val, y_val):.4f}")

    # 과제 2. XGBoost 모델 채우기
    xgb_model = xgb.XGBRegressor(n_estimators=100, random_state=42)
    xgb_model.fit(X_train, y_train)
    print(f"XGBoost : {xgb_model.score(X_val, y_val):.4f}")

    # 과제 3. LightGBM 모델 채우기
    lgb_model = lgb.LGBMRegressor(n_estimators=100, random_state=42)
    lgb_model.fit(X_train, y_train)
    print(f"LightGBM: {lgb_model.score(X_val, y_val):.4f}")

    return gbm_model, xgb_model, lgb_model


# ================================
# 4. 제출 파일 생성
# ================================
def make_submission(model, test):
    # 과제 4. test 예측 후 submission.csv 만들기
    predictions = model.predict(test)

    submission = pd.DataFrame({
        'Id': test.index + 1461,
        'SalePrice': predictions
    })
    submission.to_csv('csvs/house_prices/submission.csv', index=False)
    print("제출 파일 생성 완료 → submission.csv")

"""
GBM     : 0.9005
XGBoost : 0.9045
[LightGBM] [Warning] Found whitespace in feature_names, replace with underlines
[LightGBM] [Info] Auto-choosing col-wise multi-threading, the overhead of testing was 0.001000 seconds.
You can set `force_col_wise=true` to remove the overhead.
[LightGBM] [Info] Total Bins 3449
[LightGBM] [Info] Number of data points in the train set: 1168, number of used features: 180
[LightGBM] [Info] Start training from score 181441.541952
LightGBM: 0.8880
제출 파일 생성 완료 → submission.csv

"""
# ================================
# 5. 실행
# ================================
def main():
    train, test = load_data()
    X, y, test = preprocess(train, test)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    gbm_model, xgb_model, lgb_model = train_models(X_train, X_val, y_train, y_val)

    # 과제 5. 제일 좋은 모델 골라서 넣기
    make_submission(xgb_model, test)


main()
