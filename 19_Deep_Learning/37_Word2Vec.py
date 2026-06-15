"""
비슷한 상황에서 쓰이는 비슷한 단어다 와 같은 개념을 가지고 진행하는 학습
단어를 의미를 담은 숫자를 벡터로 변환함

Word2Vec 어떻게 학습하는가
대량의 텍스트를 보면서 주변에 같이 나오는 단어들을 기억한다.

마법같은 결과
왕 - 남자 + 여자 = 여왕
과 같은 관계를 벡터 연산으로 계산할 수 있다.

두 가지 학습 방식
CBOW       주변 단어들 → 중간 단어 예측
Skip-gram  중간   단어 → 주변 단어 예측

보통 Skip-gram 이 성능이 더 좋다.
"""
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras import layers, Model
import tensorflow as tf

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

import random

_기존숫자변환 = random.randint
random.randint = lambda a, b: _기존숫자변환(a, int(b))
# 케라스 내 내부 버그가 고쳐지지 않아 발생하는 문제
# 케라스에서 단어를 숫자로 변경할 때
# 케라스 내부 코드

# 씨드 = random.randint(0,10e6)
# 10e6 = 10000000.0 소수점 형태로 되어있다.
# 단어는 숫자 int 형태로 되어있어 정수 소수 형태가 맞지 않아 발생하는 문제

# 케라스 자체에서 업데이트를 오랫동안 하지 않아 발생하는 문제

for seq in 시퀀스:
    p, l = skipgrams(seq, vocabulary_size=단어사이즈, window_size=2)
    짝꿍들.extend(p)
    라벨들.extend(l)
짝꿍들 = np.array(짝꿍들)
라벨들 = np.array(라벨들)

print("학습 쌍 예시 : ", 짝꿍들[3])  # [1 5] (주변단어, 중심단어) 형태로 이루어진 것
print("레이블  예시 : ", 라벨들[3])  # 0      (진짜=1 가짜=0)

# 4. Word2Vec 모델
벡터차원설정 = 10  # 몇 차원 벡터로 할 것인가

# 입력 : 중심 단어
input_target = layers.Input(shape=(1,))
# 입력 : 주변 단어
input_context = layers.Input(shape=(1,))

# 임베딩 레이어 단어를 숫자로 변환하는 과정
임베딩 = layers.Embedding(단어사이즈, 벡터차원설정)
타겟_임베딩 = 임베딩(input_target)
컨텍스트_임베딩 = 임베딩(input_context)

# 두 벡터가 얼마나 비슷한지 계산
dot = layers.Dot(axes=2)([타겟_임베딩, 컨텍스트_임베딩])
dot = layers.Flatten()(dot)

# 시그모이드로 0~1 출력(진짜  쌍인지 아닌지)
output = layers.Dense(1, activation='sigmoid')(dot)

model = Model(inputs=[input_target, input_context], output=output)
model.compile(loss='binary_crossentropy', optimizer="adam")
model.summary()

# 5. 학습
model.fit(
    [짝꿍들[:, 0], 짝꿍들[:, 1]],
    라벨들,
    epochs=100,
    batch_size=64,
    verbose=1
)

# 6. 임베딩 벡터 뽑기
단어_벡터들 = 임베딩.get_weights()[0]

# 특정 단어 벡터 확인
word = "왕을"
idx = 토크나이저.word_index[word]
print(f"{word} 벡터 : {단어_벡터들[idx]}")
