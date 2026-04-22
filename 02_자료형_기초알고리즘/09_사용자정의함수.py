'''
파이썬 함수 = 기능 기본 내장 함수 vs 사용자 정의 함수
기본 내장 함수 = 파이썬 개발자들이 처음부터 제공하는 기능들
사용자 정의 함수 = 회사 부서 개발자가 재사용하거나 코드를 관리하기 위해 키워드로 직접 만드는 기능
def = 기능만들기 시작하겠다.
'''
# print("hello") # 출력
len([1, 2, 3])  # 길이를 반환하는 것
# def len(매개변수ok):
#     return  리스트 안에 있는 데이터 총 개수 반환
sum([1, 2, 3])  # 총 합을 반환하는 것
type(42)  # 타입 반환 <class 'int'>


# 사용자 정의 함수 - def 로 직접 만들어야 사용 가능
def 인사기능(이름):
    print(f"안녕하세요 {이름}님!")


# 인사기능("철수")

##### return 의 유무 차이
###   return 이 없는 함수(=기능)
def say_hello():
    print("안녕!!!")  # 출력만 하고 끝이다.


결과1번 = say_hello()  # 실행은 된다.
print(결과1번)  # None 나는 결과1번에서 return 으로 받은 데이터가 없다!!!! NoneNoneNone


###   return 이 있는 함수(=기능)
def 더하기기능(a, b):
    return a + b  # 값을 반환해줌


결과2번 = 더하기기능(3, 5)
print(결과2번)  # 값을 전달받아 출력 가능한 상태


### 매개변수(parameter) 종류
## 1. 기본값이 존재하는 매개변수
def greet(name, msg="안녕하세요"):
    print(f"{msg}, {name}님!")


greet("철수")  # 안녕하세요,  철수님! 기본 msg 사용
greet("영희", "반갑습니다.")  # 반갑습니다., 영희님! 매개변수로 추가된 msg 사용


# greet("영희", "반갑습니다.","ㅎㅎ")      # 매개변수 데이터로 존재하지 않는 데이터는 작성 불가

## 2. 키워드 인수
def profile(name, age, city):
    print(f"{name} / {age}세 / {city}")


profile(age=25, city="서울", name='민수')  # 순서 상관 없이 매개변수 이름에 맞춰서 데이터 전달할 수 있다.

## 3. 가변 인수
#    *args : 개수   제한 없이    받기 (튜 플 로 들어옴) 튜플은 받아온 값을 수정할 수 없다.
# 데이터를 받아올 것인데 개수 제한을 하고싶지 않을 때 사용
def 총합(*args):
    return sum(args)
print(총합(1,2,3,4,5))

# **kwargs : 키워드 인수 여러 개 받기 (딕셔너리 들어옴) { "키이름":"데이터"}
def 정보(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
정보(name="철수",age=20, city="부산")