from .Model import Model
from flask import Blueprint, request, redirect, url_for, session

actions = Blueprint("actions", __name__)

@actions.route("/add-todo", methods=["POST"])
def add_todo():
    if request.method == "POST":
        text = request.form["todo-text"]
        model = Model()
        current_user = session["current_user"]
        model.insert(text, current_user["user_id"])
        model.close()
        return redirect(url_for("views.index"))

@actions.route("/delete") # /delete?id=1
def delete_todo():
    if "current_user" in session:
        todo_id = request.args.get("id")
        model = Model()
        model.delete(todo_id)
        return redirect(url_for("views.index"))
    return "Unauthorized"

@actions.route("/edit", methods=["POST"])
def edit_todo():
    if request.method == 'POST':
        if "current_user" in session:
            edit_data = request.get_json()
            model = Model()
            model.update(int(edit_data["todo_id"]), edit_data["edit_text"])
            model.close()
            return redirect(url_for("views.index"))
    