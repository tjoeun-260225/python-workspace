from elasticsearch import Elasticsearch, helpers
import config
import db


def get_es():
    return Elasticsearch(config.ES_HOST)


def create_index(es):
    print("\n[4단계] Elasticsearch 인덱스 생성")

    if es.indices.exists(index=config.ES_INDEX):
        es.indices.delete(index=config.ES_INDEX)

    es.indices.create(index=config.ES_INDEX, body={
        "mappings": {
            "properties": {
                "id":       {"type": "integer"},
                "name":     {"type": "text"},
                "height":   {"type": "integer"},
                "weight":   {"type": "integer"},
                "type1":    {"type": "keyword"},
                "type2":    {"type": "keyword"},
                "base_exp": {"type": "integer"},
            }
        }
    })

    print("  완료")


def sync(es):
    print("\n[5단계] MySQL -> Elasticsearch 동기화")

    pokemons = db.fetch_all()

    def actions():
        for p in pokemons:
            yield {
                "_index":  config.ES_INDEX,
                "_id":     p["id"],
                "_source": p,
            }

    helpers.bulk(es, actions())
    print("  동기화 완료")