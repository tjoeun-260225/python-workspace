import folium
### 서울특별시 종로구 관철동 위도 경도를 검색하여 위치 설정하거나
#### 나의 동네 위도 경도로 변경해서 진행
### 주변 카페 3가지의 위도경도를 알아내어, myLocationMap.html 로 생성하기
# TODO 1. 지도 만들기 (내 동네 위도/경도로 바꿔보기)
m = folium.Map(
    location=[37.570278, 126.983056],  # 위도, 경도
    zoom_start=17       # 동네 보기 좋은 줌 레벨
)

# TODO 2. 첫 번째 카페 마커
folium.Marker(
    location=[37.570278, 126.983056],
    popup='스타벅스 광화문점',   # 카페 이름
    tooltip='클릭해보세요.'  # 마우스 올렸을 때 텍스트
).add_to(m)

# TODO 3. 두 번째 카페 마커
folium.Marker(
    location=[37.571000,126.982000],
    popup='이디야 경복궁점',
    tooltip='클릭해보세요.'
).add_to(m)

# TODO 4. 세 번째 카페 마커
folium.Marker(
    location=[37.539500,126.984000],
    popup='투썸플레이스 광화문점',
    tooltip='클릭해보세요.'
).add_to(m)

# TODO 5. 저장
m.save('myLocationMap.html')  # 파일 이름