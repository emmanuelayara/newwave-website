from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

class user(db.Model, UserMixin):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column[db.string(20)], nullable=False
    password = db.Column[db.string(80)], nullable=False

@app.route("/")
def newwave():
    return render_template ("home.html")

@app.route("/feed")
def feed():
    return render_template ("feed.html")

@app.route("/jobs")
def jobs():
    return render_template ("jobs.html")

@app.route("/login")
def login():
    return render_template ("login.html")

@app.route("/register")
def register():
    return render_template ("register.html")

@app.route("/profile")
def profile():
    return render_template ("profile.html")

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)