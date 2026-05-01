import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("소상공인시장진흥공단_전국 카페 점포수_11_04_2019.csv", encoding="cp949")
업소수 = np.array(df["업소수"])

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False


def 데이터확인():
    # 1. df.head()로 상위 5개 행을 출력하세요
    print(df.head())
    # 2. df.shape로 행과 열 개수를 출력하세요
    print(df.shape)
    # 3. 업소수 배열을 출력하세요
    print(업소수)


def 통계분석():
    # 1. 전체 기간 중 총 업소수 합계를 출력하세요
    print(np.sum(업소수))
    # 2. 가장 많은 카페가 있던 달의 업소수를 출력하세요
    print(np.max(업소수))
    # 3. 가장 적은 카페가 있던 달의 업소수를 출력하세요
    print(np.min(업소수))
    # 4. 월평균 카페 점포수를 출력하세요
    print(np.mean(업소수))
    # 5. 표준편차를 출력하고, 수치가 크면 어떤 의미인지 주석으로 작성하세요
    print(np.std(업소수))
    # 6. 중앙값을 출력하세요
    print(np.median(업소수))


def 인덱싱_슬라이싱_필터링():
    # 1. 첫 번째 달의 업소수를 출력하세요
    print(업소수[0])
    # 2. 마지막 달의 업소수를 출력하세요
    print(업소수[-1])
    # 3. 인덱스 5번부터 15번까지 슬라이싱해서 출력하세요
    print(업소수[5:16])
    # 4. 업소수가 80000개 이상인 달만 필터링해서 출력하세요
    print(업소수[업소수 >= 80000])
    # 5. 평균보다 업소수가 많은 달만 필터링해서 출력하세요
    print(업소수[업소수 >= np.mean(업소수)])


def 배열연산응용():
    # 1. 전체 업소수를 10000으로 나눈 배열을 만들고 출력하세요
    # (단위를 만 단위로 보기 편하게)
    만단위_업소수 = 업소수 / 10000
    print(만단위_업소수)
    # 2. 업소수가 전월 대비 증가했는지 보려면 어떤 연산이 필요할지
    # 생각해보고, 두 번째 달부터 마지막 달까지의 배열과
    # 첫 번째 달부터 마지막 직전 달까지의 배열을 빼서 출력하세요
    #
    # 힌트: 업소수[1:] - 업소수[:-1]
    전월대비증감 = 업소수[1:] - 업소수[:-1]
    print(전월대비증감)


def 시각화():
    # 1. 기준월을 x축, 업소수를 y축으로 꺾은선 그래프를 그리세요
    plt.figure(figsize=(12, 5))
    plt.plot(df["기준월"], df["업소수"], marker="o")
    # 2. 제목을 "전국 카페 월별 점포수 변화"로 설정하세요
    plt.title("전국 카페 월별 점포수 변화")
    # 3. x축 이름을 "기준월", y축 이름을 "업소수"로 설정하세요
    plt.xlabel("기준월")
    plt.ylabel("업소수")
    # 4. x축 레이블이 겹치지 않도록 rotation=45 를 적용하세요
    plt.xticks(rotation=45)
    # 5. 그래프를 출력하세요
    plt.show()
