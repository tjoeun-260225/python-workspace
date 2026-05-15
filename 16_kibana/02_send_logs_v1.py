import time
import random
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "my-app-logs"# 인덱스 이름 설정
levels = ["INFO", "WARN", "ERROR"]
services = ["auth-api", "shopping-cart", "payment-service"]
print(f"'{index_name}' 인덱스로 데이터 전송 시작")
for i in range(30):
    doc = {
        "@timestamp": datetime.utcnow().isoformat(),
        "level": random.choice(levels),
        "service": random.choice(services),
        "message": f"User action number {i} processed"
    }
    # 지정한 인덱스 이름으로 데이터 저장
    es.index(index=index_name, document=doc)
    if i % 10 == 0:
        print(f"--- {i}개 완료 ---")
    time.sleep(0.05)
