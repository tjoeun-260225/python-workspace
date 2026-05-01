import numpy as np

# todo_1: 0이 7개인 배열을 만들고 출력하세요
print(np.zeros(7))
# todo_2: 1이 4개인 배열을 만들고 출력하세요
print(np.ones(4))
# todo_3: 0부터 20까지 3씩 건너뛰는 배열을 만들고 출력하세요
print(np.arange(0, 21, 3))
# todo_4: 0부터 1까지 균등하게 나눈 값이 6개인 배열을 만들고 출력하세요
print(np.arange(0, 1, 6))

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# todo_1: a와 b를 더한 결과를 출력하세요
print(a + b)
# todo_2: a에서 b를 뺀 결과를 출력하세요
print(a - b)
# todo_3: a와 b를 곱한 결과를 출력하세요
print(a * b)
# todo_4: a를 b로 나눈 결과를 출력하세요
print(a / b)
# todo_5: 일반 파이썬 리스트 [10, 20, 30] + [1, 2, 3] 을 출력하고 NumPy 결과와 어떻게 다른지 주석으로 작성하세요
print([10, 20, 30] + [1, 2, 3])

a = np.array([5, 15, 25, 35, 45, 55])

# todo_1: 첫 번째 값을 출력하세요
print(a[0])
# todo_2: 마지막 값을 출력하세요
print(a[-1])
# todo_3: 인덱스 2번부터 4번까지 슬라이싱해서 출력하세요
print(a[2:5])
# todo_4: 30보다 큰 값만 필터링해서 출력하세요
print(a[a > 30])
# todo_5: 15로 나누어 떨어지는 값만 필터링해서 출력하세요
print(a[a % 15 == 0])

scores = np.array([88, 72, 95, 60, 83, 77, 91, 68])

# todo_1: 점수의 총합을 출력하세요
print(np.sum(scores))
# todo_2: 가장 높은 점수를 출력하세요
print(np.max(scores))
# todo_3: 가장 낮은 점수를 출력하세요
print(np.min(scores))
# todo_4: 평균 점수를 출력하세요
print(np.mean(scores))
# todo_5: 표준편차를 출력하세요
print(np.std(scores))
# todo_6: 중앙값을 출력하세요
print(np.median(scores))

# 아래 배열은 어느 가게의 7일간 일별 매출액(만원)입니다.
sales = np.array([120, 85, 200, 150, 95, 175, 210])

# todo_1: 7일 총 매출을 출력하세요
print(np.sum(sales))

# todo_2: 하루 평균 매출을 출력하세요
print(np.mean(sales))
# todo_3: 가장 높은 매출과 가장 낮은 매출을 출력하세요
print(np.max(sales))
print(np.min(sales))
# todo_4: 평균보다 높은 매출이 발생한 날의 매출액만 필터링해서 출력하세요
print(sales[sales > np.mean(sales)])

# todo_5: 매출에 부가세 10%를 추가한 새로운 배열을 만들고 출력하세요
print(sales * 1.1)
