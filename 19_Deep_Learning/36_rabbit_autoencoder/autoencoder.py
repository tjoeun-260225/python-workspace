import tensorflow as tf
# GPT 를 이용해서 현재 데이터셋과 현재 컴퓨터 사양을 기준으로
# 제대로된 keras 모델 만드는 방향
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import matplotlib.pyplot as plt
# 참고로 파이썬에서 from 과 import 는 숫자로 시작할 수 없다.
# 파일이름 앞에 보통은 숫자를 붙여 작성하지 않는다.
# from 2_preprocessing import 데이터준비, 이미지크기

from preprocessing import 데이터준비, 이미지크기

입력크기 = 이미지크기 * 이미지크기 * 3


# from preprocessing import 데이터준비 작성하지 않는다면
# 2 ~ 5번까지 하나의 파일에 코드를 작성하거나
# 2번 코드를 3번에도 똑같이 작성을 해주어야 한다.
# 그런데 2번에서 특정 기능을 내보내기 처리를 하고 return 으로
# 내보낼 데이터를 지정해주면 파일을 분류하여 코드관리를 할 수 있고,
# 내보내진 데이터를 다른 파일에서 활용할 수 있다.
def 모델만들기():
    모델 = Sequential([
        Input(shape=(입력크기,)),
        Dense(1024, activation="relu"),
        Dense(512, activation="relu"),
        Dense(256, activation="relu"),
        Dense(128, activation="relu"),
        Dense(256, activation="relu"),
        Dense(512, activation="relu"),
        Dense(1024, activation="relu"),
        Dense(입력크기, activation="sigmoid"),
    ])
    모델.compile(optimizer="adam", loss="mse")
    return 모델


def 메인():
    훈련, 테스트 = 데이터준비()
    로봇뇌 = 모델만들기()
    로봇뇌.summary()
    로봇뇌.fit(
        훈련, 훈련,
        epochs=50,
        batch_size=32,
        validation_split=0.1,
        verbose=1
    )
    복원이미지 = 로봇뇌.predict(테스트[:5])

    그림, 축 = plt.subplots(2, 5, figsize=(15, 6))
    for i in range(5):
        축[0, i].imshow(테스트[i].reshape(이미지크기, 이미지크기, 3))
        축[1, i].imshow(복원이미지[i].reshape(이미지크기, 이미지크기, 3))
        for j in range(2):
            축[j, i].axis("off")
    축[0, 0].set_ylabel("원본")
    축[1, 0].set_ylabel("복원")
    plt.suptitle("토끼 이미지 오토인코더 복원 결과")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    메인()

"""
if __name__ =="__main__":
- 이 파일을 직접 실행했을 때만 그 안에 코드를 실행하고,
다른 파일에서 import 할 때는 실행하지 않는다.

preprocessing 의 경우 코드를 정의하는 것이지 정의를 내린 후
시각화를 한다와 같은 부가적인 작업을 할 이유가 없기 때문에
if __name__ =="__main__": 을 사용할 이유가 없다.

autoencoder 의 경우 메인() 이라는 기능에는 직접 실행 학습 + 시각화까지
한 번에 돌아가는 코드가 존재하는데, 4번 파일에서 이 파일을 import 할때
어디서 코드를 사용하겠다 표기를 해야지 코드 실행

if 최상단에 호출을 했을 때 실행하는 구문

폴더 __init__.py
생성을 하여 경로 설정
if __name__ =="__main__":

"""
