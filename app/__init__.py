from flask import Flask

app = Flask(__name__)

# module import 
from .views import views
from .actions import actions
# register blueprint
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(actions, url_prefix="/")

