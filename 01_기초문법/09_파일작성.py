'''
open("파일이름.확장자이름","모드",encoding="utf-8")
- 파일이름.확장자이름 이 존재하면 열어서 작업하는 것
- 파일이름.확장자이름 이 존재하지 않고 작성모드일 경우 알아서 파일을 만들고 작성

open("파일명.txt", "w") write - 기존 내용 삭제하고 다시 새롭게 작성하기
open("파일명.txt", "r") read - 읽기 모드
open("파일명.txt", "a") append - 기존 내용이 존재한다면 유지한 채 이어 쓰기
'''
# 파일 열기
파일 = open("my_diary.txt","w", encoding="utf-8")

#### 수기로 닫기 처리 하는 방법 레거시 방법
while True:
    글자작성 = input("입력하세요 (그만하려면 q 입력) : ")
    if 글자작성.lower() == "q":
        print("저장 완료!")
        break
    파일.write(글자작성 + "\n")
파일.close()


#### 자동으로 닫기 처리 하는 방법 평균적으로 사용하는 방법
# with 안에 작성한 파일열기 파일쓰기 와 같은 블록을 자동으로 코드가 종료되면
# close() 처리해주는 기능이 담겨 있다.
# with = 나는 알아서 파일을 열고 닫을 것이다.   as 이 모든 동작을 파일 이라는 명칭으로 진행하겠다.
with open("my_diary.txt","w", encoding="utf-8") as 파일:
    while True:
        글자작성 = input("입력하세요 (그만하려면 q 입력) : ")
        if 글자작성.lower() == "q":
            print("저장 완료!")
            break
        파일.write(글자작성 + "\n")
#파일.close()