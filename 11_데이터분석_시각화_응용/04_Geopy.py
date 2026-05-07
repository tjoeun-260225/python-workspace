'''
주소를 위도/경도로 바꿔주는 라이브러리

pip install geopy

만약  주소 데이터를 가져왔고, 데이터를 확인해보니, 위도 경도가 존재하지 않아
지도에 표기를 할 수 없다.
--> 주소를 위도 경도로 변환

주소만 있는 CSV
    ->    geopy 라이브러리이용해서 위도 / 경도 변환
            ->    Folium 으로 지도에 찍기


주요 메서드
- .geocode("주소")        =    주소    -> 위도/경도 변경할 때 사용
- .reverse("위도","경도") = 위도/경도  ->    주소   변경할 때 사용

주요 속성
- .latitude  = 위도
- .longitude = 경도
- .address   = 전체 주소 문자열 반환
- .raw       = 딕셔너리 형태로 모든 정보 반환

'''
import time

import pandas as pd
from geopy.geocoders import Nominatim  # OpenStreetMap 기반 무료
from geopy.geocoders import GoogleV3  # Google         기반 유료


# from geopy.geocoders import Kakao  카카오처럼 특정 나라 기반 map 없음
# 참고로 한국의 경우는 Nominatim 을 이용하는 것보다 Kakao에서
# 무료 API를 발급받아 사용하는 것이 더 정확
def 기본문법():
    geolocoder_1 = Nominatim(user_agent='test')
    geolocoder_2 = Nominatim(user_agent='홍길동')
    # Nominatim 지도 서비스를 꺼내서 서버에 test 유저라 보낸다.
    # user_agent = Nominatim 서버에게 나는 test 라는 사람이다 하고 보내는 이름표
    # 아무 문자열이나 작성해도 된다.
    location_1 = geolocoder_1.geocode('서울특별시 마포구 월드컵로 72')
    location_2 = geolocoder_2.geocode('이상한주소')

    print(location_1.latitude)  # 37.562096 위도
    print(location_1.longitude)  # 126.9046772 경도

    print(location_2.latitude)  # 37.562096 위도
    print(location_2.longitude)  # 126.9046772 경도
    # AttributeError: 'NoneType' object has no attribute 'latitude'
    # 위도 경도가 없는 주소는 에러 발생 try 예외처리 해주는 방법도 좋다.
    # 데이터 전처리를 해도 된다.


def csv_주소_변환():
    df = pd.read_csv('데이터실습파일/전국도서관표준데이터.csv', encoding='cp949')
    #                             데이터가 없는 행 데이터 정보들만 따로 복사해서 사용하겠다.
    df_위도가없는데이터 = df[df['위도'].isna()].copy()  # 주소는 존재하나, 위도 경도가 csv 데이터로 없을 경우
    # 위도 경도가 없는 행만 갖고온 후 데이터 채우기
    # dropna() = NaN 있는 행 버리기
    # isna()  = 없는 행만 추출하기
    geolocoder = Nominatim(user_agent="honggildong")
    lats, lngs = [], []
    for _, row in df_위도가없는데이터.iterrows():
        try:
            location = geolocoder.geocode(row["소재지도로명주소"])
            if location:
                lats.append(location.latitude)
                lngs.append(location.longtitude)
            else:
                lats.append(None)
                lngs.append(None)
        except:
            lats.append(None)
            lngs.append(None)
        time.sleep(1)
    print(lats)
    print(lngs)


# 데이터를 변환해야하는 데이터가 매우 많을 것이며, 시간이 오래 걸릴 경우
# 제대로 코드를 작성했는지 테스트 하는 방법
def csv_주소_변환_데이터테스트():
    df = pd.read_csv('데이터실습파일/전국도서관표준데이터.csv', encoding='cp949')
    df_위도가없는데이터 = df[df['위도'].isna()].copy()#.head(10) # 상위 10개 의 데이터만 존재
    print("df_위도가없는데이터 개수 확인 : ", len(df_위도가없는데이터))
    df_위도가없는데이터 = df_위도가없는데이터.head(1) # 상위 1개 의 데이터만 존재
    print("df_위도가없는데이터 head : ", df_위도가없는데이터)
    geolocoder = Nominatim(user_agent="honggildong")
    lats, lngs = [], []
    for _, row in df_위도가없는데이터.iterrows():
        try:
            location = geolocoder.geocode(row["소재지도로명주소"])
            print("row[소재지도로명주소]  : ", row["소재지도로명주소"])
            print("location  : ", location)
            if location:
                lats.append(location.latitude)
                lngs.append(location.longitude)
            else:
                lats.append(None)
                lngs.append(None)
        except:
            lats.append(None)
            lngs.append(None)
        time.sleep(1)
    print(lats)
    print(lngs)
csv_주소_변환_데이터테스트()
