from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Flatten, Dense

# fashion_mnist 의 경우 데이터셋이 흑백이기 때문에
# 흰 배경에 옷만 있는 이미지 거의 가능
# 가운데 정렬된 데이터만 가능
# 사람이 입고 있는 사진이나 복잡한 배경 고해상도의 컬러 사진 불가
# 이 과정을 해결하기 위한 개선된 모델 출시

labels = ['티셔츠', '바지', '스웨터', '드레스', '코트',
          '샌들', '셔츠', '스니커즈', '가방', '부츠']

def run_fashion_mnist():
    # Step 1. 데이터 불러오기
    (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    # Step 2. 정규화
    X_train, X_test = X_train / 255.0, X_test / 255.0

    # Step 3. 모델 설계
    model = Sequential([
        Input(shape=(28, 28)),
        Flatten(),
        Dense(256, activation='relu'),
        Dense(10, activation='softmax')
    ])

    # Step 4. 컴파일
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    # Step 5. 학습
    model.fit(X_train, y_train, epochs=10, verbose=1)

    # Step 6. 평가
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"[Fashion MNIST] 정확도: {acc*100:.1f}%")

    # Step 7. 모델 저장
    model.save('fashion_model.keras')
    print("모델 저장 완료")

run_fashion_mnist()