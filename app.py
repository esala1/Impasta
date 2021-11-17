# pylint: disable=no-member
# pylint: disable=too-few-public-methods
import os
import json
import random
import flask
from flask import Flask, redirect, render_template, request, url_for, jsonify
from places import nearby_restaurants
from documenu import get_restaurant_id, get_restaurant_info
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from flask_login import (
    login_user,
    current_user,
    LoginManager,
    UserMixin,
    login_required,
    logout_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


load_dotenv(find_dotenv())

app = Flask(__name__, static_folder="./build/static")
# Point SQLAlchemy to your Heroku database
url = os.getenv("DATABASE_URL")
if url and url.startswith("://"):
    url = url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = url

# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv("APP_SECRET_KEY")

db = SQLAlchemy(app)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __repr__(self):
        return f"<User {self.username}>"

    def get_username(self):
        return self.username


db.create_all()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return Users.query.get(user_name)


bp = flask.Blueprint("bp", __name__, template_folder="./build")


@bp.route("/index")
@login_required
def index():

    url = "http://ipinfo.io/json"

    response = urlopen(url)
    data = json.load(response)

    nearby_restaurants_list = nearby_restaurants(data["ip"])

    data = json.dumps(
        {
            "username": current_user.username,
            "page": "homepage",
            "restaurants": nearby_restaurants_list,
        }
    )
    return render_template(
        "index.html",
        data=data,
    )


@bp.route("/menu/<restaurant_name>/<restaurant_address>")
@login_required
def menu(restaurant_name, restaurant_address):
    restaurant_id = get_restaurant_id(restaurant_name, restaurant_address)
    restaurant_data = get_restaurant_info(restaurant_id)

    data = json.dumps(
        {
            "username": current_user.username,
            "page": "menu",
            "restaurant_name": restaurant_name,
            "restaurant_address": restaurant_address,
            "foodItems": restaurant_data,
        }
    )
    return render_template(
        "index.html",
        data=data,
    )


app.register_blueprint(bp)


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    username = request.form.get("username")
    password = request.form.get("password")
    user = Users.query.filter_by(username=username).first()
    if user:
        return render_template("signup.html", user_exists=True)
    add_user(username, password)

    return redirect(url_for("login"))


def add_user(username, password):
    password_hash = generate_password_hash(password, method="sha256")
    user = Users(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()


@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("bp.index"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    user = Users.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password.strip()):
        login_user(user)
        return redirect(url_for("bp.index"))
    return render_template("login.html", invalid_credentials=True)


@app.route("/")
def main():
    if current_user.is_authenticated:
        return redirect(url_for("bp.index"))
    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "8081")),
    )
