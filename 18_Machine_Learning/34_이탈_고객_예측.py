"""
이커머스 고객 이탈 예측
- 실제 쇼핑몰에서 "이 고객 다음 달에 안 올 것 같다" 예측
- RandomForest vs VotingClassifier 비교
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


def 고객이탈예측():
    df = pd.read_csv("csvs/ecommerce_customer_data_custom_ratios.csv")
    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print(f"\n이탈 고객 수 : {df['Churn'].sum()}명")
    print(f"유지 고객 수 : {(df['Churn'] == 0).sum()}명")

    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    df['Returns'] = df['Returns'].fillna(df['Returns'].mean())

    features = [
        'Product Price',
        'Quantity',
        'Total Purchase Amount',
        'Age',
        'Returns',
        'Gender',
    ]

    X = df[features]
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf.fit(X_train, y_train)
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['유지고객', '이탈고객']))

    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    voting = VotingClassifier(
        estimators=[('rf', model1), ('dt', model2), ('lr', model3)],
        voting='hard'
    )
    voting.fit(X_train, y_train)
    pred_voting = voting.predict(X_test)

    print("\n=== 보팅 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['유지고객', '이탈고객']))

    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 : {accuracy_score(y_test, pred_rf): .4f}")
    print(f"보팅        : {accuracy_score(y_test, pred_voting): .4f}")
    if accuracy_score(y_test, pred_voting) > accuracy_score(y_test, pred_rf):
        print("보팅이 더 좋다.")
    else:
        print("랜덤포레스트가 더 좋다.")

    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)

    print("\n=== 이탈에 영향주는 요소 순위 ===")
    print(중요도)


고객이탈예측()

"""
=== 데이터 미리보기 ===
   Customer ID        Purchase Date Product Category  ...  Age  Gender  Churn
0        46251  2020-09-08 09:38:32      Electronics  ...   37    Male      0
1        46251  2022-03-05 12:56:35             Home  ...   37    Male      0
2        46251  2022-05-23 18:18:01             Home  ...   37    Male      0
3        46251  2020-11-12 13:13:29         Clothing  ...   37    Male      0
4        13593  2020-11-27 17:55:11             Home  ...   49  Female      1

[5 rows x 13 columns]

=== 결측치 확인 ===
Customer ID                  0
Purchase Date                0
Product Category             0
Product Price                0
Quantity                     0
Total Purchase Amount        0
Payment Method               0
Customer Age                 0
Returns                  47596
Customer Name                0
Age                          0
Gender                       0
Churn                        0
dtype: int64

이탈 고객 수 : 49874명
유지 고객 수 : 200126명

=== 랜덤 포레스트 결과 ===
정확도 : 0.7880
              precision    recall  f1-score   support

        유지고객       0.80      0.98      0.88     40016
        이탈고객       0.21      0.02      0.04      9984

    accuracy                           0.79     50000
   macro avg       0.50      0.50      0.46     50000
weighted avg       0.68      0.79      0.71     50000


=== 보팅 결과 ===
정확도 : 0.7939
              precision    recall  f1-score   support

        유지고객       0.80      0.99      0.88     40016
        이탈고객       0.21      0.01      0.02      9984

    accuracy                           0.79     50000
   macro avg       0.50      0.50      0.45     50000
weighted avg       0.68      0.79      0.71     50000


=== 모델 비교 ===
랜덤포레스트 :  0.7880
보팅        :  0.7939
보팅이 더 좋다.

=== 이탈에 영향주는 요소 순위 ===
                      특성       중요도
2  Total Purchase Amount  0.418739
0          Product Price  0.359771
3                    Age  0.163008
1               Quantity  0.035224
4                Returns  0.018829
5                 Gender  0.004429
"""
