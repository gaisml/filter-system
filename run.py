from flask import Flask,render_template, redirect,url_for,logging,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/Reglogsys'
db = SQLAlchemy(app)


class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route('/',methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form['fullname']
        city = request.form['city']
        phone_no = request.form['phone']
        uname = request.form['uname']
        passw = request.form['passw']

        register = User(fullname=fname,city=city,phone_no=phone_no,username=uname,password=passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = User.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("home"))
    return render_template("login.html")


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
