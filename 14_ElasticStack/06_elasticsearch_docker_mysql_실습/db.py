import random
import mysql.connector
from faker import Faker # 가짜 데이터를 만들어주는 라이브러리
# 실제로 DB에 테스트 데이터를 넣을 때 사용
# 50만개를 손으로 입력할 수 없기 때문에 Faker 가 랜덤으로 만들어줌

from tqdm import tqdm # 진행바 만들어주는 라이브러리
# 데이터베이스에서 데이터를 어디까지 insert 하고 있는지 보기위한 표기용

import config # 우리가 만들어준 config.py 파일



fake = Faker("ko_KR")

BRANDS     = ["삼성", "LG", "애플", "나이키", "아디다스", "다이슨", "유니클로", "소니"]
CATEGORIES = ["스마트폰", "노트북", "운동화", "청바지", "청소기", "이어폰", "태블릿", "자켓"]
ADJECTIVES = ["프리미엄", "슬림", "울트라", "프로", "에어", "맥스"]
DESCS      = [
    "최신 기술이 집약된 프리미엄 제품입니다.",
    "인체공학적 설계로 편안한 착용감을 제공합니다.",
    "에너지 효율 1등급으로 전기세 걱정이 없습니다.",
    "초경량 설계로 휴대성을 극대화했습니다.",
]

def get_conn():
    return mysql.connector.connect(**config.MYSQL)

def make_row():
    brand = random.choice(BRANDS)
    cat   = random.choice(CATEGORIES)
    name  = f"{brand} {random.choice(ADJECTIVES)} {cat} {random.randint(1, 9999)}"
    return (
        name, brand, cat,
        random.choice(DESCS),
        round(random.uniform(9900, 2_000_000), 2),
        random.randint(0, 10_000),
        round(random.uniform(1.0, 5.0), 1)
    )

def insert_data():
    print(f"\n[1단계] MySQL {config.TOTAL:,}건 INSERT 시작")
    conn   = get_conn()
    cursor = conn.cursor()
    sql    = """
             INSERT INTO products (name, brand, category, description, price, stock, rating)
             VALUES (%s, %s, %s, %s, %s, %s, %s) \
             """
    done = 0
    with tqdm(total=config.TOTAL, unit="건") as bar:
        while done < config.TOTAL:
            size  = min(config.BATCH_SIZE, config.TOTAL - done)
            batch = [make_row() for _ in range(size)]
            cursor.executemany(sql, batch)
            conn.commit()
            done += size
            bar.update(size)

    cursor.close()
    conn.close()
    print(f"  완료: {done:,}건")


'''
많이 하는 실수 __main__ 에서 __를 제거하고 작성하는 것
__ 파이썬에서 특수하게 명령을 부여한 단어임을 표기
만약  __name__  현재 파일이   __main__ 메인이라면


if __name__ =="__main__": # 이 파일에 개발자가 와서 실행하겠다 라는 버튼을 클릭해야지 insert_data() 실행
    insert_data()
    
insert_data()        # 이 파일이 다른 파일에 import 만 되어도 insert_data() 를 바로 실행!!
'''
if __name__ =="__main__": # import 를 하고 나서 이 기능을 사용하겠다 다른 py 에서 호출해야지 기능 실행하도록 설정
    insert_data()