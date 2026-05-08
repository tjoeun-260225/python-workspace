# 1. pymongo 통째로 기능들을 가져와서 꺼내서 그때그때 사용하겠다.
# import pymongo
# pymongo.MongoClient()

# 2. pymongo 에서 MongoClient 콕 찝어 사용하겠다.
from pymongo import MongoClient
from datetime import datetime

# MongoClient()

# 3. pymongo 에서 MongoClient 콕 찝어 사용하되, mc 명칭으로 줄여서 사용하겠다.
# from pymongo import MongoClient as mc
# mc()

# ** as 는 import 가 없는 곳에서는 사용을 할 수 없도록 설계되어 있다.

client = MongoClient("mongodb://localhost:27017/")
db = client['mydb']
# col = collection
col_books = db['books']
col_products = db['products']
col_posts = db['posts']


def insert_문제1_도서관_책_등록():
    # 한 건 저장
    한건저장 = col_books.insert_one(
        {
            'title': '파이썬 완전정복',
            'author': '김코딩',
            'price': 28000,
            'pub_year': 2024
        }
    )
    print("한 건 저장한 결과 id : ", 한건저장.inserted_id)
    여러건저장 = col_books.insert_many(
        [
            {
                'title': 'mongoDB 바이블',
                'author': '이데이터',
                'price': 35000,
                'pub_year': 2023
            },
            {
                'title': '자바스크립트 입문',
                'author': '박프론트',
                'price': 22000,
                'pub_year': 2025
            },
            {
                'title': '리눅스 실전',
                'author': '최서버',
                'price': 19000,
                'pub_year': 2022
            },
        ]
    )


def insert_문제2_쇼핑몰_상품_등록():
    결과 = col_products.insert_many([
        {
            'product_name': "무선 마우스",
            'price': 35000,
            'stock': 100,
            'tags': ["전자기기", "컴퓨터"]
        },
        {
            'product_name': "맨투맨 티셔츠",
            'price': 45000,
            'stock': 50,
            'options': {
                "color": ["검정", "흰색", "회색"],
                "size": ["S", "M", "L", "XL"]
            }
        },
        {
            'product_name': "블루투스 이어폰",
            'price': 89000,
            'stock': 30,
            'sale_price': 71200,
            'discount_rate': 20
        },
    ])
    print("상품 저장 ids : ", 결과.inserted_ids)
    '''
    mongoDB 와 같은 nosql 은 왜 각 행마다 필드가 달라도 저장이 되는가?
    
    관계형 DB는 테이블을 만들 때 구조를 먼저 정의 -> 데이터 제대로 들어오는 것이 가장 중요
    
    mongoDB 와 같은 nosql 은 각 행마다 독립적으로 존재하며 필요한 필드만 지니면 되며, 
                             없는 필드는 그냥 없는 것이지 Null로 채우지 않는다.
                             
            데이터를 제대로 저장하자 xxxx -> 데이터를 빠르게 조회 / 데이터 작업을 할 때 문제 최소화
    
    '''


def insert_문제3_SNS_게시물_등록():
    # 게시물 1 - insert_one
    한건결과 = col_posts.insert_one(
        {
            "author": "김개발",
            "content": "오늘 MongoDB 공부 시작!",
            "likes": 0,
            "created_at": datetime.now(),
        }
    )
    print("게시물 1 저장 id : ", 한건결과.inserted_id)
    # 데이터 다수 = [  ] 시작   데이터 한 건 = {  }

    여러건결과 = col_posts.insert_many(
        [
            {
                "author": "이몽고",
                "content": "맛집 발견",
                "images": ["img1.jpg", "img2.jpg", "img3.jpg"],
                "likes": 0,
                "comments": [],
                "created_at": datetime.now(),
            },
            {
                "author": "박클라",
                "content": "주말 코딩중",
                "hashtags": ["개발", "파이썬", "mongoDB"],
                "likes": 5,
                "comments": [
                    {"writer": "최데이", "text": "멋지다!"},
                    {"writer": "김개발", "text": "나도 공부해야지"}
                ],
                "created_at": datetime.now(),
            }
        ]
    )


