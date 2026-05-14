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
