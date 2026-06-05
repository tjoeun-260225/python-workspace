import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path("weather")

날씨폴더목록 = [
    "dew", "fogsmog", "frost", "glaze", "hail",
    "lightning", "rain", "rainbow", "rime", "sandstorm", "snow"
]

for 폴더 in 날씨폴더목록:
    for 파일 in (데이터경로 / 폴더).glob("*.jpg"):
        try:
            img = tf.io.read_file(str(파일))
            tf.image.decode_jpeg(img)
        except:
            os.remove(파일)

# ↓↓↓ 여기 숫자들을 바꿔가며 실습 ↓↓↓
EPOCHS     = 10   # 기본값 10  → 20 으로 늘려보기
BATCH_SIZE = 32   # 기본값 32  → 16, 64 로 바꿔보기
DENSE_수   = 128   # 기본값 128 → 256 으로 늘려보기
CONV_필터  = 32   # 기본값 32  → 64 로 늘려보기

모델이름 = f"models/weather_ep{EPOCHS}_batch{BATCH_SIZE}_dense{DENSE_수}.keras"
print(f"저장될 모델 이름: {모델이름}")

훈련데이터 = image_dataset_from_directory(
    데이터경로, image_size=(150, 150),
    batch_size=BATCH_SIZE,
    validation_split=0.2, subset='training', seed=42
)
검증데이터 = image_dataset_from_directory(
    데이터경로, image_size=(150, 150),
    batch_size=BATCH_SIZE,
    validation_split=0.2, subset='validation', seed=42
)

norm = Rescaling(1./255)
훈련데이터 = 훈련데이터.map(lambda x, y: (norm(x), y)).prefetch(1)
검증데이터 = 검증데이터.map(lambda x, y: (norm(x), y)).prefetch(1)

로봇뇌 = Sequential([
    Input(shape=(150, 150, 3)),
    Conv2D(CONV_필터, (3, 3), activation='relu'),
    MaxPooling2D(),
    Conv2D(CONV_필터, (3, 3), activation='relu'),
    MaxPooling2D(),
    Conv2D(CONV_필터, (3, 3), activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(DENSE_수, activation='relu'),
    Dense(11, activation='softmax'),
])

로봇뇌.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
로봇뇌.fit(훈련데이터, epochs=EPOCHS, validation_data=검증데이터)

os.makedirs('models', exist_ok=True)
로봇뇌.save(모델이름)
print(f"저장 완료 → {모델이름}")