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


app.run()



