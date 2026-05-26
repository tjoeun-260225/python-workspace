"""
로지스틱회귀(Logistic Regression)
- 분류(Classification) 문제를 푸는 알고리즘
- 이름에 회귀가 있지만 실제로는 예/아니오 같은 이진(두가지)분류 사용

1. 시그모이드 함수 - 결과를 0~1 사이로 바꿔주는 기능
                     model = LogisticRegression(max_iter=10000) 안에 시그모이드가 내장되어 있다.

2. 이     진 분류 -  둘 중 하나 고르기  YES OR NO 위에서 바뀐 결과를 0.5 기준으로 0이나 1로 변경
                     predict()    predict_proba() 기능이 이진 분류 해당

3. 다     중 분류 - 강아지 / 고양이 / 새 처럼 3가지 이상 중 하나 고르는 상황
                     model = LogisticRegression(multi_class="multinomial",max_iter=10000)
                     multi_class="multinomial" -> 여러 분류 처리 표기
                     붓꽃 데이터 : 꽃잎 길이,너비로 예상 흐름에 따라 품종 3가지 중 한가지로 맞추기

4. 정    규    화 - 적절히 가중치를 조절할 때 사용하는 규칙
                    새로운 데이터에 가중치로 인하여 모델이 제대로 동작하지 않음을 방지하기 위하여 하는 작업

5. ROC   /   AUC - ROC 곡선은 모델이 얼마나 잘 구분하는지 보여주는 그래프 에서 사용
                    Receiver Under the Curve
                   AUC 그 점수  1.0 에 가까울 수록 완벽한 모델
                                0.5 동전던지기 수준으로 구리다.
                    Area Under the Curve = 곡선 아래쪽 면적이 AUC 점수인데, 면적이 넓을수록(1에 가까울수록)좋은 모델








  선형 회귀
- 값 예측
- 집값 예측
- 어떻게 결과가 나올 것 같다.

  로지스틱 회귀
- 확률(0 ~ 1)
- 분류
- 합격/불합격 예측
- 예측을 통한 결과가 기다 아니다 로 분류

선형 회귀로 나온 결과로 로지스틱 회귀에서 사용하여 분류를 하고자 할 경우
확률이 1을 넘거나 음수가 나올 수 있어 문제가 발생
시그모이드 함수로 0~1 사이로 값을 조절

어떤 값이 들어와도 0과 1 사이로 변환 이게 확률처럼 동작

출력이 0.7 → 70% 확률로 양성
보통 0.5 기준으로 분류 → 0.5 이상이면 1, 미만이면 0 분류

* 시그모이드 함수
  - 19세기 벨기에 수학자 피에르 베르휠스트 1838 ~ 1845 개발
  - 인구 증가 모델링
  - 인구는 무한정 증가하지않고, 환경의 한계(먹이, 공간)에 따라 수렴한다.
  - 이걸 수식으로 표현하려니 자연스레 S자 곡선
  - 이후 머신러닝 연구자들이 0~1 사이로 눌러주어 예측에 따른 결과를 2가지로 분류하고자 하는
    성질이 일치하다 판단하여 머신러닝으로 시그모이드 함수를 가져온 것

선형 회귀 결과를 로지스틱 회귀에서 사용하여 분류할 때 결과를 0~1 사이로 정제해야할 상황 발생

선형 회귀로 나온 결과에 시그모이드를 덧씌운 게 로지스틱 회귀

로지스틱 회귀 = 선형 회귀 + 시그모이드
              예    측  + 예측에 따른 결과를 0.5 기준 미달성 달성과 같이 분류

로지스틱 왜 로지스틱인가
-> 베르휠스트 - 인구 모델 논문 S 자 곡선에 대하여 logistique 이름을 붙임
       수학에서 log 가장 많이 사용하기 때문에 logis 라는 것을 붙여 이름 창조하지 않았을까 추측
"""

import  pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics  import accuracy_score

# 1. 모델 불러오기
data = load_breast_cancer()
X = data.data # 유방암 종양 특성 30가지 들어있는 데이터셋 가져오기
y = data.target # 0=악성 1=양성


print(data.DESCR) # 데이터 설명 출력
print("feature 이름 : ", data.feature_names)
print("X shape : ", X.shape) # (569, 30) 569 데이터와 30개의 컬럼 존재
print("y 분  포 : ",{0: sum(y==0), 1: sum(y==1)}) # 악성 / 양성 개수 확인

# 2. 학습과 학습이 제대로 되었는지 확인하기 위하여 데이터 && 정답 8:2 로 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 학습 위에서 분리한 데이터를 훈련시킬 모델 선택
# max_iter = 모델이 학습할 때 반복 횟수 최대값
# 학습 = 정답에 가까워지도록 가중치를 조금씩 수정 이걸 여러번 반복
# max_iter = 100 번만 반복 훈련(기본값, 경고 뜰 수 있다.)
# max_iter = 10000 반복 훈련
# 모델 학습을 100번 하게 할지 10000번 하게 할지 선택
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train) # 위에서 선택한 모델로 훈련시키기

# 4. 예측 & 성능 확인
# y_test = 테스트용 20% 들어있는 정답 데이터
# y_pred = LogisticRegression 을 이용하여 X_test 확인하고 예측한 결과 저장
# y_prob = 0 또는 1로 딱 자르는 거이 아니라 각 클래스일 확률 반환
# [:,1] 처음부터 끝까지 가져오되, 1열만 조회하겠다.
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1] # 양성일 확률
"""
predict() = 결론만 말한다. 0이다 1이다.
predict_proba() = 확률도 말해준다. 1일 확률이 77% 다.

확률까지 보고 싶을 때 predict_proba() 사용

"""


#  * 100:.1f%
# % 는 계산할 때 반드시 필요한 것이 아니라 결과를 사람들이 보기좋게 붙이는 기호
print(f"정확도 : {accuracy_score(y_test, y_pred) * 100:.1f}%")

result = pd.DataFrame({
    "실제":y_test[:10],
    "예측":y_pred[:10],
    "양성확률":y_prob[:10].round(2),
})



