from flask import Blueprint, request, render_template, session, redirect, url_for
from .Model import Model

auth = Blueprint("auth", __name__)

def is_user(email, password):
    model = Model()
    user = model.user(email, password)
    if user:
        return user
    return None


@auth.route("/signup", methods=["POST", "GET"]) 
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        model = Model()
        current_user = model.createUser(username, email, password)
        model.close()
        current_user = {
            "user_id": current_user[0],
            "username": current_user[1],
        }
        session["current_user"] = current_user
        return redirect(url_for("views.index"))
    return redirect(url_for("views.signup_view"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        current_user = is_user(email, password)
        if current_user:
            current_user = {
            "user_id": current_user[0],
            "username": current_user[1],
            }
            session["current_user"] = current_user
            return redirect(url_for("views.index"))
        return redirect(url_for("views.login_view", message="Invalid Username or Password"))


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("views.signup_view"))