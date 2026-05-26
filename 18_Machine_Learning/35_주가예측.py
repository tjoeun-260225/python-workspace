"""
주식 데이터로 내일 오를지 내릴지 예측
시가 / 고가 / 저가 / 거래량 → 상승 or 하락 분류
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def 주식예측():

    df = pd.read_csv("csvs/stock_data.csv")

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print("\n=== 몇 행 몇 열? ===")
    print(df.shape)

    df['Target'] = (df['Close'] > df['Open']).astype(int)

    print(f"\n상승일 수 : {df['Target'].sum()}일")
    print(f"하락일 수 : {(df['Target'] == 0).sum()}일")

    df['Open']   = df['Open'].fillna(df['Open'].mean())
    df['High']   = df['High'].fillna(df['High'].mean())
    df['Low']    = df['Low'].fillna(df['Low'].mean())
    df['Volume'] = df['Volume'].fillna(df['Volume'].mean())

    features = ['Open', 'High', 'Low', 'Volume']

    X = df[features]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf.fit(X_train, y_train)
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['하락', '상승']))

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
    print(classification_report(y_test, pred_voting, target_names=['하락', '상승']))

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

    print("\n=== 주가 예측에 영향주는 요소 순위 ===")
    print(중요도)

주식예측()

"""
=== 데이터 미리보기 ===
       Open     Close      High  ...  GDP_Growth  Inflation_Rate  Target
0  0.374639  0.374780  0.373510  ...    0.580868        0.038604       0
1  0.950982  0.937746  0.938422  ...    0.527044        0.108908       0
2  0.732198  0.719825  0.723644  ...    0.351052        0.432540       0
3  0.598823  0.599865  0.596973  ...    0.493274        0.946349       0
4  0.156053  0.163410  0.155891  ...    0.365116        0.074867       0

[5 rows x 13 columns]

=== 컬럼 목록 ===
['Open', 'Close', 'High', 'Low', 'Volume', 'RSI', 'MACD', 'Bollinger_Upper', 'Bollinger_Lower', 'Sentiment_Score', 'GDP_Growth', 'Inflation_Rate', 'Target']

=== 결측치 확인 ===
Open               0
Close              0
High               0
Low                0
Volume             0
RSI                0
MACD               0
Bollinger_Upper    0
Bollinger_Lower    0
Sentiment_Score    0
GDP_Growth         0
Inflation_Rate     0
Target             0
dtype: int64

=== 몇 행 몇 열? ===
(10000, 13)

상승일 수 : 5307일
하락일 수 : 4693일

=== 랜덤 포레스트 결과 ===
정확도 : 0.8790
              precision    recall  f1-score   support

          하락       0.86      0.88      0.87       929
          상승       0.90      0.87      0.89      1071

    accuracy                           0.88      2000
   macro avg       0.88      0.88      0.88      2000
weighted avg       0.88      0.88      0.88      2000


=== 보팅 결과 (3개 모델 투표) ===
정확도 : 0.8690
              precision    recall  f1-score   support

          하락       0.85      0.87      0.86       929
          상승       0.88      0.87      0.88      1071

    accuracy                           0.87      2000
   macro avg       0.87      0.87      0.87      2000
weighted avg       0.87      0.87      0.87      2000


=== 모델 비교 ===
랜덤포레스트 정확도 :  0.8790
보팅        정확도 :  0.8690
랜덤포레스트가 더 좋다.

=== 주가 예측에 영향주는 요소 순위 ===
       특성       중요도
0    Open  0.399154
1    High  0.269184
2     Low  0.241303
3  Volume  0.090359
"""