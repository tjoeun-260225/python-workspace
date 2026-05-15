import time
import random
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
index_name = "my-shop-logs"

levels   = ["INFO", "WARN", "ERROR"]
services = ["user-api", "product-api", "cart-api", "payment-api"]
countries = ["KR", "US", "JP", "DE", "SG"]

# 인덱스 새로 만들기
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name, body={
    "mappings": {
        "properties": {
            "@timestamp":    {"type": "date"},
            "level":         {"type": "keyword"},
            "service":       {"type": "keyword"},
            "status_code":   {"type": "integer"},
            "response_time": {"type": "float"},
            "country":       {"type": "keyword"},
            "message":       {"type": "text"},
        }
    }
})

print(f"'{index_name}' 인덱스 생성 완료")
print("데이터 삽입 중...\n")

base_time = datetime.utcnow()

for i in range(200):
    level = random.choices(levels, weights=[70, 20, 10])[0]

    if level == "INFO":
        status = random.choice([200, 201])
        resp   = round(random.uniform(0.01, 0.5), 3)
        msg    = "Request processed successfully"
    elif level == "WARN":
        status = random.choice([400, 401, 429])
        resp   = round(random.uniform(0.5, 2.0), 3)
        msg    = "Slow response or invalid request"
    else:
        status = random.choice([500, 502, 503])
        resp   = round(random.uniform(2.0, 8.0), 3)
        msg    = "Internal server error occurred"

    random_sec = random.randint(0, 7 * 24 * 3600)
    doc_time   = base_time - timedelta(seconds=random_sec)

    doc = {
        "@timestamp":    doc_time.isoformat() + "Z",
        "level":         level,
        "service":       random.choice(services),
        "status_code":   status,
        "response_time": resp,
        "country":       random.choice(countries),
        "message":       msg,
    }

    es.index(index=index_name, document=doc)

    if (i + 1) % 50 == 0:
        print(f"{i + 1}건 완료")
    time.sleep(0.03)

print(f"\n200건 삽입 완료!")
print(f"Kibana → http://localhost:5601 에서 확인하세요.")