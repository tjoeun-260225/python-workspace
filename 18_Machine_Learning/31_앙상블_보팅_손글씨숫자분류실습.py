"""
앙상블 실습 - 손글씨 숫자 분류
- 0~9 숫자 이미지를 분류 (10개 클래스)
- 이미지 데이터라 피처가 64개 (8x8 픽셀)
- 클래스가 10개라 모델별 차이가 더 극명하게 남

예)
   손글씨 이미지를 X에 넣으면 숫자를 예측
   X = [[픽셀1, 픽셀2, 픽셀3 ... 픽셀64]]  # 8x8 이미지를 1줄로 펼친 것

   lr.predict(X)  # 로지스틱 회귀가 판단 → [3] (숫자 3) → 경계선       그려 판단
   dt.predict(X)  # 결  정  트 리가 판단 → [3] (숫자 3) → 스무고개 방식으로 판단
   knn.predict(X) # K   N    N  이 판단 → [5] (숫자 5) → 비슷한 이미지 찾아서 판단
   다수 모델의 다수결로 최종 결정
"""

# TODO 1: 아래 빈칸에 필요한 라이브러리를 임포트 하세요
#          힌트: 유방암 실습과 동일, 데이터셋만 load_digits 로 교체
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# TODO 2: 손글씨 데이터를 X, y 로 불러오세요
X, y = load_digits(return_X_y=True)

# TODO 3: 학습/테스트 데이터를 8:2 로 분리하세요 (random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO 4: 세 모델 변수를 선언하세요 (로지스틱은 max_iter=1000)
로지스틱모델 = LogisticRegression(max_iter=1000)
결정트리모델 = DecisionTreeClassifier()
KNN모델 = KNeighborsClassifier()


def 하드투표기능():
    # TODO 5: VotingClassifier 로 하드 보팅 모델을 만드세요
    하드투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='hard'
    )
    하드투표.fit(X_train, y_train)
    결과 = 하드투표.predict(X_test)
    print(f"하드 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")


def 소프트투표기능():
    # TODO 6: VotingClassifier 로 소프트 보팅 모델을 만드세요
    소프트투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='hard'
    )
    소프트투표.fit(X_train, y_train)
    결과 = 소프트투표.predict(X_test)
    print(f"소프트 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")


def 개별모델비교():
    # TODO 7: 로지스틱, 결정트리, KNN 각각 학습하고 정확도를 출력하세요
    for 이름, 모델 in [('로지스틱', 로지스틱모델), ('결정트리', 결정트리모델), ('KNN', KNN모델)]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 정확도 : {accuracy_score(y_test, 결과):.4f}")


# TODO 8: 세 함수를 모두 호출하세요
하드투표기능()
소프트투표기능()
개별모델비교()

# 기대 출력 예시
# 하드 보팅 정확도 : 0.9694
# 소프트 보팅 정확도 : 0.9750
# 로지스틱 정확도 : 0.9583
# 결정트리 정확도 : 0.8361   ← 제일 약함
# KNN     정확도 : 0.9833
