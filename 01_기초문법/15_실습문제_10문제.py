def 문제1():
    name = "홍길동"
    age = 25
    print(f"안녕하세요! 저는 {name}이고 {age}살입니다.")

문제1()


def 문제2():
    name = input("이름을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    print(f"{name}님은 내년에 {age + 1}살이 됩니다!")

문제2()


def 문제3():
    점수 = int(input("점수를 입력하세요: "))
    if 점수 >= 90:
        print("A학점")
    elif 점수 >= 80:
        print("B학점")
    elif 점수 >= 70:
        print("C학점")
    else:
        print("F학점")

문제3()


def 문제4():
    total = 0
    while True:
        num = input("숫자를 입력하세요 (exit 종료): ")
        if num.lower() == "exit":
            break
        total += int(num)
    print(f"합계: {total}")

문제4()


def 문제5():
    단 = int(input("단수를 입력하세요: "))
    for i in range(1, 10):
        print(f"{단} X {i} = {단 * i}")

문제5()


def 문제6():
    과일들 = ["사과", "바나나", "포도"]
    과일들.append("수박")
    과일들.remove("바나나")
    print(과일들)
    print(f"과일 개수: {len(과일들)}")

문제6()


def 문제7():
    언어들 = ["Python", "Java", "JavaScript", "HTML", "CSS"]
    for 번호, 언어 in enumerate(언어들, start=1):
        print(f"{번호}번: {언어}")

문제7()


def 문제8():
    파일이름 = input("파일 이름을 입력하세요: ")
    확장자 = input("확장자를 입력하세요 (txt, py, csv): ")
    전체파일명 = 파일이름 + "." + 확장자
    with open(전체파일명, "w", encoding="utf-8") as file:
        while True:
            text = input("입력하세요 (exit 종료): ")
            if text.lower() == "exit":
                print(f"{전체파일명} 작성완료!")
                break
            file.write(text + "\n")

문제8()


def 문제9():
    파일이름 = input("읽을 파일 이름을 입력하세요: ")
    확장자 = input("확장자를 입력하세요 (txt, py, csv): ")
    전체파일명 = 파일이름 + "." + 확장자
    count = 1
    with open(전체파일명, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if line == "":
                break
            print(f"{count}번째 줄: {line.strip()}")
            count += 1

문제9()


def 문제10():
    이름들 = []
    점수들 = []
    for i in range(1, 4):
        이름 = input(f"{i}번째 이름 입력: ")
        점수 = int(input(f"{i}번째 점수 입력: "))
        이름들.append(이름)
        점수들.append(점수)

    for 번호, 이름 in enumerate(이름들, start=1):
        print(f"{번호}번: {이름} - {점수들[번호 - 1]}점")

    평균 = sum(점수들) / len(점수들)
    print(f"평균: {평균}점")

문제10()