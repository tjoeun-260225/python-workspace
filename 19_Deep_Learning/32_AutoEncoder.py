import os

"""
AutoEncoder
- 입력을 압축(인코딩)했다가 다시 복원(디코딩)하는 신경망
입력 → [Encoder] → 잠재 벡터(z) → [Decoder] → 복원 출력
중간 병목을 통과하면서 데이터의 핵심 특징만 학습

사람으로 비유하면 :
책 한 권을 읽고 →  한 줄 요약 → 그 요약으로 다시 책 내용 설명
"""
import tensorflow as tf
# 아래 12 ~ 20 번까지 전부타 11번으로 사용할 수 있으나
# 가로로 코드가 길어지는 것을 싫어하는 개발자는 아래와 같이 from import 구문을 상세히 작성
from tensorflow import keras  # 만약 이걸 작성하지 않았다면 tf.keras 형태로 사용할 수 있다.
from tensorflow.keras.layers import Dense, Input
# 만약 이걸 작성하지 않았다면 tf.keras.layers.Dense
# 만약 이걸 작성하지 않았다면 tf.keras.layers.Input
# 매번 앞에다가 텐서플로우.케라스.레이어즈.에서 가져온 Input 기능이다 와 같이 표기
from tensorflow.keras.models import Model, Sequential
# 만약 이걸 작성하지 않았다면 tf.keras.models.Model
# 만약 이걸 작성하지 않았다면 tf.keras.Models.Sequential 와 같이 매번 표기
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# 1. 데이터 준비
# (훈련이미지, _), (테스트이미지, _) = tf.keras.datasets.mnist.load_data()
# from tensorflow.keras.datasets import  mnist 을 작성하면
# 아래와 같이 단축하여 원하는 코딩 구문을 표기할 수 있다
(훈련이미지, _), (테스트이미지, _) = mnist.load_data()
훈련이미지 = 훈련이미지.astype("float32") / 255.0
테스트이미지 = 테스트이미지.astype("float32") / 255.0
훈련이미지 = 훈련이미지.reshape(-1, 784)
테스트이미지 = 테스트이미지.reshape(-1, 784)

"""
왜 오토인코더를 배우는가

지금까지 배운 딥러닝 흐름(지도학습)
입력 → 로봇뇌 → 정답
정답이 항상 있는 상태로 숫자 맞추기, 긍정/부정, 꽃 분류 전부 정답 y가 존재함

오토인코더(비지도학습)
정답이 없을 경우 데이터 자체에서 스스로 특징을 찾아내 정답 생성
입력 → 로봇뇌 → 입력 복원

공장 불량품 탐지 모델
정상 부품 사진 10만장은 있는데
불량품 사진은 거의 없다.
정답 y를 만들 수가 없다..
나는 모델 못만드니 퇴사해야하나..? 이직해야하나..? 가아니라
오토인코더를 이용해서 정상만 학습 → 정상과 다른 것 탐지 하기 위하여 존재

병원 희귀병 탐지 모델
정상 MRI 넘쳐나는데
희귀병 MRI 는 몇 장 없다
마찬가지로 정답 y 만들기 불가
정상 MRI를 학습하여 정상 MRI 벗어나는 것을 이상한 것으로 탐지하는 모델을 만들 때 사용

              지도학습                       오토인코더
정답 y          있음                            없음
용도          분류,예측                특징추출, 이상탐지, 생성
데이터    정답 라벨링 필요               데이터만 있으면 된다.
현실       라벨링 비용 큼              데이터만 있으면 바로 가능
        선생님이 정답지 주고              정답지 없이 스스로
           채점하는 방식                     공부하는 방식
                                      정답에 있는 데이터 이외 모두 다르다.
                                      실무에서는 정답이 없는 데이터가 많다.
"""


# 2. 로봇뇌 만들기
로봇뇌 = Sequential([
    Input(shape=(784,)),
    # Dense 안에 8 16 32 128 256 512 와 같은 8자리 숫자를 사용할 의무는 없다.
    # 업계 관습 상 GPU 메모리 구조가 32 와 같은 8 표기법 구조에 최적화 되어 있어
    # 계산이 빠르기 때문에 사용  200, 100, 300 쓰고 싶은 숫자 작성해도 된다.
    Dense(256, activation='relu'),  # 인코더 : 압축
    # 중요한 데이터를 제외하고 억지로 256개에 784개 데이터를 구겨넣는다.
    # 정말 중요한 256개
    Dense(128, activation='relu'), # 정말 중요한 128개만 놔둔다.
    Dense(64, activation='relu'),  # 잠재벡터(병목) 최종적으로 중요한 64개 만 냅둔다.
    Dense(128, activation='relu'), # 디코더 : 복원 64개를 기준으로 128개로 늘렸을 때 제대로 늘리고 있는지 확인하는 신경망
    Dense(256, activation='relu'), # 디코더 : 복원 128개를 기준으로 256개로 늘렸을 때 제대로 늘리고 있는지 확인하는 신경망
    Dense(784, activation='sigmoid'),  # 출력 : 0~1 픽셀값 원상크기로 복원
])

# 3. 환경 세팅
로봇뇌.compile(optimizer='adam', loss='mse')
로봇뇌.summary()

# 4. 학습하기
로봇뇌.fit(
    훈련이미지, 훈련이미지,  # 입력 = 정답 자기 자신을 복원하면서 정답만 학습
    epochs=20,               # 전체 데이터를 20번 반복 학습
    batch_size=256,          # 한 번에 256장씩 묶어서 학습
    validation_split=0.1,    # 훈련데이터 10%는 검증용으로 빼둠
                            # sklearn = 머신러닝이 아니기 때문에
                            # train_test_split(test_size=0.8) 을 사용하지 않은 것일 뿐!
                            # 텐서플로우 = 딥러닝에서 사이킷런 = 머신러닝에서 사용한
                            # 데이터 분리 작업 기능을 해도 되지만 보통은
                            # 딥러닝  에서는   딥러닝 회사 분류 기능을 사용하려 하고,
                            # 머신러닝에서는 머신러닝 회사 분류 기능을 사용해주려 한다.
    verbose=1               # 학습 진행상황 출력 0=안보임 1=모두보임 2=프로그래스바만 안보임
)

# 5. 모델 저장하기


# AI 의 경우 1~5번 사이 순서가 매우 중요

# 6. 시각화
복원이미지 = 로봇뇌.predict(테스트이미지[:10])
# 만들어진 뇌를 테스트이미지 10장으로 잘 만들어졌는지 확인

# 테스트 결과를 시각화하여 개발자가 눈으로 직접 확인하는 과정
그림, 축 = plt.subplots(2, 10, figsize=(15, 3))
for i in range(10):
    축[0, i].imshow(테스트이미지[i].reshape(28, 28), cmap='gray')
    축[1, i].imshow(복원이미지[i].reshape(28, 28), cmap='gray')
    for j in range(2):
        축[j, i].axis("off")
축[0, 0].set_ylabel("원본")
축[1, 0].set_ylabel("복원")

plt.tight_layout()
plt.show()
