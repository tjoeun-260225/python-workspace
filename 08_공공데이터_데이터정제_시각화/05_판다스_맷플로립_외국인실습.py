import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 설정 2줄을 작성하시오. (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("국토교통부_외국인 조종사 국적별 현황_20250331.csv", encoding="cp949")
# 항공사 컬럼만 추출 (국적 컬럼 제외)
#국적	대한항공	아시아나항공	에어부산	이스타항공	제주항공	진에어	티웨이	에어서울	에어로케이	에어프레미아	에어제타

#항공사목록 = df.columns[0:]        # 국적부터 에어제타 모두 갖고오기
항공사목록 = df.columns[1:]        # 국적빼고 모든 컬럼 갖고오기
항공사별_합계 = df[항공사목록].sum()  # TODO: 각 항공사별 전체 합계를 구하시오.

plt.bar(항공사별_합계.index, 항공사별_합계.values)                    # TODO: x축 항공사명, y축 합계로 막대그래프를 그리시오.
plt.title("항공사별 외국인 조종사 수")                        # TODO: 적절한 제목을 작성하시오.
plt.xlabel("항공사")
plt.ylabel("조종사 수")
plt.xticks(rotation=45)             # TODO: X축 글자가 겹치지 않게 기울이시오.
plt.tight_layout()
plt.savefig("항공사별 외국인 조종사 수.png")
plt.show()

# 대한항공 조종사가 1명 이상인 국적만 필터링
df_대한항공 = df[df['대한항공'] >= 1]

plt.pie(df_대한항공['대한항공'], labels=df_대한항공['국적'], autopct="%1.1f%%")
plt.title("대한항공 외국인 조종사 국적 비율")
plt.savefig("대한항공 외국인 조종사 국적 비율.png")
plt.show()

# 각 국적별로 전체 항공사 합계 구하기
df['전체합계'] = df[df.columns[1:]].sum(axis=1) #가로로 더해서 국적마다 전체 항공사 합계 구하기
# TODO: 각 행(국적)의 합계를 구해 '전체합계' 컬럼에 저장하시오.
# axis=1 이면 행 방향(가로) 합계

# 전체합계가 0보다 큰 국적만 필터링
df_합계 = df[df['전체합계'] > 0]

plt.barh(df_합계['국적'], df_합계['전체합계'])  # TODO: y축 국적, x축 전체합계
plt.title("국적별 항공사 전체 외국인 조종사 수")
plt.xlabel("각 항공사 조종사 수")
plt.tight_layout()
plt.savefig("국적별 항공사 전체 외국인 조종사 수.png")
plt.show()

plt.hist(df['대한항공'], bins=10)   # TODO: 대한항공 컬럼, 구간 10개
plt.title('대한항공 국적별 조종사 수 분포')
plt.xlabel("조종사 수")
plt.ylabel("국적 수")
plt.savefig("대한항공 국적별 조종사 수 분포.png")
plt.show()
#plt.savefig("아무것도 없는 이미지.png")

# df['전체합계'] = df[df.columns[1:]].sum(axis=1)
# sum 안에 axis 가 없으면 기본값은 axis = 0 이다.
# 만약에 sum() 안에 아무것도 없으면 세로로 더하기 진행한다는 의미
항공사별_합계 = df[df.columns[1:]].sum()  # == df[df.columns[1:]].sum(axis = 0)

plt.bar(항공사별_합계.index, 항공사별_합계.values)
plt.title("항공사별 외국인 조종사 수")
plt.xticks(rotation=45)
plt.tight_layout()
# save 를 할 생각을 했을까
plt.savefig("외국인조종사_차트.png")    # TODO: "외국인조종사_차트.png" 로 저장하시오.
plt.show()