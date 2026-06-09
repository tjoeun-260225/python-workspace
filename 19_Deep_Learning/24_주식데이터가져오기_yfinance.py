"""
pip install yfinance
야후에서 제공하는 주식 데이터를 실시간으로 조회할 수 있는 도구
"""
import yfinance as yf


# 야후 금융에서 제공하는 도구를 이용해서 원하는 주식 데이터 csv 가져오기
def 단일종목_csv():
    # yf.download("주식이름",start="시작날짜",end="종료날짜")
    # 전세계적으로 등록된 주식 번호를 기재하여 다운로드하기
    # yf.download = yfinance.download 단순히 야후 증권에서 데이터 가져오기
    애플주식 = yf.download("AAPL", start="2020-01-01", end="2026-06-09")
    애플주식.to_csv('apple.csv')  # 나의 컴퓨터로 가져온 데이터 csv 파일로 저장

    # 위와 같이 start 와 end를 이용하는 것이 아니라
    # 단순 현재시점으로 하루치, 일주일치, 3달치 모든데이터 가져오고 싶다면
    # period 사용 (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y,10y, ytd, max)
    #           YTD = Year To Date 올해 1월 1일부터 오늘까지의 기간
    #           max = 상장일 기준 오늘 까지 전체 데이터
    삼성주식 = yf.download("005930.KS", period='1d')
    삼성주식.to_csv('samsung.csv')  # 나의 컴퓨터로 가져온 데이터 csv 파일로 저장

    # interval 몇 시간 기준 가져올 것인가
    # (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
    # 구글 주식은 하루치를 1시간 단위 기준으로 데이터를 가져올 것이다.
    구글주식 = yf.download("Google", period='1d', interval='1h')
    구글주식.to_csv('google.csv')  # 나의 컴퓨터로 가져온 데이터 csv 파일로 저장


def 다수종목_csv():
    df = yf.download(['AAPL', 'Google', 'MSFT'], period='5y')
    df.to_csv("apple_google_microsoft.csv")


import time

#  삼성전자 실시간 주가 모니터링


def get_samsung_price():
    주식종목 = yf.Ticker("005930.KS")
    data = 주식종목.fast_info # .info 보다 빠르게 현재가 가져오기 기능
    price = data.last_price   # 마지막으로 체결된 가격 장 중에는 현재가 장 마감후에는 종가
    """
    9:00 ~ 15:30 
    
    fast_info
    - 현재가
    - 시가
    - 고가
    - 저가
    - 전일 종가
    - 거래량
    - 시가 총액
    - 발행주식 수
    - 통화
    - 거래소 이름
    """
    return price
print("삼성전자 실시간 주가 모니터링(종료 : Ctrl + C)")
print("="* 40)

while True:
    가격 = get_samsung_price()
    print(f"삼성전자 : {가격:,.0f}원")
    time.sleep(5) # 5초마다 가격 보여주기










