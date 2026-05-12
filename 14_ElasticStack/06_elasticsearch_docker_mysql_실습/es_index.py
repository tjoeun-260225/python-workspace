# MySQL -> ElasticSearch 동기화 (표 데이터베이스를 JSON 형태로 변환하여 저장)
"""
MySQL             ES
database   →    cluster
table      →    index
row        →    document
column     →    field

es.indices.exists()  # 인덱스 존재하는지 확인 (=테이블 존재하는지 확인)
es.indices.create()  # 인덱스 생성            (=테이블 생성)
es.indices.delete()  # 인덱스 삭제            (=테이블 삭제)
es.indices.refresh() # 인덱스 갱신            (=테이블 새로고침)
                       엘라스틱서치의 경우 관계형 데이터베이스에 존재하는 데이터를 기준으로 생성되는 것이기 때문에
                       관계형 데이터베이스에서 수정 추가 삭제가 일어나면 그 상태를 그대로 반영

shards(샤드) 인덱스를 물리적으로 쪼개는 단위
인덱스 (100만 건)
├────shard 0 (33만 건) → 서버 A
├────shard 1 (33만 건) → 서버 B
└────shard 2 (33만 건) → 서버 C

데이터가 많을 때 여러 서버에 분산해서 병렬 검색 가능
현재는 작은 데이터라 numbers_of_shards : 1 쪼갤 필요 없음

replicas(레플리카) 샤드의 복사본(백업 + 검색 부하 분산)
shard 0 (원본)  → 서버 A
shard 0 replica → 서버 B ← 서버 A 가 죽어도 여기서 서빙 운영하는데 문제가 발생하지 않도록 설정


cursor DB에서 쿼리 결과를 순서대로 읽는 것
cursor.execute("select * from 테이블이름")
for 데이터한줄 in cursor:  cursor 로 가져온 "select * from 테이블이름" 결과를
    print(데이터한줄)      데이터한줄에 하나씩 담아 사용

dictionary=True  → row[0] 대신 row["id"] 와 같이 키 명칭으로 접근 가능


bulk(벌크) 여러 문서를 한 번에 ES에 삽입하는 방식

# 느린방식 (1건씩, for 문을 이용해서 저장)
for row in data:
    es.index(index="테이블이름", body=row)

# 빠른방식 ( 한 번에 처리)
helpers.bulk(es. action())

for 문 경우 : [요청] → [응답] [요청] → [응답] [요청] → [응답] [요청] → [응답] [요청] → [응답] 반복...
bulk   경우 :  [요청요청요청요청요청요청요청]         →  [응답응답응답응답응답응답응답]

chunk_size : bulk 할 때 한 번에 묶어서 보낼 건수
너무 크면 메모리 부족, 타임아웃 위험
너무 작으면 네트워크 왕복이 많아져서 느림
보통 1000~5000 사이가 적당

indices(인덱스들)
- ES에서 데이터를 저장하는 단위
- RDB의 테이블과 유사


request_timeout
응답 대기 최대 시간(초 단위)
Elasticsearch(config.ES_HOST,                request_timeout=30) # 연결 : 30초 안에 응답 없으면 에러
helpers.bulk(es, actions(), chunk_size=2000, request_timeout=60) # bulk : 60초 데이터가 많으니 여유있게 연결
"""
from elasticsearch import Elasticsearch, helpers
import config
import db


def get_es():
    # ES_HOST = "http://localhost:9200" docker 에 9200 으로 띄워놓은 엘라스틱 서치 연결
    # 30초 동안 연결이 되지 않으면 연결 실패 반환
    return Elasticsearch(config.ES_HOST, request_timeout=30)


def create_index(es):
    print("\n[2단계] ES 인덱스 생성")
    if es.indices.exists(index=config.ES_INDEX): # 만약 인덱스가 존재하면
        es.indices.delete(index=config.ES_INDEX) # 삭제하기

    es.indices.create(index=config.ES_INDEX, body={ # 어떤 데이터에 추가 수정 삭제가 일어났을지 모르니 초기화
        "settings": {
            "number_of_shards": 1,  # 데이터 1개를 샤드에만 저장 (소규모)
            "number_of_replicas": 0 # 복제본 없음 (개발용)
        },
        # 각 필드 타입 정의 text keyword 구분이 중요
        # text    = 검색 시 분석기 전용 (부분 검색 가능)
        # keyword = 있는 그대로 저장   (필터/집계/정렬 에 사용)
        "mappings": {
            "properties": {
                "id": {"type": "integer"},      # 정수형
                "name": {"type": "text"},       # 형태소 분석 O (전문검색)
                "brand": {"type": "keyword"},   # 형태소 분석 X (정확히 일치)
                "category": {"type": "keyword"},# 형태소 분석 X (정확히 일치)
                "description": {"type": "text"},# 형태소 분석 O (전문검색)
                "price": {"type": "float"},     # 실수형
                "stock": {"type": "integer"},   # 정수형
                "rating": {"type": "float"},    # 실수형
                "created_at": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"}
            }
        }
    })
    print("  완료")


def sync(es):
    print("\n[3단계] MySQL → ES 동기화")
    conn = db.get_conn()                   # db 연결 후
    cursor = conn.cursor(dictionary=True)  # 결과를 {"컬럼명":"값"} 딕셔너리 형태로 받을 수 있도록 설정
    cursor.execute("""
                   SELECT id,
                          name,
                          brand,
                          category,
                          description,
                          price,
                          stock,
                          rating,
                          DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at
                   FROM products
                   """)

    def actions():
        for row in cursor:
            yield {
                "_index": config.ES_INDEX,  # 저장할 인덱스
                "_id": row["id"],           # MySQL의 id를 ES 문서 ID로 사용
                "_source": row              # 나머지 전체 행이 문서 본문
            }
    #  성공에_대한_결과를_담는변수 , 실패에_대한_결과를_담는변수 = helper.bulk(서버위치, 데이터, 한 번의 http 요청에 2000건씩 묶어서 보내겠다,
    #          ok                 ,                _            = helpers.bulk(es, actions(), chunk_size=2000, request_timeout=60)
    ok, _ = helpers.bulk(es, actions(), chunk_size=2000, request_timeout=60)
    es.indices.refresh(index=config.ES_INDEX)
    cursor.close()
    conn.close()
    print(f"  완료: {ok:,}건")
