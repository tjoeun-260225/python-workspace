import random
import psycopg2
from faker import Faker
from tqdm import tqdm
import config

fake = Faker("ko_KR")

BRANDS = ["삼성", "LG", "애플", "나이키", "아디다스", "다이슨", "유니클로", "소니"]
CATEGORIES = ["스마트폰", "노트북", "운동화", "청바지", "청소기", "이어폰", "태블릿", "자켓"]
ADJECTIVES = ["프리미엄", "슬림", "울트라", "프로", "에어", "맥스"]
DESCS = [
    "최신 기술이 집약된 프리미엄 제품입니다.",
    "인체공학적 설계로 편안한 착용감을 제공합니다.",
    "에너지 효율 1등급으로 전기세 걱정이 없습니다.",
    "초경량 설계로 휴대성을 극대화했습니다.",
]


def get_conn():
    return psycopg2.connect(**config.POSTGRES)


def make_row():
    brand = random.choice(BRANDS)
    cat = random.choice(CATEGORIES)
    name = f"{brand} {random.choice(ADJECTIVES)} {cat} {random.randint(1, 9999)}"
    return (
        name, brand, cat,
        random.choice(DESCS),
        round(random.uniform(9900, 2_000_000), 2),
        random.randint(0, 10_000),
        round(random.uniform(1.0, 5.0), 1)
    )


def insert_data():
    print(f"\n[1단계] PostgreSQL {config.TOTAL:,}건 INSERT 시작")
    conn = get_conn()
    cursor = conn.cursor()
    sql = """
          INSERT INTO products (name, brand, category, description, price, stock, rating)
          VALUES (%s, %s, %s, %s, %s, %s, %s) \
          """
    done = 0
    with tqdm(total=config.TOTAL, unit="건") as bar:
        while done < config.TOTAL:
            size = min(config.BATCH_SIZE, config.TOTAL - done)
            batch = [make_row() for _ in range(size)]
            cursor.executemany(sql, batch)
            conn.commit()
            done += size
            bar.update(size)

    cursor.close()
    conn.close()
    print(f"  완료: {done:,}건")


if __name__ == "__main__":
    insert_data()
