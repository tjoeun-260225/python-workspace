import pandas as pd
import folium
from folium.plugins import MarkerCluster

def 노숙인_시설():
    df = pd.read_csv('노숙인_생활시설_및_생활인원_2015년_이후__20260507123008.csv', encoding='cp949', skiprows=1)
    print(df.head(10))
    print(df.columns)

    # 자치구별 행만 추출 (서울시 소계 제외)
    df_자치구 = df[df["자치구별(1)"] == "서울시"]
    df_자치구 = df_자치구[df_자치구["자치구별(2)"] != "소계"]

    # 자치구별 시설 수 출력
    print(df_자치구[["자치구별(2)", "소계"]])

    # 시설 수가 가장 많은 자치구
    print(df_자치구.sort_values("소계", ascending=False).head(1))


def 성북구_약국_지도():
    df = pd.read_csv('서울특별시_성북구_약국현황_20200101.csv', encoding='cp949')
    print(df.columns)

    df = df.dropna(subset=["위도", "경도"])

    # 행정동 종류 확인
    print(df["행정동"].unique())

    # 행정동별 색깔 지정
    색깔_맵 = {}
    색깔_목록 = ["red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige", "darkblue", "darkgreen"]
    for i, 동 in enumerate(df["행정동"].unique()):
        색깔_맵[동] = 색깔_목록[i % len(색깔_목록)]

    m = folium.Map(location=[37.5894, 127.0167], zoom_start=14)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["위도"], row["경도"]],
            popup=row["약국명"],
            icon=folium.Icon(color=색깔_맵[row["행정동"]])
        ).add_to(m)

    m.save("약국지도.html")

성북구_약국_지도()