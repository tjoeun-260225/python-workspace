import config
import db


def search_mysql_by_type(type_name: str):
    conn   = db.get_conn()
    cursor = conn.cursor(db.pymysql.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM pokemons WHERE type1 = %s OR type2 = %s",
        (type_name, type_name)
    )
    return cursor.fetchall()


def search_mysql_by_name(keyword: str):
    conn   = db.get_conn()
    cursor = conn.cursor(db.pymysql.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM pokemons WHERE name LIKE %s",
        (f"%{keyword}%",)
    )
    return cursor.fetchall()


def search_es_by_type(es, type_name: str):
    result = es.search(index=config.ES_INDEX, body={
        "query": {
            "term": {"type1": type_name}
        },
        "size": 50
    })
    return [h["_source"] for h in result["hits"]["hits"]]


def search_es_by_name(es, keyword: str):
    result = es.search(index=config.ES_INDEX, body={
        "query": {
            "match": {"name": keyword}
        },
        "size": 50
    })
    return [h["_source"] for h in result["hits"]["hits"]]


def print_results(hits):
    if not hits:
        print("  검색 결과가 없습니다.")
        return
    for p in hits:
        t2 = f"/{p['type2']}" if p.get("type2") else ""
        print(f"  #{p['id']:03d} {p['name']:<12} 타입: {p['type1']}{t2:<10} "
              f"키: {p['height']}dm  몸무게: {p['weight']}hg  경험치: {p['base_exp']}")