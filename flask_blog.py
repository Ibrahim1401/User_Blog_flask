from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "546nhhh98"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class users_data(db.Model):
    uid = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    pwd = db.Column(db.String(80))
    date = db.Column(db.String(80))

    def __init__(self, uid, name, pwd):
        self.uid = uid
        self.name = name
        self.pwd = pwd

@app.route("/login",methods=["POST","GET"])
def login():
    userss = {}
    if request.method == "POST" and reques.form.get(type) == 'create':
        session['user'] = request.form["uname"]
        check_user = users_data.query.filter_by(name=session['user']).first()
        if check_user:
            session['uid'] =  request.form['uid']
            session['user'] = request.form['uname']
            session['password'] = request.form['pasw']
            session['date'] = request.form['date']
            if session['password'] != check_user.pwd:
                return render_template("login.html")
        else:
            uid = users_data(uid, "")
            db.session.add(uid)
            name = users_data(name, "")
            db.session.add(name)
            pwd = users_data(pwd, "")
            db.session.add(pwd)
            date = users_data(date, "")
            db.session.add(date)
            db.commit()
        return redirect(url_for("users"))
    elif request.form.get(type) == "delete" and users_data.query.filter_by(name=session['user']).first():
        db.session.delete(request.form['uid'])
        db.session.delete(request.form['name'])
        db.session.delete(request.form['pwd'])
        db.session.delete(request.form['date'])
    else:
        return render_template("login.html")

@app.route("/user")
def users():
    param = {}
    param['uid'] = session['uid']
    param['username'] = session['user']
    param['passwordd'] = session['pasw']
    param['date'] = session['date']
    return render_template("blog.html", param=param)

@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("password",None)
    return redirect(url_for("login"))

if __name__ =="__main__":
    db.create_all()
    app.run(debug=True)
