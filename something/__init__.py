__name__ = "something"
__author__ = "modora"
__version__ = "0.1"


from flask import Flask as _Flask

from . import api
from . import db
from . import middleware
from . import config
from . import logger as _logger
from . import flask_extensions as _flask_extensions

app = _Flask(__name__)

config.loadConfig(app)
logger = _logger.configure_logger(app, __name__)
_flask_extensions.uploads.configure_upload_sets(app)

app.register_blueprint(api.v1.bp, url_prefix="/api/v1")
