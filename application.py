from flask import Flask, render_template, request, redirect, url_for
from sql import sql_read
app = Flask(__name__)

@app.route('/')
def index(): # 기본 페이지
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login(): # 로그인 요청
    id = request.form.get('id') # id값 받기
    password = request.form.get('password') # password값 받기
    if sql_read.read(id, password): # mysql 조회
         return render_template("login.html") # True / 성공 페이지
    else:
        return redirect(url_for('index')) # False / 리다이렉트
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)