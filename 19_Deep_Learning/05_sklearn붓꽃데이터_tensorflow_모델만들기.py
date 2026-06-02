# 목표 하나를 개발하는데 방법은 수십 수백만가지가 존재
# 머신러닝 / 딥러닝은 그 중 하나의 방법일 뿐
# 머신러닝이나 딥러닝이 아니어도 코딩으로 목표를 개발할 수 있다.
# 하지만 머신러닝이나 딥러닝에 비해서 개발자의 손이 심하게 많이 갈 뿐

import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# return_X_y 기능 안에는 1번째로 오는 변수에 데이터를 넣고
#                       2번째로 오는 변수에 정답을 넣는다 와 같은
#                       코딩이 기재되어 있다.
# 그래서 y, X 의 위치를 바꾸어서 작성하면 에러 발생
# AI 개발을 할 때 보통 X, y 의 형태로 train, test ,val 과 같은 명칭으로
# 훈련 데이터셋 정답 데이터셋을 사용하자 와 같은 개발자 간의 관례
X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Sequential = 머신러닝과 같은 AI 모델 만들기 도안
# 반드시 지켜야 할 규칙
# 1. 들어오는 데이터가 어떻게 생겼는지 입력층 세팅 데이터 1D 2D 3D ... 인지 확인하기
# 2. 데이터에서 사용할 컬럼의 개수 확인
#   꽃받침길이, 꽃받침너비, 꽃잎길이, 꽃잎너비
"""
옛날 방식
tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
Dense 가 두 가지 일을 동시에 한다 입력 정의 + 계산
DeepLearning 의 경우 모델을 세분화 해서 사람 뇌 처럼 AI 뇌도 세분화 하여 만들었으면 좋겠다.
keras = google 에서 권장하는 방식

권장 방식 -> 데이터 불러올거면 불러오는거만해라 
tf.keras.layers.Input(shape=4,),
tf.keras.layers.Dense(8, activation='relu'), 그 다음에 계산을 처리해라


tf.keras.layers.Input(shape=4,),
tf.keras.layers.Dense(8, activation='relu'), 이 둘 줄이
옛날방식의 tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)), 와
동일한 효과를 가진 코드 두 줄이다.

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1780362175.043768   20324 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1780362176.902147   20324 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.

tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
107: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
I0000 00:00:1780362178.463100   20324 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.

To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:TensorFlow GPU support is not available on native Windows for TensorFlow >= 2.11. Even if CUDA/cuDNN are installed, GPU will not be used. Please use WSL2 or the TensorFlow-DirectML plugin.



tf.keras.layers.Input(shape=4,), UserWarning 이 없다.

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1780362041.026190   21684 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1780362042.883331   21684 port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
I0000 00:00:1780362044.432535   21684 cpu_feature_guard.cc:227] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.

To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:TensorFlow GPU support is not available on native Windows for TensorFlow >= 2.11. Even if CUDA/cuDNN are installed, GPU will not be used. Please use WSL2 or the TensorFlow-DirectML plugin.

"""
model = tf.keras.Sequential([
    # 사람의 뇌처럼 a-z 까지 촘촘하게 AI뇌 신경망을 만들었으면 좋겠다.
    # tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    tf.keras.layers.Input(shape=(4,) ),# shape=(4,) 반드시 소괄호를 해주어야 한다.
    tf.keras.layers.Dense(8, activation='relu'),

    # softmax 는 확률로 바꿔주는 역할
    # 만약 softmax가 없으면 단순 훈련 숫자만 나온다.
    # 단순 훈련 숫자는 무엇인지 알 수 없다.
    # softmax 를 이용해서 각각의 숫자들을 3개 결과로 나타낼 때 확률로 나타낸다
    # setosa 일 확률 70% versicolor 일 확률 15%, virginica 10% 가 나왔다
    # 이 세가지 결과 중에서 가장 높은 숫자가 예측 결과로 Sequential 탈출해서 나올 것이다.
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # loss = mse
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=1000, verbose=1)
# epochs 는 크면 클수록 모델 훈련이 잘 될 수 있고, 과적합(=훈련데이터만 외움) 될 수 있다.
#           크면 클수록 모델이 완성되는 시간이 오래 걸리며, 컴퓨터 성능도 더 좋아야한다.
# verbose = 0 출력안봄 1 출력모두봄 2 진행상황만안봄

loss, acc = model.evaluate(X_test, y_test)
print(f"정확도 : {acc * 100:.1f}%")
