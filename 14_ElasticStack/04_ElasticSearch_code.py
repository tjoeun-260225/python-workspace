'''
pip install elasticsearch
'''

from elasticsearch import Elasticsearch

# 반드시 도커에서 이미지기반으로 만들어놓은 컨테이너가 실행된 다음 작업

# 1. 연결
es = Elasticsearch("http://localhost:9200")

# 연결  확인
print(es.info())

# ──────────────────────────────────────
# 2. 인덱스 생성
es.indices.create(index="my-index", ignore=400)  # 400  = 이미 현재 인덱스 이름이 있다면 무시
# 상태코드 400 뜨지말고 건너뛰거라
print("인덱스 생성 완료")

# ──────────────────────────────────────
# 3. 문서 저장 (INSERT)
doc1 = {"title": "엘라스틱서치 입문", "author": "홍길동", "price": 30000}
doc2 = {"title": "파이썬 기초", "author": "김철수", "price": 25000}
doc3 = {"title": "도커 정복", "author": "이영희", "price": 28000}

es.index(index="my-index", id=1, document=doc1)
es.index(index="my-index", id=2, document=doc2)
es.index(index="my-index", id=3, document=doc3)
print("문서 저장 완료")

# ──────────────────────────────────────
# 4. 문서 조회 (SELECT by ID)
result = es.get(index="my-index", id=1)
print("조회 결과 : ", result["_source"])
