'''
텍스트에서 단어의 빈도에 따라 크기를 다르게 표시하는 시각화 기법
많이 나올수록 크게, 적게 나올수록 작게 표시

쇼핑몰 리뷰 수천 개 분석, 뉴스 키워드 파악, 유튜브 댓글 패턴 분석, 설문 주관식 요약 등 사용

pip install wordcloud
'''
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# 파이썬은 여러줄 문자열 사용할 경우 아래와 같이 사용할 수 있다.
# ''' '''    """ """ 구분 없다.
text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""
'''
기본값
WordCloud(
    width=400,                   # 이미지 너비
    height=200,                  # 이미지 높이
    background_color='black',    # 배경색상
    max_words=200,               # 최대 단어 수
    colormap ='viridis',         # 색상 테마
    font_path=None,              # 폰트 경로(한글일경우 필수)
    stopwords=None,              # 제외할 단어 집합
    min_font_size=4,             # 최소 글자 크기
    max_font_size=None,          # 최대 글자 크기
    mask=None,                   # 모양 마스크 이미지
    prefer_horizontal=0.9,       # 가로 단언 비율(0~1)
    scale=1,                     # 캔버스 비율
    relative_scaling=0.5         # 빈도 반영 강도(0~1)
)
colormap  = wordCloud에서 단어 색상을 지정하는 방법
- viridis = Matplotlib 에서 제공하는 색상 맵
            보라 -> 파랑 -> 초록 -> 노랑 순으로 색이 변하는 그라이데이션
- plasma  = 보라 -> 주황 -> 노랑
- inferno = 검정 -> 빨강 -> 노랑
- magma   = 검정 -> 보라 -> 노랑
- cividis = 청록/노랑 계열 색약 친화적
- cool, hot, spring, summer, autumn, winter 등 wordCloud docs에서 추가적으로 확인 가능

plt 내에 존재하는
interpolation = 보간법 = 알고 있는 데이터 지점들을 기반으로 그 사이의 값을 추정하여 
                         데이터의 공백채우거나 곡선을 생성하는 데이터 처리 기법
- imshow() : 이미지를 화면에 표시할 때 쓰는 기능
- 이미지를 확대/축소할 때 픽셀을 어떻게 부드럽게 보간할지 결정하는 옵션
- bilinear : 2*2 픽셀 주변 평균을 기반으로 부드럽게 보임 처리
'''

def 기본문법():
    # 1. WordCloud() 기능을 갖고온 후, wc 공간의 내부에 보관
    wc = WordCloud() # 커스텀을 하지 않을 경우, 기본값으로 세팅된다.

    # 2. .generate("문자데이터")
    # 문자열을 받아서 단어 빈도를 자동으로  계산하고 WordCloud 를 만들어주는 기능
    # 문자열을 공백 기준으로 단어 분리
    # 각 단어 빈도 자동 계산
    # 빈도가 높은 단어일수록 크게 배치 -> wordCould 이미지 생성
    # 반환
    wc.generate("Hello world")

    # 참고로 한국어 지원 안됨
    # 한국어를 하고 싶다면.. 한국인이 직접 계산해서 넣어야한다...

def wordcloud_plt_활용():
    wc = WordCloud(
        width=800,                  # 이미지 너비
        height=400,                 # 이미지 높이
        background_color='white',   # 배경색상
        max_words=100,              # 최대 단어 수
        colormap='viridis'          # 색상 테마
    ).generate(text)

    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('wordCloud.png',dpi=150)
    plt.show()







