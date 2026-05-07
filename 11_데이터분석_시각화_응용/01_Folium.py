'''
https://python-visualization.github.io/folium/latest/
인터랙티브 지도를 만들 수 있는 라이브러리
Leaflet.js 기반으로 동작해서 html 파일로 저장하여 사용할 수 있다.
지도 위에 데이터 시각화, 클러스터링, 히트맵 등 가능
설치
pip install folium

* 추가개념
** Leaflet : Folium이 내부적으로 사용하는 지도 엔진
** 클러스터링 : 마커가 너무 많을 때 뭉쳐서 보여주는 것
           예를들어 마커 2799개 -> 그냥 찍으면 지도가 점으로 가득 참
                               -> 클러스터링 처리하면 숫자로 묶어서 보여줌
** 히트맵 : 밀집도를 색상으로 표현
           예를 들어 휴게소가 많은 곳 -> 빨갛게 표기
                     휴게소가 적은 곳 -> 파랗게 표기

흐름
folium.Map() 생성
    -> .add_to(변수 = 공간데이터명칭) 으로 추가
      --> 모든 추가가 끝난다면 변수.save("저장할_파일이름.html")


데이터
전국 편의점 / 카페 위치
전국 주유소 위치 / 가격
서울시 따릉이 대여소
전국 공공화장실 위치 등 사용하며 데이터 분석할 수 있다.


csv 데이터를 선택할 때 주의할 점
1. 위도 경도가 컬럼으로 존재하는가?
2. 데이터를 제한없이 다운로드하여 가져올 수 있는가?



'''
# csv 파일로 불러온 위도 경도 표기를 위하여 csv 파일 읽기
import pandas as pd
import folium
from folium.plugins import  MarkerCluster # folium_excel_클러스터링 위해 추가한 라이브러리 모듈
#  folium 큰 상자 안에
##      plugins 에서
###       MarkerCluster 만 가져와서 사용하겠다.
#### 만약 위와 같이 작성하지 않는다면  folium.plugins.MarkerCluster() 작성해서 기능을 사용하면 된다.
##### from folium.plugins import  MarkerCluster 이렇게 쓸 이유가 없다.
###### 하지만 from~import MarkerCluster 를 작성하지 않으면 너무 길게 작성하게 되기 때문에
####### from~import MarkerCluster 를 작성해서 MarkerCluster() 으로 줄여서 사용하겠다.
####### 만약 as 를 붙이고 싶다면
######## from folium.plugins import  MarkerCluster as mc 와 같이 사용가능하다.

