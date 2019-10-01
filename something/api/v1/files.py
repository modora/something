from flask import jsonify

import something.api.v1.metadata as metadata


class FilesEndpoint:
    def GET(self):
        """
        Returns a summary of all files in the archive

        Same as /metadata/files
        """

        return metadata.FileMetadata.GET_summary()

    def POST(self):
        """
        Uploads a file into the archive

        :return:    file_id of the new file
        """
        return jsonify({"file_id": "01234567"})


class BaseFilesEndpoint:
    def __init__(self, file_id: str):
        self.file_id = file_id

    def GET(self):
        """
        Get metadata relative to the archive e.g. item_of this list of 
        collections

        Same as /metadata/files?<file_id>
        """

        return metadata.FileMetadata(self.file_id).GET()

    def DELETE(self):
        """
        Removes the file from the archive
        """
        return jsonify({"return_code": 0})

    def GET_metadata(self):
        """
        Returns the metadata for the file. If no parameters are given, then all
        key/values will be returned

        Same as /metadata/files?file_id=<file_id>
        """
        return metadata.FileMetadata(self.file_id).GET()

    def POST_metadata(self):
        """
        Add metadata for the file. If the key already exists, then that key will
        be skipped
        
        :return:    key/value pairs added
        """
        return metadata.FileMetadata(self.file_id).POST()

    def PUT_metadata(self):
        """
        Change metadata for the file

        :return:    key and new_value pair
        """
        return metadata.FileMetadata(self.file_id).PUT()

    def DELETE_metadata(self):
        """
        Removes metadata for the file. If no parameters are given, then all
        keys will be removed.

        :return:    return_code, deleted_keys
        """
        return jsonify({"return_code": 0, "deleted_keys": ["key1"]})
