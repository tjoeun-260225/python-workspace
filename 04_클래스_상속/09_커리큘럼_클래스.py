class Student:
    school = "파이썬 고등학교" # 클래스 변수 (모든 인스턴스 공유)
    def __init__(self, name, age, grade):
        # 인스턴스 변수 (각 객체 독립)
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = []

    def add_score(self, subject, score):
        self.scores.append({"subject": subject, "score": score})

    def average(self):
        if not self.scores: return 0
        return sum(s['score'] for s in self.scores) / len(self.scores)
    # 자바 toString
    # print-> 현재 클래스에 존재하는 필드에 데이터 정보 조회 출력
    # python __str__ = java toString
    def __str__(self): # print() 시 호출
        return f"[{self.grade}학년] {self.name} (평균: {self.average():.1f})"

    # __str__ 비슷하지만 개발자용 출력은 개발자가 볼 수 있는 구문들의 정보 추가해서 만듦
    # info error debug 와 같은 기능 추가할 수 있다.
    def __repr__(self): # 디버그용
        return f"Student({self.name!r}, {self.age})"
# 객체 생성
s1 = Student("홍길동", 17, 2)
s2 = Student("김철수", 18, 3)
s1.add_score("국어", 90)
s1.add_score("수학", 85)
s1.add_score("영어", 92)
print(s1) # __str__ 호출
print(Student.school) # 클래스 변수
print(s1.school) # 인스턴스에서도 접근 가능