### 1. print() 출력하기  , sep end 조합   f-string 조합
def 프린트기능():
    print("안녕하세요")
    name = "김철수"
    print("안녕하세요!", name, "님!")
    print("안녕하세요!", name, "님!", sep="~~~")
    print("안녕하세요!", name, "님!", sep="~~~", end="끝입니다.")
    print(f"안녕하세요! {name}님! ~~")
### 2. input() 사용자의 키보드 입력을 받는 기능
## 키보드로 입력받은 데이터를 특정 변수 공간에 저장하여 사용
## 컴퓨터는 코드를 한 줄 씩 실행할 때 마다 실행하고 실행한 데이터를 소멸하기 때문에
#  변수 공간에 담아서 보관한다.
#  input 의 경우 소비자가 어떤 데이터를 작성할지 모르기 때문에 무조건 String 으로 데이터를 가져온다.
#  가져온 데이터를 개발자가 원하는 형식에 맞추어 데이터 작업
#  숫자입력 -> 크기 비교 or 연산을 해야할 경우 int("숫자") 를 사용해서 변환 처리를 해야한다.
def input_int_try기능():
    소비자입력데이터 = input("이름을 입력하세요 : ")
    while True:
        try:
            소비자숫자데이터 = int(input("나이를 입력하세요 : "))
            print(f"{소비자입력데이터}님의 나이는 {소비자숫자데이터} 입니다.")
            break
        except ValueError:
            print("숫자 데이터만 작성할 수 있습니다. (예 : 20) ")
        except:
            print("예기치 못한 문제가 발생했습니다. 다시 시도해주세요.")
'''
ValueError: invalid literal for int() with base 10: '스무살'
이러한 에러를 해결하기 위해서는 try: except: 를 사용한다.
try:
    실행할코드
except ValueError:
    ValueError = 숫자데이터가 아닌 글자가 들어왔을 때 개발자가 진행해야할 안내 코드나 멘트 작성
except: 개발자가 인지하지 못한 것을 포함하여 모든 오류 처리
    오류났을 때 코드
'''

'''
for 문은 종류가 굉장히 많다.
for   하나씩_데이터를_꺼내와서_사용할_변수이름    in   순회할_것들 :
     순회하면서 진행할 코드 작업들 작성
     
숫자 순회 range

for 숫자데이터 in range(5):        0 에서 부터 4까지 순회
    print(숫자데이터)

for 숫자데이터 in range(1, 6):     1 에서 부터 5까지 순회
    print(숫자데이터)

for 숫자데이터 in range(0, 10, 2): 0 에서 부터 9까지 순회하는데 2씩 증가하여 출력
    print(숫자데이터)
    
for 숫자데이터 in range(5, 0, -1): 5에서 부터 -1 씩 감소하여 0이 되기 직전인 1까지만 순회
    print(숫자데이터)
    
목록 순회

목록들 = ["일",2,'삼',4,True]
for 목록데이터 in 목록들:     목록에 들어있는 데이터를 0번 부터 순차적으로 꺼내와 모두 작업
    print(목록데이터)

문자열 순회

for 글자데이터 in "안녕하세요":   글자를 하나씩 꺼내서 무언가를 하겠다.
    print(글자데이터)
    
번호 붙이며 순회
목록들 = ["일",2,'삼',4,True]
for 번호매김,목록데이터 in enumerate(목록들, start=1):  목록에 있는 데이터에 1부터 번호를 매겨 작업
    print(f"{번호매김}번: {목록데이터})                 start 를 생략하면 0번부터 번호매김을 진행

두 목록을 동시 순회
이름들 = ["홍길동", "김철수", "이영희"]
점수들 = [90, 80, 70]

for 이름, 점수 in zip(이름들, 점수들):   목록 순회는 개수 제한 없다. for 다음 순서와 zip 다음 순서만 맞으면 된다.
    print(f"{이름}: {점수}점")

딕셔너리 순회
사람 = {"이름" : "홍길동", "나이", : 25, "키",175.5}

# 키 데이터만
for key in 사람:
    print(key)

# 값 데이터만
for value in 사람:
    print(value)
    
# 키 + 값 데이터만
for key, value in 사람.items():
    print(key, value)
    
    
한줄로 순회 만들기

for - else 정상 종료시 실행
'''
def 기본for문():
    숫자들 = []
    for 숫자하나 in range(1,6):
        숫자들.append(숫자하나)
    print(숫자들)
# 기본for문()

def 한줄for문():
    숫자들 = [숫자하나 for 숫자하나 in range(1,6)]
    print(숫자들)
한줄for문()

def forelse():
    for i in range(5):
        print(i)
    else:
        print("반복 완료") # for 안에서 break 없이 끝나면 실행



'''
def ifelse():
    if 조건1:
        # 조건 1이 True 일 때 수행할 구문
    elif 조건2:
        # 조건 1이 False 이고 조건 2가 True 일 때 수행할 구문
    elif 조건3:
        # 조건 1&2가 False 이고 조건 3이 True 일 때 수행할 구문
    else :
        # 위 조건이 모두 False 일 때 수행할 구문
'''
