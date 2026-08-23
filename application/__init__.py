from flask import Flask
from flask_restful import Api
from application.config import Config
from application.database import db

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
app.app_context().push()

from application import models
from application import controllers