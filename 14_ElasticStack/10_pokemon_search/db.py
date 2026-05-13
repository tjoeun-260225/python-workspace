import pymysql
import requests
import config


def get_conn():
    return pymysql.connect(
        host=config.MYSQL["host"],
        port=config.MYSQL["port"],
        user=config.MYSQL["user"],
        password=config.MYSQL["password"],
        database=config.MYSQL["database"],
        charset="utf8mb4"
    )


def create_table():
    print("[1단계] MySQL 테이블 생성")
    conn   = get_conn()
    cursor = conn.cursor()

    sql = """
          CREATE TABLE IF NOT EXISTS pokemons (
                                                  id        INT          PRIMARY KEY,
                                                  name      VARCHAR(100),
                                                  height    INT,
                                                  weight    INT,
                                                  type1     VARCHAR(50),
                                                  type2     VARCHAR(50),
                                                  base_exp  INT
          ) \
          """

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("  완료")


def fetch_from_api():
    print(f"\n[2단계] PokeAPI에서 포켓몬 {config.TOTAL_POKEMON}마리 가져오기")
    pokemons = []

    for i in range(1, config.TOTAL_POKEMON + 1):
        url  = f"{config.POKEAPI_URL}/{i}"
        resp = requests.get(url)
        data = resp.json()

        type2 = data["types"][1]["type"]["name"] if len(data["types"]) > 1 else None

        pokemon = {
            "id":       data["id"],
            "name":     data["name"],
            "height":   data["height"],
            "weight":   data["weight"],
            "type1":    data["types"][0]["type"]["name"],
            "type2":    type2,
            "base_exp": data["base_experience"],
        }
        pokemons.append(pokemon)

        if i % 50 == 0:
            print(f"  {i}마리 완료...")

    print(f"  총 {len(pokemons)}마리 수집 완료")
    return pokemons


def insert_pokemons(pokemons: list):
    print(f"\n[3단계] MySQL INSERT ({len(pokemons)}건)")
    conn   = get_conn()
    cursor = conn.cursor()

    sql = """
          INSERT IGNORE INTO pokemons (id, name, height, weight, type1, type2, base_exp)
          VALUES (%s, %s, %s, %s, %s, %s, %s) \
          """

    for p in pokemons:
        cursor.execute(sql, (
            p["id"], p["name"], p["height"],
            p["weight"], p["type1"], p["type2"], p["base_exp"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print("  완료")


def fetch_all():
    conn   = get_conn()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM pokemons")
    return cursor.fetchall()