# import openpyxl
def folium기본():
    ## 1. 지도 생성
    ### folium 라이브러리에서 Map() 지도 생성 기능 호출
    ####        지도생성 기능을 호출해서 지도를 만들 때
    ##### 중심이 되는 위도 경도 설정, 처음에 시작할 zoom 정도 세팅
    m = folium.Map(
        location=[37.5665, 126.9780],  # 위도, 경도 (서울)
        zoom_start=12  # zoom level (1 == 지구전체 ~ 18 == 건물 하나)
    )

    기본타입 = folium.Map(tiles='OpenStreetMap')
    밝은타입 = folium.Map(tiles='CartoDB position')
    어두운타입 = folium.Map(tiles='CartoDB dark_matter')
    위성지도타입 = folium.Map(tiles='Stamen Terrain')

    # 다양한 타입이 존재

    ## 2. 마커 추가
    ### folium 라이브러리에서 Marker() 위치 표기 기능 호출
    #### 어떤 위치를 표기해야하는지 설정, 클릭하면 보이는 글자, 텍스트 등 팝업 삽입
    #### 마우스를 살~짝 올리면 보여질 텍스트 툴팁 추가 folium 에서 제공하는 기본 아이콘 세팅
    ##### 모든 세팅을 끝낸 결과를 m 공간에 추가하겠다.
    folium.Marker(
        location=[37.5665, 126.9780],
        popup='서울시청',  # 클릭하면 뜨는 팝업
        tooltip='여기를 클릭 ',  # 마우스를 올려두면 뜨는 텍스트
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

    ## 3. 원형 마커
    ### folium 라이브러리에서 원형마커 표기 기능
    #### 원 둥글기, 원둘레, 색상, 색상채우기 유무, 불투명도 0~1 사이로 설정 가능
    #### 마커나 원형마커를 이용해서 범위나 현재 위치 설정
    ##### 모든 세팅을 끝낸 결과를 m 공간에 추가하겠다.
    folium.CircleMarker(
        location=[37.5700, 126.9800],
        radius=30,
        color="blue",
        fill=True,
        fill_opacity=0.4
    ).add_to(m)

    # m에 보관된 코드를 참고하여 html 파일을 나의 컴퓨터에 저장하겠다.
    m.save('01_map.html')


def folium_excel_위도경도():
    # 인텔리제이에서 현재폴더기준 유사명칭 파일들 호출이 read_csv잘 되지만
    # read_excel 에서는 잘 되지 않는다.
    # header = None 첫 줄을 컬럼명으로 사용하지 말 것
    # skiprows = 4 위에서 4줄은 건너뛰기
    df = pd.read_excel('공공자전거 대여소 정보(25.12월 기준).xlsx', header=None, skiprows=4)
    print(df.columns)  # 컬럼명 확인
    print(df.head())  # 상위 데이터 5개 확인
    '''
    Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')
       0            1    2  ...   7     8    9
    0    NaN          NaN  NaN  ... NaN   NaN  NaN
    1  102.0   망원역 1번출구 앞  마포구  ... NaN  15.0   QR
    2  103.0   망원역 2번출구 앞  마포구  ... NaN  14.0   QR
    3  104.0   합정역 1번출구 앞  마포구  ... NaN  13.0   QR
    4  105.0   합정역 5번출구 앞  마포구  ... NaN   5.0   QR

    [5 rows x 10 columns]
    '''

    df.columns = ["대여소번호", "대여소명", "자치구", "상세주소", "위도", "경도", "설치시기", "LCD거치대", "QR거치대", "운영방식"]

    # 데이터가 없는 행은 버려주세요.
    # 위도 경도에서 비어있는 행 제거 dropna(subset=[])
    # dropna() : NaN 비어있는 행 버리기
    # subset = 어떤 컬럼들의 비어있는 행을 버릴 것인지 선택해서 담아두기
    df = df.dropna(subset=["위도","경도"])

    # 지도 생성 -> 데이터가 문제 없다
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=15)

    # 마커 찍기

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["위도"], row["경도"]]
        ).add_to(m)
    m.save("따릉이지도.html")

    # ValueError: Location values cannot contain NaNs.
    # NaN 때문에 발생한 상황 위도 경도가 비어있는 행이 있다.
    # 마커 찍기를 하기 전에 위도 경도가 비어있는 행을 버리거나 0 으로 만들거나
    # 기획자와 회사가 결정한 사항에 따라서 처리
    # 위와 같은 사항을 데이터 전처리 -> 데이터로 결과를 만들기 전 전부다 처리 작업



def folium_excel_클러스터링():

    df = pd.read_excel('공공자전거 대여소 정보(25.12월 기준).xlsx', header=None, skiprows=4)
    print(df.columns)
    print(df.head())

    df.columns = ["대여소번호", "대여소명", "자치구", "상세주소", "위도", "경도", "설치시기", "LCD거치대", "QR거치대", "운영방식"]
    df = df.dropna(subset=["위도","경도"])
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=15)
    cluster = MarkerCluster().add_to(m) # 클러스터 생성
    for _, row in df.iterrows():
        folium.Marker(
            location=[row["위도"], row["경도"]]
        ).add_to(cluster) # m 이 아닌 클러스터에 추가
    m.save("따릉이지도.html")

folium_excel_클러스터링()
