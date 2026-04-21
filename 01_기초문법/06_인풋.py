"""

import  Scanner

Scanner sc = new Scanner(System.in)
System.out.print("이름을 입력하세요")
String user_name = sc.next()

파이썬의 경우 불필요한 import 나 new 와 같은 방식 지양
AI 모델을 만들거나 데이터 분석과 같은 작업을 해야하는 언어 -> 언어적으로 불필요한 추가 커스텀 지양
"""
user_name=input("이름을 입력하세요 : ")
user_age=input("나이를 입력하세요 : ")
print(f"안녕하세요, {user_name}님 ! 올해는 {user_age}살 이시군요!!")


next_age = int(user_age)
print(f"내년에는 {next_age + 1}살 이시군요!!")
# TypeError: can only concatenate str (not "int") to str
# str + int 를 더할 수 없다. 해결