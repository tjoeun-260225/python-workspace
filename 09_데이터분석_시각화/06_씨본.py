'''
Seaborn python 데이터 시각화 라이브러리
matplotlib 기반으로 만들어졌지만 훨씬 적은 코드로 예쁜 그래프 그릴 수 있다.
판다스 DataFrame 과 함께 데이터 분석할 때 자주 사용

주 종류
scatterplot 산점도 분포 파악
lineplot    선 그래프 추세 파악
histplot    히스토그램
barplot     바 그래프 카테고리별 평균
boxplot     분포 이상치 확인
heatmap     색상으로 상관관계

설치 방법
pip install seaborn
'''
import os

import seaborn as sns
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프로 확인할 데이터셋 선택
# df = sns.load_dataset("tips")
# seaborn 회사에 tips.csv 와 같은 형태로 데이터가 csv 형태로 보관되어 있는 데이터를
# seborn 회사에서 .csv 없이 사용할 수 있도록 코딩 세팅을 해놓았기 때문에
# tips 라는 명칭으로 가볍게 우리가 seaborn 테스트 할 수 있는 것
df = sns.load_dataset("tips")


def 판다스를_이용하여_데이터구조확인():
    print(df.head())
    print("==" * 80)
    print(df.shape)
    print("==" * 80)
    print(df.columns)
    print("==" * 80)
    print(df.dtypes)
    print("==" * 80)
    print(df.describe())


# 판다스를_이용하여_데이터구조확인()
def 맷플로립을_이용하여_데이터눈으로확인():
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
    plt.title("계산서 vs 팁")
    plt.show()


def seaborn에서_만든데이터_나의컴퓨터에_판다스로_csv_저장하기():
    df.to_csv("seaborn_tips.csv", index=False, encoding="utf-8-sig")
    print("seaborn 에서 만든 데이터 csv 로 저장 완료")


def seaborn_dataset_all_save():
    저장할폴더 = "seaborn_data"
    os.makedirs(저장할폴더,exist_ok=True)

    # 폴더 없으면 자동 생성
    dataset = ["tips", "titanic", "iris", "penguins", "flights", "diamonds", "mpg"]
    for name in dataset:
        df_2 = sns.load_dataset(name)
        df_2.to_csv(f"{저장할폴더}/seaborn_{name}.csv",index=False,encoding="utf-8-sig")
        print(f"seaborn_{name}.csv 저장완료")
    # for 문을 이용해서 데이터셋 모두 저장하기

seaborn_dataset_all_save()

    # 저장할 때 마다 seaborn_{name}.csv 저장완료 표기

# seaborn에서_만든데이터_나의컴퓨터에_판다스로_csv_저장하기()
