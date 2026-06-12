import matplotlib.pyplot as plt
import numpy as np
from preprocessing import 이미지크기
from autoencoder import 모델만들기,메인
이미지크기_값 = 이미지크기
입력크기 = 이미지크기 * 이미지크기 * 3
def 노이즈추가(데이터, 노이즈강도=0.2):
    return np.clip(
        데이터 + 노이즈강도 * np.random.randn(*데이터.shape),
        0.0 ,
        1.0
    )
로봇뇌,훈련,테스트 = 메인()
훈련노이즈 = 노이즈추가(훈련)
테스트노이즈 = 노이즈추가(테스트)

노이즈제거뇌 = 모델만들기()


노이즈제거뇌.fit(
    훈련노이즈,
    훈련,
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

복원이미지 = 노이즈제거뇌.predict(테스트노이즈[:5])

그림, 축 = plt.subplots(3, 5, figsize=(15, 9))
for i in range(5):
    축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
    축[1, i].imshow(테스트노이즈[i].reshape(이미지크기, 이미지크기, 3))
    축[2, i].imshow(복원이미지[i].reshape(이미지크기, 이미지크기, 3))
    for j in range(3):
        축[j, i].axis("off")
for j, 이름 in enumerate(["원본", "노이즈", "복원"]):
    축[j, 0].set_ylabel(이름)
plt.suptitle("토끼 노이즈 제거 결과")
plt.tight_layout()
plt.show()