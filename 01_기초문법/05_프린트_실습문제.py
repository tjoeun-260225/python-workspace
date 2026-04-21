'''
이름: 본인 이름
나이: 본인 나이
키: 본인 키
학생여부: True 또는 False

# 출력 결과 예시
홍길동
25
175.5
True

f-string 이용해서 출력
안녕하세요! 제 이름은 홍길동이고 나이는 25살입니다.
제 키는 175.5cm 입니다.
저는 학생입니다: True
'''

name="홍길동"
age=25
height=175.5
is_student=True

# 1단계 - 하나씩 출력
print(name)
print(age)
print(height)
print(is_student)

# 2단계 - f-string 출력
print(f"안녕하세요! 제 이름은 {name}이고 나이는 {age}살입니다.")
print(f"제 키는 {height}cm 입니다.")
print(f"저는 학생입니다: {is_student}")















