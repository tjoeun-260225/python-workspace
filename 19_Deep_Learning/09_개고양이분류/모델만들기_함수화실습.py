import os
import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

데이터경로 = pathlib.Path(r"PetImages")

def 깨진파일제거(경로, 폴더목록=["Cat", "Dog"]):
    for 폴더 in 폴더목록:
        for 파일 in (경로 / 폴더).glob("*.jpg"):
            try:
                img = tf.io.read_file(str(파일))
                tf.image.decode_jpeg(img)
            except:
                print(f"깨진파일 삭제 : {파일}")
                os.remove(파일)

def 데이터불러오기(경로, 이미지크기=(64, 64), 배치=32):
    """
    훈련데이터와 검증데이터를 불러오고 정규화까지 하는 함수
    경로     : 데이터 폴더 경로
    이미지크기: 이미지 resize 크기 (기본값 64x64)
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
def 모델만들기(이미지크기=(64, 64)):
    """
    CNN 모델을 만들고 컴파일까지 하는 함수
    이미지크기: Input shape 에 사용 (기본값 64x64)
    """
    모델 = Sequential([
        # 이미지크기=(64, 64) 에서 맨 앞 64를 가져올 때는  이미지크기[0] 와 같이 작성
        # 이미지크기=(64, 64) 에서 맨 뒤 64를 가져올 때는  이미지크기[1] 와 같이 작성
        Input(shape=(이미지크기[0],  이미지크기[1], 3)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid'),
    ])
    모델.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return 모델


def 모델저장(모델, 폴더='models', 파일명='dog_cat_model.keras'):
    """
    모델을 저장하고 결과를 출력하는 함수
    모델  : 저장할 모델
    폴더  : 저장할 폴더명 (기본값 models)
    파일명: 저장할 파일명 (기본값 dog_cat_model.keras)
    """
    os.makedirs(폴더, exist_ok=True)

    # 힌트: 폴더 + '/' + 파일명
    저장경로 = 폴더 + '/' + 파일명

    모델.save(저장경로)
    print(f"모델 저장 완료! → {저장경로}")

    if os.path.exists(저장경로):
        print("저장 성공!")
    else:
        print("저장 실패!")

# =============================================
# 함수 실행 (여기는 수정하지 않아도 됩니다)
# =============================================
# 전처리 def 호출
깨진파일제거(데이터경로)

# 전처리된 데이터 사용
훈련데이터, 검증확인데이터 = 데이터불러오기(데이터경로)

# 뇌 만들기 def 호출
로봇뇌 = 모델만들기()

로봇뇌.fit(훈련데이터, epochs=5, validation_data=검증확인데이터)

# 모델저장 def 호출 사용
모델저장(로봇뇌)