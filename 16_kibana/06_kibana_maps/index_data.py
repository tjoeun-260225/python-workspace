# index_data.py
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

cities = [
    {"city": "서울", "region": "수도권", "value": 950, "location": {"lat": 37.5665, "lon": 126.9780}},
    {"city": "부산", "region": "영남",   "value": 340, "location": {"lat": 35.1796, "lon": 129.0756}},
    {"city": "대구", "region": "영남",   "value": 240, "location": {"lat": 35.8714, "lon": 128.6014}},
    {"city": "인천", "region": "수도권", "value": 290, "location": {"lat": 37.4563, "lon": 126.7052}},
    {"city": "광주", "region": "호남",   "value": 150, "location": {"lat": 35.1595, "lon": 126.8526}},
    {"city": "대전", "region": "충청",   "value": 150, "location": {"lat": 36.3504, "lon": 127.3845}},
    {"city": "울산", "region": "영남",   "value": 113, "location": {"lat": 35.5384, "lon": 129.3114}},
    {"city": "수원", "region": "수도권", "value": 120, "location": {"lat": 37.2636, "lon": 127.0286}},
    {"city": "창원", "region": "영남",   "value": 100, "location": {"lat": 35.2280, "lon": 128.6811}},
    {"city": "제주", "region": "제주",   "value": 67,  "location": {"lat": 33.4996, "lon": 126.5312}},
]

mapping = {
    "mappings": {
        "properties": {
            "city":     {"type": "keyword"},
            "region":   {"type": "keyword"},
            "value":    {"type": "integer"},
            "location": {"type": "geo_point"}
        }
    }
}

index_name = "korea-cities"

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name, body=mapping)

for doc in cities:
    es.index(index=index_name, document=doc)

print(f"총 {len(cities)}개 문서 인덱싱 완료")
print(es.count(index=index_name))