def read_문제1_도서관_books_조회():
    # 1. books 전체 조회
    # find() = select *   col_books = from books
    #         from books   select  *
    #          col_books  .find  (  ):
    for doc in col_books.find():
        print("전체 조회 : ", doc)

    # 2. author 가 "김코딩" 인 책 한 건 조회
    # find_one({"author": "김코딩"})
    # SELECT *   FROM Books WHERE author =  "김코딩"
    doc = col_books.find_one({"author": "김코딩"})
    print("김코딩 한 건 조회 : ", doc)

    # 3. price 가 20000 이상인 책만 조회
    for doc in col_books.find({"price": {"$gte": 20000}}):
        print(f"가격이 20000 이상인데이터 조회 : {doc}")

    # 4. pub_year 기준 최신순(내림차순) 정렬 조회
    for doc in col_books.find().sort("pub_year", -1):
        print(f"최신순 정렬 : {doc}")

    # 5. 가격 낮은 책 2권만 조회 (오름차순 정렬 + limit)
    for doc in col_books.find().sort("price", 1).limit(2):
        print(f"가격 낮은 책 2권만 조회 : {doc}")

    # 6. title, price 필드만 보기 (_id 숨기기)
    for doc in col_books.find({}, {"_id": 0, "title": 1, "price": 1}):
        print(f"title, price 만 조회 : {doc}")

    # 7. books 컬렉션 전체 책 권수 세기
    count = col_books.count_documents({})
    print(f"전체 책 권수 세기 : {count} ")

    # 8. author 가 "홍길동" 인 책 존재 여부 확인 (True/False)
    exists = col_books.find_one({"author": "홍길동"}) is not None
    print(f"홍길동 존재 여부 : {exists}")


def read_문제2_쇼핑몰_product_조회():
    # 1. products 전체 조회
    for doc in col_products.find():
        print("전체 조회 : ", doc)
    # 2. price 가 50000 이상인 상품만 조회
    for doc in col_products.find({"price": {"$gte": 50000}}):
        print("50000 이상 : ", doc)

    # 3. price 기준 내림차순 정렬 조회
    for doc in col_products.find().sort("price", -1):
        print("가격 내림차순 : ", doc)
    # 4. 가장 비싼 상품 1개만 조회
    doc = col_products.find_one({}, sort=[("price", -1)])
    print("가장 비싼 상품 : ", doc)
    # 5. product_name, price 필드만 보기 (_id 숨기기)
    for doc in col_products.find({}, {"_id": 0, "product_name": 1, "price": 1}):
        print("product_name, price 조회 : ", doc)

    # 6. stock 이 50 이하인 상품 개수 세기
    count = col_products.count_documents({"stock": {"$lte": 50}})
    print("stock 50 이하 총 개수 : ", count)
    # 7. 2번째 상품부터 2개만 조회 (skip + limit)
    for doc in col_products.find().skip(1).limit(2):
        print("skip + limit : ", doc)
    # 8. discount_rate 필드가 존재하는 상품만 조회
    for doc in col_products.find({"discount_rate": {"$exists": True}}):
        print("할인 상품 : ", doc)


def read_문제3_SNS_posts_조회():
    # 1. posts 전체 조회
    for doc in col_posts.find():
        print("전체 조회 : ", doc)
    # 2. author 가 "김개발" 인 게시물 한 건 조회
    doc = col_posts.find_one(({"author": "김개발"}))
    print("김개발 한 건 조회 : ", doc)
    # 3. likes 가 1 이상인 게시물만 조회
    # hint : find({"likes": {"$gte": 1}})
    for doc in col_posts.find({"likes": {"$gte": 1}}):
        print("likes 1 이상 인 게시물 : ", doc)
    # 4. likes 기준 내림차순 정렬 조회
    for doc in col_posts.find().sort("likes", -1):
        print("likes 내림차순 : ", doc)
    # 5. author, content, likes 필드만 보기 (_id 숨기기)
    for doc in col_posts.find({}, {"_id": 0, "author": 1, "content": 1, "likes": 1}):
        print("author, content, likes 조회 : ", doc)
    # 6. hashtags 필드가 존재하는 게시물만 조회
    # hint : find({"hashtags": {"$exists": True}})
    for doc in col_posts.find({"hashtags": {"$exists": True}}):
        print("해시태그가 존재하는 게시물만 조회 : ", doc)
    # 7. comments 배열 안에 writer 가 "최데이" 인 게시물 조회
    # hint : find({"comments.writer": "최데이"})
    for doc in col_posts.find({"comments.writer": "최데이"}):
        print("최데이 댓글을 단 게시물만 조회", doc)
    # 8. 전체 게시물 수 세기
    count = col_posts.count_documents({})
    print("전체 게시무 수 : ", count)

read_문제3_SNS_posts_조회()
