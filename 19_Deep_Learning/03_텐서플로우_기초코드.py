# warning 메세지가 보기 싫을 때 끄는 방법
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' # ONDNN 만 안하겠다.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # 0=전부 출력, 1=INFO제거 2=WARNING제거 3=전부출력안함
import tensorflow as tf

# 1. 가짜 데이터로 텐서플로우 이용해보기
X = tf.random.normal((100, 10))  # 샘플 100개 컬럼 10개
y = tf.random.normal((100, 1))  # 정답 100개 컬럼  1개

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