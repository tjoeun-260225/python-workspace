'''
파이썬으로 "브라우저처럼" 서버에 요청을 보내는 도구
pip install requests
'''
import requests

네이버_온_응답 = requests.get("https://www.naver.com")

print(네이버_온_응답.status_code)
print(네이버_온_응답.text)