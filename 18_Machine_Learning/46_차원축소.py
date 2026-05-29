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
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# 위에서 작성한 1~5번 까지의 모델들
from sklearn.decomposition import PCA, KernelPCA, NMF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.manifold import LocallyLinearEmbedding as LLE

# as 는 import가 있어야지 쓸 수 있다. from 만 있어서는 사용할 수 없다.

# 모델을 들어가기 전에 공통적으로 설정해야하는 데이터 호출, 시각화 세팅 진행

# 시각화를 하기 위해 한글 폰트 깨짐 방지
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 준비 (iris 붓꽃 데이터 셋 사용)
X, y = load_iris(return_X_y=True)  # X = 붓꽃데이터 , y = 붓꽃데이터 정답
print("행렬 확인 : ", X.shape)  # 행렬 확인 :  (150, 4)
print("헤드 확인 : ", X[:5])  # 0~ 4 앞 5개의 행 출력

# df = pd.DataFrame(X, columns=iris.feature_names) 와 같이 변환해서 사용
# print("헤드 확인 : ", df.head()) # head()는 csv 파일에서 사용

# labels = load_iris.target_names error 발생 # load_iris() 붓꽃 데이터 가져오기는 ()가 뒤에 있어야한다
labels = load_iris().target_names  # labels :  ['setosa' 'versicolor' 'virginica']
# print("labels : ", labels)

# 데이터 전처리 작업
# 어떤 데이터와 어떤 모델을 사용하느냐에 따라 전처리 작업은 모두 다르다.
# 많은 모델과 많은 데이터를 만나며 사용방법을 익히는 것이 가장 중요
scalar = StandardScaler()  # 스케일러라는 공간에 정규화 도구 를 추가
X_scaled = scalar.fit_transform(X)  # 스케일러 안에 존재하는 정규화 도구를 이용해서
# fit(평균/표준편차 계산) +transform(실제 변환작업)처리

colors = ['red', 'green', 'blue']  # 꽃 3종류가 어떻게 분포되어 있는지 색상으로 비교하기 위해 설정

# 아래 2행 3열은 필수가 아니나.. 다른 모델들은 어떻게 표현하는지 확인하기 위해 세팅
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # 총 2행 3열로 6칸 그래프 틀 생성
fig.suptitle('차원축소 기법 비교', fontsize=16)

# 붓꽃은 꽃받침 길이 / 꽃받침 너비 / 꽃잎 길이 / 꽃잎 너비
# 총 4개의 컬럼으로 되어있다. = 4차원
# 컬럼이 100개라면? 100차원

# =====================================================
# 1. PCA(주성분 분석)
# =====================================================
# - 데이터 분산이 최대가 되는 방향으로 축을 찾아서 투영
# - 선형 변환만 가능, 속도 빠름
# - 반드시 StandardScaler 정규화 후 사용
# - 붓꽃 데이터 뿐만 아니라 숫자로 되어있는 컬럼이 많은 데이터는
#   대부분 숫자들이 중구난방이기 때문에 (예: 나이 / 키 / 연봉  숫자대가 중구난방)
#   공통된 범위를 제공하여 모델 학습
# =====================================================
print("\n" + "=" * 50)
print("1. PCA")
print("=" * 50)

# 붓꽃은 꽃받침 길이 / 꽃받침 너비 / 꽃잎 길이 / 꽃잎 너비
# 여기서 2차원으로 줄일 때 기준은? 길이나 너비 꽃받침 꽃잎 중 2가지는  버려진 것
# 살아남은 2가지의 기준과 버려진 2가지의 기준
# PCA 모델 자체에서 학습을 할 때 중요한 컬럼 순서대로 줄을 세운 뒤, 내가 필요한 개수만큼
# 앞에서부터 자르는 것
# 데이터 평균을 낸 후 , 모델 학습할 때 필요한 정도를 테스트하며 모델 완성
# 1번 사진 꽃받침 길이 꽃받침 너비를 너무 중요하게 생각해서 냅두고 모델 정답 → 틀림
# 2번 사진 꽃받침 너비 꽃받침 너비를 너무 중요하게 생각해서 냅두고 모델 정답 → 틀림
# 3번 사진 꽃받침 길이   꽃잎 길이를 너무 중요하게 생각해서 냅두고 모델 정답 → 정답
#            꽃잎 길이가 중요하거나 꽃받침 길이가 중요할 수 있겠다 우선순위 올라감
# 이런식으로 우선순위를 배치

