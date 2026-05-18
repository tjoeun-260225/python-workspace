'''
컴퓨터가 몃이적인 프로그래밍 없이 데이터를 통해 스스로 학습하는 작업
사람이 "이럴 땐 이렇게 해" 라고 일일이 규칙을 짜주는 게 아니라
데이터를 잔뜩 보여주면 컴퓨터가 패턴을 찾아서 스스로 판단

스팸 메일 필터 → 수천 개의 스팸 / 정상 메일을 학습해서 메일이 스팸인지 차단
유튜브    추천 → 내 시청기록을 분석해서 좋아할 영상 추천
얼굴      인식 → 수백만 장의 얼굴 사진을 학습해서 누구인지 구별

크게 3가지 방식
지  도 학습 ─ 정답이 있는 데이터로 학습    (예 : 고양이 / 개 사진 분류)
            이미지 조회, 마스크 착용 유무
비지도 학습 ─ 정답 없이 데이터 패턴만 찾기 (예 : 고객 군집 분석)
강  화 학습 - 보상 / 패널티를  통해 학습   (예 : 바둑 AI, 게임 AI)

데이터 많이 보여주면 알아서 똑똑해지는 알고리즘

처음 머신러닝을 접하는 개발자들이 많이 사용하는 방식
pip install scikit-learn

scikit-learn
 - 파이썬에서 머신러닝을 쉽게 쓸 수 있게 만들어놓은 라이브러리(도구 모음)

 머신러닝 알고리즘을 처음부터 직접 작성하면 수백 수만 줄이된다.
 scikit-learn 위와 같은 알고리즘을 미리 만들고, 가져다 개발자들이 사용하면 되는 구조

 계산기를 몰라도 계산기를 사용할 수 있는 것처럼 머신러닝 초기 기능 제공

 존재하는 종류
 분  류 - 스팸이냐 아니냐 고양이냐 개냐 판단
 회  귀 - 집값 예측, 주가 예측
 군  집 - 비슷한 고객끼리 묶기
 전처리 - 데이터 정규화, 결측값 처리
 평  가 - 모델이 얼마나 정확한지 측정

 작성 방법
 from sklearn.가져올기능 import 사용할기능

 model = 기능 model 에 담아두기
 model.fit(X_train, y_train) # 학습
 model.predict(X_test)       # 예측
 model.score(X_test, y_test) # 정확도
 위 4가지는 모든 모델에서 똑같이 사용, 모델만 바꾸면 나머지는 동일하게 사용 가능
'''
# sklearn 에 존재하는 붓꽃 분류
# from 큰창고.작은창고 import 필요한 것
# 큰 창고 안에 용도별로 작은 창고가 있고, 거기서 필요한 것만 꺼내사용 이름이 길 경우 as 로 별칭을 붙여 사용가능
from sklearn.datasets import load_iris  # sklearn 에서 만든 150개의 붓꽃 데이터가 준비되어 있다.
from sklearn.model_selection import train_test_split  # 데이터를 학습용이랑 테스트용으로 나눠주는 도구
# 예를 들어 100개의 데이터가 있으면 80개는 공부용, 20개는 시험용으로 자동으로 데이터 쪼개준다.
from sklearn.neighbors import KNeighborsClassifier  # KNN 이라는 머신러닝 모델을 가져오는 것
# KNN 새로운 데이터가 들어오면 주변에 가장 가까운 이웃들을 보고
# 얘네가 다 고양이니까 너도 고양이겠다 라는 식으로 판단하는 알고리즘
from sklearn.metrics import accuracy_score  # 모델이 얼마나 맞혔는지 정확도를 계산해주는 도구 예측값이랑 실제 정답을 비교하여 몇 % 맞았는지 숫자로 알려준다.

# sklearn 은 회사에서 자주 사용하지 않는다. 회사마다 원하는 AI가 다르고, 코드가 100% 동일하다는 보장은 없다.
# 모델을 불러오고 / 모델선택 학습 / 예측 / 정확도 확인 -> 결과 시각화나 페이지에서 확인할 수 있는가
# 에 대해서 공부!

# 1. 데이터 불러오기
"""
대문자 X를 사용하는 이유
관례 / 규칙이 아니라 전 세계 머신러닝 개발자들이 약속처럼 사용하는 것
X ─ 입력 데이터 여러 개의 열(컬럼)이 있는 2차원의 표 이기 때문에 수학에서 행렬을 대문자로 표기하는 관례를 따른 것
y ─ 정답 데이터 1줄짜리 1차원 이라서 소문자 
    수학에서 y = f(x) 할 때 y
붓꽃의 데이터는 아래와 같은 표 형태로 생겼다.

꽃받침길이      꽃받침너비      꽃잎길이      꽃잎너비
   5.1            3.5             1.4           0.2
   4.9            3.0             1.4           0.2
   
1936년도 로널드 피셔라는 통계학자가 붓꽃 3종류를 직접 측정해서 논문에 쓴 데이터가 존재
통계/머신 러닝 역사에서 가장 유명한 예제 데이터
거의 모든 교과서에 등장
전통처럼 내려오는 데이터
"""

붓꽃 = load_iris()
X = 붓꽃.data         # 입력값 (꽃잎길이, 너비 등)
y = 붓꽃.target       # 정답(0:setosa, 1:versicolor, 2:virginica

print("데이터 shape : ", X.shape)  # 데이터 shape:(150,4) 꽃받침길이 꽃받침너비 꽃잎길이 꽃잎너비 데이터가 150개 존재
print("정답 종류 : ", 붓꽃.target_names)
#   index          0           1           2
# 정답 종류 :  ['setosa' 'versicolor' 'virginica']
# setosa     (세토사)   : 털붓꽃 꽃잎이 작고 아담한 종류
# versicolor(버시컬러)  : 버들붓꽃 색이 여러 가지로 변하는 붓꽃
# virginica(버지니카)   : 미국 버지니아 지역에서 발견된 붓꽃 3종류 중 꽃잎이 제일 크고  화려하다

# print("정답 종류 : ", 붓꽃.target_name)
#  AttributeError: target_name. Did you mean: 'target_names'?

# pd.DataFrame() 을이용해서 iris() 표형태를 조회할 수 있다.
print(dir(붓꽃))  # ['DESCR', 'data', 'data_module', 'feature_names', 'filename', 'frame', 'target', 'target_names']
# dir(변수) = 해당변수에서 사용할 수 있는 속성이나 메서드 조회 가능


# 2. 학습용 / 테스트용 나누기 (8:2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 선텍 & 학습
model = KNeighborsClassifier(n_neighbors=3)  # KNN : 가까운 이웃 3개로 판단
model.fit(X_train, y_train)                     # 학습

# 4. 예측
y_pred = model.predict(X_test)

# 5. 정확도 확인
acc = accuracy_score(y_test, y_pred)
print(f"정확도:{acc * 100:.1f}%")

#### 개발자는 원하는 예측과 정확도로 추후 모델 생성(부품처럼)
#### 만들어진 부품을 웹사이트나, 기계에 장착하여 붓꽃인지 아닌지 판단하는 사이트나 기계 생성