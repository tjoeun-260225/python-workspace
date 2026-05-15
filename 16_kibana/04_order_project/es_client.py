from elasticsearch import Elasticsearch
from config import Config

es    = Elasticsearch(Config.ES_URL)
INDEX = Config.ES_INDEX

_MAPPING = {
    "mappings": {
        "properties": {
            "user_name":    {"type": "text",    "analyzer": "standard"},
            "product_name": {"type": "text",    "analyzer": "standard"},
            "category":     {"type": "keyword"},
            "status":       {"type": "keyword"},
            "total_price":  {"type": "integer"},
            "quantity":     {"type": "integer"},
            "created_at":   {"type": "date",    "format": "yyyy-MM-dd HH:mm:ss||strict_date_optional_time"},
        }
    }
}


def ensure_index():
    if not es.indices.exists(index=INDEX):
        es.indices.create(index=INDEX, body=_MAPPING)
        print(f"ES 인덱스 '{INDEX}' 생성 완료")


def index_order(order_id: int, doc: dict):
    es.index(index=INDEX, id=order_id, body=doc)


def search_orders(query: str, size: int = 20) -> dict:
    res = es.search(index=INDEX, body={
        "query": {
            "multi_match": {
                "query":     query,
                "fields":    ["user_name^3", "product_name^2", "category", "status"],
                "fuzziness": "AUTO",
            }
        },
        "size": size,
    })
    return {
        "hits":  [h["_source"] for h in res["hits"]["hits"]],
        "total": res["hits"]["total"]["value"],
    }


def delete_all_orders():
    es.delete_by_query(index=INDEX, body={"query": {"match_all": {}}})


def count_orders() -> int:
    return es.count(index=INDEX)["count"]