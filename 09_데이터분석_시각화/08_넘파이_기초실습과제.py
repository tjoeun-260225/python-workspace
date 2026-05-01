import numpy as np


def 배열만들기():
    print(np.zeros(6))
    print(np.ones(5))
    print(np.arange(0, 31, 5))
    print(np.linspace(0, 1, 8))


def 배열연산():
    a = np.array([10, 30, 50])
    b = np.array([2, 3, 5])
    # 1. a와 b를 더한 결과를 출력하세요
    print(a + b)
    # 2. a에서 b를 뺀 결과를 출력하세요
    print(a - b)
    # 3. a와 b를 곱한 결과를 출력하세요
    print(a * b)
    # 4. a를 b로 나눈 결과를 출력하세요
    print(a / b)
    # 5. 일반 파이썬 리스트 [10, 30, 50] + [2, 3, 5] 를 출력하고,
    print([10, 30, 50] + [2, 3, 5])
    print(a + b)
    # NumPy 결과와 어떻게 다른지 주석으로 작성하세요
    # 파이썬 리스트 : 두 리스트를 이어 붙인 결과
    # NumPy 배열 같은 인덱스끼리 덧셈 수행


def 인덱싱_슬라이싱_필터링():
    a = np.array([10, 20, 30, 40, 50, 60, 70])

    # 1. 첫 번째 값을 출력하세요
    print(a[0])
    # 2. 마지막 값을 출력하세요
    print(a[-1])
    # 3. 인덱스 2번부터 5번까지 슬라이싱해서 출력하세요
    print(a[2:6])
    # 4. 40보다 큰 값만 필터링해서 출력하세요
    print(a[a > 40])
    # 5. 20으로 나누어 떨어지는 값만 필터링해서 출력하세요
    # / 몫.나머지 // 몫   % 나머지
    print(a[a % 20 == 0])


def 통계함수():
    scores = np.array([70, 85, 90, 55, 78, 92, 63, 88])

    # 1. 점수의 총합을 출력하세요
    print(np.sum(scores))
    # 2. 가장 높은 점수를 출력하세요
    print(np.max(scores))
    # 3. 가장 낮은 점수를 출력하세요
    print(np.min(scores))
    # 4. 평균 점수를 출력하세요
    print(np.mean(scores))
    # 5. 표준편차를 출력하세요
    print(np.std(scores))
    # 6. 중앙값을 출력하세요
    print(np.median(scores))


# ctrl + / 전체 주석이 되고 전체 주석이 해지된다.
def 카페매출분석():
    # 아래 배열은 8일간 카페 아메리카노 판매량입니다.

    sales = np.array([30, 15, 42, 27, 38, 19, 50, 33])
    # 넘파이회사에서 만든 기능들 중에서.총더하기기능을사용(모두 더할 리스트가 들어있는 공간의 명칭)
    # np                              .      sum        (sales)
    # 1. 총 판매량을 출력하세요
    print("1. 총 판매량 : ", np.sum(sales), "잔")
    # 2. 하루 평균 판매량을 출력하세요
    print("2. 하루 평균 판매량 : ", np.mean(sales), "잔")
    # 3. 가장 많이 팔린 날과 가장 적게 팔린 날의 판매량을 출력하세요
    print("3. 가장 많이 팔린 날 : ", np.max(sales), "잔")
    print("   가장 적게 팔린 날 : ", np.min(sales), "잔")
    # 4. 평균보다 많이 팔린 날의 판매량만 필터링해서 출력하세요
    print("4. 평균 초과 판매량 : ", sales[sales > np.mean(sales)])
    # 5. 아메리카노 한 잔 가격이 4500원일 때,
    # 각 날짜별 매출 금액 배열을 만들고 출력하세요
    print("5. 날짜별 매출 금액 (한잔 = 4500) : ", sales * 4500)
