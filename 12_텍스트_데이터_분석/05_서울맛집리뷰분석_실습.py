import pandas as pd
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# ===========================
# 1단계 : 샘플 데이터 만들기
# ===========================

data = {
    '식당명': ['맛있는 삼겹살', '강남 스시', '홍대 파스타', '명동 칼국수', '이태원 버거'],
    '지역': ['마포구', '강남구', '마포구', '중구', '용산구'],
    '별점': [4.5, 4.8, 4.2, 4.0, 4.6],
    '리뷰': [
        '고기가 신선하고 맛있어요 직원도 친절하고 분위기도 좋아요 재방문 의사 있어요',
        '스시가 정말 신선해요 가격이 비싸지만 맛은 최고 분위기도 고급스러워요',
        '파스타 면이 쫄깃하고 소스가 진해요 양도 많고 가격도 합리적이에요',
        '칼국수 국물이 진하고 맛있어요 줄 서서 먹을 만해요 양도 푸짐해요',
        '패티가 두툼하고 육즙이 풍부해요 빵도 신선하고 감자튀김도 맛있어요'
    ]
}

df = pd.DataFrame(data)  # 딕셔너리 형태의 데이터를 표 형태의 데이터로 변환

print(df)

print(df.info())

# ===========================
# 2단계 : 기본 분석
# ===========================

print(df['별점'].mean())  # 별점 열을 선택해서 평균값을 계산하여 출력
print(df['지역'].value_counts())  # 지역 열에서 각 값이 몇 번 등장하는지 세서 많은 순으로 출력
# 마포구 2번 등장 강남구가 1번등장 중구 1번 등장 처럼 개수 세기
print(df.sort_values('별점', ascending=False))  # 별점 열을 가준으로 DataFrame 전체를 정렬해서 출력
# ascending=True(기본값) 오름차순  ascending=False 내림차순

# ===========================
# 3단계 : 리뷰 WordCloud
# ===========================
all_reviews = ' '.join(df['리뷰'])
# '구분방법'.join() = 리스트의 요소들을 특정 문자열로 이어붙이는 기능
# 단어들 = ["사과","바나나","딸기"]
#   ' '.join(단어들)  # 사과 바나나 딸기 공백으로 연결
# '!!!'.join(단어들)  # 사과!!!바나나!!!딸기 !!!로 연결
okt = Okt()
nouns = okt.nouns(all_reviews)  # 은 는 이 가 처럼 기본 불용어 제거

# nouns 에서 제공하지 않고, 개발자가 원하는 결과에 필요하지 않은 불(필요한)용어를 추가로 작성
stopwords = {'것', '수', '등', '정말', '매우', '너무'}
'''
filtered = []
for w in nouns:
    if w not in stopwords and len(w) >= 2 :
        filtered.append(w)
'''
filtered = [w for w in nouns if w not in stopwords and len(w) >= 2]
counts = Counter(filtered)
print(counts.most_common(5))
font_path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(
    font_path=font_path, width=800, height=400, background_color='white', colormap='Set2'
).generate_from_frequencies(counts)


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['axes.unicode_minus'] = False 마이너스 깨짐 방지 하지 않으면
# 데이터에 있는 -20 -30 -40 이 □20 □30 □40



plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('review_wordcloud.png', dpi=150)
plt.show()

# ===========================
# 4단계 : 별점 막대그래프
# ===========================
plt.figure(figsize=(8, 4))
plt.bar(df['식당명'], df['별점'], color='coral')
plt.ylim(3.5, 5.0)
plt.title('식당별 별점')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('rating_bar.png', dpi=150)
plt.show()
