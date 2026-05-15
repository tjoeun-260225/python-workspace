# application.properties
import os # 운영체제 = 맥북이나 윈도우에 필요한 환경에 대하여 세팅

class Config: # public class Confing{}
    # 나의컴퓨터에.세팅된설정가져오기("컴퓨터에세팅된변수이름","변수이름이 없으면 기본값으로 사용")
    #           os.getenv           ("    MYSQL_USER       ", "            appuser            ")
    MYSQL_USER     = os.getenv("MYSQL_USER",     "appuser")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "apppass")
    MYSQL_HOST     = os.getenv("MYSQL_HOST",     "localhost")
    MYSQL_PORT     = os.getenv("MYSQL_PORT",     "3308")
    MYSQL_DB       = os.getenv("MYSQL_DB",       "orderdb")
    # 위에서 모은 값들로 MySQl을 접속하고
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )
    # mysql+mysqlconnector://appuser:apppass@localhost:3308/orderdb
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB 변경사항 추적하게 되면 계속 경고 메세지가 뜨고 속도 느려짐  그래서 보통 꺼서 사용
    # MySQL을 python에 연동처리한 개발자는 경고를 우선 추적했으면 하는 바램
    ES_HOST  = os.getenv("ES_HOST", "localhost")
    ES_PORT  = os.getenv("ES_PORT", "9200")
    ES_URL   = f"http://{ES_HOST}:{ES_PORT}"
    ES_INDEX = "orders"

    DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    # 웹사이트에서 문제가 있는가 없는가 추적
    HOST  = "0.0.0.0" # 나의 컴퓨터에서 웹사이트를 개발함에 있어 문제가 없도록 접속 허용처리
    PORT  = int(os.getenv("PORT", 5000))
    # Flask 기본 포트가 5000 이지만, 개발자가 원하는 포트로 변경하고 싶다면 변경가능