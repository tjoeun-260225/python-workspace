'''
for - 끝이 정해져 있는 반복문
while - 끝이 정해져 있지 않은 반복문 에서 주로 사용

range() - 숫자 범위 만들기
몇 번 반복할지 숫자 범위를 만들어주는 것

range() 구조

range(시작숫자, 끝나는숫자+1, 증가값)

range(5) -> 0부터 5-1 4까지 반복

range(1,6) -> 1부터 6-1 까지 반복

range(0, 10, 2) -> 0 번 부터 + 2씩 증가해서 9까지 반복

range(10, 0, -1) -> 10번 부터 -1 씩 거꾸로 0이 되기 전까지 반복 10 ~ 1까지 반복


for 숫자하나 in  range(시작숫자, 끝나는숫자+1):
    print(숫자하나)

break    = 반복을 완전 종료
continue = 건너 뛰고 계속 진행
'''


def 기본for문():
    for 숫자하나 in range(5):
        print(숫자하나)


# 기본for문()


def 시작_끝_for문():
    for i in range(1, 6):
        print(i)
    # 1부터 5까지 출력하는 for문 만들기 변수이름 = i


def 시작_끝_2씩_증가_for문():
    for i in range(0, 10, 2):
        print(i)
    # 0부터 9까지 2씩 증가하는 for문 만들기 변수이름 = i


def break_5에서_멈추는_for문():
    for i in range(0, 10):
        if i == 5:
            break
        print(i)
    # 0 ~ 9 까지 출력 5를 만나면 break 변수이름 = i


def contiue_8에서_멈추는_for문():
    for i in range(0, 10):
        if i == 8:
            continue
    print(i)


# 0 ~ 9 까지 출력 8을 만나면 출력하지 않고 건너뛰어 계속 진행하는 변수이름 = i

def 구구단():
    단 = int(input("단수를 입력하세요 : ")) # str -> int
    for i in range(1, 10):
        print(f"{단} X {i} = {단*i}")

'''
리스트 목록 순회하기
목록들 = ["포도", '신발', 100, '안녕' , True]

for i in 목록들 : 
    print(i)

'''

def 과일들():
    과일리스트 = ["사과", "바나나","포도"]
    for 과일 in 과일리스트:
        print(과일)
#과일들()

def 코드들():
    언어_리스트 = ["C","Java", "Python", "HTML", "CSS", "JavaScript"]
    for 언어 in 언어_리스트:
        print(언어)

#코드들()


'''
파일 이름을 입력하세요: 오늘일기
확장자를 입력하세요 (txt, py, csv): txt
입력하세요 (exit 종료): 오늘 파이썬 공부했다
입력하세요 (exit 종료): 재미있었다
입력하세요 (exit 종료): exit
오늘일기.txt 작성 완료

'''
def 파일만들기():
    파일이름 = input("파일 이름을 입력하세요 : ")
    확장자 = input("확장자를 입력하세요(txt,py,csv) : ")
    전체파일이름 = 파일이름+"."+확장자

    with open(전체파일이름, "w",encoding="utf-8") as file :
        while True:
            text = input("입력하세요(exit 종료) : ")
            if text.lower() == "exit":
                print(f"{전체파일이름}작성 완료")
                break
            file.write(text+"\n")
#파일만들기()


def 파일읽기():
    with open("오늘일기.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
파일읽기()