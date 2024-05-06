from flask import Blueprint, render_template
from .Model import Model

views = Blueprint("views", __name__)

@views.route("/") # 127.0.0.1:5000
def index():
    model = Model()
    my_todos = model.viewTodos()
    model.close()
    return render_template("index.html", my_todos=my_todos)

