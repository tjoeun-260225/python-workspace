"""
기본적인 주식 용어 정리
가격 관련
시          가 - 그 날 장 시작할 때 첫 거래 가격
종          가 - 그 날 장 마감할 때 마지막 거래 가격(보통 예측 대상)
고가   /  저가 - 그 날 중 제일 높았던 / 낮았던 가격
전일      대비 - 어제 종가 대비 오늘 얼마나 올랐는지/내렸는지
52주 최고/최저 - 1년 중 제일 높았던/낮았던 가격

거래 관련
거    래    량 - 그 날 몇 주를 사고 팔았는가
거래      대금 - 거래량 X 가격 (총 얼마어치 거래되었는가)
호          가 - 사겠다 / 팔겠다 올려놓은 가격
   매수   호가 - 사려는 사람이 부른 가격
   매도   호가 - 팔려는 사람이 부른 가격

시장 관련
코    스    피 - 삼성전자, 현대차 같은 대형 기업이 모인 시장
코    스    닥 - 중소 / 벤처기업 위주 시장
상한가/하한가  - 하루에 오를 수 있는 최대 / 내릴 수 있는 최대

LSTM 으로 예측할 때 쓰는 것들

Close    종가   주로 이것으로 가격 예측
Open     시가   보조로 가끔 사용
High     고가   보조로 가끔 사용
Low      저가   보조로 가끔 사용
Volume 거래량   같이 넣으면 정확도 올라간다.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense


def 데이터불러오기(경로):
    df = pd.read_csv(경로, header=[0, 1], index_col=0, skiprows=2)
