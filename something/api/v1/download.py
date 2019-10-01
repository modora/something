from flask import request

class Download:
    def __init__(self, file_id=None, coll_id=None):
        self.file_id = file_id
        self.coll_id = coll_id

        if not (file_id or coll_id):
            raise SyntaxError("No download id specified")
        elif (file_id and coll_id):
            raise SyntaxError("Abigious download id given")

    @classmethod
    def from_request(cls):
        file_id = request.args.get('file_id', None)
        coll_id = request.args.get('coll_id', None)

        return cls(file_id, coll_id)

    def download(self):
        if self.file_id:
            return self._download_file()
        return self._download_collection()

    def _download_file(self):
        return "file"

    def _download_collection(self):
        return "collection"
