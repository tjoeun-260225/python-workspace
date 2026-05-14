'''
ImportError: cannot import name 'Elasticsearch' from 'elasticsearch'
es_client.py' if it has the same name as a library you intended to import

개발자가 만든 es_client.py 와 elasticsearch 회사에서 만든 es_client.py 충돌

되도록이면 회사에서 만든 모듈 명칭을 파일로 만들지 말자!!!!

elasticsearch 기능을 작성하는 py 파일이 필요하다.
es_client.py
'''

from elasticsearch import Elasticsearch
from config import Config

es = Elasticsearch(Config.ES_URL)
INDEX = Config.ES_INDEX

_MAPPING = {
    "mappings": {
        "properties": {
            "name": {"type": "text", "analyzer": "standard"},
            "email": {"type": "keyword"},
            "job": {"type": "text"},
            "company": {"type": "text"},
            "city": {"type": "keyword"},
            "country": {"type": "keyword"},
        }
    }
}


def ensure_index() -> None:
    if not es.indices.exists(index=INDEX):
        es.indices.create(index=INDEX, body=_MAPPING)
        print(f"ES 인덱스 '{INDEX}' 생성 완료")


def index_user(user_id: int, doc: dict) -> None:
    es.index(index=INDEX, id=user_id, body=doc)


def search_users(query: str, size: int = 20) -> dict:
    res = es.search(index=INDEX, body={
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name^3", "company^2", "job", "email", "city"],
                "fuzziness": "AUTO",
            }
        },
        "size": size,
    })
    return {
        "hits": [h["_source"] for h in res["hits"]["hits"]],
        "total": res["hits"]["total"]["value"],
    }


def delete_all_users() -> None:
    es.delete_by_query(index=INDEX, body={"query": {"match_all": {}}})


def count_users() -> int:
    return es.count(index=INDEX)["count"]
