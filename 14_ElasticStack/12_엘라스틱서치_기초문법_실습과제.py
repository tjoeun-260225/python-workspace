from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")


def 실습1():
    es.indices.create("my_first_index")
    es.indices.exists("my_first_index")
    es.indices.delete("my_first_index")


def 실습2():
    es.indices.create(index="products", body={
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "brand": {"type": "keyword"},
                "price": {"type": "integer"},
                "rating": {"type": "float"},
                "created_at": {"type": "date"}
            }
        }
    })


def 실습3():
    query = {
        "query": {
            "match": {
                "name": "나이키 운동화"
            }
        }
    }

    query = {
        "query": {
            "term": {
                "brand": "Nike"
            }
        }
    }
    query = {
        "query": {
            "range": {
                "price": {
                    "gte": 10000,
                    "lte": 50000,
                }
            }
        }
    }
def 실습4():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"name": "나이키 운동화"}}
                ],
                "filter": [
                    {"range": {"price": {"lte": 50000}}}
                ],
                "must_not": [
                    {"term": {"brand": "품절"}}
                ]
            }
        }
    }


def 실습5():
    query = {
        "query": {"match_all": {}},

        "sort": [
            {"price": {"order": "asc"}}
        ],

        "from": 0,
        "size": 10,

        "highlight": {
            "fields": {
                "name": {}
            }
        }
    }


def 실습6():
    query = {
        "aggs": {
            "브랜드별_상품수": {
                "terms": {"field": "brand"}
            }
        }
    }
    query = {
        "aggs": {
            "평균_평점": {
                "avg": {"field": "rating"}
            }
        }
    }
