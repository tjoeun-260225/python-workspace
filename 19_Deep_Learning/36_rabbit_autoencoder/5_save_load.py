import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from preprocessing import 이미지크기, 데이터준비
from denoising import 메인
로봇뇌, 노이즈제거뇌, 훈련, 테스트 = 메인()
로봇뇌.save("autoencoder.keras")
노이즈제거뇌.save("denoising_autoencoder.keras")
print("모델 저장 완료")

불러온_모델       = load_model("autoencoder.keras")   # (22) "autoencoder.keras"
불러온_노이즈모델 = load_model("denoising_autoencoder.keras")   # (23) "denoising_autoencoder.keras"

print("모델 불러오기 완료")
불러온_모델.summary()


# ── 불러온 모델로 예측 ─────────────────────────────────────
복원이미지_저장모델 = 불러온_모델.predict(테스트[:5])

그림, 축 = plt.subplots(2, 5, figsize=(15, 6))
for i in range(5):
    축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
    축[1, i].imshow(복원이미지_저장모델[i].reshape(이미지크기, 이미지크기, 3))
    for j in range(2):
        축[j, i].axis("off")
축[0, 0].set_ylabel("원본")
축[1, 0].set_ylabel("복원 (저장된 모델)")
plt.suptitle("저장된 모델로 복원한 결과")
plt.tight_layout()
plt.show()