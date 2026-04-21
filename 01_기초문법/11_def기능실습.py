'''
def 기능이름(매개변수):      # 기능을 정의내린다.
    실행할 코드              # 동작할 코드들 작성
    실행할 코드
    실행할 코드
    실행할 코드
    실행할 코드
    return 결과값            # 결과 돌려주기 ( 없어도 된다. )

기능이름(매개변수값)

'''
# return 없다면 ??? public          void 기능이름(){}
# return 있다면 ??? public return_자료형 기능이름(){}
# java 와 달리 python 은 기능에 return 여부를 def와 기능이름 사이에 작성하지 않아도 된다.

# def = 나 새로운 기능을 만들기 시작하겠다. 기능이름을 쓰겠다.
#기능만들기 기능이름(매개변수자리)   기능작성시작!
def         인사기능(           )     :
    print("==========")
    print("안녕하세요!")
    print("==========")

# 인사기능()
# 인사기능()
# 인사기능()


def 커피만들기(사이즈):
    print(f"{사이즈} 컵 꺼내기")
    print(f"{사이즈} 원두 넣기")
    print(f"{사이즈} 만큼 물 붓기")

#커피만들기("Large") # 커피만드는 메뉴얼대로 Large 사이즈 커피 만들기 실행
#커피만들기("Small")

def 프로필출력():
    name = "홍길동"
    age = 25
    height = 175.5
    print("====================")
    print(f"이름: {name}")
    print(f"나이: {age}살")
    print(f"키: {height}cm")
    print("====================")

프로필출력()

def 나이계산기():
    name = input("이름을 입력하세요: ")
    birth = int(input("태어난 연도를 입력하세요: "))
    age = 2026 - birth
    print(f"{name}님의 나이는 {age}살 입니다!")

나이계산기()

def 학점계산기():
    score = int(input("점수를 입력하세요: "))
    if score >= 90:
        print("A학점 입니다!")
    elif score >= 80:
        print("B학점 입니다!")
    elif score >= 70:
        print("C학점 입니다!")
    else:
        print("F학점 입니다!")

학점계산기()



def 합계계산기():
    total = 0
    while True:
        num = input("숫자를 입력하세요 (exit 종료): ")
        if num.lower() == "exit":
            break
        total += int(num)
    print(f"합계: {total}")

합계계산기()

def 파일저장():
    with open("result.txt", "w", encoding="utf-8") as file:
        while True:
            text = input("입력하세요 (exit 종료): ")
            if text.lower() == "exit":
                print("저장 완료!")
                break
            file.write(text + "\n")


def 파일읽기():
    count = 1
    with open("result.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if line == "":
                break
            print(f"{count}번째 줄: {line.strip()}")
            count += 1

# 실행
print("=== 파일 저장 ===")
파일저장()
print("\n=== 파일 읽기 ===")
파일읽기()