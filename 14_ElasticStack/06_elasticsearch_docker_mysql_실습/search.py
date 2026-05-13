'''
test code 를 작성해본 경험이 있는자
MySQL Elasticsearch 검색 성능 벤치마크 도구

전체 구조
3개의 검색 케이스(CASE)를 MySQL 과 ES에서 각각 실행해 속도 비교

CASES - 테스트할 검색 시나리오
케이스                 내용
'삼성' 상품 검색       상품명에 "삼성" 포함 여부
설명 전문 검색         상품 설명에 "인체공학" 포함 여부
카테고리 + 가격 필터   카테고리 = '노트북' 이면서 가격 10만~50만원

각 케이스는 MySQL 쿼리와 ES 쿼리 두가지를 쌍으로 보유하고 있어, 같은 조건을 두 DB에서 비교
'''

import time
from elasticsearch import Elasticsearch
import config
import db

CASES = [
    {
        "label": "'삼성' 상품 검색",
        "mysql": "SELECT COUNT(*) as c FROM products WHERE name LIKE '%삼성%'",
        "es": {"query": {"match": {"name": "삼성"}}, "size": 0, "track_total_hits": True},
    },
    {
        "label": "설명 전문 검색",
        "mysql": "SELECT COUNT(*) as c FROM products WHERE description LIKE '%인체공학%'",
        "es": {"query": {"match": {"description": "인체공학"}}, "size": 0, "track_total_hits": True},
    },
    {
        "label": "카테고리 + 가격 필터",
        "mysql": "SELECT COUNT(*) as c FROM products WHERE category='노트북' AND price BETWEEN 100000 AND 500000",
        "es": {
            "query": {"bool": {"filter": [
                {"term": {"category": "노트북"}},
                {"range": {"price": {"gte": 100000, "lte": 500000}}}
            ]}},
            "size": 0, "track_total_hits": True
        },
    },
]

# MySQL 연결 → 각 케이스 SQL 실행 → 실행 시간(ms) 측정 → 결과 출력
# time.time() 으로 쿼리 전후 시간을 재서 ms 단위로 계산
# LIKE '%삼성%' 방식은 인덱스를 못 타서 풀 스캔(하나씩 일일이 모두 확인) → 느림
def benchmark_mysql():
    print("\n[4단계] MySQL 검색 속도 측정")
    conn = db.get_conn()
    cursor = conn.cursor(dictionary=True)
    results = []
    for c in CASES:
        t = time.time()
        cursor.execute(c["mysql"])
        cnt = cursor.fetchone()["c"]
        ms = (time.time() - t) * 1000
        results.append(ms)
        print(f"  {c['label']:<22}  결과: {cnt:>8,}건  시간: {ms:>8.0f}ms")
    cursor.close()
    conn.close()
    return results

# ES 클라이언트 → 각 케이스 쿼리 실행 → 실행 시간(ms) 측정 → 결과 출력
# size: 0 문서 내용은 안가져오고 건수만 조회(빠름) 문서 내용 xxx 건수 ok
# track_total_hits True -> 정확한 총 건수 반환
def benchmark_es(es):
    print("\n[5단계] ES 검색 속도 측정")
    results = []
    for c in CASES:
        t = time.time()
        resp = es.search(index=config.ES_INDEX, body=c["es"])
        ms = (time.time() - t) * 1000
        cnt = resp["hits"]["total"]["value"]
        results.append(ms)
        print(f"  {c['label']:<22}  결과: {cnt:>8,}건  시간: {ms:>8.0f}ms")
    return results

# 두 결과를 나란히 출력 + 향상 배율(몇 배 빠른지) 계산
# m / e MySQL 시간 ÷ ES 시간 = ES 가 몇 배 빠른지 확인
def print_summary(mysql_ms, es_ms):
    print("\n" + "=" * 52)
    print(f"  {'검색':<22} {'MySQL':>8} {'ES':>8} {'향상':>8}")
    print("-" * 52)
    for c, m, e in zip(CASES, mysql_ms, es_ms):
        print(f"  {c['label']:<22} {m:>6.0f}ms {e:>6.0f}ms {m / e:>6.1f}x")
    print("=" * 52)
