from elasticsearch import Elasticsearch, NotFoundError

# ── 연결 ──────────────────────────────────────────────
es = Elasticsearch("http://localhost:9200")
print("ES 버전:", es.info()["version"]["number"])


# ── 1단계: 인덱스 생성 ────────────────────────────────
# TODO: "books" 라는 이름의 인덱스를 생성해 보세요.
#       힌트: es.indices.create(index=___, ignore=400)
es.indices.delete(index="books", ignore=[400, 404])  # 기존 인덱스 초기화 (수정하지 마세요)
es.indices.create(index="books", ignore=400)


print("인덱스 생성 완료")


# ── 2단계: 문서 저장 (INSERT) ─────────────────────────
# TODO: 아래 books 리스트를 순서대로 저장해 보세요.
#       힌트:

books = [
    {"id": 1, "title": "파이썬 완전정복",  "author": "홍길동", "price": 32000, "genre": "프로그래밍"},
    {"id": 2, "title": "도커 입문",        "author": "김철수", "price": 28000, "genre": "인프라"},
    {"id": 3, "title": "ES 검색 마스터",   "author": "이영희", "price": 35000, "genre": "검색"},
    {"id": 4, "title": "파이썬 데이터분석", "author": "박민준", "price": 30000, "genre": "데이터"},
]

for book in books:
    es.index(index="books", id=book["id"], document=book)
    pass

print("문서 저장 완료")


# ── 3단계: 단건 조회 (SELECT by ID) ───────────────────
result = es.get(index="books", id=1)
print("조회 결과:", result["_source"])


# ── 4단계: 텍스트 검색 ────────────────────────────────
# TODO: title에 "파이썬"이 포함된 책을 검색해 보세요.
#       힌트: 04_ElasticSearch_code.py 의 query / es.search() 참고

query = {
    "query": {
        "match": {
            "title": "파이썬"  # title에 "파이썬" 포함된 문서 검색
        }
    }
}
result2 = es.search(index="books", body=query)
print("\n[파이썬 검색 결과]")
for hit in result2["hits"]["hits"]:
    print(" -", hit["_source"]["title"], "/", hit["_source"]["author"])


# ── 5단계: 수정 (UPDATE) ──────────────────────────────
es.update(index="books", id=1, doc={"price": 36000})
updated = es.get(index="books", id=1)
print("\n수정 후 가격:", updated["_source"]["price"])


# ── 6단계: 삭제 후 예외처리 ───────────────────────────
es.delete(index="books", id=4)

try:
    es.get(index="books", id=4)
except NotFoundError:
    print("삭제된 책입니다.")

# ── 7단계: 인덱스 전체 삭제 ───────────────────────────
es.indices.delete(index="books")



print("인덱스 삭제 완료")