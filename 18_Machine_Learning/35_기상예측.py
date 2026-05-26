"""
날씨 데이터로 내일 비 올지 예측
기온 / 습도 / 풍속 → 비 올지 안 올지 분류
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def 날씨예측():

    df = pd.read_csv("csvs/weather_forecast_data.csv")

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print("\n=== 몇 행 몇 열? ===")
    print(df.shape)

    df['Temperature']   = df['Temperature'].fillna(df['Temperature'].mean())
    df['Humidity']      = df['Humidity'].fillna(df['Humidity'].mean())
    df['Wind_Speed']    = df['Wind_Speed'].fillna(df['Wind_Speed'].mean())
    df['Precipitation'] = df['Precipitation'].fillna(df['Precipitation'].mean()) if 'Precipitation' in df.columns else df['Cloud_Cover'].fillna(df['Cloud_Cover'].mean())

    # Rain 컬럼 숫자 변환 (rain=1, no rain=0)
    df['Rain'] = df['Rain'].map({'rain': 1, 'no rain': 0})

    features = ['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover']

    X = df[features]
    y = df['Rain']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf.fit(X_train, y_train)
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['맑음', '비']))

    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    voting = VotingClassifier(
        estimators=[('rf', model1), ('dt', model2), ('lr', model3)],
        voting='hard'
    )
    voting.fit(X_train, y_train)
    pred_voting = voting.predict(X_test)

    print("\n=== 보팅 결과 (3개 모델 투표) ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['맑음', '비']))

    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 정확도 : {accuracy_score(y_test, pred_rf): .4f}")
    print(f"보팅        정확도 : {accuracy_score(y_test, pred_voting): .4f}")
    if accuracy_score(y_test, pred_voting) > accuracy_score(y_test, pred_rf):
        print("보팅이 더 좋다.")
    else:
        print("랜덤포레스트가 더 좋다.")

    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)

    print("\n=== 비 오는 데 영향주는 요소 순위 ===")
    print(중요도)

날씨예측()

"""
=== 데이터 미리보기 ===
   Temperature   Humidity  Wind_Speed  Cloud_Cover     Pressure     Rain
0    23.720338  89.592641    7.335604    50.501694  1032.378759     rain
1    27.879734  46.489704    5.952484     4.990053   992.614190  no rain
2    25.069084  83.072843    1.371992    14.855784  1007.231620  no rain
3    23.622080  74.367758    7.050551    67.255282   982.632013     rain
4    20.591370  96.858822    4.643921    47.676444   980.825142  no rain

=== 컬럼 목록 ===
['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'Pressure', 'Rain']

=== 결측치 확인 ===
Temperature    0
Humidity       0
Wind_Speed     0
Cloud_Cover    0
Pressure       0
Rain           0
dtype: int64

=== 몇 행 몇 열? ===
(2500, 6)

=== 랜덤 포레스트 결과 ===
정확도 : 0.9980
              precision    recall  f1-score   support

          맑음       1.00      1.00      1.00       443
           비       1.00      0.98      0.99        57

    accuracy                           1.00       500
   macro avg       1.00      0.99      1.00       500
weighted avg       1.00      1.00      1.00       500


=== 보팅 결과 (3개 모델 투표) ===
정확도 : 0.9980
              precision    recall  f1-score   support

          맑음       1.00      1.00      1.00       443
           비       1.00      0.98      0.99        57

    accuracy                           1.00       500
   macro avg       1.00      0.99      1.00       500
weighted avg       1.00      1.00      1.00       500


=== 모델 비교 ===
랜덤포레스트 정확도 :  0.9980
보팅        정확도 :  0.9980
랜덤포레스트가 더 좋다.

=== 비 오는 데 영향주는 요소 순위 ===
            특성       중요도
3  Cloud_Cover  0.361350
1     Humidity  0.333083
0  Temperature  0.296283
2   Wind_Speed  0.009283

"""