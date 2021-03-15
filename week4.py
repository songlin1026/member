from flask import Flask  #載入Flask模組
from flask import request #載入request物件
from flask import redirect #載入redirect 函式
from flask import render_template
from flask import session
from flask import url_for

app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def homePage():
    if session.get('username')=='name':
        print("使用者已登入")
        return redirect("/member")
    print("使用者未登入")
    return render_template("homePage.html")

@app.route("/signin",methods=["POST"])
def logIn():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test":
        session['username']='name'
        print("使用者已登入")
        return redirect("/member")
    else:
        print("使用者未登入")
        return redirect("/error")

@app.route("/member")
def member():
    if session.get('username')=='name':
        print("使用者已登入")
        return render_template("member.html")
    print("使用者未登入")
    return redirect("/")

@app.route("/error")
def error():
    if session.get('username')=='name':
        print("使用者已登入")
        return render_template("member.html")
    return render_template("error.html")


@app.route("/signout")
def signout():
        session['username'] = False
        return render_template("signout.html")

app.run(port=3000)