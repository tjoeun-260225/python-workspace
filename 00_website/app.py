'''
파이썬으로 기초 웹 만들기

from ~~~ import ~~, ~  = ~~~에서 ~~, ~ 를 가져와서 사용하겠다.

from = 가져온 flask 기능에서    import = 이 기능들을 사용하겠다.
    Flask = 웹 서버 만드는 기능
    render_template = templates 에 존재하는 .html 파일 보여주는 기능

'''
from flask import Flask, render_template
# __name__ = 현재 app.py 에 존재하는 파일 위치를 Flask 에게 알려주는 것
# Flask(__name__)  = 현재 app.py 파일을 기준으로 웹 서버를 생성하겠다.
# 이러한 모든 정보를 app 이라는 변수 공간에 담아두겠다.
app = Flask(__name__)


@app.route("/") # "/" 주소로 접속하면 바로 아래에 존재하는 기능을 실행하기  app 변수안에 등록
def 메인페이지():
    return  render_template("index.html") # templates 폴더 안에 있는 index.html 파일을 브라우저에게 보여줘

# .html 파일은 서버를 실행할 능력이 없다.
# app.py 라는 파일로 위치해서 실행하기
app.run() # 위 내용을 바탕으로 서버를 실행하겠다.