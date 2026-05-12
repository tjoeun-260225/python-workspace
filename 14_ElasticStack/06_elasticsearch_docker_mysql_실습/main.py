#import db
'''
1번
if __name__ =="__main__":
    insert_data()
2번
insert_data()
1번과 같이 작성하지 않으면
db.insert_data() 존재유무와 관계없이
import db 가 되었다는 이유 하나만으로도 insert_data() 가 실행된다.
'''
import es_index
import search

def main():
    print("="*52)
    print("  MySQL + Elasticsearch 성능 비교")
    print("="*52)

    es = es_index.get_es()
    print(f"  ES 버전: {es.info()['version']['number']}")

    #db.insert_data()

    es_index.create_index(es)
    es_index.sync(es)

    mysql_ms = search.benchmark_mysql()
    es_ms    = search.benchmark_es(es)

    search.print_summary(mysql_ms, es_ms)

    print("\n  Kibana → http://localhost:5601")

if __name__ == "__main__":
    main()