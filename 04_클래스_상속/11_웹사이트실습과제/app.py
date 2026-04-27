from flask import Flask, render_template
from 상품서비스 import 상품서비스

app = Flask(__name__)
서비스 = 상품서비스()

@app.route("/")
def 메인페이지():
    상품목록 = 서비스.전체조회()
    return render_template("index.html", 상품들=상품목록)

@app.route("/상품/<__:id>")
def 상세페이지(id):
    상품 = 서비스.상세조회(id)
    return render_template("detail.html", 상품=상품)

app.run()