import flask

from . import collections
from . import files
from . import user

from flask import jsonify, request  # delete this later, placeholder responses

bp = flask.Blueprint("v1", __name__)

# Get a summary of all files in the archive
@bp.route("/files", methods=["GET"])
@bp.route("/metadata/files", methods=["GET"])
def get_file_summary():
    return jsonify({"num_files": 1, "size": 2})


# Get metadata summary for all collections
@bp.route("/metadata/collections", methods=["GET"])
@bp.route("/collections", methods=["GET"])
def get_collection_summary():
    return jsonify({"num_coll": 3})


# Get metadata for the "files" collection
@bp.route("/collections/files", methods=["POST"])
def get_file_collection_metadata():
    return jsonify({"coll_id": "01234567"})


# Get metadata for the "collections" collection
@bp.route("/collections/collections", methods=["GET"])
def get_collection_collection_metadata():
    return jsonify({"coll_id": "1234567", "name": "collection_name", "items": []})


# Get a list of files in the archive
@bp.route("/collections/files/items", methods=["GET"])
def get_file_list():
    return jsonify({"items": ["item1", "item2"]})


# Get the list of collections in the archive
@bp.route("/collections/collections/items", methods=["GET"])
def get_collection_list():
    return jsonify({"items": ["item1", "item2"]})


# Upload a new file into the archive
@bp.route("/files", methods=["POST"])
@bp.route("/collections/files/items", methods=["POST"])
def upload_file():
    app = flask.current_app
    request = flask.request
    return jsonify(files.upload(app, request))


# Deletes a file from the archive
@bp.route("/files/<file_id>", methods=["DELETE"])
@bp.route("/collections/files/items/<file_id>", methods=["DELETE"])
def delete_file(file_id):
    return jsonify({"return_code": 0})


# Create a new collection
@bp.route("/collections", methods=["POST"])
@bp.route("/collections/collections/items", methods=["POST"])
def create_new_collection():
    return jsonify({"coll_id": "01234567"})


# Delete a collection
@bp.route("/collections/collections/items/<coll_id>", methods=["DELETE"])
@bp.route("/collections/<coll_id>", methods=["DELETE"])
def delete_collection(coll_id):
    return jsonify({"return_code": 0})


# Get a list of items in the collection
@bp.route("/collections/<coll_id>/items", methods=["GET"])
def get_collection_items(coll_id):
    return jsonify({"items": ["item1", "item2"]})


# Add a new item to the collection
@bp.route("/collections/<coll_id>/items", methods=["POST"])
def add_collection_item(coll_id):
    return jsonify({"item_id": "01234567"})


# Remove an item from the collection
@bp.route("/collections/<coll_id>/items/<item_id>", methods=["DELETE"])
def delete_collection_item(coll_id, item_id):
    return jsonify({"coll_id": coll_id, "item_id": item_id, "return_code": 0})


# Get file metadata
@bp.route("/files/<file_id>")
@bp.route("/metadata/files/file_id")
def get_file_metadata(file_id):
    return jsonify({"item_of": ["coll_id1"]})


# Set file metadata
@bp.route("/files/<file_id>/metadata", methods=["POST"])
@bp.route("/metadata/files/<file_id>", methods=["POST"])
def set_file_metadata(file_id):
    return jsonify({"file_id": file_id, "key1": "value1", "key1.key3": "value3"})


# Modify file metadata
@bp.route("/files/<file_id>/metadata", methods=["PUT"])
@bp.route("/metadata/files/<file_id>", methods=["PUT"])
def update_file_metadata(file_id):
    return jsonify({"coll_id": file_id, "key": "value"})


# Delete file metadata
@bp.route("/files/<file_id>/metadata", methods=["DELETE"])
@bp.route("/metadata/files/<file_id>", methods=["DELETE"])
def delete_file_metadata(file_id):
    return jsonify({"return_code": 0, "deleted_keys": ["key1"]})


# Get collection metadata
@bp.route("/collections/<coll_id>", methods=["GET"])
@bp.route("/metadata/collections/<coll_id>", methods=["GET"])
def get_collection_metadata(coll_id):
    return jsonify({"coll_id": "123456", "name": "collection_name", "items": []})


# Set collection metadata
@bp.route("/collections/<coll_id>/metadata", methods=["POST"])
@bp.route("/metadata/collections/<coll_id>", methods=["POST"])
def set_collection_metadata(coll_id):
    return jsonify({"coll_id": coll_id, "key": "value"})


# Modify collection metadata
@bp.route("/collections/<coll_id>/metadata", methods=["PUT"])
@bp.route("/metadata/collections/<coll_id>", methods=["PUT"])
def update_collection_metadata(coll_id):
    return jsonify({"coll_id": coll_id, "key": "value"})


# Delete collection metadata
@bp.route("/collections/<coll_id>/metadata", methods=["DELETE"])
@bp.route("/metadata/collections/<coll_id>", methods=["DELETE"])
def delete_collection_metadata(coll_id):
    return jsonify({"coll_id": coll_id, "return_code": 0})


# Get item metadata
@bp.route("/collections/<coll_id>/items/<item_id>/metadata", methods=["POST"])
def get_item_metadata(coll_id, item_id):
    return jsonify({"coll_id": coll_id, "item_id": item_id, "key1": "value1"})


# Add item metadata
@bp.route("/collections/<coll_id>/items/<item_id>/metadata", methods=["POST"])
def set_item_metadata(coll_id, item_id):
    return jsonify({"coll_id": coll_id, "item_id": item_id, "key1": "value1"})


# Update item metadata
@bp.route("/collections/<coll_id>/items/<item_id>/metadata", methods=["POST"])
def update_item_metadata(coll_id, item_id):
    return jsonify({"coll_id": coll_id, "item_id": item_id, "key": "new_value"})


# Remove item metadata
@bp.route("/collections/<coll_id>/items/<item_id>/metadata", methods=["POST"])
def delete_item_metadata(coll_id, item_id):
    return jsonify({"coll_id": coll_id, "item_id": item_id, "return_code": 0})


# Search archive
@bp.route("/search", methods=["GET"])
def search_archive():
    return jsonify({"results": [{"type": "file", "id": "01234567"}]})


# Authenticate user credentials
@bp.route("/user/auth", methods=["POST"])
def authenticate():
    return "JWT"


# Download a single file or collection as a zip
@bp.route("/download")
def download(file_id=None, coll_id=None):
    file_id = request.args["file_id"]
    coll_id = request.args["coll_id"]
    return "file or collection"
