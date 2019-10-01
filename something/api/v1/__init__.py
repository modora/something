from flask import Blueprint

from . import collections
from . import files
from . import search
from . import user
from . import metadata
from . import download

bp = Blueprint("v1", __name__)

# Get metadata summary for all collections
# Alias of GET /metadata/collections
bp.add_url_rule(
    "/collections",
    "get_collection_summary",
    collections.CollectionEndpoint().GET,
    methods=["GET"],
)
# Create a new collection
bp.add_url_rule(
    "/collections",
    "post_collections",
    collections.CollectionEndpoint().POST,
    methods=["POST"],
)
# Get metadata for the "files" collection
bp.add_url_rule(
    "/collections/files",
    "get_files_collection",
    collections.FilesCollection().GET,
    methods=["GET"],
)
# Get a list of files in the archive
bp.add_url_rule(
    "/collections/files/items",
    "get_filelist",
    collections.FilesCollection().GET_items,
    methods=["GET"],
)
# Upload a new file into the archive
# Alias of POST /files
bp.add_url_rule(
    "/collections/files/items",
    "post_files_collection",
    collections.FilesCollection().POST_item,
    methods=["POST"],
)
# Deletes a file from the archive
# Alias of DELETE /files
bp.add_url_rule(
    "/collections/files/items",
    "delete_file_from_files_collection",
    collections.FilesCollection().DELETE_item,
    methods=["DELETE"],
)
# Get metadata for the "collections" collection
bp.add_url_rule(
    "/collections/collections",
    "get_collections_collection",
    collections.CollectionsCollection().GET,
    methods=["GET"],
)
# Get a list of collections in the archive
bp.add_url_rule(
    "/collections/collections/items",
    "get_collection_list_from_collections_collection",
    collections.CollectionsCollection().GET_items,
    methods=["GET"],
)
# Create a new collection
# Alias for POST /collections
bp.add_url_rule(
    "/collections/collections/items",
    "post_collection_from_collections_collection",
    collections.CollectionsCollection().POST_item,
    methods=["POST"],
)
# Delete a collection
# Alias of DELETE /collections/<coll_id>
bp.add_url_rule(
    "/collections/collections/items",
    "delete_collection_from_collections_collection",
    collections.CollectionsCollection().DELETE_item,
    methods=["DELETE"],
)
# Get collection metadata for a given coll_id
# Alias of GET /metadata/collections?id=<coll_id>
bp.add_url_rule(
    "/collections/<coll_id>",
    "get_collection_metadata_by_id",
    lambda coll_id: collections.BaseCollection(coll_id).GET(),
    methods=["GET"],
)
# Delete the collection
bp.add_url_rule(
    "/collections/<coll_id>",
    "delete_collection_by_id",
    lambda coll_id: collections.BaseCollection(coll_id).DELETE(),
    methods=["DELETE"],
)
# Get a list of items in the collection
bp.add_url_rule(
    "/collections/<coll_id>/items",
    "get_items_by_collection_id",
    lambda coll_id: collections.BaseCollection(coll_id).GET_items(),
    methods=["GET"],
)
# Add a new item to the collection
bp.add_url_rule(
    "/collections/<coll_id>/items",
    "post_item_by_collection_id",
    lambda coll_id: collections.BaseCollection(coll_id).POST_item(),
    methods=["POST"],
)
# Add item metadata
# Alias for POST /metadata/items
bp.add_url_rule(
    "/collections/<coll_id>/items/<item_id>/metadata",
    "post_item_metadata_by_collection_id",
    lambda coll_id: collections.BaseCollection(coll_id).POST_item_metadata(),
    methods=["POST"],
)
# Get a summary of all files in the archive
bp.add_url_rule("/files", "get_files", files.FilesEndpoint().GET, methods=["GET"])
# Upload a new file to the collection
bp.add_url_rule("/files", "post_files", files.FilesEndpoint().POST, methods=["POST"])
# Get file metadata
# Alias of /metadata/files?<file_id>
bp.add_url_rule(
    "/files/<file_id>",
    "get_file_by_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).GET(),
    methods=["GET"],
)
# Removes the file from the archive
bp.add_url_rule(
    "/files/<file_id>",
    "delete_file_by_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).DELETE(),
    methods=["DELETE"],
)
# Get file metadata
# Alias of GET /metadata/files?file_id=<file_id>
bp.add_url_rule(
    "/files/<file_id>/metadata",
    "get_metadata_by_file_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).GET_metadata(),
    methods=["GET"],
)
# Set file metadata
# Alias of POST /metadata/files
bp.add_url_rule(
    "/files/<file_id>/metadata",
    "post_metadata_by_file_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).POST_metadata(),
    methods=["POST"],
)
# Modify file metadata
# Alias of PUT /metadata/files
bp.add_url_rule(
    "/files/<file_id>/metadata",
    "put_metadata_by_file_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).PUT_metadata(),
    methods=["PUT"],
)
# Delete file metadata
# Alias of DELETE /metadata/files?file_id=<file_id>
bp.add_url_rule(
    "/files/<file_id>/metadata",
    "delete_metadata_by_file_id",
    lambda file_id: files.BaseFilesEndpoint(file_id).DELETE_metadata(),
    methods=["DELETE"],
)
# Search archive
bp.add_url_rule("/search", "search_archive", search.Search.GET, methods=["GET"])
# Authenticate user credentials
bp.add_url_rule(
    "/user/auth", "authenticate_user", user.User.POST_authenticate, methods=["POST"]
)
# Get collection metadata
bp.add_url_rule(
    "/metadata/collections",
    "get_collection_metadata",
    metadata.CollectionMetadata("coll_id").GET,
    methods=["GET"],
)
# Add collection metadata
bp.add_url_rule(
    "/metadata/collections",
    "post_collection_metadata",
    metadata.CollectionMetadata("coll_id").POST,
    methods=["POST"],
)
# Modify collection metadata
bp.add_url_rule(
    "/metadata/collections",
    "put_collection_metadata",
    metadata.CollectionMetadata("coll_id").PUT,
    methods=["PUT"],
)
# Remove collection metadata
bp.add_url_rule(
    "/metadata/collections",
    "delete_collection_metadata",
    metadata.CollectionMetadata("coll_id").DELETE,
    methods=["DELETE"],
)
# Get item metadata
bp.add_url_rule(
    "/metadata/items",
    "get_item_metadata",
    metadata.ItemMetadata("coll_id", "item_id").GET,
    methods=["GET"],
)
# Add item metadata
bp.add_url_rule(
    "/metadata/items",
    "post_item_metadata",
    metadata.ItemMetadata("coll_id", "item_id").POST,
    methods=["POST"],
)
# Modify item metadata
bp.add_url_rule(
    "/metadata/items",
    "put_item_metadata",
    metadata.ItemMetadata("coll_id", "item_id").PUT,
    methods=["PUT"],
)
# Remove item metadata
bp.add_url_rule(
    "/metadata/items",
    "delete_item_metadata",
    metadata.ItemMetadata("coll_id", "item_id").DELETE,
    methods=["DELETE"],
)
# Get file metadata
bp.add_url_rule(
    "/metadata/files",
    "get_file_metadata",
    metadata.FileMetadata("file_id").GET,
    methods=["GET"],
)
# Add file metadata
bp.add_url_rule(
    "/metadata/files",
    "post_file_metadata",
    metadata.FileMetadata("file_id").POST,
    methods=["POST"],
)
# Modify file metadata
bp.add_url_rule(
    "/metadata/files",
    "put_file_metadata",
    metadata.FileMetadata("file_id").PUT,
    methods=["PUT"],
)
# Remove file metadata
bp.add_url_rule(
    "/metadata/files",
    "delete_file_metadata",
    metadata.FileMetadata("file_id").DELETE,
    methods=["DELETE"],
)
# Download a single file or collection as a zip
bp.add_url_rule(
    "/download",
    "download_file",
    lambda: download.Download.from_request().download(),
    methods=["GET"],
)
