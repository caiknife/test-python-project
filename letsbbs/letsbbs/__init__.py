# -*- encoding:utf-8 -*-
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from letsbbs.helpers import register_blueprint
import settings
from .models import db

app = Flask(__name__)

register_blueprint(app)

app.config.from_object(settings)

app.debug = True
toolbar = DebugToolbarExtension(app)

db.init_app(app)
db.app = app

__all__ = [
    'app', 'db', 'toolbar'
]