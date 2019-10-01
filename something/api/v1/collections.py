from flask import jsonify

import something.api.v1.metadata as metadata
import something.api.v1.files as files


class BaseCollection:
    def __init__(self, coll_id: str):
        self.coll_id = coll_id

    def GET(self):
        """
        Returns metadata for the collection

        Same as /metadata/collections?id=<coll_id>
        """
        return metadata.CollectionMetadata(self.coll_id).GET()

    def DELETE(self):
        """
        Deletes this collection and return a status code
        """
        return jsonify({"return_code": 0})

    def GET_items(self):
        """
        :return:    Return a list of all items within this collection
        """

        return jsonify({"items": ["item1", "item2"]})

    def POST_item(self):
        """
        Add an item into the collection
        """
        return jsonify({"item_id": "01234567"})

    def DELETE_item(self):
        """
        Removes an item from this collection
        """
        return jsonify({"return_code": 0})

    def GET_item_metadata(self):
        """
        Get the metadata for some item in the collection

        Same as /metadata/items?coll_id=<coll_id>&item_id=<item_id>
        """
        return metadata.ItemMetadata(self.coll_id, "item_id").GET()

    def POST_item_metadata(self):
        """
        Add metadata for some item in the collection

        Same as /metadata/items
        """
        return metadata.ItemMetadata(self.coll_id, "item_id").POST()

    def PUT_item_metadata(self):
        """
        Modify metadata for some item in the collection

        Same as /metadata/items
        """
        return metadata.ItemMetadata(self.coll_id, "item_id").PUT()

    def DELETE_item_metadata(self):
        """
        Remove metadata for some item in the collection

        Same as /metadata/items
        """
        return metadata.ItemMetadata(self.coll_id, "item_id").DELETE()


class _BaseBuiltinCollection(BaseCollection):
    def DELETE(self):
        """
        Safety to prevent the DELETE method to be used on builtin collections
        """
        raise NotImplementedError("Surpressed method")


class FilesCollection(_BaseBuiltinCollection):
    """
    Built-in special collection which contains all the files in the archive
    """

    def __init__(self):
        super().__init__("00000001")
        # TODO: insert into collectionsTable if not exist

    def POST_item(self):
        """
        Uploads a file into the archive

        Same as /files
        """
        return jsonify({"file_id": "01234567"})

    def DELETE_item(self):
        """
        Removes a file from the archive

        Same as DELETE /files?<file_id>
        """
        return files.BaseFilesEndpoint("file_id").DELETE()

    def GET_item_metadata(self):
        """
        Return file metadata

        Same as /metadata/files?file_id=<file_id>
        """
        return metadata.FileMetadata("file_id").GET()

    def POST_item_metadata(self):
        """
        Add file metadata

        Same as POST /metadata/files
        """
        return metadata.FileMetadata("file_id").POST()

    def PUT_item_metadata(self):
        """
        Modify file metadata

        Same as /metadata/files
        """
        return metadata.FileMetadata("file_id").PUT()

    def DELETE_item_metadata(self):
        """
        Delete file metadata

        Same as DELETE /metadata/files
        """
        return metadata.FileMetadata("file_id").DELETE()


class CollectionsCollection(_BaseBuiltinCollection):
    """
    Built-in special collection which contains all the collections in the archive
    """

    def __init__(self):
        super().__init__("00000002")
        # TODO: insert into collectionsTable if not exist

    def POST_item(self):
        """
        Add a new collection to the archive
        
        Same as POST /collections
        """
        return CollectionEndpoint().POST()

    def DELETE_item(self):
        """
        Removes a collection from the archive

        Same as DELETE /collections/<coll_id>
        """
        return BaseCollection("coll_id").DELETE()

    def GET_item_metadata(self):
        """
        Get collection metadata

        Same as /metadata/collections?coll_id=<coll_id>
        """
        return metadata.CollectionMetadata("coll_id").GET()

    def POST_item_metadata(self):
        """
        Add collection metadata

        Same as /metadata/collections
        """
        return metadata.CollectionMetadata("coll_id").POST()

    def PUT_item_metadata(self):
        """
        Remove collection metadata

        Same as /metadata/collections
        """
        return metadata.CollectionMetadata("coll_id").PUT()

    def DELETE_item_metadata(self):
        """
        Remove collection metadata

        Same as /metadata/collections
        """
        return metadata.CollectionMetadata("coll_id").DELETE()


class CollectionEndpoint:
    def GET(self):
        """
        Gets metadata detailing information for all collections
        :return:    json

        Same as /metadata/collections
        """
        return metadata.CollectionMetadata.GET_summary()

    def POST(self):
        """
        Creates a new collection

        :return:    json containing the created collection_id
        """
        return jsonify({"coll_id": "01234567"})
