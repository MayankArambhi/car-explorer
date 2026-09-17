from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, session
from application.config import Config
from application.database import db

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config.from_object(Config)
db.init_app(app)
app.secret_key = os.environ["SECRET_KEY"]

from application import models
from application import controllers