pca = PCA(n_components=2)  # 4차원을 2차원으로 축소
X_pca = pca.fit_transform(X_scaled)  # 4차원 데이터를 2차원으로 변환

print(f"원본      차원 : {X_scaled.shape}")  # 원본      차원 : (150, 4)
print(f"축소  후  차원 : {X_pca.shape}")  # 축소  후  차원 : (150, 2)
print(f"분산 설명 비율 : {pca.explained_variance_ratio_}")  # 분산 설명 비율 : [0.72962445 0.22850762]
# 각 주성분이 말하는 분산 비율
print(f"총   설명 분산 : {sum(pca.explained_variance_ratio_):.4f}")  # 총   설명 분산 : 0.9581
# 합계가 높을수록 정보 손실 적다.

ax = axes[0, 0]  # 위에서 작업한 것을 6칸 중에서 맨 첫번째 칸에 배치하겠다.
for i, (label, color) in enumerate(zip(labels, colors)):
    mask = y == i  # 해당 클래스만 True
    ax.scatter(X_pca[mask, 0], X_pca[mask, 1], c=color, label=label, alpha=0.7)

ax.set_title("PCA")
ax.set_xlabel('주성분1 (PC1)')
ax.set_ylabel('주성분2 (PC2)')
ax.legend()

# plt.tight_layout()
# plt.show()


# =====================================================
# 2. 커널 PCA(Kernel PCA)
# =====================================================
# - PCA를 비선형으로 확장
# - 커널 함수로 고차원 공간에서 PCA 수행
# - 커널 종류 : rbf, ploy, sigmoid, consine
# =====================================================
print("\n" + "=" * 50)
print("2. Kernel PCA")
print("=" * 50)
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.1)
X_kpca = kpca.fit_transform(X_scaled)
print(f"원본      차원 : {X_scaled.shape}")
print(f"축소  후  차원 : {X_kpca.shape}")
print(f"사용 커널 : rbf (가우시안)")

ax = axes[0, 1]  # PCA 옆에 배치
for i, (label, color) in enumerate(zip(labels, colors)):
    mask = y == i
    ax.scatter(X_kpca[mask, 0], X_kpca[mask, 1], c=color, label=label, alpha=0.7)
ax.set_title("Kernel PCA (RBF)")
ax.set_xlabel('컴포넌트 1')
ax.set_ylabel('컴포넌트 2')
ax.legend()

# =====================================================
# 3. LDA(선형 판별 분석)
# =====================================================
# - PCA : 데이터 퍼짐(분산)을 최대화 -> 클래스 무시
# - LDA : 클래스 간의 거리를 최대화  -> 클래스 정보(y) 사용
# - 지도학습 방식(레이블 y 필요)
# - 최대 축소 차원 수 = 클래스 수 -1 (3클래스면 최대 2차원)
# =====================================================
print("\n" + "=" * 50)
print("3. LDA(선형 판별 분석)")
print("=" * 50)
lda = LDA(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)  # 반드시 정답 데이터 도 작업해야한다.

print(f"원본      차원 : {X_scaled.shape}")
print(f"축소  후  차원 : {X_lda.shape}")
print(f"판별 설명 비율 : {lda.explained_variance_ratio_}")

ax = axes[0, 2]
for i, (label, color) in enumerate(zip(labels, colors)):
    mask = y == i
    ax.scatter(X_lda[mask, 0], X_lda[mask, 1], c=color, label=label, alpha=0.7)
ax.set_title("LDA (선형 판별 분석)")
ax.set_xlabel('판별 축 1(LD1)')
ax.set_ylabel('판별 축 2(LD2)')
ax.legend()

