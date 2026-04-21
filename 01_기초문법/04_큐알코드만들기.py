# 04_큐알코드만들기.py
# pip install qrcode[pil] -> 터미널 cmd 창에서 작성하는 것!
# pypi 에서 qrcode 가 세팅된 주소에서 나의 컴퓨터로 모듈 세팅
import qrcode

# QR 코드 만들기
qr = qrcode.QRCode(version=1,    # 크기 조절 (1~40) 숫자가 클수록 큼
                   box_size=10,  # QR 코드의 각 박스 크기
                   border=4)     # QR 코드의 테두리 크기

# QR 코드에 데이터 추가
data = "https://www.naver.com"
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("qrcode.png 파일이 생성되었습니다.")