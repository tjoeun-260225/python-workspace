from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


def 실습1():
    # TODO: WordCloud 객체 생성 (기본값으로)
    wc = WordCloud()

    # TODO: text 로 WordCloud 생성
    text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""


def 실습2():
    text = """
Python machine learning data science artificial intelligence
deep learning neural network programming code development
algorithm model training dataset feature engineering
"""
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='plasma'
    ).generate(text)

    # TODO: figure 사이즈 (10, 5)
    plt.figure(figsize=(10, 5))
    # TODO: wc 이미지 출력, 보간법 bilinear
    plt.imshow(wc, interpolation='bilinear')
    # TODO: 축 끄기
    plt.axis('off')  # x축 y 축 그릴 필요 없으므로 축 제거하기
    # TODO: 여백 자동조정
    plt.tight_layout()
    # TODO: 'wordcloud.png' 로 저장, dpi=150
    plt.savefig('wordCloud.png', dpi=150)
    # TODO: 화면에 출력
    plt.show()


text = """
game player character level skill attack defense magic sword shield
warrior mage archer knight paladin ranger assassin monk wizard priest
quest dungeon boss monster enemy battle victory defeat reward experience
item weapon armor potion gold treasure map village castle dragon
team strategy strength speed agility intelligence stamina power ability
"""


def 실습3():
    wc = WordCloud(
        background_color='black',
        width=1000,
        height=500,
        max_words=50
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def 실습4():
    colormaps = ['plasma', 'inferno', 'cool']
    plt.figure(figsize=(15, 5))
    for i, cmap in enumerate(colormaps):
        wc = WordCloud(
            colormap=cmap
        ).generate(text)
        plt.subplot(1, 3, i + 1)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(cmap)
    plt.tight_layout()
    plt.show()


def 실습5():
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text)
    wc.to_file('wc_file.png')


def 실습6_형태소분석():
    okt = Okt()
    text = "나는 파이썬으로 자연어 처리를 공부하고 있어요"

    # TODO: 형태소 분리 출력
    print(okt.morphs(text))

    # TODO: 명사만 추출 출력
    print(okt.nouns(text))

    # TODO: 어간추출(stem=True) 형태소 분리 출력
    print(okt.morphs(text, stem=True))


def 실습7_wordcloud연결():
    text = """
파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
데이터 과학자들은 파이썬으로 딥러닝 모델을 학습시킵니다.
자연어 처리와 컴퓨터 비전 분야에서도 파이썬이 인기입니다.
인공지능 시대에 데이터 분석 능력은 매우 중요합니다.
"""
    okt = Okt()
    ###### nouns 거치기 전 : 파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
    nouns = okt.nouns(text)  # 은 는 이 가 와 과 같은 조사를 여기서 제거
    # 불용어 = 텍스트에서 의미가 없는 단어 / 자주 나오지만 분석에 도움이 안 되는 단어들

    ###### nouns 거치고 난 후 : 파이썬 데이터 분석 머신러닝
    ###### nous로 거르지 못한 단어를 2차적으로 거르기 위해서 추가해놓은 옵션
    stopwords = {'것', '수', '등', '및', '더', '이', '그', '저', '때', '년', '들'}
    filtered = [w for w in nouns if w not in stopwords and len(w) > 1]
    '''
    filtered = [w for w in nouns if w not in stopwords and len(w) > 1]
    filtered = []
    
    for w in nouns:  nouns 리스트에서 하나씩 꺼내서 w 에 담는다.
        조건1번 =  w not in stopwords   # w 가 불용어 목록에 없으면 True
        조건2번 = len(w) > 1            # w 의 글자 수가 1보다 크면 True
        if 조건1번 and 조건2:           # 위 결과가 둘다 True일 때 만 
            filtered.append(w)          # 리스트에 추가
            
    파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
    은 과 에 이 다 어떤 텍스트에나 붙고 의미가 없다.
    파이썬은 -> 은 을 제거한다.
    '''
    counts = Counter(filtered)
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    wc = WordCloud(
        font_path=font_path,
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='Set2'
    ).generate_from_frequencies(counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('korean_wordcloud.png', dpi=150)
    plt.show()
