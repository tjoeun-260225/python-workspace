# train_and_save.py
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

NUM_WORDS = 10000
MAX_LEN = 200

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=NUM_WORDS)
x_train = pad_sequences(x_train, maxlen=MAX_LEN)
x_test  = pad_sequences(x_test,  maxlen=MAX_LEN)

model = Sequential([
    Embedding(input_dim=NUM_WORDS, output_dim=32, input_length=MAX_LEN),
    SimpleRNN(units=32),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.2)

# .keras 포맷으로 저장
model.save('sentiment_model.keras')
print("모델 저장 완료: sentiment_model.keras")

word_index = imdb.get_word_index()
with open('word_index.pkl', 'wb') as f:
    pickle.dump(word_index, f)
print("단어사전 저장 완료: word_index.pkl")