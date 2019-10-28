from pathlib import Path
from logging import getLogger

import flask_uploads

from something.utils.uuid import generate_uuid

logger = getLogger(__name__)

def upload(app, request):
    download_dir = app.config.get("DATA_DIR")  # root download dir
    
    file_id = generate_uuid()
    # This will create a class that gives us the ability to save files onto the
    # file system. All saved files will be placed in the "default_dest" folder
    # under the subdirectory specified by the set name. In this case, the files
    # will be stored in $DATA_DIR/files/<filename>
    fileSet = flask_uploads.UploadSet(
        "files", extensions=flask_uploads.ALL, default_dest=download_dir
    )
    filename = fileSet.save(
        request.files["file"], name=f"{file_id}."
    )

    logger.debug(f'Uploaded file: {filename}')


    return {"file_id": file_id}
