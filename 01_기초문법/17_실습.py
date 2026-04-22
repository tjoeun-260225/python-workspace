def 문제1():
    # 일반 for문
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    print(numbers)
    # [1, 2, 3, 4, 5]

    # list comprehension 으로 바꾸기
    numbers = [i for i in range(1, 6)]
    print(numbers)

def 문제2():
    # 일반 for문
    squares = []
    for i in range(1, 6):
        squares.append(i ** 2)
    print(squares)
    squares = [i ** 2 for i in range(1, 6)]
    print(squares)

def 문제3():
    # 일반 for문
    even = []
    for i in range(1, 11):
        if i % 2 == 0:
            even.append(i)
    print(even)
    # [2, 4, 6, 8, 10]

    # list comprehension 으로 바꾸기
    even = [i for i in range(1, 11) if i % 2 == 0]
    print(even)

def 문제4():
    # 일반 for문
    fruits = ["사과", "바나나", "포도"]
    result = []
    for fruit in fruits:
        result.append(fruit + "맛있다")
    print(result)
    # ['사과맛있다', '바나나맛있다', '포도맛있다']

    # list comprehension 으로 바꾸기
    result = [fruit + "맛있다" for fruit in fruits]
    print(result)