# =====================================================
# 4. LLE(지역 선형 임베딩)
# =====================================================
# - 각 점을 주변 이웃들의 선형 조합으로 표현
# - 비선형 매니폴드(구부러진 공간) 구조를 보존
# - PCA : 전체를 한 번에 납작하게 누름( 전체기준 )
# - LLE : 주변 이웃 관계를 유지하며 조심조심 펼침 (동네기준부터)
# - n_neighbors : 이웃 수(너무 작으면 노이즈, 너무 크면 구조 왜곡)
# =====================================================
print("\n" + "=" * 50)
print("4. LLE(지역 선형 임베딩)")
print("=" * 50)
lle = LLE(n_components=2, n_neighbors=10)
X_lle = lle.fit_transform(X_scaled)  # 반드시 정답 데이터 도 작업해야한다.

print(f"원본      차원 : {X_scaled.shape}")
print(f"축소  후  차원 : {X_lle.shape}")
print(f"재구성  오류도 : {lle.reconstruction_error_:.6f}")
# 재구성 오류도 3d 지구본을 2d 지구본으로 얼마나 완벽하게 만들었는지
# 재구성 오류도가 낮을 수록 원본 구조 잘 보존
ax = axes[1, 0]
for i, (label, color) in enumerate(zip(labels, colors)):
    mask = y == i
    ax.scatter(X_lle[mask, 0], X_lle[mask, 1], c=color, label=label, alpha=0.7)
ax.set_title("LLE (지역 선형 임베딩)")
ax.set_xlabel('성분 1')
ax.set_ylabel('성분 2')
ax.legend()

# =====================================================
# 5. NMF(비음수 행렬 분해)
# =====================================================
# - 데이터를 W(비율 ) x H(패턴) 두 행렬의 곱으로 분해
# - 피자 = 도우 x 0.4 + 소스 x 0.3 + 치즈 x 0.2 + 토핑 x 0.1
# - 모든 값이 0 이상이어야 함 → MinMaxScalr 사용 (0~1 사이로 변환 음수 없음)
#                               StandardScaler 음수가 발생하므로 사용 불가
# - 이미지, 텍스트 데이터 적합
# =====================================================
print("\n" + "=" * 50)
print("5. NMF(비음수 행렬 분해)")
print("=" * 50)
# 음수가 불가하여 StandardScaler 사용할 수 없다.
# 0과 1 사이만 존재하는 MinMaxScaler 사용
X_positive = MinMaxScaler().fit_transform(X)

nmf = NMF(n_components=2, random_state=42, max_iter=500)
X_nmf = nmf.fit_transform(X_positive)
print(f"원본      차원 : {X_positive.shape}")
print(f"축소  후  차원 : {X_nmf.shape}")
print(f"재구성  오류도 : {nmf.reconstruction_err_:.6f}") # 낮을 수록 원본 잘 보존
ax = axes[1, 1]
for i, (label, color) in enumerate(zip(labels, colors)):
    mask = y == i
    ax.scatter(X_nmf[mask, 0], X_nmf[mask, 1], c=color, label=label, alpha=0.7)
ax.set_title("NMF (비음수 행렬 분해)")
ax.set_xlabel('성분 1')
ax.set_ylabel('성분 2')
ax.legend()

plt.tight_layout()
plt.show()
'''
데이터에 따른 1~5 시각화 모델 사용 예

이미지 / 텍스트(음수가 없는 글자나 숫자) = 5. NMF
                                                뉴스 기사 단어 빈도 / 얼굴 사진 픽셀
y 라벨 있음( 분류 문제 )                 = 3. LDA
                                                 y라벨 있음
일반 숫자 데이터
           선형으로 분리된다.            = 1. PCA
                                                 고객 구매 내역(나이/연봉/구매금액...)
           원형/나선형 꼬임              = 2. 커널PCA (= PCA 결과 별로일 때 사실 많이 사용)
                                                 동심원/나선형 데이터
           구부러진 3D구조               = 4. LLE
                                                 3D 데이터

'''






