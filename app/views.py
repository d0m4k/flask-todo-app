from flask import Blueprint, render_template, session, request
from .Model import Model

views = Blueprint("views", __name__)

@views.route("/") # 127.0.0.1:5000
def index():
    if "current_user" in session:
        current_user = session["current_user"]
        model = Model()
        my_todos = model.viewTodos()
        model.close()
        return render_template("index.html", my_todos=my_todos, current_user=current_user)
    return render_template("signup.html")

@views.route("/signup")
def signup_view():
    return render_template("signup.html")

@views.route("/login")
def login_view():
    return render_template("login.html")

@views.route("/getuser")
def getuser():
    user_id = request.args.get("user_id")
    model = Model()
    print(model.getByUserID(user_id))
    return f"user found"