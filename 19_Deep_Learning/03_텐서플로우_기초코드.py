# warning 메세지가 보기 싫을 때 끄는 방법
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' # ONDNN 만 안하겠다.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # 0=전부 출력, 1=INFO제거 2=WARNING제거 3=전부출력안함
import tensorflow as tf

# 1. 가짜 데이터로 텐서플로우 이용해보기
X = tf.random.normal((100, 10))  # 샘플 100개 컬럼 10개
y = tf.random.normal((100, 1))  # 정답 100개 컬럼  1개
'''
tf. 구글에서 개발한 텐서플로우 자체에서 만든 랜덤으로 
귀로빈섬(=파이썬창시자)가 만든 random과 착각해서는 안된다.
둘은 다른 것이다.
tf
.random : 무언가를 임의적으로 작업한다.
 - .normal() = 0 근처 숫자가 많이 나오게끔 만들겠다.    가중치 초기화
 - .uniform() = 정해진 범위 안에서 골고루 나오게끔      범위를 지정해서 무언가 해야할 때
 - .set_seed() = 랜덤인데 항상 같은 결과가 나오게 고정  같은 결과를 재현해야 할 때
 ==== 위 세가지 많이 사용 ====
 - .shuffle() = 순서를 랜덤으로 섞어준다.               데이터 섞을 때
 - .truncated_normal() = normal 과 비슷한데 크기가 너무 크거나 작은 값은 잘라내겠다.
                                                        안정적으로 초기화 진행할 때
Sequential
- 레이어를 순서대로 쌓는다
- AI 뇌를 만들 때 어떤 구조로 뇌를 만들 것인지 층층이 쌓는 것
- 개발자가 AI 뇌를 만들 때 어떤 형태로 뇌를 만들 것인지 레고 블록을 쌓듯이, 
  층을 원하는 만큼 만드는 것
layers   = AI 뇌의 층으로 용도에 따라 종류가 다르다.
기본층
- .Dense = 빽빽한 촘촘한 뜻 모든 점이 다음 층 모든 점이랑 빠짐없이 전부 연결되어 있다.
이미지용
- .Conv2D = 이미지에 특징을 찾아내는 층 / 사진을 인식할 때 사용
-     1층 Conv2D 에서 선     점 같은 단순한 특징을 찾고
-     2층 Conv2D 에서 눈     코 같은 복잡한 특징을 찾고
-     3층 Conv2D 에서 얼굴 전체 같은 고차원 특징을 찾는다. 왜 같은 뇌를 개발자가 작성
- .MaxPooling2D = 이미지 크기를 줄여주는 층 / 학습할 때 이미지가 너무 크면 학습하는데 시간이
                  오래 걸리므로 이미지 사이즈를 임의적으로 줄여서 사용
                  Conv2D와 같이 사용
                  
                  보통 Conv2D를 이용한 다음에 Conv2D에 존재하는 데이터를 바탕으로
                  중요해보이는 데이터만 남겨두고 나머지 필요없는 데이터를 버릴 때 사용
                  Conv2D       → MaxPooling2D 이런식으로 많이 사용
                  MaxPooling2D → Conv2D       이렇게는 사용하지 않는다.
                  
- .Flatten      = 2D이미지를 1D 일자로 펴주는 층
                  Conv2D 로 (표형태)로 나온 결과를 Dense 로 작업해야할 때 중간에 사용
                  Dense 같은 경우 표가 아닌 목록 형태로 되어 있는 데이터만 받아서 사용할 수 있다.
                  만약에 Conv2D에서 Dense 로 가야할 일이 있을 때 중간에
                  Conv2D → Flatten → Dense  넣어 왼쪽과 같이 사용
텍스트/순서용
- .LSTM        = 앞 뒤 순서를 기억하는 층. 문장, 주가 예측할 때 사용
                 문장의 순서를 기억할 때 사용
                 Dense 의 경우 나는 / 밥을 / 먹었다 에서 순서를 모른다.
                 LSTM  의 경우 나는 → 밥을 → 먹었다 흐름 순서를 기억한다.
                 글자에서는 DENSE 보다 LSTM 사용한다.
                 
                 
- .Embedding   = 단어를 숫자로 바꿔주는 층 / 자연어 처리할 때 사용(파파고 만들 때)
학습 도움용
- .Dropout     = 학습할 때 뉴런 일부를 랜덤으로 꺼냄. 외워버리는 것을 방지
- .BatchNormalization = 숫자 크기를 일정하게 정규화해줌. 학습 안정시킬 때 사용

activation
relu
input_shape
compile
optimizer
adam
loss
mse
epochs
- 같은 데이터를 몇  번 해서 반복하여 공부할지 기입
- 사람도 한 번봐서 모르는 것처럼 같은 데이터를 여러 번 봐야 외우듯이 AI도 여러번 
  보게끔 하여 공부시킨다.
- 에포크가 클수록 메모리나 gpu 사용량도 커진다. 컴퓨터 사양에 따라 적절히 숫자 크기 작성
verbose
- 0 = 아무것도 학습하는 동안 개발자에게 안보여주겠다. 개발자는 끝나고나서 결과만 확인
- 1 = 진행바 + 결과 보여줌
- 2 = 진행바 없이 텍스트로만 보여줌
시간이 없어 급해 0을 사용해서 출력하는 메모리소비 없이 모델 생성
시간 여유 있고 나는 제대로된 모델 학습을 하고 있는지 궁금해 1 사용
아.. 나는 시간 여유는 있는데.. 굳이 하나하나 봐야해? 진행바 없이 텍스트로만 진행상황 조회
'''

# 2. 모델 만들기
model = tf.keras.Sequential([
    tf.keras.layers.Dense(5, activation='relu', input_shape=(10, )), #input_shape=(10, 0))
    tf.keras.layers.Dense(1)
])

# 3. 학습 준비 + 학습
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=100, verbose=1)


























"""
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1780281484.620415   16396 port.cc:153]
Tensorflow 내부 로그 시스템이 초기화 되기 전에 메세지가 출력될 수 있다 와 같은 단순 알림

oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
intel 에서 추가적으로 만든 딥러닝 연산 최적화 라이브러리
cpu 연산을 더 빠르게 해준다.
활성화되어 있어, 부동소수점 연산 순서가 달라질 수 있고, 
그로 인해 결과값이 아무 미세하게 달라질 수 있다. 안내문구

위 두가지는 정보성 메세지 이므로 그냥 두어 된다.
"""