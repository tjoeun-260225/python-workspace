from flask import Flask, render_template
# 택 1  서비스 = 회원서비스()            작성하고 싶을 때
# from 회원서비스 import 회원서비스
# 택 2  서비스 = 회원서비스.회원서비스() 작성하고 싶을 때
# import 회원서비스

from 회원서비스 import 회원서비스

app = Flask(__name__)
서비스 = 회원서비스()


@app.route("/")
def 메인페이지():
    회원목록 = 서비스.전체조회()
    return render_template("index.html", 회원들=회원목록)

@app.route("/회원/<int:id>")
# <이메일> = 주소에서 데이터를 받아오는 것
# http://127.0.0.1:5000/회원/hong@test.com 이렇게 접속하면
# 이메일 변수에 hong@test.com 이 담김
def 상세페이지(id):
    회원 = 서비스.상세조회(id)
    return render_template("detail.html", 회원=회원)

app.run()



