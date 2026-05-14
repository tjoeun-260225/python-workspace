import os

class Config:
    MYSQL_USER     = os.getenv("MYSQL_USER",     "appuser")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "apppass")
    MYSQL_HOST     = os.getenv("MYSQL_HOST",     "localhost")
    MYSQL_PORT     = os.getenv("MYSQL_PORT",     "3308") # 3306 → 3308
    MYSQL_DB       = os.getenv("MYSQL_DB",       "userdb")

    SQLALCHEMY_DATABASE_URI = (
        # AI 검색했을 경우 나오는 대표적인 두가지 케이스

        # 1. pip install pymysql
        # 2. pip install mysql-connector-python

        # 파이썬과 mysql 을 사랑한 두 개발자가 만든 모듈 두가지 버전
        # 개발자들이 자주 사용하는 모듈 두가지

        # f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ES_HOST  = os.getenv("ES_HOST", "localhost")
    ES_PORT  = os.getenv("ES_PORT", "9200")
    ES_URL   = f"http://{ES_HOST}:{ES_PORT}"
    ES_INDEX = "users"

    DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    HOST  = "0.0.0.0"
    PORT  = int(os.getenv("PORT", 5000))