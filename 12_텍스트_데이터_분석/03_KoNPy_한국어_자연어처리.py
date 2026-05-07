'''
한국어 자연어 처리(NLP)
한국어 문장을 형태소 단위로 쪼개고, 품사를 태깅하고, 명사만 뽑아내는 등의 작업을 한다.

형태소 분석기
               속도          정확도                       특징
Okt            빠름           보통           가장 많이 사용 / SNS 텍스트에 강함
   -- Open Korean Text 트위터 코리아 개발자 출신 이수민
   -- Twitter Korean Text 에서 Okt 명칭 변경
   -- SNS 텍스트(줄임말, 신조어)에 강한 이유는 트위터 데이터로 훈련했기 때문

Komoran        보통           높음                  균형 잡힌 성능
   -- 단국대학교 자연어처리 연구실
   -- 자바 기반으로 KoNLPy에 잘 통함 성능이 균형잡혀 있어 실무에서 많이 사용

Kkma           느림           높음                    상세한 분석
   -- 꼬꼬마 서울대학교 IDS(지능형 데이터 시스템) 연구실에서 개발
   -- 꼬리에 꼬리를 무는 형태소 분석기
   -- 느리지만 분석이 정교

Hannanum        보통           보통                    KAIST 개발
   -- KAIST 시맨틱웹 연구센터에서 개발
   -- 가장 오래된 분석기 중 하나
   -- 학술 연구용으로 시작

Mecab        매우 빠름        높음                    별도 설치 필요
   -- 일본 나라첨단과학기술대학원대학(NAIST) 에서 일본어용으로 개발
   -- 이후 한국어 버전인 Mecab-ko 를 카카오 개발자들이 포팅
   -- 속도가 빠른 이유는 C++ 로 짜여 있고, 사전 기반 탐색 알고리즘이 매우 최적화 되어 있기 때문
'''
import os.path

# 형태소 = 모양 형 , 상태 모습 태 , 바탕 요소 소
# 의미를 가진 가장 작은 언어 단위
# 더 쪼개면 의미가 없어지는 최소 단위

from konlpy.tag import Okt


def okt기반():
    okt = Okt()
    text = "나는 파이썬으로 자연어 처리를 공부하고 있어요"
    # 형태소 분리
    # .morphs(text) 형태소 분리
    # .morphs(text,  stem=True, norm=True)
    # stem=True 어간 추출 (공부하고 -> 공부하다)     norm=True 정규화(ㅋㅋㅋㅋㅋㅋㅋㅋㅋ->ㅋㅋ)
    print(okt.morphs(text))  # ['나', '는', '파이썬', '으로', '자연어', '처리', '를', '공부', '하고', '있어요']
    # 명사만 추출
    # .nouns(text) 명사만 추출
    print(okt.nouns(text))  # ['나', '파이썬', '자연어', '처리', '공부']
    # 형태소 + 품사 태깅
    # .pos(text)
    # .pos(text, stem=True, join=True)
    # stem=True   품사태깅 + 어간 추출, join=True 단어/품사 형태로 반환
    print(okt.morphs(text, stem=True))  # ['나', '는', '파이썬', '으로', '자연어', '처리', '를', '공부', '하고', '있다']

    '''
    품사 태그 종류(Okt 기준)
    Noun         명사    파이썬, 데이터
    Verb         동사    하다, 가다
    Adjective    형용사  좋다, 크다
    Adverb       부사    매우, 빨리
    Josa         조사    은, 는, 이, 가
    Eomi         어미    ~고, ~서
    Punctuation  구두점  . ! ?
    Foreign      외국어  Python
    Number       숫자    100
    '''


from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter


def wordcloud_okt_연결():
    # 1. 텍스트 준비
    text = """
파이썬은 데이터 분석과 머신러닝에 많이 사용됩니다.
데이터 과학자들은 파이썬으로 딥러닝 모델을 학습시킵니다.
자연어 처리와 컴퓨터 비전 분야에서도 파이썬이 인기입니다.
인공지능 시대에 데이터 분석 능력은 매우 중요합니다.
    """
    # 2. 형태소 분석기 초기화
    okt = Okt()

    # 3. 명사 추출
    nouns = okt.nouns(text)

    # 4. 불용어 정의 & 필터링
    stopwords = {'것', '수', '등', '및', '더', '이', '그', '저', '때', '년', '들'}

    # 컴프리핸션 리스트로 변환
    filtered = [w for w in nouns if w not in stopwords and len(w) > 1]
    '''
    filtered = []

    for w in nouns:
        if w not in stopwords and len(w) > 1:
            filtered.append(w)
    '''

    # 5. 단어 빈도 계산
    counts = Counter(filtered)
    print("상위 10개 : ", counts.most_common(10))

    # 6. 한글 폰트 경로 설정
    font_path = 'C:/Windows/Fonts/malgun.ttf'

    # 7. WordCloud 생성
    wc = WordCloud(
        font_path=font_path,
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='Set2'
    ).generate_from_frequencies(counts)
    # 계산된 빈도의 결과를 추가

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig("korean_word_cloud.png", dpi=150) # Dots Per Inch 1인치 안에 점(픽셀)이 몇개 들어가는지 나타내는 해상도 단위
    # 높을 수록 선명하다
    # 낮은 용도 화면용 평균 150 인쇄용 300 정도
    plt.show()

wordcloud_okt_연결()
def 한글폰트위치확인():
    print(os.path.exists('C:/Windows/Fonts/malgun.ttf'))

# 한글폰트위치확인()
