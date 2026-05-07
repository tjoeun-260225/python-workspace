import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
'''
SYLLABLE RO}) missing from font(s) Arial.
  self.print_png(buf)

국적별 매출파일처럼 한글 데이터가 그래프 상호에 직접적으로 들어가있어서 깨지는 경우
폰트의 위치를 직접적으로 가져와서 세팅
Malgun Gothic
'''
plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False

sns.set_theme(style='whitegrid')
sns.set_palette('pastel')

df = pd.read_csv('제주국제자유도시개발센터_JDC지정면세점_국적별 매출 정보_20241231.csv', encoding='euc-kr')

# =============================================
# TODO 1
# 컬럼 이름과 shape 를 출력하세요.
# =============================================
print(df.columns)
print(df.shape)

# =============================================
# TODO 2
# 국적 열에 어떤 값들이 있는지 확인하세요.
# 힌트 : value_counts()
# =============================================
print(df['국적'].value_counts())

# =============================================
# TODO 3
# 국적별 매출 합계를 내림차순으로 출력하세요.
# 힌트 : groupby → sum → sort_values
# =============================================
국적별 = df.groupby('국적')['매출'].sum().sort_values(ascending=False)
print(국적별)

# =============================================
# TODO 4
# 국적별 매출 합계를 막대 그래프로 그리세요.
# 제목은 '국적별 연간 매출'
# =============================================
plt.bar(국적별.index, 국적별.values)
plt.title('국적별 연간 매출')
plt.xticks(rotation=45)
plt.show()

# =============================================
# TODO 5
# 내국인 데이터만 필터링하고
# 월별 매출을 꺾은선 그래프로 그리세요.
# 제목은 '내국인 월별 매출'
# =============================================
내국인 = df[df['국적'] == '내국인']
plt.plot(내국인['판매년월'], 내국인['매출'])
plt.title('내국인 월별 매출')
plt.xticks(rotation=45)
plt.show()

# =============================================
# TODO 6
# 내국인 제외하고 외국인 데이터만 필터링하세요.
# 힌트 : df[df[???] != ???]
# =============================================
외국인 = df[df['국적'] != '내국인']

# =============================================
# TODO 7
# 외국인 국적별 매출 합계를 구하고
# 가로 막대 그래프로 그리세요. (barh)
# 제목은 '외국인 국적별 매출'
# =============================================
외국인별 = 외국인.groupby('국적')['매출'].sum().sort_values(ascending=True)
plt.barh(외국인별.index, 외국인별.values)
plt.title('외국인 국적별 매출')
plt.show()

# =============================================
# TODO 8
# 월별 전체 매출 합계를 구하고
# 가장 많이 팔린 달을 출력하세요.
# 힌트 : groupby → sum → idxmax()
# =============================================
월별 = df.groupby('판매년월')['매출'].sum()
print('매출 1위 월 :', 월별.idxmax())
'''
메서드
.idxmax()
index max 의 줄임말
최댓값을 가진 인덱스(라벨) 반환
최고의 데이터의 라벨을 반환한다.
'''

# =============================================
# TODO 9
# 국적별 매출 분포를 boxplot 으로 그리세요.
# x='국적', y='매출'
# 제목은 '국적별 매출 분포'
# =============================================
sns.boxplot(x='국적', y='매출', data=df)
plt.title('국적별 매출 분포')
plt.xticks(rotation=45)
plt.show()

# =============================================
# TODO 10
# 1행 2열 서브플롯으로
# 왼쪽 = TODO 4 국적별 막대 그래프
# 오른쪽 = TODO 7 외국인 가로 막대 그래프
# =============================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(국적별.index, 국적별.values)
axes[0].set_title('국적별 막대 그래프')
axes[0].tick_params(axis='x', rotation=45)

axes[1].barh(외국인별.index, 외국인별.values)
axes[1].set_title('외국인 가로 막대 그래프')

plt.tight_layout()
plt.show()
