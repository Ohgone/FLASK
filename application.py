from flask import Flask, render_template, request, redirect, url_for, flash
from sql import sql_read, sql_create
app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"

@app.route('/')
def index(): # 기본 페이지
    return render_template("index.html")

@app.route('/signup')
def signup(): # 회원가입 페이지
    return render_template("signup.html")

@app.route('/login', methods=['POST'])
def login(): # 로그인 요청
    id = request.form.get('id') # id값 받기
    password = request.form.get('password') # password값 받기
    if sql_read.read(id, password): # mysql 조회
        name = sql_read.read_name(id)
        print(name)
        return render_template("login.html", name=name) # True / 성공 페이지
    else:
        flash("로그인 정보가 없습니다.")
        return render_template("alert.html")
        # return redirect(url_for('index')) # False / 리다이렉트

@app.route('/signupreq', methods=['POST'])
def signupreq(): # 회원가입 요청
    name = request.form.get('name') # name값 받기
    id = request.form.get('id') # id값 받기
    password = request.form.get('password') # password값 받기
    password_check = request.form.get('password_check') # password_check값 받기
    if password != password_check: # password, password_check 일치여부 확인
        flash("비밀번호가 일치하지 않습니다.")
        return render_template("alert.html")
        # return redirect(url_for('signup')) # 일치하지 않으면 회원가입창으로
    else:
        sql_create.create(name, id, password) # 일치하면 DB에 데이터 생성 후 
        return redirect(url_for('index')) # 메인홈페이지로 REDIRECT
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)