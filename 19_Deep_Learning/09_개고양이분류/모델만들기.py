import os

import tensorflow as tf
import pathlib
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

# 데이터를 실제로 가져올 경로 선택
# r = 파이썬에서 주석에라도 \ 을 잘못 작성하면 에러 발생
# 모든 언어에서 \ 는 특수문자 시작 신호
# \n = 줄바꿈 \t = 탭 과 같은 경로이고 윈도우 경로는 대부분 \로 되어 있다.
# C: \ 바탕화면 바탕화면 폴더를 가고 싶은데 특수문자로 인식해서
# 주석이더라도 에러 발생
# r 코딩할 때 사용하는 특수문자가 아니라 경로 이다. 표기법을 함께 사용
데이터경로 = pathlib.Path(r"PetImages")

"""
line 59, in quick_execute
    except TypeError as e:
    ...<5 lines>...
      raise e
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node decode_image/DecodeImage defined at (most recent call last):
<stack traces unavailable>
Input is empty.
	 [[{{node decode_image/DecodeImage}}]]
	 [[IteratorGetNext]] [Op:__inference_multi_step_on_iterator_1820]
수집된 데이터 =  파일이나 동영상 글자가 깨져서 사용하지 못할 때 발생하는 에러

훈련데이터와 테스트(검증 데이터)로 분류하기 전에 깨진 데이터는 미리 제거
"""
# 깨진 데이터 전처리
def 깨진파일제거(경로, 폴더목록=["Cat","Dog"]) :
    """
    깨진 이미지 파일을 찾아서 삭제하는 함수
    :param 경로:     데이터가 있는 폴더 경로
    :param 폴더목록: 확인할 폴더 이름 리스트(기본값 Cat, Dog)
                     폴더 이름을 교체하고 싶다면, 함수를 호출할 때 교체하면 자동으로
                     폴더이름에 교체된 폴더들의 명칭 삽입
    """
    """
    데이터를 훈련하기 전에 데이터에 이상이 없는지 확인하고 이상있는 데이터 대체하거나 제거
                 분류하고 자 하는 폴더 이름 모두 작성
        하나씩 순차적으로 폴더라는 변수 공간에 넣어준 후 사용
    for 폴더 in ["Cat", "Dog"]:
                        PetImages/Cat = 각 폴더 안에 있는 .jpg 파일을 전부 하나씩 꺼냄
                                .glob = 패턴으로 특정 파일 찾기
                                *.jpg = 확장자가 jpg 인 전부
        for 파일 in (데이터경로 / 폴더).glob("*.jpg"):
            try:
                img = tf.io.read_file(str(파일))  특정 파일이름을 문자열처리해서 파일 읽기 시도
                tf.image.decode_jpeg(img)         파일을 읽고 이미지 변환 시도를 했을 때 
                                                  제대로 동작하면 깨진 파일 아니다.
            except:                               이미지 변환 시도할 때 문제가 생기면
                print(f"깨진파일 삭제 : {파일}")  깨진 파일이다.
                os.remove(파일)                   깨진 파일은 데이터에 도움이 안되니 내 컴퓨터에서 삭제하자
    
    경고
    - 이 이미지 약간 손상되었는데 그냥 읽었다.
      완전히 깨진 이미지는 아니고 살짝 불량인 이미지인 것 같아.
      완전      정상 → 경고 없음, 학습에 사용
      살짝      불량 → Corrupt JPEG 경고, 그래도 읽힘 → 학습에 사용
      완전 깨진 파일 → 아까 try/except 로 이미 삭제됨
    Corrupt JPEG data: 162 extraneous bytes before marker 0xd9
        사진 파일 끝부분에 불필요한 데이터가 붙어있다.
        근데 이미지 내용 자체는 읽을 수 있어서
        텐서플로우가 알아서 처리하고 학습에 사용하겠다.
        
        학습 결과에는 거의 영향 없음
    """
    for 폴더 in 폴더목록:
        for 파일 in (경로 / 폴더).glob("*.jpg"):
            try:
                img = tf.io.read_file(str(파일))
                tf.image.decode_jpeg(img)
            except:
                print(f"깨진파일 삭제 : {파일}")
                os.remove(파일)

#깨진 파일 확인해야할 경우
# 깨진파일제거(데이터경로) # 현재 PetImages 폴더 안에 존재하는 경로


# 깨진파일제거(데이터경로, ["강아지","돼지","토끼"])
# 현재 PetImages 폴더 안에 존재하는 경로
# Cat, Dog 라는 폴더 대신 강아지, 돼지, 토끼 경로를 폴더로 선택해서 폴더목록 삽입

#깨진파일제거("../특정폴더이름") # 현재 폴더를 탈출하여 특정 폴더에 존재하는 데이터셋 경로

# tf.keras.utils.image_dataset_from_directory 레거시 AI
# from tensorflow.keras.utils import image_dataset_from_directory 와 같이 작성해서 사용
훈련데이터 = image_dataset_from_directory(
    데이터경로,
    image_size=(64, 64),
    batch_size=32,
    validation_split=0.2,
    subset='training',
    seed=42
)
검증확인데이터 = image_dataset_from_directory(
    데이터경로,
    image_size=(64, 64),
    batch_size=32,
    validation_split=0.2,
    subset='validation',  # 보통 test 나 validation 이라는 표기법 사용
    seed=42
)

# 정규화
norm = Rescaling(1. / 255)
훈련데이터 = 훈련데이터.map(lambda x, y: (norm(x), y)).prefetch(1)
검증확인데이터 = 검증확인데이터.map(lambda x, y: (norm(x), y)).prefetch(1)

# CNN 모델
# 태어났을 때 부터 뇌 신경이 완벽한 것이 아니라 완벽해지도록 성장
# 생후 2~ 흑 백 밖에 읽을 수 없고, 100 전 후 다른 색상을 사람도 읽게 된다.
로봇뇌 = Sequential([
    Input(shape=(64, 64, 3)),
    # ========= 이미지 뇌 신경에서 빠르게 사용하도록 작업 시작
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(),
    Flatten(),
    # ========= 이미지 뇌 신경에서 빠르게 사용하도록 작업 종료
    # ========= 위 내용을 바탕으로 아래에서 신경망 생성
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid'),

])
로봇뇌.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
로봇뇌.fit(훈련데이터, epochs=5, validation_data=검증확인데이터)

# 폴더 모델 이름 변수화 처리
DIR_MODEL = 'models'
MODEL_NAME = 'dog_cat_model.keras'
# Step 1. models 폴더 만들기
os.makedirs(DIR_MODEL, exist_ok=True)

# Step 2. 모델 저장하기
로봇뇌.save(DIR_MODEL + '/' + MODEL_NAME)
print("모델 저장 완료!!!")

# Step 3. 저장됐는지 확인
if os.path.exists(DIR_MODEL + '/' + MODEL_NAME):
    print("저장 성공!!!")
else:
    print("저장 실패!!!")
