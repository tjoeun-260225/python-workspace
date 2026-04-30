import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 설정 2줄을 작성하시오. (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv("경찰청_범죄 발생 지역별 통계_20241231.csv", encoding="cp949")

# 강력범죄만 필터링
df_강력 = df[df['범죄대분류'] == '강력범죄']

plt.bar(df_강력['범죄중분류'], df_강력['서울 강남구'])  # TODO: x축 범죄중분류, y축 서울 강남구
plt.title("강남구 강력범죄 현황")                         # TODO: 적절한 제목 작성
plt.xlabel('범죄 종류')
plt.ylabel('발생 건수')
plt.xticks(rotation=45)              # TODO: X축 글자 겹치지 않게 기울이기
plt.tight_layout()
plt.show()

df_강력 = df[df['범죄대분류'] == '강력범죄']

plt.pie(df_강력['서울 강남구'], labels=df_강력['범죄중분류'], autopct="%1.1f%%")
plt.title("강남구 강력범죄 종류별 비율")
plt.show()

plt.barh(df['범죄중분류'], df['서울 강남구'], label='서울 강남구')  # TODO: y축 범죄중분류, x축 서울 강남구
plt.barh(df['범죄중분류'], df['부산 중구'], label='부산 중구')  # TODO: y축 범죄중분류, x축 부산 중구
plt.title('범죄 종류별 강남구 vs 부산 중구')
plt.xlabel('발생 건수')
plt.legend()       # 범례 표시
plt.tight_layout()
plt.show()

plt.hist(df['서울 강남구'], bins=10)  # TODO: 서울 강남구 컬럼, 구간 10개
plt.title('서울 강남구 범죄 건수 빈도 상관관계')
plt.xlabel("범죄 건수")
plt.ylabel("빈도")
plt.show()

plt.scatter(df['서울 강남구'], df['서울 서초구'], alpha=0.7)
# TODO: x축 서울 강남구, y축 서울 서초구, 투명도 0.7
plt.title('강남구 서초구 범죄 상관관계')
plt.xlabel("서울 강남구")
plt.ylabel("서울 서초구")
plt.show()

df_강력 = df[df['범죄대분류'] == '강력범죄']

plt.bar(df_강력['범죄중분류'], df_강력['서울 강남구'])
plt.title("강남구 강력범죄 현황")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("강남구_강력범죄.png")    # TODO: "강남구_강력범죄.png" 로 저장하시오.
plt.show()