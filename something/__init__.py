from flask import Flask as _Flask

from . import api
from . import db
from . import middleware
from . import __about__
from . import config

app_dirs = __about__.app_dirs

app = _Flask(__name__)

app.register_blueprint(api.v1.bp, url_prefix='/api/v1')
