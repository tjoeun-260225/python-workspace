from elasticsearch import Elasticsearch, helpers
import config
import db

def get_es():
    return Elasticsearch(config.ES_HOST, request_timeout=30)

def create_index(es):
    print("\n[2단계] ES 인덱스 생성")
    if es.indices.exists(index=config.ES_INDEX):
        es.indices.delete(index=config.ES_INDEX)

    es.indices.create(index=config.ES_INDEX, body={
        "settings": {
            "number_of_shards":   1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "id":          {"type": "integer"},
                "name":        {"type": "text"},
                "brand":       {"type": "keyword"},
                "category":    {"type": "keyword"},
                "description": {"type": "text"},
                "price":       {"type": "float"},
                "stock":       {"type": "integer"},
                "rating":      {"type": "float"},
                "created_at":  {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"}
            }
        }
    })
    print("  완료")

def sync(es):
    print("\n[3단계] MySQL → ES 동기화")
    conn   = db.get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
                   SELECT id, name, brand, category, description,
                          price, stock, rating,
                          DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at
                   FROM products
                   """)

    def actions():
        for row in cursor:
            yield {
                "_index": config.ES_INDEX,
                "_id":    row["id"],
                "_source": row
            }

    ok, _ = helpers.bulk(es, actions(), chunk_size=2000, request_timeout=60)
    es.indices.refresh(index=config.ES_INDEX)
    cursor.close()
    conn.close()
    print(f"  완료: {ok:,}건")