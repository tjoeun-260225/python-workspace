from elasticsearch import Elasticsearch
from config import ES_HOST, ES_INDEX

es = Elasticsearch(ES_HOST)


def search_by_title(keyword):
    result = es.search(index=ES_INDEX, body={
        "query": {
            "match": {"title": keyword}
        },
        "highlight": {
            "fields": {"title": {}}
        },
        "size": 10
    })
    return result["hits"]["hits"]


def search_by_publisher(publisher):
    result = es.search(index=ES_INDEX, body={
        "query": {
            "term": {"publisher": publisher}
        },
        "size": 10
    })
    return result["hits"]["hits"]


def search_top_loans(n=10):
    result = es.search(index=ES_INDEX, body={
        "query": {"match_all": {}},
        "sort": [{"loan_count": {"order": "desc"}}],
        "size": n
    })
    return result["hits"]["hits"]


def search_combined(keyword, min_loan):
    result = es.search(index=ES_INDEX, body={
        "query": {
            "bool": {
                "must":   [{"match": {"title": keyword}}],
                "filter": [{"range": {"loan_count": {"gte": min_loan}}}]
            }
        },
        "size": 10
    })
    return result["hits"]["hits"]