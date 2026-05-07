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

from geopy.geocoders import Nominatim # OpenStreetMap 기반 무료
from geopy.geocoders import GoogleV3 # Google         기반 유료
#from geopy.geocoders import Kakao  카카오처럼 특정 나라 기반 map 없음
# 참고로 한국의 경우는 Nominatim 을 이용하는 것보다 Kakao에서
# 무료 API를 발급받아 사용하는 것이 더 정확

geolocoder = Nominatim(user_agent='test')
location_1 = geolocoder.geocode('서울특별시 마포구 월드컵로 72')
location_2 = geolocoder.geocode('이상한주소')

print(location_1.latitude) # 37.562096 위도
print(location_1.longitude) # 126.9046772 경도


print(location_2.latitude) # 37.562096 위도
print(location_2.longitude) # 126.9046772 경도
# AttributeError: 'NoneType' object has no attribute 'latitude'
# 위도 경도가 없는 주소는 에러 발생 try 예외처리 해주는 방법도 좋다.
# 데이터 전처리를 해도 된다.