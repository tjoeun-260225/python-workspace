'''
with 를 이용해서 my_text.txt  파일을 만들고
한글깨짐없이 글을 작성 후 저장
변수명 = file

'''
# def 기능이름():
def 한줄작성기능():
    with open("my_text.txt","w", encoding="utf-8") as file :
        text = input("입력하세요 : ")

        file.write(text + "\n")

def 여러줄작성기능():
    with open("my_text.txt","w", encoding="utf-8") as file :
        while True:
            text = input("입력하세요 (그만하려면 exit 입력) :  ")
            if text.lower() == "exit":
                print("저장완료")
                break
            file.write(text + "\n")

여러줄작성기능()