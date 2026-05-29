"""
차원축소
고차원 데이터를 저차원으로 압축하는 기술
예를 들어 100개의 특성(컬럼)을 2~3개로 줄여서 시각화 하거나 학습을 빠르게 만든다.
        주성분     구성요소  분석
1. PCA(=Principal Component Analysis 주성분 분석)
 모델데이터의 결과를 직선으로 보겠다.
 데이터의 분산이 최대가 되는 축을 찾아서 투영한다.
 선형 변환만 가능
 속도 빠름 가장 기본적인 방법
 데이터를 정규화(=StandardScaler) 사용 후 사용할 수 있다.

 예를 들어 100명의 학생 데이터가 있다.
 키(cm), 몸무게(kg), 발사이즈(mm), 허리둘레(cm), 팔길이(cm), ... 총 50개의 컬럼
 이 50개를 모두다 그래프로 그리거나 분석하기 복잡
  - 컬럼들 중에서 중요한 정보만 뽑아서 2~3개로 줄일 수 없을까?

2. 커널 PCA(Kernel PCA)
 모델데이터의 결과를 곡선으로 보겠다.
 rbf와 같은 기능을 사용하며 선형으로 분리 안되는 데이터를 분리되는 방식을 찾은 후 다시
 원래 형태로 압축하는 것
 kernel 종류 : rbf, poly, sigmoid, cosine

3. LDA(=Linear Discriminant Analysis 선형 판별 분석)
 PCA는 데이터 퍼짐을 최대화, LDA 클래스 간의 거리를 최대화
 예) 시험 성적 데이터로 PCA 와 차이점 확인하기
 학생 100명의 데이터 :
 - 수학 점수
 - 영어 점수
 - 과학 점수
 → 이 학생들이 "문과 / 이과 / 예체능" 중 어디 속하는지 알고 있다.

 PCA : 데이터가 가장 넓게 퍼지는 방향으로 축을잡고 모델 학습 시작
       여기서 문과 이과 예체능은 무시한다.
       성적 데이터에 따른모델이 중요한 것이지 문과 이과 예체능은 성적과 무관
 LDA : 문과 이과 예체능이 가장 잘 분리되는 방향으로 축을 잡아서 모델 학습 시작
       성적 데이터에 영향을 주는 컬럼일 것이다는 전제하에 학습 시작

4.LLE(= LocallyLinearEmbedding 지역 선형 임베딩)
 각 점을 이웃들의 선형 결합으로 표현
 노이즈에 민감하고 대규모 데이터에 느림

 비선형 매니폴드(구부러진 공간) 처리 기능
 n_neighbors 파라미터가 매우 중요

 PCA 와 LLE 비교
 PCA 는 전체를 한 번에 펼쳐서 확인
 LLE 는 동네별로 쪼개서 펼침
 3D지구를 2D평면 지도로 만들 때
 PCA 방식 : 지구 전체를 한 번에 찍어서 납작하게 누름 왜곡 현상이 발생할 수 있다.
 LLE 방식 : 우선 가운데 선을 기준으로 펼치고 조심조심 펼친다.
            남극 북극 쪽에는 데이터 훼손이 없는지 확인(크기)
            각 주변 국가들 관계를 유지하면서 펼친다.

5. NMF(비음수 행렬 분해)
 얼굴 사진이 있다. 얼굴 사진을 눈 코 입 같은 부분들의 합으로 분해하는 것
 모든 값이 양수여야 하며(= 이미지, 텍스트 적합) 어떤성분이 얼마나 기여했는지 파악하는게 중요

 피자(완성품) = 도우 x 0.4 + 소스 0.3 + 치즈 x 0.2 + 토핑 0.1
 위와 같이 각 부분들의 중요도를 변경하며 모델을 완성하는 것
 MMF 가 하는 일
 완성된 피자 사진 1000장을 보고
 이 피자들은 공통적으로 도우 소스 치즈 토핑으로 이루어져 있구나 학습
 피자 1000장 = 각 피자의 재료 비율을 스캔   어떤패턴으로 피자가 만들어졌는지 확인
      X        =       W        *                 H
 피자1000장       각 피자의               도우 치즈 소스
                  재료 비율         토핑 패턴과 같은 공통 패턴확인


 사진 1000장에서 어떤 피자는 치즈만 가득 있고, 어떤 피자는 토핑만 있고 치즈 없으며
  어떤 피자는 소스가 안보이고 와 같은 패턴들을 분석하며 재료 비율 에 가중치를 설정
"""

# 보통 차원 축소는 시각화까지 해서 확인
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
# 위에서 작성한 1~5번 까지의 모델들
from sklearn.decomposition import PCA, KernelPCA, NMF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# as 는 import가 있어야지 쓸 수 있다. from 만 있어서는 사용할 수 없다.

# 모델을 들어가기 전에 공통적으로 설정해야하는 데이터 호출, 시각화 세팅 진행

# 시각화를 하기 위해 한글 폰트 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 준비 (iris 붓꽃 데이터 셋 사용)
X, y = load_iris(return_X_y=True)
# labels = load_iris.target_names error 발생
labels = load_iris().target_names  # load_iris() 붓꽃 데이터 가져오기는 ()가 뒤에 있어야한다.
print("labels : ", labels)  # labels :  ['setosa' 'versicolor' 'virginica']

# 데이터 전처리 작업
# 어떤 데이터와 어떤 모델을 사용하느냐에 따라 전처리 작업은 모두 다르다.
# 많은 모델과 많은 데이터를 만나며 사용방법을 익히는 것이 가장 중요
scalar = StandardScaler
X_scaled = scalar.fit_transform(X)

colors = ['red', 'green', 'blue']

fig, axes = plt.subplot(2, 3, figsize=(15, 10))
fig.suptitle('title', fontsize=16)
