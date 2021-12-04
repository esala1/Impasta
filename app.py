# pylint: disable=no-member
# pylint: disable=too-few-public-methods
"""
This is the main file that runs to display the website to user. It uses Flask and its functions
to provide website functionality to the user. It consists of multiple routes that a user will
visit during their time on the website.
"""
import os
import json
import flask
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv, find_dotenv
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
from places import nearby_restaurants
from documenu import get_restaurant_id, get_restaurant_info
from search import searchRestaurant


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
    """
    Database Table called Users that stores information about the users using the website.
    It includes id, username, and password columns where id is unique and is set as primary key
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __repr__(self):
        return f"<User {self.username}>"

    def get_username(self):
        """This function returns the username"""
        return self.username


class Foods(db.Model):
    """
    Database table called Foods that stores information about the foods that a user saves.
    It includes id, username, foodname and price columns where id is unique and is set as
    primary key
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    foodname = db.Column(db.String(120))
    price = db.Column(db.String(120))

    def __repr__(self):
        return f"<Username: {self.username}, Restaurant Name: {self.foodname}>"

    def get_username(self):
        """This function returns the username and foodname"""
        return self.username, self.foodname


if os.getenv("DATABASE_URL") is not None:
    db.create_all()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    """placeholder"""
    return Users.query.get(user_name)


bp = flask.Blueprint("bp", __name__, template_folder="./build")


@bp.route("/index")
@login_required
def index():
    """
    This function serves as homepage that a user is redirected to after logging in. The page
    displays restaurants near the user so he or she can view more information about each
    restaurant including address, rating, menu, etc.
    """

    if not request.headers.getlist("X-Forwarded-For"):
        ip_value = request.remote_addr
    else:
        ip_value = request.headers.getlist("X-Forwarded-For")[0]

    print("ip address", ip_value)
    nearby_restaurants_list = nearby_restaurants(ip_value)
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


@bp.route("/search", methods=["POST"])
def search():
    """
    This function calls the Google Maps API to search for user specified input
    through searchRestaurant function. Then, sends data to react frontend to display
    the results to the user.
    """
    search_input = flask.request.json.get("search_input")
    print("search input", search_input)
    search_restaurant_list = searchRestaurant(search_input)
    return flask.jsonify({"search_restaurant_list": search_restaurant_list})


@bp.route("/menu/<restaurant_name>/<restaurant_address>")
@login_required
def menu(restaurant_name, restaurant_address):
    """
    This function calls the Documenu API through get_restaurant_id and get_restaurant_info
    functions. Then, sends the data to React frontend so that the menu items are displayed
    to the user.
    """
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


@app.route("/favorite-foods")
@login_required
def favorite_foods():
    """
    This function reads all the food items stored by a user in the database and sends
    the data to React frontend so that they can be displayed.
    """
    error = False
    username = current_user.username
    food_data = Foods.query.filter_by(username=username).all()
    food_names = []
    food_prices = []
    for food in food_data:
        food_names.append(food.foodname)
        food_prices.append(food.price)

    username = username[0].upper() + username[1:]
    if len(food_data) == 0:
        return render_template(
            "favorites.html", no_saved_artists=True, username=username
        )

    return render_template(
        "favorites.html",
        food_data=zip(food_names, food_prices),
        username=username,
        error=error,
    )


@app.route("/save", methods=["POST"])
@login_required
def save():
    """
    This function saves a user's favorite food items sent from the react frontend into database.
    """
    favorite_food_items = flask.request.json.get("favoriteFoods")
    username = current_user.username
    existing_food_items = [
        food.foodname for food in Foods.query.filter_by(username=username).all()
    ]

    new_food_items = []
    for food in favorite_food_items:
        if food["name"] not in existing_food_items:
            if food["name"] not in new_food_items:
                new_food_items.append(food["name"])
                db.session.add(
                    Foods(foodname=food["name"], price=food["price"], username=username)
                )

    db.session.commit()
    return {"status": "success"}

@app.route("/guide")
@login_required
def guide():
    return render_template("guide.html")

@app.route("/delete-action", methods=["GET", "POST"])
@login_required
def delete_artist():
    """
    This function deletes a user chosen artist from the database.
    """
    if request.method == "POST":
        username = current_user.username
        food_name = request.form.get("food_name")

        db.session.query(Foods).filter_by(
            username=username, foodname=food_name
        ).delete()

        db.session.commit()
    return redirect("/favorite-foods")


@app.route("/signup")
def signup():
    """
    This function displays the signup page to the user so that he or she can create an account
    and use the website.
    """
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    """
    This function allows the user to create an account using the input username and password fields.
    If an account is successfully created, the user is redirected to login. If not, a message
    indicating that a username already exists is shown to user, and he or she needs to use a
    different one.
    """
    username = request.form.get("username")
    password = request.form.get("password")
    user = Users.query.filter_by(username=username).first()
    if user:
        return render_template("signup.html", user_exists=True)
    add_user(username, password)

    return redirect(url_for("login"))


def add_user(username, password):
    """A helper function that adds a user to the database given their username and password."""
    password_hash = generate_password_hash(password, method="sha256")
    user = Users(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()


@app.route("/login")
def login():
    """
    This is an alternative endpoint to '/'. It achieves the same purpose - checks
    if the user is logged in or not. If logged in, he or she is directed to bp.index page.
    If not, he or she is directed to login page.
    """
    print(request.headers.getlist("X-Forwarded-For"))
    print(request.remote_addr)
    if current_user.is_authenticated:
        return redirect(url_for("bp.index"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """
    The function gets the user inputs of username and password. Checks if the user exists in
    the database or not. If the user exists, then he or she is directed to the homepage (bp.index).
    If not, then he or she is redirected to the login page with an error that says invalid username
    or password.
    """
    username = request.form.get("username")
    password = request.form.get("password")
    user = Users.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password.strip()):
        login_user(user)
        return redirect(url_for("bp.index"))
    return render_template("login.html", invalid_credentials=True)


@app.route("/")
def main():
    """
    This function directs a user to the login page if they are not logged in
    and the homepage (i.e., bp.index) if they are already logged in.
    """
    if current_user.is_authenticated:
        return redirect(url_for("bp.index"))
    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    """
    The function uses logout_user from flask login to logout the user. After a user is logged out,
    he or she is redirected to the login page which serves as the default page for users
    who are not logged in.
    """
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "8081")),
    )
