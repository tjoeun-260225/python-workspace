import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path("weather-dataset/dataset")

'''
데이터셋에 존재하는 폴더이름과 날씨폴더목록의 폴더이름이 다르면
잘못된 데이터 훈련
반드시 폴더 명칭 순서도 동일하게 작성
날씨폴더목록 = [
    "shine", "rain", "cloudy", "snow", "fogsmog",
    "thunder", "rainbow", "sandstorm", "lightning", "tornado", "frost"
]'''
날씨폴더목록 = [
    "dew", "fogsmog", "frost", "glaze", "hail",
    "lightning", "rain", "rainbow", "rime", "sandstorm", "snow"
]
# =============================================
# 과제 1 : 각 폴더별 데이터 개수 확인 함수
# =============================================
def 각폴더별_데이터개수확인(경로, 폴더목록=날씨폴더목록):
    전체합계 = 0
    for 폴더 in 폴더목록:
        폴더경로 = 경로 / 폴더
        개수 = len(list(폴더경로.glob("*.jpg")))
        전체합계 += 개수
        print(f"{폴더} : {개수:,}장")
    print(f"전체 합계 : {전체합계:,}장")


# =============================================
# 과제 2 : 깨진 파일 제거 함수
# =============================================
def 깨진파일제거(경로, 폴더목록=날씨폴더목록):
    for 폴더 in 폴더목록:
        for 파일 in (경로 / 폴더).glob("*.jpg"):
            try:
                img = tf.io.read_file(str(파일))
                tf.image.decode_jpeg(img)
            except:
                print(f"깨진파일 삭제 : {파일}")
                os.remove(파일)


# =============================================
# 과제 3 : 데이터 불러오기 함수
# =============================================
def 데이터불러오기(경로, 이미지크기=(150, 150), 배치=32):
    """
    훈련데이터와 검증데이터를 불러오고 정규화까지 하는 함수
    경로     : 데이터 폴더 경로
    이미지크기: 이미지 resize 크기 (기본값 150x150)
    배치     : batch_size (기본값 32)
    """
    훈련 = image_dataset_from_directory(
        경로,
        image_size=이미지크기,
        batch_size=배치,
        validation_split=0.2,
        subset='training',
        seed=42
    )
    검증 = image_dataset_from_directory(
        경로,
        image_size=이미지크기,
        batch_size=배치,
        validation_split=0.2,
        subset='validation',
        seed=42
    )
    norm = Rescaling(1./255)
    훈련 = 훈련.map(lambda x, y: (norm(x), y)).prefetch(1)
    검증 = 검증.map(lambda x, y: (norm(x), y)).prefetch(1)

    return 훈련, 검증


# =============================================
# 과제 4 : 모델 만들기 함수
# =============================================
def 모델만들기(이미지크기=(150, 150)):
    """
    CNN 모델을 만들고 컴파일까지 하는 함수
    날씨 11가지 → 마지막 Dense(11), softmax 사용
    """
    모델 = Sequential([
        Input(shape=(이미지크기[0], 이미지크기[1], 3)),
        Conv2D(32,  (3, 3), activation='relu'),
        MaxPooling2D(),
        Conv2D(64,  (3, 3), activation='relu'),
        MaxPooling2D(),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(11,  activation='softmax'),   # 날씨 11가지
    ])
    모델.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',  # 3가지 이상 분류
        metrics=['accuracy']
    )
    return 모델


# =============================================
# 과제 5 : 모델 저장 함수
# =============================================
def 모델저장(모델, 폴더='models', 파일명='weather_model.keras'):
    os.makedirs(폴더, exist_ok=True)
    저장경로 = 폴더 + '/' + 파일명
    모델.save(저장경로)
    print(f"모델 저장 완료 → {저장경로}")
    if os.path.exists(저장경로):
        print("저장 성공")
    else:
        print("저장 실패")


# =============================================
# 함수 실행
# =============================================
각폴더별_데이터개수확인(데이터경로)
깨진파일제거(데이터경로)

훈련데이터, 검증데이터 = 데이터불러오기(데이터경로)
로봇뇌 = 모델만들기()
로봇뇌.fit(훈련데이터, epochs=10, validation_data=검증데이터)
모델저장(로봇뇌)