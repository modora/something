from flask import Flask as _Flask

from . import api
from . import db
from . import middleware
from . import __about__
from .app_dirs import app_dirs
from . import config

app = _Flask(__name__)

app.register_blueprint(api.v1.bp, url_prefix='/api/v1')
config.loadConfig(app)
