'''
pip install numpy

import numpy as np # np 는 numpy 이름이 너무 길어서 np로 줄여서 작성하겠다.
'''

import numpy as np


def 기본넘파이기능():
    # 일반 파이썬 숫자 목록
    기본파이썬 = [1, 2, 3, 4, 5]
    # np 로 만들어진 array = 배열이다.
    넘파이 = np.array([1, 2, 3, 4, 5])

    print(type(기본파이썬))  # <class 'list'>
    print(type(넘파이))  # <class 'numpy.ndarray'>

    # Numpy 로 자주 사용하는 배열 생성 방법
    영_5개 = np.zeros(5)  # [0. 0. 0. 0. 0.]          원하는 개수만큼 0만 있는 목록 만들 때 사용
    일_5개 = np.ones(5)  # [1. 1. 1. 1. 1.]          원하는 개수만큼 1만 있는 목록 만들 때 사용
    이_5개 = np.arange(0, 10, 2)  # [0 2 4 6 8]                0부터 10-1 까지 2씩 건너뛰어 생성
    균등간격_5개 = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ] 실수형태로 0부터 1까지 n만큼 균등하게 생성

    print(영_5개)
    print(일_5개)
    print(이_5개)
    print(균등간격_5개)


def 파이썬과넘파이_연산비교():
    a_python = [1, 2, 3]
    b_python = [4, 5, 6]

    # 일반파이썬은 더하기가 이어붙이기 이어붙이는 것은 가능하지만 셈 계산 안됨
    print(a_python + b_python)  # [1, 2, 3, 4, 5, 6]

    # NumPy 수학적 연산
    a_numpy = np.array([1, 2, 3])
    b_numpy = np.array([4, 5, 6])

    더하기 = a_numpy + b_numpy
    빼기 = a_numpy - b_numpy
    곱하기 = a_numpy * b_numpy
    나누기 = a_numpy / b_numpy

    print("넘파이 더하기 : ", 더하기)  # 넘파이 더하기 :  [5 7 9]
    print("넘파이 빼기 : ", 빼기)  # 넘파이 빼기 :  [-3 -3 -3]
    print("넘파이 곱하기 : ", 곱하기)  # 넘파이 곱하기 :  [ 4 10 18]
    print("넘파이 나누기 : ", 나누기)  # 넘파이 나누기 :  [0.25 0.4  0.5 ]


def for문연산비교():
    a_python = [1, 2, 3]
    # 일반 for 문
    for i in a_python:
        print(i * 2)

    # 리스트 컴프리핸션
    #      결과 for 과정
    print([i * 2 for i in a_python])

    # 리스트 연산을 마치 기본 연산처럼 다룰 수 있게 기능 특화되어 있는 라이브러리
    a_numpy = np.array([1, 2, 3])
    print(a_numpy * 2)


# 기본 파이썬과 비교없이 넘파이 기능만 작성
def 인덱싱_슬라이싱():
    a = np.array([10, 20, 30, 40, 50])

    # 기본 인덱싱(파이썬 리스트랑 동일)
    print("a[0] : ", a[0])  # a[0]           :  10
    print("a[-1] : ", a[-1])  # a[-1]          :  50
    print("a[1:3] : ", a[1:3])  # a[1:3]         :  [20 30]
    # 조건 필터링 NumPy 만의 기능
    # a > 25       [10, 20, 30, 40, 50] 에서 25 보다 큰 숫자만 걸러내어 a 안에 담아두겠다.
    print("a[a > 25] : ", a[a > 25])  # a[a > 25]      :  [30 40 50]
    # a % 20 == 0   [10, 20, 30, 40, 50] 에서  20으로 나누어 떨어지는 숫자만 a 안에 담아두겠다.
    print("a[a % 20 == 0] : ", a[a % 20 == 0])  # a[a % 20 == 0] :  [20 40]


def 조건필터비교():
    a_numpy = np.array([10, 20, 30, 40, 50])
    넘파이_필터처리 = a_numpy[a_numpy > 10]  # 위 리스트에서 10보다 큰 수만 남게된다.

    # 일반 파이썬 필터처리
    a_python = [10, 20, 30, 40, 50]
    for i in a_python:
        if i > 10:
            print("10보다 큰 숫자들 : ", i)

    # 일반 파이썬 컴프리핸션
    #     결과        작업과정       작업과정 중 지켜야할 조건
    # [    i     for i in a_python          if i > 10          ]
    [i for i in a_python if i > 10]


def 넘파이_유용한_통계함수():
    a = np.array(([1, 2, 3, 4, 5]))

    np.sum(a)      # 리스트 내 총 합
    np.max(a)      # 리스트에서 제일 큰 값
    np.min(a)     # 리스트에서 제일 작은 값
    np.mean(a)    # 평균
    np.std(a)     # 표준 편차
    np.median(a)  # 중앙값


넘파이_유용한_통계함수()
