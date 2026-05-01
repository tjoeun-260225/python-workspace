# 컬럼 사업명	서비스	기준년월	지급건수	지급금액

# STEP 0 - Setting - 한글 폰트 등 기본 세팅
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'D2Coding'
# matplotlib.rcParams['font.family'] = 'AppleGothic' # 맥북에는 맑은 고딕 대신 애플고딕 존재
matplotlib.rcParams['axes.unicode_minus'] = False
# STEP 1 - Pandas 파일 불러오기
df = pd.read_csv('한국사회보장정보원_복지사업 월별 급여지급 현황_20241231.CSV', encoding='cp949')


# STEP 2 - Pandas 불러온 파일 기본정보 파악
def step2():
    print(df.head())
    print(df.tail())
    print("df.shape : ", df.shape)  # (108, 5)
    print("df.columns : ", df.columns)  # Index(['사업명', '서비스', '기준년월', '지급건수', '지급금액'], dtype='str')
    print(df['사업명'].unique())  # <StringArray>
    print(df.info())  # ['기초생활', '장애인복지', '기초연금']
    print(df.describe())  # Length: 3, dtype: str
    print(df.isnull().sum)  # RangeIndex: 108 entries, 0 to 107
    print(df['사업명'].value_counts())  # 사업명에 존재하는 세로 데이터 하나하나 확인해서 명칭 작성 개발자가 직접 해야한다.
    # value_counts() 가 없었다면 len(df['사업명']=='기초연금') 을 일일이 하나씩 다 써주어야 하는 상황 발생!


# STEP 3 - NumPay 기본 통계 계산
def step3():
    # 지급 금액만 배열로 추출
    금액 = df['지급금액'].values  # NumPy 배열로 변환되어 데이터 리스트 형태로 보관
    건수 = df['지급건수'].values

    print("지급금액 합계 : ", np.sum(금액))  # 33145867
    print("지급금액 평균 : ", np.mean(금액))  # 306906.1759259259
    print("지급금액 최대 : ", np.max(금액))  # 1855385
    print("지급금액 최소 : ", np.min(금액))  # 5
    print("표  준  편 차 : ", np.std(금액))  # 567170.5976330427
    print("사업명별 평균 지급금액 : ", df.groupby('사업명')['지급금액'].mean())
    '''
    기초생활     1.177620e+05    1,177.6  억원
    기초연금     1.833347e+06    18,333.5 억원
    장애인복지    1.044740e+05   1,044.7  억원
    '''


# STEP 4 - Pandas 데이터 필터링
def step4():
    기초연금 = df[df['사업명'] == '기초연금']
    print(기초연금.head())

    # 기준년월 컬럼에서 문자열로되어있고 2024로 시작하는
    #  df[df['기준년월'].     str      .startswith('2024')]
    df_2024 = df[df['기준년월'].str.startswith('2024')]
    print(df_2024)

    # 지급건수 100만 이상인 행만
    많은건수 = df[df['지급건수'] > 1000000]
    print(많은건수['서비스'].value_counts())


# STEP 5 - Matplotlib 선그래프 그리기 (plot)
def step5():
    # 기초연금 월별 지급금액 추이
    기초연금 = df[df['사업명'] == '기초연금']
    plt.figure(figsize=(12, 5))  # 그래프가 나오는 가로 세로 크기 설정
    # figsize=(12, 5) 가로가 길고, 세로가 짧은 그래프
    # figsize=(6, 6) 정사각형 그래프
    # figsize=(5, 10) 세로가 긴 그래프
    plt.plot(기초연금['기준년월'], 기초연금['지급금액'], marker='o')
    plt.title('기초연금 월별 지급금액 추이')
    plt.xlabel('기준년월')
    plt.ylabel('지급금액(백만원)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# STEP 6 - Matplotlib 막대그래프 그리기 (bar)
def step6():
    # 사업명별 평균 지급금액 비교
    사업별평균 = df.groupby('사업명')['지급금액'].mean()

    plt.figure(figsize=(8, 5))
    plt.bar(사업별평균.index, 사업별평균.values, color=['skyblue', 'salmon', 'lightgreen'])
    plt.title("사업명별 평균 지급금액")
    plt.xlabel('사업명')
    plt.ylabel('평균 지급금액(백만원)')
    plt.tight_layout()
    plt.show()
step6()
# STEP 7 - Matplotlib 선그래프 그리기 (plot) - 사업명 3개를 한 화면에서 비교
