# upload_geojson.py
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

url = "https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2018/json/skorea-provinces-2018-geo.json"
geojson = requests.get(url).json()

for feature in geojson["features"]:
    doc = {
        "name": feature["properties"].get("name", ""),
        "geometry": feature["geometry"]
    }
    es.index(index="korea-provinces-geo", document=doc)

print("GeoJSON 업로드 완료")
