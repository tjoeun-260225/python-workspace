from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX

es = Elasticsearch(ES_HOST)


def create_index():
    if es.indices.exists(index=ES_INDEX):
        print("이미 인덱스 존재")
        return

    es.indices.create(index=ES_INDEX, body={
        "mappings": {
            "properties": {
                "rank": {"type": "integer"},
                "reg_no": {"type": "keyword"},
                "title": {"type": "text"},
                "author": {"type": "text"},
                "publisher": {"type": "keyword"},
                "call_no": {"type": "keyword"},
                "loan_count": {"type": "integer"},
            }
        }
    })
    print("ES 인덱스 생성 완료")


def index_books(books):
    for book in books:
        es.index(index=ES_INDEX, id=book["id"], body={
            "rank": book["rank"],
            "reg_no": book["reg_no"],
            "title": book["title"],
            "author": book["author"],
            "publisher": book["publisher"],
            "call_no": book["call_no"],
            "loan_count": book["loan_count"],
        })
    print(f"ES 색인 완료: {len(books)}건")
