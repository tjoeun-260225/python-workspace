"""
앙상블 실습 - 와인 품종 분류
- 와인의 알콜, 산도, 색상 등 13개 성분으로 와인 품종 3가지를 분류
- 아이리스(=붓꽃)보다 KNN이 약해서 보팅(모델 투표를 통한 결과) 효과가 더 잘 보임

예)
   와인 데이터를 X에 넣으면 품종을 예측
   X = [[알콜, 산도, 색상강도, 플라보노이드,...]]

   lr.predict(X)  # 로지스틱 회귀가 판단 → [0] (1등급 와인) → 경계선       그려 판단
   dt.predict(X)  # 결  정  트 리가 판단 → [0] (1등급 와인) → 스무고개 방식으로 판단
   knn.predict(X) # K   N    N  이 판단 → [0] (2등급 와인) → 비슷한 와인 찾아서 판단
   다수 모델의 다수결로 최종 결정
"""

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine  # 데이터만 붓꽃 → wine 교체
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터를 데이터셋과 어떤 데이터인지 정답으로 분리하기
X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT
로지스틱모델 = LogisticRegression(max_iter=20000)  # 모델 데이터에 비해서 200번 학습은 너무 적다
결정트리모델 = DecisionTreeClassifier()
KNN모델 = KNeighborsClassifier()


def 하드투표기능():
    하드투표 = VotingClassifier(
        estimators=[
            ('lr', 로지스틱모델),
            ('dt', 결정트리모델),
            ('knn', KNN모델),
        ],
        voting='hard'
    )
    하드투표.fit(X_train, y_train)
    결과 = 하드투표.predict(X_test)
    print(f"하드 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")

def 소프트투표기능():
    소프트투표 = VotingClassifier(
        estimators=[
            ('lr', 로지스틱모델),
            ('dt', 결정트리모델),
            ('knn', KNN모델),
        ],
        voting='soft'
    )
    소프트투표.fit(X_train, y_train)
    결과 = 소프트투표.predict(X_test)
    print(f"소프트 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")

def 하드_소프트투표기능():
    하드투표 = VotingClassifier(
        estimators=[
            ('lr', 로지스틱모델),
            ('dt', 결정트리모델),
            ('knn', KNN모델),
        ],
        voting='hard'
    )
    소프트투표 = VotingClassifier(
        estimators=[
            ('lr', 로지스틱모델),
            ('dt', 결정트리모델),
            ('knn', KNN모델),
        ],
        voting='soft'
    )
    # 학습 & 평가 version1 = 하드인가 소프트인가 확인
    for 이름, 모델 in [ ('하드투표',하드투표),('소프트투표',소프트투표)]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")

    # 학습 & 평가 version2 = 로지스틱 / 결정트리 / KNN 모델별 정확도 확인
    for 이름, 모델 in [ ('lr', 로지스틱모델),
                    ('dt', 결정트리모델),
                    ('knn', KNN모델),]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 정확도 : {accuracy_score(y_test, 결과):.4f}")

print(하드투표기능())
print("="*20)
print(소프트투표기능())
print("="*20)
print(하드_소프트투표기능())
"""
하드 보팅 정확도 : 1.0000
====================
소프트 보팅 정확도 : 0.9722
====================
하드투표 보팅 정확도 : 1.0000
소프트투표 보팅 정확도 : 0.9722
lr 정확도 : 1.0000
dt 정확도 : 0.9444
knn 정확도 : 0.7222
knn -> 정확도가 불안정해서 소프트도 애매한 정답률을 준다.

스케일링
"""