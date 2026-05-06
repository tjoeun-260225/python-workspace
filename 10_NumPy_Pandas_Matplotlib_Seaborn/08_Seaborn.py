import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'D2Coding'  # 나의 컴퓨터에 없는폰트는 지원 안됨 □□□□ 형식으로 나옴
plt.rcParams['axes.unicode_minus'] = False
# 글꼴 깨짐 방지나 스타일은 보통 import 나 from 아래 작성

# seaborn 스타일 꾸미기
sns.set_theme(style='whitegrid') # 아주깔끔한 흰배경
sns.set_palette('pastel')



# seaborn에 존재하는 데이터 갖고오기
# 식당팁 데이터 # seaborn 에 접속해서 데이터 파악

# 샘플 데이터(seaborn 내장)
df = sns.load_dataset('tips') # = pd.read_scv("seaborn에서_만든_데이터셋.csv")

# 분포보기
sns.histplot(df['total_bill'], kde=True) # kde=True 하면 곡선도 같이
plt.show()
# 두 변수의 상관관계
sns.scatterplot(x='total_bill', y='tip',data=df)
plt.show()
# 카테고리별 비교
sns.boxplot(x='day', y='total_bill',data=df)
plt.show()
