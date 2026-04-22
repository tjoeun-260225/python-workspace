# 파이썬 개발자들이 만들어서 기본으로 제공하는 기능
# 개발자들이 print() 만큼 자주 사용하지 않는 기능들은 import 로 가져와서 사용
# 이미 파이썬 언어를 설치할 때 같이 세팅이 되어있고, 무겁지만 엄청나게 사용하지 않는
# 기본 모듈은 import로 가져와서 사용한다.
import random
# def 기능이름 사이는 띄어쓰기를 해야한다.
# ()뒤에 오는 :은 띄어쓰기를 작성해도 되고 작성하지 않아도 된다.
def 로또번호생성():
    # sample = 중복없이 랜덤으로 뽑는 기능
    # sample(리스트, 뽑을 개수)
    숫자들 = random.sample(range(1,46), 6)
    숫자들.sort() # 오름차순 정렬
    print("로또번호 :", 숫자들)

#로또번호생성()
def 로또번호여러줄생성():
    구매_원하는_줄수 = int(input("로또 번호 몇 장 필요하신가요? : "))

    for i in range(1, 구매_원하는_줄수 + 1) :
        숫자들 = random.sample(range(1,46),6)
        숫자들.sort()
        print(f"{i}줄: {숫자들}")
# 로또번호여러줄생성()

def 로또번호여러줄생성_응용버전():
    while True:
        try:
            구매_원하는_줄수 = int(input("로또 번호 몇 장 필요하신가요? : "))
            break
        except ValueError:
            print("숫자만 입력해주세요! 다시 입력해 주세요.")

    for i in range(1, 구매_원하는_줄수 + 1) :
        숫자들 = random.sample(range(1,46),6)
        숫자들.sort()
        print(f"{i}줄: {숫자들}")
로또번호여러줄생성_응용버전()