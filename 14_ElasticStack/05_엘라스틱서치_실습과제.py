from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 실습용 데이터 세팅
es.indices.delete(index="movies", ignore=[400, 404])
es.indices.create(index="movies", ignore=400)

movies = [
    {"id": 1, "title": "어벤져스",     "genre": "액션",   "rating": 8.4, "year": 2012},
    {"id": 2, "title": "기생충",       "genre": "드라마", "rating": 8.6, "year": 2019},
    {"id": 3, "title": "어벤져스 엔드게임", "genre": "액션", "rating": 8.4, "year": 2019},
    {"id": 4, "title": "인터스텔라",   "genre": "SF",     "rating": 8.6, "year": 2014},
    {"id": 5, "title": "버드박스",     "genre": "공포",   "rating": 6.6, "year": 2018},
]

for movie in movies:
    es.index(index="movies", id=movie["id"], document=movie)

print("데이터 세팅 완료\n")

# ──────────────────────────────────────────────────────
# TODO 1. title에 "어벤져스" 가 포함된 문서를 검색하고
#         title과 year를 출력하세요
# 힌트: es.search(index=..., body={"query": {"match": {...}}})
# 출력 예시:
# - 어벤져스 (2012)
# - 어벤져스 엔드게임 (2019)

query1 = None  # TODO: 여기를 채우세요
# result1 = es.search(???)
# for hit in result1["hits"]["hits"]:
#     print(???)

# ──────────────────────────────────────────────────────
# TODO 2. genre가 "액션" 인 문서를 검색하고
#         title, genre, rating을 출력하세요
# 출력 예시:
# - 어벤져스 | 액션 | 8.4

query2 = None  # TODO: 여기를 채우세요

# ──────────────────────────────────────────────────────
# TODO 3. id=4 문서의 rating을 9.0으로 수정하고
#         수정된 결과를 조회해서 출력하세요
# 힌트: es.update(index=..., id=..., doc={...})
# 출력 예시: 수정 후: {'title': '인터스텔라', 'rating': 9.0, ...}

# TODO: 여기를 채우세요

# ──────────────────────────────────────────────────────
# TODO 4. id=5 문서를 삭제하고
#         삭제 후 id=5 조회 시 "삭제된 문서입니다" 출력하세요
# 힌트: es.delete() 후 try/except

# TODO: 여기를 채우세요

# ──────────────────────────────────────────────────────
# TODO 5. movies 인덱스 전체를 삭제하세요
#         삭제 후 "movies 인덱스 삭제 완료" 출력

# TODO: 여기를 채우세요