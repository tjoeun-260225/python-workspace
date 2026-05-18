"""
앱 = 어플리케이션 = 개발자가 만든 모~든 프로젝트
17 폴더 프로젝트 시작 구조

1. 시작점 - docker-compose up(최초 1회 실행해줌)
   실행 후 desktop 에 설치된 도커에서 ▷ 재생 버튼 클릭하기
   │
   ├─→ MySQL :3308 컨테이너 시작
   │    └── mysql_init/init.sql 자동 실행 (테이블 생성)
   │
   ├─→ Elasticsearch :9200 컨테이너 시작
   │    └── healthcheck 통과 대기
   │
   ├─→ Kibana :5601 컨테이너 시작
   │    └── ES healthcheck 통과 후에 시작(depends_on) 엘라스틱서치로 기록된 데이터 시각화 관리자페이지 조회)
   │
   └─→ Filebeat : 컨테이너 시작
        └── ES healthcheck 통과 후에 시작(depends_on) 엘라스틱서치로 기록된 데이터 연결 확인 후 조회)
        └── filebeat.yml 읽고 logs/app.log 감시 시작

2. Flask 앱 (run.py) 시작
   │
   ├─ create_app()
   │    ├── Flask() 앱 객체 생성
   │    ├── config.py 읽기
   │    │     └─ MYSQL_USER, ES_HOST 등 환경변수 로딩
   │    ├─ db.init_app(app)
   │    │     └─ db.py 의 SQLAlchemy 객체에 앱 연결
   │    └─ register_blueprint(routes)
   │          └─ routes.py 의 URL 등록
   │
   └─ app.app_context() 안에서
        ├── db.create_all()
        │     └─ models.py 읽어서 MySQL 테이블 생성
        │           ├─ User → mysql 에 users 테이블생성
        │           ├─ Product → mysql 에 products 테이블생성
        │           └─ Order → mysql 에 orders 테이블생성
        ├── es_service.ensure_index()
        │     └─ es_client.py → ES에 orders 인덱스 + 매핑 생성
        └── app.run(host, port, debug)
              └─ Flask 웹서버 :5000 오픈

전체 구조 (Filebeat 추가 후)
Flask 앱(run.py) - 관리자(= 회사 소속이나 개발자)가 회사 사이트를 접속하는 클라이언트를 확인하기 위한 구조
   └── JSON 로그 파일 기록(/logs/app.log)
       └── Filebeat (파일 감시)
           └── Elasticsearch :9200
               └── Kibana :5601 (로그 시각화)

관리자 확인용 로그와 분석페이지에 새로 만들 파일과, 수정할 파일들 작성
17_웹사이트코드_기본틀정리/
├── logs/                  ← 새로 생김 (logger.py가 자동 생성)
│   └── app.log            ← Flask가 기록, Filebeat가 읽음
├── logger.py              ← 새로 만든 파일
├── filebeat.yml           ← 새로 만든 파일
├── docker-compose_flask.yml     ← filebeat 서비스 추가
├── config.py
├── db.py
├── es_client.py
├── models.py
├── routes.py
└── run.py
"""

import time
from flask import Flask
from config import Config
from db import db
from routes import routes
import es_client as es_service


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(routes)
    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        for attempt in range(10):
            try:
                db.create_all()
                es_service.ensure_index()
                print("DB & ES 준비 완료")
                break
            except Exception as e:
                print(f"연결 대기 중... ({attempt + 1}/10): {e}")
                time.sleep(5)

    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)