import es_index
import db
import search


def main():
    print("=" * 52)
    print("  MySQL + Elasticsearch 성능 비교")
    print("=" * 52)

    es = es_index.get_es()
    print(f"  ES 버전: {es.info()['version']['number']}")

    db.insert_data()  # 데이터가 없을 때 주석 해제 후 실행

    es_index.create_index(es)
    es_index.sync(es)

    mysql_ms = search.benchmark_mysql()
    es_ms = search.benchmark_es(es)

    search.print_summary(mysql_ms, es_ms)

    print("\n  Kibana → http://localhost:5601")


if __name__ == "__main__":
    main()
'''
{
  "took": 3,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10000,
      "relation": "gte"
    },
    "max_score": 2.0712295,
    "hits": [
      {
        "_index": "products",
        "_id": "74004",
        "_score": 2.0712295,
        "_source": {
          "id": 74004,
          "name": "삼성 프로 노트북 4467",
          "brand": "삼성",
          "category": "노트북",
          "description": "에너지 효율 1등급으로 전기세 걱정이 없습니다.",
          "price": 1388093.26,
          "stock": 4879,
          "rating": 4,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74005",
        "_score": 2.0712295,
        "_source": {
          "id": 74005,
          "name": "삼성 울트라 운동화 9551",
          "brand": "삼성",
          "category": "운동화",
          "description": "에너지 효율 1등급으로 전기세 걱정이 없습니다.",
          "price": 1060975.99,
          "stock": 4632,
          "rating": 2.7,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74008",
        "_score": 2.0712295,
        "_source": {
          "id": 74008,
          "name": "삼성 맥스 운동화 5291",
          "brand": "삼성",
          "category": "운동화",
          "description": "최신 기술이 집약된 프리미엄 제품입니다.",
          "price": 235728.14,
          "stock": 2714,
          "rating": 3.6,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74016",
        "_score": 2.0712295,
        "_source": {
          "id": 74016,
          "name": "삼성 에어 노트북 1031",
          "brand": "삼성",
          "category": "노트북",
          "description": "최신 기술이 집약된 프리미엄 제품입니다.",
          "price": 593921.65,
          "stock": 4143,
          "rating": 2.6,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74040",
        "_score": 2.0712295,
        "_source": {
          "id": 74040,
          "name": "삼성 울트라 자켓 906",
          "brand": "삼성",
          "category": "자켓",
          "description": "인체공학적 설계로 편안한 착용감을 제공합니다.",
          "price": 1143084.88,
          "stock": 2005,
          "rating": 4.9,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74046",
        "_score": 2.0712295,
        "_source": {
          "id": 74046,
          "name": "삼성 슬림 스마트폰 4299",
          "brand": "삼성",
          "category": "스마트폰",
          "description": "최신 기술이 집약된 프리미엄 제품입니다.",
          "price": 102358.71,
          "stock": 2883,
          "rating": 3,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74049",
        "_score": 2.0712295,
        "_source": {
          "id": 74049,
          "name": "삼성 맥스 노트북 5097",
          "brand": "삼성",
          "category": "노트북",
          "description": "초경량 설계로 휴대성을 극대화했습니다.",
          "price": 977816.7,
          "stock": 2234,
          "rating": 3.7,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74070",
        "_score": 2.0712295,
        "_source": {
          "id": 74070,
          "name": "삼성 울트라 스마트폰 9379",
          "brand": "삼성",
          "category": "스마트폰",
          "description": "에너지 효율 1등급으로 전기세 걱정이 없습니다.",
          "price": 1213064.95,
          "stock": 8372,
          "rating": 4.1,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74082",
        "_score": 2.0712295,
        "_source": {
          "id": 74082,
          "name": "삼성 프리미엄 스마트폰 9849",
          "brand": "삼성",
          "category": "스마트폰",
          "description": "최신 기술이 집약된 프리미엄 제품입니다.",
          "price": 1941013.82,
          "stock": 1518,
          "rating": 3.7,
          "created_at": "2026-05-12 06:05:31"
        }
      },
      {
        "_index": "products",
        "_id": "74095",
        "_score": 2.0712295,
        "_source": {
          "id": 74095,
          "name": "삼성 맥스 노트북 2808",
          "brand": "삼성",
          "category": "노트북",
          "description": "최신 기술이 집약된 프리미엄 제품입니다.",
          "price": 785429.58,
          "stock": 6416,
          "rating": 2.4,
          "created_at": "2026-05-12 06:05:31"
        }
      }
    ]
  }
}


'''