from flask import jsonify


class Search:
    @staticmethod
    def GET():
        """
        :return:    A list of results
        """
        return jsonify({"results": [{"type": "file", "id": "01234567"}]})
