import os

"""
1. KNN(K-Nearest Neighbors)
 - 가장 가까운 이웃 K를 보고 다수결로 분류하는 알고리즘
 - 보통 n_neighbors=3 or 5 몇 개의 이웃을 볼지 결정하고, 너무 크면 오히려 정확도가 떨어짐
 - 분류실습에서 주로 사용



2. 선형 회귀(Linear Regression)
- 숫자를 예측하는 회귀 모델
- 직선을 찾는 방식
- 집값, 주가, 판매량 예측 등 연속적인 숫자 예측 사용
- 평가 지표는 정확도가 아닌 RMSE R² 사용



3. 로지스틱 회귀(Logistic Regression)
- 이름은 회귀이지만 실제로는 분류하는 모델
- 데이터의 경계선을 그어서 0 또는 1처럼 확률로 분류
- max_iter 로 학습 반복 횟수 조절 데이터는 많은데 학습이 적으면 경고 발생
-                                 데이터는 적은데 학습이 많으면 경고 발생



4. 나이브 베이즈(Naive Bayes)
- 조건부 확률을 기반으로 분류하는 알고리즘
- 각 단어가 서로 독립적이고 단순하게 가정하고 확률을 곱해서 판단
- 텍스트 데이터에서 주로 사용 스팸 분류, 감정 분석, 뉴스 카테고리 분류에서 주로 사용
- MultinomialNB 사용하고, 반드시 CountVectorizer 로 텍스트를 숫자로 변환한 뒤 사용



5. 결정 트리(Decision Tree)
- 스무고개 방식으로 데이터를 분류하는 모델
- 질문을 던지고 Yes/No 로 나누는 과정을 반복해서 최종 답을 낸다.
- 질문을 너무 깊게 파고들면 훈련 데이터만 통째로 외워 새로운 데이터에 약해지는 문제가 발생
- 주로 랜덤 포레스트에서 참고하여 사용



6. 앙상블 - 보팅(Voting)
- 여러 모델을 합쳐서 다수결로 최종 결과를 내는 방식
- 하나의 모델만 쓰는 게 아니라 로지스틱, 결정트리, KNN 등 여러 모델 동시 사용
- 하드 보팅 : 각 모델의 결과를 칼같이 다수결로 결정
- 소프트 보팅 : 각 모델의 확률까지 고려해서 유연하게 판단 실무에서 주로 사용
- VotingClassifier



7. 앙상블 - 랜덤 포레스트(Random Forest)
- 보팅이 서로 다른 종류의 모델을 합치는 것과 달리, 같은 결정 트리를 여러개 만들어서 합침
- 각 트리를 다르게 만들기 위해 데이터와 피처를 무작위로 뽑아서 학습
- 트리 하나하나는 약하지만 여러 개가 합쳐지면 강력
- n_estimators 로 트리 개수 조절

현재 배운 모델 기준으로 상황에 따른 모델 사용 방법
- 숫자 예측 → 선형 호귀
- 텍스트 분류 → 나이브 베이즈
- 일반 분류, 빠르게 공부 시작 → KNN, 로지스틱 회귀
- 정확도를 더 높이고 싶다 → 랜덤 포레스트
- 여러 모델 결과를 합쳐서 하나의 결과로 보고싶다 → 보팅
"""

# 1. KNN
# 데이터가 많을 수록 좋고, 이미지/수치 분류 사용 / 텍스트 데이터엔 잘 안 씀
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)  # 기본값으로 3 또는 5
model.fit('X_train', "y_train")
model.predict("X_test")

# 2. 선형 회귀(Linear Regression)
# 숫자를 예측할 때 사용 집값, 주가, 판매량처럼 결과가 연속된 숫자일 때 사용
# 분류에서 사용 안 함, 평가는 정확도 대신 예측도 RMSE, R² 사용
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit('X_train', "y_train")
model.predict("X_test")

# 3. 로직스틱 회귀(Logistic Regression)
# 이름은 회귀이지만 회귀에 따른 분류 모델 결과가 0 또는 1 처럼 두가지로 나뉠 때 사용
# 스팸 정상, 양성 음성 처럼 경계선을 그어 확률로 분류
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=100)  # 데이터 양에 비해 학습이 적으면 경고 뜬다.
# 데이터가 많은데 이거로 잘 되겠어?!?!?!?!?!
# 정확도를 확인하면서 max_iter 조절 경고뜬다하여 개발자의 자아가 흔들리지 말 것!!
model.fit('X_train', "y_train")
model.predict("X_test")

# 4. 나이브 베이즈(Naive Bayes)
# 텍스트 데이터 분류 전용
# 스팸 분류, 감정 분석, 뉴스 카데고리 분류에 사용
# 데이터가 적어도 잘 작동하고 속도 빠름
# 반드시 CountVectorizer로 텍스트를 숫자로 바꾼 뒤 사용
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform("X_train")  # fit_transform 훈련용 데이터 다듬기
X_test_vec = vectorizer.transform("X_test")  # transform 훈련 제대로 되었는지 확인용 데이터 다듬기
model = MultinomialNB()
model.fit(X_train_vec, X_test_vec)
model.predict(X_test_vec)

# 5. 결정 트리(Decision Tree)
# 스무고개 방식 분류
# 단독 사용 보다 앙상블의 재료로 주로 사용
# 단독으로 사용하면 정확도 불안정
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit("X_train", "y_train")
model.predict("X_test")

# 6. 앙상블 - 보팅
# 여러 모델을 동시에 돌려서 다수결로 결과 내기
# 모델 하나가 틀려도 나머지가 보완해줘서 단일 모델보다 안정적
# 소프트 보팅이 확률까지 고려해서 더 좋고, 실무에서도 소프트를 주로 사용
# 참고로 위 전제는 모두 앙상블-보팅을 회사에서 사용한다면 소프트가 좋다는 것이다.
# 앙상블 - 보팅을 안쓰면 실무에서 의미 없다.

# 7. 앙상블 - 랜덤 포레스트
# 결정 트리를 여러 개 만들어서 합친다.
# 결정 트리의 과적합 문제를 해결한 모델
# 수치 데이터 분류에서 정확도가 높고 안정적이라 실무에서 많이 사용되는 앙상블 모델 중 하나
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit("X_train", "y_train")
model.predict("X_test")
