import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ================================
# 1. CSV 불러오기
# ================================
df = pd.read_csv("csvs/google_app_review.csv")
print(df.head())
print(df.shape)
print(df['rating'].value_counts())

# ================================
# 2. 전처리 - 라벨 만들기
# ================================
df = df[df['rating'] != 3]
df = df.dropna(subset=['review'])
df['label'] = df['rating'].apply(
    lambda x: 'positive' if x >= 4 else 'negative'
)

print(df['label'].value_counts())
# ================================
# 3. 데이터 분리
# ================================
X = df['review']  # TODO 5: 입력값 - 리뷰 텍스트 컬럼
y = df['label']  # TODO 6: 정답값 - 라벨 컬럼

test_size = 0.2
random_state = 42

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)

# ================================
# 4. 텍스트 → 숫자 변환
# ================================
# 리뷰   → 텍스트 데이터       → CountVectorizer 로 먼저 숫자로 바꿔야 함

"""
CountVectorizer 옵션이 존재 옵션을 검색해서 찾은 후 적용
print(dir(vectorizer))

['_CountVectorizer__metadata_request__fit', '_CountVectorizer__metadata_request__transform', '__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__sklearn_clone__', '__sklearn_tags__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_char_ngrams', '_char_wb_ngrams', '_check_stop_words_consistency', '_check_vocabulary', '_count_vocab', '_doc_link_module', '_doc_link_template', '_doc_link_url_param_generator', '_get_class_level_metadata_request_values', '_get_doc_link', '_get_metadata_request', '_get_param_names', '_get_params_html', '_html_repr', '_limit_features', '_parameter_constraints', '_repr_html_', '_repr_html_inner', '_repr_mimebundle_', '_sort_features', '_validate_ngram_range', '_validate_params', '_validate_vocabulary', '_warn_for_unused_params', '_white_spaces', '_word_ngrams', 'analyzer', 'binary', 'build_analyzer', 'build_preprocessor', 'build_tokenizer', 'decode', 'decode_error', 'dtype', 'encoding', 'fit', 'fit_transform', 'get_feature_names_out', 'get_metadata_routing', 'get_params', 'get_stop_words', 'input', 'inverse_transform', 'lowercase', 'max_df', 'max_features', 'min_df', 'ngram_range', 'preprocessor', 'set_params', 'stop_words', 'strip_accents', 'token_pattern', 'tokenizer', 'transform', 'vocabulary']
"""
#vectorizer = CountVectorizer()
vectorizer = CountVectorizer(
    ngram_range=(1,2),
    min_df=2,
    max_features=10000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
# ================================
# 5. 모델 학습
# ================================
model = MultinomialNB()
#model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
acc = accuracy_score(y_test, model.predict(X_test_vec))
print(f"정확도: {acc * 100:.1f}%")

# ================================
# 6. 모델 저장
# ================================
# digit  → model 만 pkl 저장
# 리뷰   → model + vectorizer 를 딕셔너리로 묶어서 저장
#           → 왜? 나중에 app.py 에서 새 리뷰가 들어오면
#             똑같은 vectorizer 로 글자→숫자 변환을 해야 하기 때문

파일명 = f'models/review_model_{test_size}_{random_state}_{acc * 100:.1f}.pkl'

with open(파일명, 'wb') as f:
    pickle.dump({'model': model, 'vectorizer': vectorizer},
                f)
print(f"저장완료: {파일명}")
