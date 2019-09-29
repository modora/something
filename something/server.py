import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({'msg': 'it works'})

if __name__ == "__main__":
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug)