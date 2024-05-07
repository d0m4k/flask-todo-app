from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "TEST"
# module import 
from .views import views
from .actions import actions
from .auth import auth
# register blueprint
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(actions, url_prefix="/")
app.register_blueprint(auth, url_prefix="/auth")
