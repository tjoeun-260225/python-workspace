import datetime
'''
YYYY - Year
MM   - Month  (0월    +1)
d    - day

h    - hour
mm   - minute
ss   - second

M - 월을 뜻한다. 
m - 분을 뜻한다.

'''
def 현재시간():
    # datetime 라이브러리 이름 안에 datetime 파일존재 파일 안에 now() 기능 존재
    지금 = datetime.datetime.now()
    return f"{지금.hour}:{지금.minute:02d}"

def 단체전송(*받는사람들, 메세지, 타입="text"):
    for 사람 in 받는사람들:
        print(f"{사람}에게 {타입}로 {메세지} 전송")