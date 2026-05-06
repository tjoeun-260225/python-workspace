def 문제1():
    price = 15000
    print(f"{price:,}")
    # price 를 천 단위 쉼표로 출력하세요.
    # 출력 결과: 15,000


def 문제2():
    rate = 0.875
    print(f"{rate:.2f}")
    # rate 를 소수점 둘째 자리까지 출력하세요.
    # 출력 결과: 0.88


def 문제3():
    rate = 0.875
    print(f"{rate:.1%}")
    # rate 를 퍼센트로, 소수점 첫째 자리까지 출력하세요.
    # 출력 결과: 87.5%


def 문제4():
    num = 42
    print(f"{num:7d}")
    # num 을 7칸 확보해서 오른쪽 정렬로 출력하세요.
    # 출력 결과: '     42'


def 문제5():
    num = 42
    print(f"{num:06d}")
    # num 앞을 0으로 채워서 6자리로 출력하세요.
    # 출력 결과: 000042


def 문제6():
    name = "Kim"
    print(f"{name:10s}")
    # name 을 10칸 확보해서 왼쪽 정렬로 출력하세요.
    # 출력 결과: 'Kim       '
