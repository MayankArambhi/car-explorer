from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, session
from flask_restful import Api
from application.config import Config
from application.database import db

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
app.app_context().push()
app.secret_key = os.environ["SECRET_KEY"]

from application import models
from application import controllers