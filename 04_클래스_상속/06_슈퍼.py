class 사람:
    def __init__(self, 이름):
        self.이름 = 이름


class 학생(사람):
    def __init__(self, 이름, 학교):
        super().__init__(이름)                              # 부모의 __init_ 실행
        self.학교 = 학교

A군 = 학생("철수","서울대")
print(A군.이름)
print(A군.학교)

