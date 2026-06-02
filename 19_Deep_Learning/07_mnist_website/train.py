from tensorflow.keras.datasets import mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense

"""
구글은 무엇이든 자체적인 것을 좋아한다.
완성된 기계 뇌를 만들 때도
pkl 을 사용하는 것이 아니라
keras 확장자 명칭이나 h5 와 같은 확장자 명칭을 선호
"""

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0
# 컬러체계가 0~255개 존재하여 255이다.
# 실수 범위까지 포함해서 나누기를 진행해라 하여 .0 붙은 것

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),  # 한줄로 정렬 시켜서 학습하겠다. 이미지형태 그대로 계산을 하게되면
    # 계산 식이 느려지고 메모리 성능도 많이 차지하기 때문에
    # 한줄정렬 형태로 만들어서 계산처리를 원활하도록 하겠다.
    Dense(128, activation='relu'),  # 보통 64나 128 256 숫자범위로 많이 시작
    Dense(10, activation='softmax')
])
# compile = 위에서 Sequential 내에 만들어진 기계 두뇌로 학습할 준비
#           optimizer = 정답을 틀렸을 때 어떻게 정답 맞추도록 오답노트를 작성할까 선택
#                      가장 많이 사용하는 오답노트 방법 adam
#           loss     = 정답을 객관식으로 표기하여 얼마나 정답을 틀렸는지 계산하는 방법
#           metrics  = 학습하면서 정확도 측정 / metrics 작성하지 않으면 loss 만 보임
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# X_train = 문제지 이미지 60,000 장
# y_train = 정답지 0~9 숫자
# epochs  = 문제집을 30번 반복해서 풀기
# verbose = 학습 과정을 어떻게 보여줄 것인가 개발자에게
model.fit(X_train, y_train, epochs=10, verbose=1)
# 훈련한거 시험보자~
loss, acc = model.evaluate(X_test, y_test, verbose=1)
print(f"mnist정확도 : {acc*100:.1f}%")

# .keras = made in google
# 요즘 구글은.. jpg 나 png 대신 webp 밀고있다.. 이미지도..
model.save("mnist_model.keras")


"""
model = Sequential([])  AI 뇌 만들기 뇌꾸
model.compile()         만들어진 뇌로 학습할 준비 세팅
model.fit()             만들어진 뇌와 준비된 세팅을 참고해서 훈련하기
model.evaluate()        훈련이 끝난 뇌가 개발자가 원하는대로 잘 만들어졌는지 확인
model.save()            훈련이 끝났고, 개발자 마음에 드는 완성된 부품 저장하기

1611/1875 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - 
accuracy: 0.9986 - loss: 0.0047
NaN -> 우리가 계산한 식이 잘못되었다.
Sequential 을 다시 계산해서 작성해야한다.

"""