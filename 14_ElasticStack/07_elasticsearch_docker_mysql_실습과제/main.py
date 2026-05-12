import es_index
import search


def main():
    print("=" * 52)
    print("  MySQL + Elasticsearch 성능 비교")
    print("=" * 52)

    es = es_index.get_es()
    print(f"  ES 버전: {es.info()['version']['number']}")

    # db.insert_data()  # 데이터가 없을 때 주석 해제 후 실행

    es_index.create_index(es)
    es_index.sync(es)

    mysql_ms = search.benchmark_mysql()
    es_ms = search.benchmark_es(es)

    search.print_summary(mysql_ms, es_ms)

    print("\n  Kibana → http://localhost:5601")


if __name__ == "__main__":
    main()
