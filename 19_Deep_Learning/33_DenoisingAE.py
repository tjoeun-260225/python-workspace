import os

"""
기본 AE와 딱 한가지 다르다.
입력에 노이즈를 섞어서 넣고, 정답은 깨끗한 원본으로 학습시켜서
흐릿하게 보이는 말이나 이미지를 맥락을 추론해서 이해하는 것과 같음

노이즈 입력 → 인코더 → Z → 디코더 → 깨끗한 복원
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt

# 1. 데이터 준비
(훈련이미지, _), (테스트이미지, _) = mnist.load_data()

# 2. 데이터 전처리
훈련이미지 = 훈련이미지.astype("float32") / 255.0
테스트이미지 = 테스트이미지.astype("float32") / 255.0
훈련이미지 = 훈련이미지.reshape(-1, 784)
테스트이미지 = 테스트이미지.reshape(-1, 784)


# 3. 노이즈 추가
def 노이즈추가(데이터, 노이즈강도=0.3):
    return np.clip(데이터 + 노이즈강도 * np.random.randn(*데이터.shape),
                   0.0,
                   1.0
                   )


훈련노이즈 = 노이즈추가(훈련이미지)
테스트노이즈 = 노이즈추가(테스트이미지)

# 4. 로봇뇌 만들기
로봇뇌 = Sequential([
    Input(shape=(784,)),
    Dense(256, activation="relu"),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(128, activation="relu"),
    Dense(256, activation="relu"),
    Dense(784, activation="sigmoid"),
])

# 5. 환경 세팅
로봇뇌.compile(optimizer='adam', loss='mse')
로봇뇌.summary()

# 6. 학습하기
로봇뇌.fit(
    훈련노이즈, 훈련이미지,  # 노이즈입력 → 깨끗한 정답이 나오는지 확인
    epochs=20,
    batch_size=256,
    validation_split=0.1,
    verbose=1
)

# 테스트 결과를 시각화하여 개발자가 눈으로 직접 확인하는 과정
복원이미지 = 로봇뇌.predict(테스트노이즈[:10])
그림, 축 = plt.subplots(3, 10, figsize=(15, 4))
for i in range(10):
    축[0, i].imshow(테스트이미지[i].reshape(28, 28), cmap='gray')
    축[1, i].imshow(테스트노이즈[i].reshape(28, 28), cmap='gray')
    축[1, i].imshow(복원이미지[i].reshape(28, 28), cmap='gray')
    for j in range(3):
        축[j, i].axis("off")
축[0, 0].set_ylabel("원본")
축[1, 0].set_ylabel("노이즈")
축[2, 0].set_ylabel("복원")

plt.suptitle("Denoising AE : 원본 / 노이즈 / 복원", fontsize=20)
plt.tight_layout()
plt.show()
