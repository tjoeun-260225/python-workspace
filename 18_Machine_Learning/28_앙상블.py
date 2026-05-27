"""
앙상블
- 여태 했던 것처럼 모델을 하나만 쓰는 것이 아닌 2개 이상 사용하는 상황에 대한 용어
- 하나의 모델이 아닌 여러 모델을 합쳐서 더 정확한 모델을 만들겠다.
- Ensemble = 프랑스어 함께 같이 뜻
  음악에서 여러 악기가 합주하는 것 앙상블이라 부르며, 악기 하나하나는 소리가 제한적인데,
  여러 악기가 각자 다른 소리를 내면서 합쳐지면훨씬 풍부한 음악이 된다.

예 )
  환자 데이터 를 X에 넣으면 예측값을 뱉어낸다.
  X = [[키, 몸무게, 혈압, 나이]]    [] = 하나의 컬럼데이터가 들어있는것, [[]] = 표 형태의 컬럼데이터

  lr.redict(X)  # 로지스틱 회귀가 판단  → [1] (양성)   → 데이터를 보고 경계선을 그려 판단
  dt.redict(X)  # 결정     트리가 판단  → [1] (양성)   → 스무고개 방식으로 판단
  knn.redict(X) # K     N    N 이 판단  → [0] (음성)  → 이 환자와 비슷한 환자 3명 찾기 비슷한 환자로 판단

  다수 모델의 다수결로 인하여 결정을 내리는 것

  현실
    데이터 하나의 3명의 의사소견을 가지고 결정을 내린다.
"""

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# data = load_iris()
# X = data.data
# y = data.target  # 아래 한 줄과 똑같이 작동한다.
X, y = load_iris(return_X_y=True)  # 반환할 때 X에 data y에 target 으로 반환하겠다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 앙상블
# 1. 투표(Voting)
# 여러 개의 다른 모델을 선언하고, 각 모델의 예측을 투표로 합친 것
# 1-1 하드  보팅 - 칼같이 각 모델에 결과를 선택
#     모델A → 고양이  모델B → 고양이 모델C → 강아지    2:1 로 고양이 승리!

# 1-1 소프트보팅 - 부드럽게 확률까지 고려하여 유연하게 판단
#     모델A → 고양이51%  모델B → 고양이52% 모델C → 강아지99%
#     애매한 두 모델의 확률보다 강아지 99% 확률을 따르겠다.   강아지 승리!

# 두 보팅을 모두 사용하기 보다는 실무에서는 소프트보팅만 주로 사용
# 모델이 확률을 못 뱉을 때 하드를 함께 사용하거나 하드만 사용
로지스틱모델 = LogisticRegression(max_iter=200)
결정트리모델 = DecisionTreeClassifier()
KNN모델 = KNeighborsClassifier()


def Voting기능설명():
    # VotingClassifier = 여러 모델을 묶어서 하나처럼 사용하게 해주는 틀
    # 모델 하나만 작성해도 되지만 의미가 없다.. 굳이 의미없는 행동하지 말자
    투표_1 = VotingClassifier(
        # estimators = 묶을 모델들을 리스트로 넣는 곳
        # estimators=[
        #          ('개발자가 붙인 별명_1', 실제 모델이 담긴 변수 공간의 명칭_1),
        #          ('개발자가 붙인 별명_2', 실제 모델이 담긴 변수 공간의 명칭_2),
        #          ('개발자가 붙인 별명_3', 실제 모델이 담긴 변수 공간의 명칭_3),
        #           ... 모델 원하는만큼 선언하고 호출 하여 비교 가능
        #        ],
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        # voting = 투표방식
        #       hard = 다수결
        voting='hard'
    )
    투표_2 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        #       soft = 확률
        voting='soft'
    )

    투표_1.fit(X_train, y_train)
    결과 = 투표_1.predict(X_test)
    print(f"하드 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")
def 하드투표기능():
    하드투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='hard'
    )
    하드투표.fit(X_train, y_train)
    결과 = 하드투표.predict(X_test)
    print(f"하드 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")
def 소프트투표기능():
    소프트투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='soft'
    )
    소프트투표.fit(X_train, y_train)
    결과 = 소프트투표.predict(X_test)
    print(f"소프트 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")
# 하드 투표 같이 사용 가능? ok 가능
# for 문이용해서 하면 된다.
def 하드_소프트_투표기능():
    하드투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='hard'
    )
    소프트투표 = VotingClassifier(
        estimators=[('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)],
        voting='soft'
    )
    # 학습 & 평가 version1 = 하드 냐 소프트 냐
    for 이름, 모델 in [('하드투표', 하드투표), ('소프트투표', 소프트투표)]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 정확도 : {accuracy_score(y_test, 결과):.4f}")

    # 개별 모델별 어떻게 정확도가 나왔는지도 몹시 궁급하네요 ^^
    # 학습 & 평가 version2 = 로지스틱 / 결정 트리 / KNN 각 확률이나 비율이 어떻게 나왔는가
    for 이름, 모델 in [('lr', 로지스틱모델), ('dt', 결정트리모델), ('knn', KNN모델)]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 정확도 : {accuracy_score(y_test, 결과):.4f}")

# 2. 랜덤포레스트(Random Forest)
#    보팅은 다른 종류의 모델을 합쳐서 결과를 하나로 확인하지만
#    랜덤포레스트는 같은 결정트리를 여러 개 만들어서 합친다
#    각 트리를 다르게 만들기 위해 두 가지 무작위성을 사용

## * 결정트리(Decision Tree)
##   스무고개 방식으로 데이터 분류
##   질문을 던지고 → Yes / No 나누고 → 또 질문 반복해서 → 최종 답을 낸다.
##   질문을 너무 깊게 파고들면 훈련 데이터를 통째로 외우기만하고, 새로운 데이터 약하다.


# 3. 앙상블 - 부스팅
## 부스팅 : 틀린 것에 집중해서 계속 고쳐가는 방식
## 랜덤포레스트는 여러 모델을 동시에 사용하여 만들지만,
## 부스팅은 모델을 순서대로 만들면서 이전 모델이 틀린 것을 다음 모델이 보완
### 부스팅 모델 종류
### 3-1. AdaBoost : 틀린 샘플에 가중치(weight)를 높여서 다음 모델이 그걸 더 열심히 학습
### 3-2. Gradient Boosting Machine : 틀린 정도를 경사 하강법으로 줄여나감
###      AdaBoost 보다 수학적으로 정교하고 성능이 좋지만 느리다.

##### pip install xgboost   pip install lightgbm 따로 설치해야한다.
### 3-3. XGBoost  : GBM(3-2)의 단점(느림, 과적합)을 개선한 버전
### 3-4. LightGBM : XGBoost 보다 빠른 버전(대용량 데이터에 최적) 데이터가 적으면 성능이 좋지않다.

#### XGBoost LightGBM 은 sklearn이 만든 Boost 를 토대로 다른 개발자와 회사가 만든 것
#### sklearn 2007년에 오픈소스 커뮤니티에서 만들어짐
###  XGBoost 2014년에 워싱턴대학교에 있는 천티안치 개발자가 만든 것
### LightGBM 2016년에 마이크로소프트가 XGBoost 를 보고 만든 것


## 4. 스태킹
## 여러 모델의 예측값을 새로운 입력으로 사용해서 최종 모델 학습
## 기존 데이터 → [모델1, 모델2, 모델3, ...] → 각 모델의 예측값 → 메타 모델 → 최종 예측

