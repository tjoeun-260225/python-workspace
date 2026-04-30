'''
파이썬에서 그래프/차트를 그리는 라이브러리 데이터를 눈으로 볼 수 있게 해준다.

설치방법 pip install matplotlib
선그래프 막대그래프 파이그래프 산점도
'''

####### 기본 구조
import matplotlib.pyplot as plt

# plot = 선그래프 추세
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("제목")
plt.xlabel("x축")
plt.ylabel("y축")

# bar  = 막대 그래프 비교
plt.bar(["A", "B", "C"], [30, 50, 20])
plt.title("항목별 비교")

# pie  = 원형 그래프 비율
plt.pie([40, 30, 20, 10], ["A", "B", "C", "D"], autopct="%1.1f%%")
plt.title("비율 차트")

# scatter = 산점도 관계 확인할 때
plt.scatter([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("두 변수의 관계")
plt.show()
