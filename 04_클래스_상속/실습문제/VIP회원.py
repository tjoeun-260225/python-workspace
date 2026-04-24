from 회원 import 회원
class VIP회원(회원):

    def __init__(self, 이름, 나이, 이메일, 한도):
        super().__init__(이름, 나이, 이메일)   # 부모 생성자 실행
        self.한도 = 한도                        # VIP 전용 추가 변수

    def 소개(self):
        print(f"[VIP] {self.이름}님 / 나이: {self.나이} / 한도: {self.한도}원")

    def 혜택안내(self):
        print(f"{self.이름}님의 혜택: VIP 적립 5% + 무료배송")


