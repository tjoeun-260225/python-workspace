import pymysql
import pandas as pd
from config import MYSQL_CONFIG, CSV_PATH


def get_connection():
    return pymysql.connect(**MYSQL_CONFIG)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books
                   (
                       id         INT AUTO_INCREMENT PRIMARY KEY,
                       rank       INT,
                       reg_no     VARCHAR(100),
                       title      VARCHAR(500),
                       author     VARCHAR(300),
                       publisher  VARCHAR(200),
                       call_no    VARCHAR(200),
                       loan_count INT
                   )
                   """)

    conn.commit()
    cursor.close()
    conn.close()
    print("테이블 생성 완료")


def insert_csv_to_mysql():
    df = pd.read_csv(CSV_PATH, encoding="cp949", header=1)

    df = df.rename(columns={
        "순위": "rank",
        "등록번호": "reg_no",
        "서명": "title",
        "저자": "author",
        "발행자": "publisher",
        "청구기호": "call_no",
        "대출횟수": "loan_count",
    })

    df = df[["rank", "reg_no", "title", "author", "publisher", "call_no", "loan_count"]]

    df["rank"] = df["rank"].fillna(0).astype(int)
    df["loan_count"] = df["loan_count"].fillna(0).astype(int)
    df = df.fillna("")

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
                       INSERT INTO books (rank, reg_no, title, author, publisher, call_no, loan_count)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                       """, (
                           row["rank"], row["reg_no"], row["title"],
                           row["author"], row["publisher"], row["call_no"], row["loan_count"]
                       ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"MySQL 저장 완료: {len(df)}건")


def fetch_all_books():
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
