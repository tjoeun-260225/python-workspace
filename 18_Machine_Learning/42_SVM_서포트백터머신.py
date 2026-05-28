"""
SVM
- 데이터를 가장 잘 나누는 선(경계)를 찾는 알고리즘
- 마진(Margin)       : 경계선에서 각 클래스의 가장 가까운 점의 거리 X 2
- 커널 트릭(kernel) : 데이터를 고차원으로 올리는 계산을 내부적으로 처리
     gamma = 각 데이터 포인트의 영향 범위
     gamma 작다 영향 범위 넓고 부드러운 경계
     gamma 크다 영향 범위 좁고 과적합 위험(과적합 = 과하게 배운것만 잘맞춘다 새로운것 응용 x)

     데이터를 학습할 때 데이터가 너무 엉망으로 섞여 있어 선을 어떻게 나누어야 할지 모델 감을잡지 못할 때
     각 데이터에 라벨=키 라는 새로운 정보로 표기
     😺 🐶 😺 🐶 😺 🐶 😺 🐶
     🐶 😺 🐶 😺 🐶 😺 🐶 😺
     섞여있을 때
     🐶 = 강아지 or 0
     😺 = 고양이 or 1
     처럼 표기를 해놓는다.
     0 과 1을 기준으로 분리 가능하게 만드는 것 = 커널 트릭

     rbf = 새로운 축 추가하는 계산을 자동으로 해주는 수학 수식이 들어있다.
     직접 하나하나 라벨처리하고 분리하면 계산이 엄청 오래 걸리는데
     rbf 수학공식을 추가해서 빠르게 처리할 수 있도록 계산을 넣어놓은 기능
     kernel='rbf'



- 종류
  SVC(Support Vector Classifier) = 분류 문제 예) 스팸/정상, 개/고양이
  SVR(Support Vector Regressor)  = 회귀 문제 예) 집값 예측, 온도 예측

- SVM 스케일링 필수
   스케일링 : 숫자 데이터 범위를 스케일링이 확인해서 0~1 사이의 범위로 나열
- 1960년대 아이디어를 내기시작 → 1990년대 완성
  1990년 당시 상황
    딥   러   닝 ? → 컴퓨터 사양이 좋지 않아 학습하는데 느려서 못씀
    신   경   망 ? → 학습이 잘 안됨, 불안정
    랜덤포레스트 ? → 아직 없었던 시절
    ----------------------------------------
    SVM 이 잘 되었던 이유
    - 데이터가 적어도 잘 작동함
    - 수학적을 왜 이 답이 맞는지 증명가능
    - 손글씨 인식, 얼굴 인식에서 당시 최고 성능
    → 2012년 컴퓨터 성능이 좋아지면서 딥러닝 재등장 이미지/음성은 딥러닝이 압도
      현  재 엑셀같은 표 데이터에서는 적은 데이터로도 잘 작동하여 사용하기도 한다.
"""
from sklearn.metrics import mean_squared_error
# 데이터가 있는데 데이터 컬럼마다 숫자가 천차만별
# 나이컬럼 연봉컬럼 자녀수컬럼 부서인원컬럼
# 0~100     천~억    0~10        0~100 ..
# 스케일링을 사용해서 각각 컬럼을 -3~3 0~1 와 같이 알아서 스케일링으로
# 범위를 비슷하게 만들어서 계산 처리를 할 수 있게 세팅해주는 것이
# 스 케 일 링!
from sklearn.svm import SVC, SVR  # Support Vector Classifier
from sklearn.datasets import load_iris, make_classification, make_circles, make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# make_classification = 가짜 데이터를 만들어서 임의적으로 무언가 확인할 때 사용
# 현재 데이터는 중요하지 않고 딱히 생각나는 데이터는 없지만
# 모델 코딩하는 과정이나 특정 기능이 궁금할 때 사용
# make_classification = 더미데이터

# make_circles       = 가짜 데이터를 만들어서 임의적으로 무언가 확인할 때 사용
#                      직선으로 못 나누는 가짜 데이터들 모임
def 마진확인방법():
    X, y = make_classification(
        n_samples=100,  # 데이터 샘플 개수
        n_features=2,  # 데이터 컬럼 개수
        n_redundant=0,  # 데이터 컬럼 개수 중에서 중복 컬럼 개수
        # 예를 들어 이름나이 컬럼이 있는 데 1을 쓰면
        # 이름 나이 이름_복제본과 같이 중복된 컬럼이 존재한다
        # 개수는 상관 없으나 n_features 컬럼두개밖에 없다 했는데 복제가 3개 있을 수는 없다
        # n_features = 5 n_redundant=4 이런식으로는 가능
        # n_features = 5 n_redundant=6 이런식으로는 불가능
        # n_features 보다 n_redundant 더 많을 수는 없다.
        random_state=42  # 랜덤 시드 고정
    )
    # C 파라미터 = 마진관련
    # C 작을수록   마진 넓게  일   반  화↑ 오분류 허용
    # C 높을수록   마진 좁게  훈련 정확도↑ 과적합 위험
    model_wide = SVC(C=0.1, kernel='linear')
    model_tight = SVC(C=100, kernel='linear')
    model_wide.fit(X, y)
    model_tight.fit(X, y)
    print(f"넓은 마진 서포트 벡터 수 : ", len(model_wide.support_vectors_))  # 30
    print(f"좁은 마진 서포트 벡터 수 : ", len(model_tight.support_vectors_))  # 5


