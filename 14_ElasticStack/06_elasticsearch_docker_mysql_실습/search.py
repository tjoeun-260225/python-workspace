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


def print_summary(mysql_ms, es_ms):
    print("\n" + "=" * 52)
    print(f"  {'검색':<22} {'MySQL':>8} {'ES':>8} {'향상':>8}")
    print("-" * 52)
    for c, m, e in zip(CASES, mysql_ms, es_ms):
        print(f"  {c['label']:<22} {m:>6.0f}ms {e:>6.0f}ms {m / e:>6.1f}x")
    print("=" * 52)
