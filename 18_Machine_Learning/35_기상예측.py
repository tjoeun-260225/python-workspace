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

    # TODO 1: CSV 파일 읽기
    # 힌트: pd.read_csv("파일명.csv")
    df = ___

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print("\n=== 몇 행 몇 열? ===")
    print(df.shape)

    # TODO 2: 결측치(빈값) 채우기
    # 힌트: df['Temperature'].fillna(df['Temperature'].mean()) 이런식으로
    # 힌트: 숫자 컬럼은 평균으로, df.isnull().sum() 에서 0 아닌 컬럼만 처리
    df['Temperature']  = ___
    df['Humidity']     = ___
    df['Wind_Speed']   = ___
    df['Precipitation']= ___

    # TODO 3: 사용할 피처(컬럼) 리스트 직접 채우기
    # 힌트: head() 출력 보고 정답(Rain) 빼고 나머지 숫자 컬럼 다 넣기
    # 힌트: features = ['Temperature', 'Humidity', ___, ___]
    features = [___, ___, ___, ___]

    # TODO 4: X (입력), y (정답) 나누기
    # 힌트: X = df[features]
    # 힌트: y = df['Rain']   ← 비옴=1, 안옴=0
    X = ___
    y = ___

    # TODO 5: 훈련/테스트 데이터 나누기
    # 힌트: train_test_split(X, y, test_size=0.2, random_state=42)
    # 힌트: 반환값 4개 → X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = ___

    # TODO 6: 랜덤포레스트 모델 만들기
    # 힌트: RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)
    rf = ___

    # TODO 7: 모델 학습시키기
    # 힌트: rf.fit(___, ___)  ← 훈련 데이터 넣기
    ___.fit(___, ___)

    # TODO 8: 테스트 데이터로 예측하기
    # 힌트: rf.predict(___)  ← 테스트 입력 넣기
    pred_rf = ___

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['맑음', '비']))

    # =======================================
    # VotingClassifier (3개 모델이 투표)
    # 맑음 / 맑음 / 비  → 다수결 → 맑음 승리
    # =======================================

    # TODO 9: 3개 모델 각각 만들기
    # 힌트: RandomForestClassifier(n_estimators=100, random_state=42)
    # 힌트: DecisionTreeClassifier(random_state=42)
    # 힌트: LogisticRegression(max_iter=1000, random_state=42)
    model1 = ___   # 랜덤포레스트
    model2 = ___   # 결정트리
    model3 = ___   # 로지스틱회귀

    # TODO 10: VotingClassifier 만들기
    # 힌트: estimators 에 이름이랑 모델 묶어서 리스트로 넣기
    # 힌트: estimators=[('rf', model1), ('dt', model2), ('lr', model3)]
    # 힌트: voting='hard'  ← 다수결 투표
    voting = VotingClassifier(
        estimators=[('rf', ___), ('dt', ___), ('lr', ___)],
        voting=___
    )

    # TODO 11: voting 모델 학습시키기
    # 힌트: TODO 7 이랑 똑같이, rf 대신 voting 넣기
    ___.fit(___, ___)

    # TODO 12: voting 모델로 예측하기
    # 힌트: TODO 8 이랑 똑같이, rf 대신 voting 넣기
    pred_voting = ___

    print("\n=== 보팅 결과 (3개 모델 투표) ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['맑음', '비']))

    # TODO 13: 랜덤포레스트 vs 보팅 정확도 비교 출력
    # 힌트: accuracy_score(y_test, pred_rf) 랑 accuracy_score(y_test, pred_voting) 비교
    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 정확도 : {accuracy_score(y_test, ___): .4f}")
    print(f"보팅        정확도 : {accuracy_score(y_test, ___): .4f}")
    if accuracy_score(y_test, pred_voting) > accuracy_score(y_test, pred_rf):
        print("보팅이 더 좋다.")
    else:
        print("랜덤포레스트가 더 좋다.")

    # TODO 14: 피처 중요도 출력
    # 힌트: 학습된 rf 모델에서 rf.feature_importances_ 로 꺼냄
    # 힌트: pd.DataFrame({'특성': features, '중요도': ___})
    # 힌트: .sort_values('중요도', ascending=False) 로 높은 순 정렬
    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': ___
    }).sort_values(___, ascending=___)

    print("\n=== 비 오는 데 영향주는 요소 순위 ===")
    print(중요도)


날씨예측()