def 커널종류확인():
    # noise=0.1 데이터를 얼마나 뒤죽박죽으로 만들 것인가
    # noise=  0 → 완벽한 원형 / 현실에는 없다.
    # noise=0.1 → 살짝 흔들림 적당하다
    # noise=0.5 → 너무 흔들려서 구분 불가 추천하지 않는 숫자
    # make_classification = 흔들이유가 없는 정제된 랜덤 데이터이기 때문에
    # noise 속성 자체가 없다.
    # 하나하나 속성이 궁금하다면.. dir(도구기능) 으로 확인할 것
    X, y = make_circles(n_samples=200, noise=0.1, random_state=42)

    # 커널 종류
    kernels = {
        '리니어': SVC(kernel='linear'),  # 직선 경계 (선형형태로 분리 가능할 때)
        '알비에프': SVC(kernel='rbf'),  # 방사형 기저 함수 - 원형/복잡한 경계에서 사용
        # 가장 많이 사용됨 경계를 기준으로 사방으로 퍼지는 원형
        '폴리': SVC(kernel='poly', degree=3),  # 다항식 경계 s자 곡선이나 여러 선으로 나눔
        '시그모이드': SVC(kernel='sigmoid')  # 신경망과 비슷    딥러닝에서 보이는 형태
        # s자 곡선으로 0~1 로 데이터 눌러버림 SVM 에서는 잘 안씀
    }

    # for 문을 이용해서 하나씩 정확도 확인
    for 모델이름, 모델 in kernels.items():  # items() '키이름': 데이터 형태로 가져와 각 변수에 대입
        모델.fit(X, y)
        print(f"{모델이름} 정확도 : {모델.score(X, y):.3f}")
    """
    리니어 정확도 : 0.510
    알비에프 정확도 : 0.830
    폴리 정확도 : 0.565
    시그모이드 정확도 : 0.510
    """


def 감마종류확인():
    X, y = make_circles(n_samples=200, noise=0.1, random_state=42)

    # gamma = 각 데이터 포인트가 주변에 얼마나 영향을 미치는가
    # gamma = 각 데이터 포인트가  "나 여기있어!!!" 를 얼마나 멀리 외치는가

    # 😺 고양이 데이터가 하나 가 들어왔다!!!!
    # gamma 작다 → 영향 범위 넓다 → 경계가 부드럽다 → 일반화 ↑
    # gamma 작다 → 😺 고양이의 고양이 뿐만 아니라 다른 강아지, 토끼, 돼지 에서도 확인
    #                  경계범위를 넓게 설정해서 맞춤   새로운 데이터 실수할 수 있다.
    # gamma 크다 → 영향 범위 좁다 → 경계가 복잡하다 → 과적합 위험
    # gamma 크다 → 😺 고양이의 경계 범위를 좁게 설정해서 맞춤 학습한 데이터는 잘 찾는다.

    gammas = {
        '매우작음': SVC(kernel='rbf', gamma=0.001),  # 아주 넓게 파문 퍼짐
        '작음': SVC(kernel='rbf', gamma=0.1),  # 파문 넓게 퍼짐
        '보통': SVC(kernel='rbf', gamma=1),  # 적당
        '큼': SVC(kernel='rbf', gamma=10),  # 바로 사라짐
        '매우큼': SVC(kernel='rbf', gamma=100),  # 관련된 딱 그 데이터경계만 봄 과적합
        '스케일': SVC(kernel='rbf', gamma='scale'),  # 요즘 기본값, 권장, 적당한 값 자동 계산해줌
        '오토': SVC(kernel='rbf', gamma='auto'),  # 옛날 기본값 scale과 비슷하지만 계산방식이 내부에서 살짝 다름
        # 보통 스케일로 많이 사용
    }

    for 모델이름, 모델 in gammas.items():
        모델.fit(X, y)
        print(f"{모델이름} (gamma) 정확도 : {모델.score(X, y):.3f}")
        """
        매우작음 (gamma) 정확도 : 0.520
        작음     (gamma) 정확도 : 0.795
        보통     (gamma) 정확도 : 0.815
        큼       (gamma) 정확도 : 0.850
        매우큼   (gamma) 정확도 : 0.930
        스케일   (gamma) 정확도 : 0.830
        오토     (gamma) 정확도 : 0.815
        정확도 1.00 이 나오면 좋은게 아니라.. 잘못됨 의심해야한다..
        """


def 회귀_SVR():
    X, y = make_regression(n_samples=200,
                           n_features=1,
                           noise=20,
                           random_state=42
                           )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    scaler_X = StandardScaler()
    scaler_y = StandardScaler()
    X_train_s = scaler_X.fit_transform(X_train)
    X_test_s = scaler_X.transform(X_test)
    y_train_s = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
    # epsilon = 이 범위 안에 있는 모든 오차는 무시하겠다.
    svr = SVR(kernel='rbf', C=1.0, epsilon=0.1)
    svr.fit(X_train_s, y_train_s)
    pred_s = svr.predict(X_test_s)
    pred = scaler_y.inverse_transform(pred_s.reshape(-1, 1)).ravel()
    print(f"SVR MSE :{mean_squared_error(y_test, pred)}")
    print(f"SVR 예측값(5개) : {pred[:5].round(1)}")

# 감마종류확인()
# 커널종류확인()
# 마진확인방법()
