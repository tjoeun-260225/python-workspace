def problem1():
    과일들 = ["사과", "바나나", "포도"]
    print(len(과일들))


def multiply(a, b):
    return a * b


result = multiply(6, 7)
print(f"6 곱하기 7은 {result}입니다.")


def welcome(name):
    print(f"{name}님, 환영합니다!")


result = welcome("철수")
print(result)  # return 이 없는 함수의 반환값은 None


def average(a, b, c):
    return (a + b + c) / 3


result = average(10, 20, 30)
print(f"10 20 30 의 평균은 {result}입니다.")


def say_hi(name, greeting="좋은 하루에요"):
    print(f"{greeting}, {name}님!")


say_hi("지수")
say_hi("민준", "오랜만이에요.")


def order(menu, size, temperature):
    print(f"{temperature} {size} {menu} 주문 완료!")


order(size="라지", temperature="아이스", menu="아메리카노")


def is_even(n):
    return n % 2 == 0


print(f"4는 짝수입니다:{is_even(4)}")
print(f"7은 홀수입니다:{is_even(7)}")


# 기본값이 있는 매개변수가 () 안에 존재할 경우에는 반드시 기본값 없는 매개변수 뒤에 위치하고,
# 매개변수 안에서 기본값이 없는 매개변수들이 맨 앞으로 위치해야 한다.
def introduce(name, age=20, city="서울"):
    print(f"{name} / {age}세 / {city}")


def profile(name, age):
    print(f"이름:{name} / 나이 : {age}세")


profile(age=23, name="하은")


def add(a, b):
    return a + b


def show(n):
    print(f"결과는 {n} 입니다")


show(add(7, 8))
print(add(7, 8))
