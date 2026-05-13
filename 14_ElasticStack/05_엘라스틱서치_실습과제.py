from elasticsearch import Elasticsearch, NotFoundError

es = Elasticsearch("http://localhost:9200")

# 실습용 데이터 세팅
es.indices.delete(index="movies", ignore=[400, 404])
es.indices.create(index="movies", ignore=400)

movies = [
    {"id": 1, "title": "어벤져스", "genre": "액션", "rating": 8.4, "year": 2012},
    {"id": 2, "title": "기생충", "genre": "드라마", "rating": 8.6, "year": 2019},
    {"id": 3, "title": "어벤져스 엔드게임", "genre": "액션", "rating": 8.4, "year": 2019},
    {"id": 4, "title": "인터스텔라", "genre": "SF", "rating": 8.6, "year": 2014},
    {"id": 5, "title": "버드박스", "genre": "공포", "rating": 6.6, "year": 2018},
]

for movie in movies:
    es.index(index="movies", id=movie["id"], document=movie)

print("데이터 세팅 완료\n")

# ──────────────────────────────────────────────────────
query1 = {"query": {"match": {"title": "어벤져스"}}}
result1 = es.search(index="movies", body=query1)
for hit in result1["hits"]["hits"]:
    src = hit["_source"]
    print(f"- {src["title"]} ({src['year']})")

# ──────────────────────────────────────────────────────
# 출력 예시:
# - 어벤져스 | 액션 | 8.4

query2 = {"query": {"term": {"gener.keyword": "액션"}}}
result2 = es.search(index="movies", body=query2)
for hit in result2["hits"]["hits"]:
    src = hit["_source"]
    print(f"- {src['title']} | {src['genre']} | {src['rating']}")
# ──────────────────────────────────────────────────────
es.update(index="movies", id=4, doc={"rating": 9.0})
updated = es.get(index="movies", id=4)
print(f"수정 후 : {updated['_source']}")
# ──────────────────────────────────────────────────────
# 힌트: es.delete() 후 try/except
es.delete(index='movies', id=5)
# 이미 get 을 통해서 삭제한 엘라스틱서치를 검색하려 하면
# elasticsearch.NotFoundError: NotFoundError(404, "{'_index': 'movies', '_id': '5', 'found': False}")
# 발생한다는 것을 미리 확인했기 때문에
# 바로 try / except 를 작성한 것
# 처음 접하는 개발자라면 try / except 없이 NotFoundError 를 겪은 후
# try / except 를 이용해서 에러 예외 처리를 해야하는 것
try:
    es.get(index='movies', id=5)
except NotFoundError:
    print("삭제된 문서입니다.")
# 확인되지 않은 참조 'NotFoundError'
# elasticsearch 에서 문서를 찾을 수 없을 때 표기하기 위한 자체 에러 표기법
# NotFoundError 라는 에러가 발생했을 때 대처를 하기 위해서는
# elasticsearch 에서 제공하는 NotFoundError 표기
# from elasticsearch import Elasticsearch, NotFoundError
# ──────────────────────────────────────────────────────
es.indices.delete(index="movies")
print("movies 인덱스(=테이블) 전체 삭제 완료")

'''
NewConnectionError(HTTPConnection(host='localhost', port=9200): 
Failed to establish a new connection: [WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다))

'''