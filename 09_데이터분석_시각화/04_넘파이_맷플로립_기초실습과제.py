import matplotlib.pyplot as plt
import numpy as np

days = np.array([1, 2, 3, 4, 5, 6, 7])
temp = np.array([18, 21, 19, 25, 27, 23, 20])

# todo_1: days를 x축, temp를 y축으로 꺾은선 그래프를 그리세요
plt.plot(days, temp)
# todo_2: 그래프 제목을 "일별 기온 변화"로 설정하세요
plt.title("일별 기온 변화")
# todo_3: x축 이름을 "날짜", y축 이름을 "기온(°C)"으로 설정하세요
plt.xlabel("날짜")
plt.ylabel("기온")
# todo_4: 그래프를 화면에 출력하세요
plt.show()

subjects = ["수학", "영어", "과학", "국어", "역사"]
scores = [85, 92, 78, 88, 74]

# todo_1: subjects를 x축, scores를 y축으로 막대 그래프를 그리세요
plt.bar(subjects, scores)
# todo_2: 그래프 제목을 "과목별 점수"로 설정하세요
plt.title("과목별 점수")
# todo_3: y축 범위를 0부터 100으로 설정하세요
plt.ylim(0, 100)
# todo_4: 그래프를 화면에 출력하세요
plt.show()

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
test_scores = np.array([50, 55, 65, 70, 75, 85, 88, 95])

# todo_1: study_hours를 x축, test_scores를 y축으로 산점도를 그리세요
plt.hist(study_hours, test_scores)
# todo_2: 그래프 제목을 "공부 시간과 시험 점수의 관계"로 설정하세요
plt.title("공부 시간과 시험 점수의 관계")
# todo_3: x축 이름을 "공부 시간(시간)", y축 이름을 "시험 점수"로 설정하세요
plt.xlabel("공부시간(시간)")
plt.ylabel("시험점수")
# todo_4: 그래프를 화면에 출력하세요
plt.show()
scores = np.array([55, 60, 62, 68, 70, 71, 73, 75, 75, 78,
                   80, 81, 83, 85, 85, 87, 88, 90, 92, 95])

# todo_1: scores 데이터로 히스토그램을 그리세요
# todo_2: 구간 개수(bins)를 5로 설정하세요
plt.hist(scores, bins=5)
# todo_3: 그래프 제목을 "점수 분포"로 설정하세요
plt.title("점수 분포")
# todo_4: x축 이름을 "점수", y축 이름을 "학생 수"로 설정하세요
plt.xlabel("점수")
plt.xlabel("학생 수")
# todo_5: 그래프를 화면에 출력하세요
plt.show()

months = np.array([1, 2, 3, 4, 5, 6])
revenue = np.array([200, 220, 250, 210, 270, 300])
expenses = np.array([150, 160, 180, 170, 190, 200])

# todo_1: plt.subplots()를 사용해 그래프 2개를 가로로 나란히 배치하세요
fig, (ax1, ax2) = plt.subplots(1, 2)
# todo_2: 왼쪽 그래프에 revenue를 막대 그래프로 그리고 제목을 "월별 매출"로 설정하세요
ax1.bar(months, revenue)
ax1.set_title("월별 매출")
# todo_3: 오른쪽 그래프에 expenses를 꺾은선 그래프로 그리고 제목을 "월별 지출"로 설정하세요
ax1.plot(months, expenses)
ax1.set_title("월별 지출")
# todo_4: 두 그래프 모두 x축 이름을 "월", y축 이름을 "금액(만원)"으로 설정하세요
ax1.set_xlabel("월")
ax1.set_ylabel("금액(만원)")
ax2.set_xlabel("월")
ax2.set_ylabel("금액(만원)")
# todo_5: 그래프를 화면에 출력하세요
plt.show()
