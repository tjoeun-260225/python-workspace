'''
Tuple : 순서가 있고, 수정 불가능한 목록 () 사용
서버 설정 / DB 설정 / 네트워크 설정 등 변하면 안되는 설정에서 주로 사용
'''
#           localhost    port   encoding
서버설정 = ("127.0.0.1", 5000, "utf-8")
print(서버설정[0])  # 127.0.0.1
print(서버설정[1])  # 5000
print(서버설정[0:2])  # ('127.0.0.1', 5000)
# 서버설정[0] = "localhost"  TypeError: 'tuple' object does not support item assignment
# print(서버설정[0]) 튜플은 상수처럼 값을 변경할 수 없다. 하위에서 절대 변경하면 안될 경우 사용
# java = final, record=여러 값을 묶어서 상수 처리  javaScript = const 처럼 python ()로 표기
서울좌표 = (37.5655, 126.9780)
부산좌표 = (35.1796, 129.0756)
빨간색 = (255, 0, 0)
DB접속정보 = ("localhost", 3306, "root", "password")


# List 장바구니 플레이리스트  Tuple 서버설정 GPS 좌표 색상표 와 같이 고정적인 값에서 주로 사용