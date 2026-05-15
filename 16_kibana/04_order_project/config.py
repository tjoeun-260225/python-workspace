import os
# application.properties
class Config:
    MYSQL_USER     = os.getenv("MYSQL_USER",     "appuser")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "apppass")
    MYSQL_HOST     = os.getenv("MYSQL_HOST",     "localhost")
    MYSQL_PORT     = os.getenv("MYSQL_PORT",     "3308")
    MYSQL_DB       = os.getenv("MYSQL_DB",       "orderdb")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ES_HOST  = os.getenv("ES_HOST", "localhost")
    ES_PORT  = os.getenv("ES_PORT", "9200")
    ES_URL   = f"http://{ES_HOST}:{ES_PORT}"
    ES_INDEX = "orders"

    DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    HOST  = "0.0.0.0"
    PORT  = int(os.getenv("PORT", 5000))