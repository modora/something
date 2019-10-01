from flask import jsonify


class CollectionMetadata:
    """
    Metadata for a collection
    """

    def __init__(self, coll_id: str):
        self.coll_id = coll_id

    @staticmethod
    def GET_summary():
        """
        Get metadata of a summary of all collections in the archive
        """
        return jsonify({"num_coll": 3})

    def GET(self):
        """
        Get metadata about the collection
        """
        return jsonify(
            {"coll_id": self.coll_id, "name": "collection_name", "items": []}
        )

    def POST(self):
        """
        Add metadata about the collection
        """
        return jsonify({"coll_id": self.coll_id, "key": "value"})

    def PUT(self):
        """
        Modify metadata about the collection
        """
        return jsonify({"coll_id": self.coll_id, "key": "value"})

    def DELETE(self):
        """
        Remove metadata about the collection
        """
        return jsonify({"coll_id": self.coll_id, "return_code": 0})


class ItemMetadata:
    """
    Metadata for an item in a given collection
    """

    def __init__(self, coll_id: str, item_id: str):
        self.coll_id = coll_id
        self.item_id = item_id

    def GET(self):
        """
        Get the metadata for the item.
        """
        return jsonify(
            {
                "coll_id": self.coll_id,
                "item_id": self.item_id,
                "item_type": "file",
                "key1": "value1",
                "key1.key3": "value3",
                "key2": "value2",
            }
        )

    def POST(self):
        """
        Add metadata for the item
        """
        return jsonify(
            {"coll_id": self.coll_id, "item_id": self.item_id, "key1": "value1"}
        )

    def PUT(self):
        """
        Modify metadata for the item
        """
        return jsonify(
            {"coll_id": self.coll_id, "item_id": self.item_id, "key1": "value1"}
        )

    def DELETE(self):
        """
        Remove metadata for the item
        """
        return jsonify(
            {"coll_id": self.coll_id, "item_id": self.item_id, "return_code": 0}
        )


class FileMetadata:
    """
    Metadata for a file in the archive
    """

    def __init__(self, file_id: str):
        self.file_id = file_id

    @staticmethod
    def GET_summary():
        """
        Get a summary of all files within the archive
        """
        return jsonify({"num_files": 1, "size": 2})

    def GET(self):
        """
        Get the metadata for the file. If no parameters are given, then all
        key/values will be returned
        """
        return jsonify({"item_of": ["coll_id1"]})

    def POST(self):
        """
        Add metadata for the file. If the key already exists, then that key will
        be skipped
        
        :return:    key/value pairs added
        """
        return jsonify(
            {"file_id": self.file_id, "key1": "value1", "key1.key3": "value3"}
        )

    def PUT(self):
        """
        Change metadata for the file

        :return:    key and new_value pair
        """
        return jsonify({"file_id": self.file_id, "key": "new_value"})

    def DELETE(self):
        """
        Removes metadata for the file. If no parameters are given, then all
        keys will be removed.

        :return:    return_code, deleted_keys
        """
        return jsonify({"return_code": 0, "deleted_keys": ["key1"]})
