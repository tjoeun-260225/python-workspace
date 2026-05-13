import db
import es_index
import search


def main():
    print("=" * 50)
    print("  포켓몬 MySQL + Elasticsearch 실습")
    print("=" * 50)

    db.create_table()
    pokemons = db.fetch_from_api()
    db.insert_pokemons(pokemons)

    es = es_index.get_es()
    es_index.create_index(es)
    es_index.sync(es)

    print("\n[MySQL] 불 타입 포켓몬")
    search.print_results(search.search_mysql_by_type("fire"))

    print("\n[MySQL] 이름에 'saur' 포함된 포켓몬")
    search.print_results(search.search_mysql_by_name("saur"))

    print("\n[ES] 물 타입 포켓몬")
    search.print_results(search.search_es_by_type(es, "water"))

    print("\n[ES] 이름에 'char' 포함된 포켓몬")
    search.print_results(search.search_es_by_name(es, "char"))

    print("\n  Kibana -> http://localhost:5601")
    print("=" * 50)


if __name__ == "__main__":
    main()