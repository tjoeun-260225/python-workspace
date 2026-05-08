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

    여러건결과 =col_posts.insert_many(
        [
            {
                "author": "이몽고",
                "content": "맛집 발견",
                "images": ["img1.jpg","img2.jpg","img3.jpg"],
                "likes": 0,
                "comments": [] ,
                "created_at": datetime.now() ,
            },
            {
                "author": "박클라",
                "content": "주말 코딩중",
                "hashtags": ["개발","파이썬","mongoDB"],
                "likes": 5,
                "comments": [
                    {"writer":"최데이", "text":"멋지다!"},
                    {"writer":"김개발", "text":"나도 공부해야지"}
                ] ,
                "created_at": datetime.now() ,
            }
        ]
    )
insert_문제3_SNS_게시물_등록()
