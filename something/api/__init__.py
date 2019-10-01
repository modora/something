from . import v1

"""
Ideally, the api version endpoints would be nested blueprints, but that feature
is not supported by flask at this time.

bp = Blueprint("api", "v1", v1.bp, url_prefix="/v1")

"""
