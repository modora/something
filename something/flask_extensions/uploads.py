from pathlib import Path

import flask_uploads

UPLOAD_SETS = [
    flask_uploads.UploadSet(
        "files",
        flask_uploads.ALL,
        lambda app: Path(app.config.get("DATA_DIR")).joinpath("files"),
    )
]

def configure_upload_sets(app):
    flask_uploads.configure_uploads(app, UPLOAD_SETS)
