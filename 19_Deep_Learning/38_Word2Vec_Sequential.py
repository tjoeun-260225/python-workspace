import numpy as np
from keras import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras import layers, Model
import tensorflow as tf
import random

_기존숫자변환 = random.randint
random.randint = lambda a, b: _기존숫자변환(a, int(b))

# 1. 샘플 텍스트
sentences = [
    "나는 왕을 만났다",
    "나는 여왕을 만났다",
    "나는 대통령을 만났다",
    "왕과 여왕은 궁전에 산다",
    "대통령은 청와대에 산다"
]

# 2. 토크나이징 (단어 → 숫자)
토크나이저 = Tokenizer()
토크나이저.fit_on_texts(sentences)
시퀀스 = 토크나이저.texts_to_sequences(sentences)
단어사이즈 = len(토크나이저.word_index) + 1

print(f"단어사전 {토크나이저.word_index}")

# 3. skip-gram 쌍 만들기
# "나는 왕을 만났다" → (왕을, 나는), (왕을, 만났다) 이런 쌍 생성
짝꿍들 = []
라벨들 = []

for seq in 시퀀스:
    p, l = skipgrams(seq, vocabulary_size=단어사이즈, window_size=2)
    짝꿍들.extend(p)
    라벨들.extend(l)
짝꿍들 = np.array(짝꿍들)
라벨들 = np.array(라벨들)

print("학습 쌍 예시 : ", 짝꿍들[3])  # [1 5] (주변단어, 중심단어) 형태로 이루어진 것
print("레이블  예시 : ", 라벨들[3])  # 0      (진짜=1 가짜=0)

# 4. Word2Vec 모델
# 37번과 같은 형태의 모델을 이해하기 어려운 상황에서
# 37번 코드를 제공받았다면
# Sequential 케라스를 사용한 형태의 코드를 다시 제공해줘
벡터차원설정 = 10  # 몇 차원 벡터로 할 것인가

model = Sequential([
    layers.Embedding(input_dim=단어사이즈, output_dim=벡터차원설정, input_length=2),
    layers.Lambda(lambda  x:tf.reduce_sum(x,axis=1)),
    layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer="adam")
model.summary()
# 5. 학습
model.fit(짝꿍들,라벨들,epochs=100,batch_size=64,verbose=1)
# 6. 임베딩 벡터 뽑기
단어_벡터들 = model.layers[0].get_weights()[0]
# 특정 단어 벡터 확인
word = "왕을"
idx = 토크나이저.word_index[word]
print(f"{word} 벡터 : {단어_벡터들[idx]}")
