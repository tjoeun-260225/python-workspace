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

    df = pd.read_csv("/csvs/ecommerce_customer_data_custom_ratios.csv")
    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print(f"\n이탈 고객 수 : {df['Churn'].sum()}명")
    print(f"유지 고객 수 : {(df['Churn'] == 0).sum()}명")

    # TODO 2: Gender 문자 → 숫자 변환
    # 힌트: df['Gender'].map({'Male': 0, 'Female': 1})
    df['Gender'] =df['Gender'].map({'Male': 0, 'Female': 1})

    # TODO 3: 결측치 채우기
    # 힌트: df['Returns'].fillna(df['Returns'].mean())
    df['Returns'] = df['Returns'].fillna(df['Returns'].mean())

    features = [
        'Product Price',
        'Quantity',
        'Total Purchase Amount',
        'Age',
        'Returns',
        'Gender',
    ]

    # TODO 4: X (입력), y (정답) 나누기
    # 힌트: X = df[features] / y = df['Churn']
    X = df[features]
    y = df['Churn']

    # TODO 5: 훈련/테스트 나누기
    # 힌트: train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TODO 6: 랜덤포레스트 모델 만들고 학습 후 예측
    # 힌트: RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    # 힌트: rf.fit(___, ___) → rf.predict(___)
    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf.fit(X_train, y_train)
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['유지고객', '이탈고객']))

    # TODO 7: 3개 모델 만들기
    # 힌트: RandomForestClassifier(n_estimators=100, random_state=42)
    # 힌트: DecisionTreeClassifier(random_state=42)
    # 힌트: LogisticRegression(max_iter=1000, random_state=42)
    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    # TODO 8: VotingClassifier 만들고 학습 후 예측
    # 힌트: estimators=[('rf', model1), ('dt', model2), ('lr', model3)]
    # 힌트: voting='hard'
    voting = VotingClassifier(
        estimators=[('rf', model1), ('dt', model2), ('lr', model3)],
    voting='hard'
    )
    voting.fit(X_train, y_train)
    pred_voting = voting.predict((X_test))

    print("\n=== 보팅 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['유지고객', '이탈고객']))

    # TODO 9: 모델 비교
    # 힌트: accuracy_score(y_test, pred_rf) vs accuracy_score(y_test, pred_voting)
    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 : {accuracy_score(y_test, pred_rf): .4f}")
    print(f"보팅        : {accuracy_score(y_test, pred_voting): .4f}")

    # TODO 10: 피처 중요도
    # 힌트: rf.feature_importances_
    # 힌트: sort_values('중요도', ascending=False)
    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf.feature_importances_
    }).sort_values('중요도',ascending=False)

    print("\n=== 이탈에 영향주는 요소 순위 ===")
    print(중요도)


고객이탈예측()