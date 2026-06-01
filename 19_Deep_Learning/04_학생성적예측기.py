import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
# 1. 가짜 데이터 생성(공부시간 → 성적)
X = tf.random.normal((100,1)) # csv 파일이나 이미지데이터 글자 데이터 가져온다.
y = X * 10 + 70               # 우리가 만들어야 하는 결말에 대하여 가져온다.
# 2. AI 뇌 만들기
model = tf.keras.Sequential([
    # 8 16과 같은 숫자는 개발자가 임의로 지정하는 숫자
    #
    #  Dense(8) 데이터 입력받는 층에서 특징을 8가지로 분석하겠다.
    # 개발자가 가정하여 숫자 와 activation을 작성하는 것이고,
    # input_shape 의 경우에는 데이터 상태에 따라 작성하는 값이 달라진다.
    # y = 결과값이 1개이므로, 1개의 컬럼만 참고하겠다. tf.random.normal((100,))
    tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(16, activation='relu'), # 음수는 모두 0으로 처리

    tf.keras.layers.Dense(1)
    # 마지막으로 예측해야하는 것은 성적 밖에 없기 때문에 1

    #마지막에 오는 출력층에는 relu 를 사용하지 않는다. 보통 linear

    # 중간 층에서는 예를 들어 총 데이터가 1GB 사진 데이터를 학습해야 하는데
    # 데이터가 너무 커서 sigmoid relu 나 다양한 방식으로 데이터를 잠시 축소하여
    # 학습할 때 사용하고 1GB 짜리 원래 데이터로 복구하여 결과를 조회하도록 해야할 일이 있다.
    # 그럴 때 데이터를 복구하는 형식 linear



    # 만약에 강아지 고양이 분류라면 마지막으로 들어와야 하는숫자는
    # tf.keras.layers.Dense(2)  위 뇌 구조를 통하여 강아지나 고양이로 나와야한다.

    # 만약에 강아지 고양이 새 분류라면 마지막으로 들어와야 하는숫자는
    # tf.keras.layers.Dense(3)  위 뇌 구조를 통하여 강아지나 고양이 새로 나와야한다.
])
"""
                       100개의 데이터   5개의 컬럼
X = tf.random.normal((    100         ,     5       ))
tf.keras.layers.Dense(8, activation='relu', input_shape=(5,)),

input_shape 은 컬럼의 개수에 영향을 받는다.
반드시 데이터 컬럼 개수와 input_shape 숫자를 동일하게 설정

                       100개의 데이터   1개의 컬럼
X = tf.random.normal((    100         ,      1      ))
tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),


X = tf.random.normal((    100         ,          )) 100개의 데이터 나열이지만
X = tf.random.normal((    100         ,    1      )) 
AI에서 데이터 행렬 에 대하여 작성할 때는 1이라는 숫자를 적어주는 것이 좋다.
"""
# 3. 학습 세팅
model.compile(optimizer='adam', loss='mse')
# 4. 학습 시작
model.fit(X, y, epochs=1000, verbose=1)

"""
Epoch 50/50
4/4 ━━━━━━━━━━━━━━━━━━━━ 0s 6ms/step - loss: 4165.8555 

loss 가 4000 대면 학습이 거의 안된 것이고 

"""