'''
loc - pandas DataFrame / Series 에서라벨(이름) 기반으로 데이터를 선택하는 인덱서
dt.loc[행] 행라벨로 선택
dt.loc[행, 열] 행 + 열 라벨로 선택

axes = 여러 그래프를 만들 때 subplot 에서 접근하는 배열
한 줄에서
axes[0] 왼쪽 그래프
axes[1] 오른쪽 그래프



'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False


def matplotlib문제1():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 5, 3]

    plt.plot(x, y)
    plt.title('내 첫 그래프')
    plt.show()

    과목 = ['수학', '영어', '과학']
    점수 = [80, 95, 70]

    plt.bar(과목, 점수)
    plt.show()
    # randn
    data = np.random.randn(1000)

    plt.hist(data, bins=20)
    plt.show()
    # 1행 2열 서브플롯 - 왼쪽은 문제1, 오른쪽은 문제2
    fig, axes = plt.subplots(1, 2)

    axes[0].plot(x, y)
    axes[1].bar(과목, 점수)

    plt.show()


def matplotlib문제2():
    plt.rcParams['font.family'] = 'D2Coding'
    plt.rcParams['axes.unicode_minus'] = False

    sns.set_theme(style='whitegrid')
    sns.set_palette('pastel')

    df = pd.read_csv('서울교통공사_역별 일별 시간대별 승하차인원 정보_20241231.csv', encoding='euc-kr')

    시간대 = [col for col in df.columns if '시' in col or '시간대' in col]
    df['총인원'] = df[시간대].sum(axis=1)  # 시간대 컬럼들을 행 방향으로 합산, axis=?

    # =============================================
    # TODO 1
    # 호선, 역명, 승하차구분, 총인원 열만 꺼내서 출력하세요.
    # 힌트 : df[[???]]
    # =============================================
    print(df[['호선', '역명', '승하차구분', '총인원']])

    # =============================================
    # TODO 2
    # 승하차구분 열에 어떤 값들이 있는지 확인하세요.
    # 힌트 : df[???].value_counts()
    # =============================================
    print(df['승하차구분'].value_counts())

    # =============================================
    # TODO 3
    # 승차 데이터만 필터링하세요.
    # 힌트 : df[df[???] == ???]
    # =============================================
    승차 = df[df['승하차구분'] == '승차']

    # =============================================
    # TODO 4
    # 호선별 총 승차 인원 합계를 내림차순으로 출력하세요.
    # 힌트 : groupby → sum → sort_values
    # =============================================
    호선별 = 승차.groupby('호선')['총인원'].sum().sort_values(ascending=False)
    print(호선별)

    # =============================================
    # TODO 5
    # 호선별 총 승차 인원을 막대 그래프로 그리세요.
    # 제목은 '호선별 총 승차 인원'
    # =============================================
    plt.bar(호선별.index, 호선별.values)
    plt.title('호선별 총 승차 인원')
    plt.xticks(rotation=45)
    plt.show()

    # =============================================
    # TODO 6
    # 강남역 데이터만 필터링하고
    # 승하차별 시간대 평균을 구하세요.
    # 힌트 : groupby → mean
    # =============================================
    강남 = df[df['역명'] == '강남']
    강남평균 = 강남.groupby('승하차구분')[시간대].mean()

    # =============================================
    # TODO 7
    # 강남역 승차/하차 시간대별 평균을 꺾은선 그래프로 그리세요.
    # legend 포함, 제목은 '강남역 시간대별 승하차'
    # =============================================
    plt.plot(시간대, 강남평균.loc['승차'], label='승차')
    plt.plot(시간대, 강남평균.loc['하차'], label='하차')
    plt.title('강남역 시간대별 승하차')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

    # =============================================
    # TODO 8
    # 승차 인원 TOP 10 역을 구하고
    # 가로 막대 그래프로 그리세요. (barh)
    # 힌트 : head(???)
    # =============================================
    top10 = 승차.groupby('역명')['총인원'].sum().sort_values(ascending=False).head(10)
    plt.barh(top10.index, top10.values)
    plt.title('승차 인원 TOP 10 역')
    plt.show()

    # =============================================
    # TODO 9
    # 1호선 총인원 분포를 히스토그램으로 그리세요.
    # bins=30, kde=True
    # =============================================
    line1 = df[df['호선'] == '1호선']['총인원']
    sns.histplot(line1, bins=30, kde=True)
    plt.title('1호선 이용 인원 분포')
    plt.show()

    # =============================================
    # TODO 10
    # 1행 2열 서브플롯으로
    # 왼쪽 = TODO 5 호선별 막대 그래프
    # 오른쪽 = TODO 8 TOP10 가로 막대 그래프
    # =============================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].bar(호선별.index, 호선별.values)
    axes[0].set_title('호선별 막대 그래프')

    axes[1].barh(top10.index, top10.values)
    axes[1].set_title('TOP10 가로 막대 그래프')

    plt.tight_layout()
    plt.show()
matplotlib문제2()