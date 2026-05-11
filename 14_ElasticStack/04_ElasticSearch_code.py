'''
pip install elasticsearch

Elasticsearch -> 검색 결과가 빠르게 나온다.
'''

from elasticsearch import Elasticsearch

# 반드시 도커에서 이미지기반으로 만들어놓은 컨테이너가 실행된 다음 작업

# 1. 연결
es = Elasticsearch("http://localhost:9200")
# 연결  확인
print(es.info())
# ──────────────────────────────────────
# 2. 인덱스 생성 RDS로 보면 테이블 생성
es.indices.create(index="my-index", ignore=400)  # 400  = 이미 현재 인덱스 이름이 있다면 무시
# 상태코드 400 뜨지말고 건너뛰거라
print("인덱스 생성 완료")
# ──────────────────────────────────────
# 3. 문서 저장 (INSERT) index="my-index" 어떤 테이블에 넣을지
# id = primary Key 와 동일 id를 작성하지 않으면 엘라스틱서치에서 자동으로 번호 부여
# document는 컬럼 데이터들 저장할 JSON 데이터
doc1 = {"title": "엘라스틱서치 입문", "author": "홍길동", "price": 30000}
doc2 = {"title": "파이썬 기초", "author": "김철수", "price": 25000}
doc3 = {"title": "도커 정복", "author": "이영희", "price": 28000}
es.index(index="my-index", id=1, document=doc1)
es.index(index="my-index", id=2, document=doc2)
es.index(index="my-index", id=3, document=doc3)
print("문서 저장 완료")
# ──────────────────────────────────────
# 4. 문서 조회 (SELECT by ID)
result = es.get(index="my-index", id=1)  # id는 where id = 1 과 같은 효과를 지님
#     select * from my-index where id = 1
'''
result 전체 생김새
{
    "_index":"my-index",                # 어느 테이블에서
    "_id":"1",                          # 데이터 번호
    "_source":{                         # 저장된 실제 데이터
        "title": "엘라스틱서치 입문", 
        "author": "홍길동", 
        "price": 30000
    }
}
'''
print("조회 결과 : ", result["_source"]) # 실제 내가 저장한 데이터를 보려면
# ["_source"]로 꺼내야 한다.
# ──────────────────────────────────────
# 5. 문서 검색 (Search)
query = {
    "query": {
        "match": {
            "title": "파이썬"  # title에 "파이썬" 포함된 문서 검색
        }
    }
}
result2 = es.search(index="my-index", body=query)
print("\n 검색 결과:")
for hit in result2["hits"]["hits"]:
    print(" -", hit["_source"])

'''
검색 결과 구조
{"hits" :{
    "total": {
        "value":1,         #몇개 찾았는지 숫자 데이터,
        }
        "hits" : [
             {
            "_id":"1",       
            "_source":{                         # 저장된 실제 데이터
                "title": "엘라스틱서치 입문", 
                "author": "홍길동", 
                "price": 30000
            }
        ]
    }
}
'''
# ──────────────────────────────────────
# 6. 문서 수정 (UPDATE)
es.update(index="my-index", id=1, doc={"price": 35000})
updated = es.get(index="my-index", id=1)
print("\n 수정 후 : ", updated["_source"])
# ──────────────────────────────────────
# 7. 문서 삭제 (DELETE)
es.indices.delete(index="my-index")
print("인덱스 삭제 완료")

"""
RDS 표 테이블 구조  Elasticsearch JSON 문서 구조
표 테이블보다 JSON 으로 되어있는 것이 읽는 속도가 더 빠름
표에 대한 틀 작업 처리를 해주지 않아도 되기 때문

     RDB                 Elasticsearch
   INSERT                 es.index()
   SELECT           es.get() / es.search()
   UPDATE                 es.update()
   DELETE                 es.delete()
 DROP TABLE          es.indices.delete()

"""
