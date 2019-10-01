from flask import Flask as _Flask

from . import api

app = _Flask(__name__)

app.register_blueprint(api.v1.bp, url_prefix='/api/v1')
