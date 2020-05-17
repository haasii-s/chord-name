from retrievers import get_chord_web

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS(app, resources={r'/.*': {'origins': 'http://localhost:3000/'}})
CORS(app)


@app.route("/test_get", methods=["GET"])
def get_test():
    if request.method == "GET":

        return jsonify(data="GET IS WORKING")

"""
@app.route("/get_chord/", methods=["POST", "GET"])
def get_chord_post():
    if request.method == "POST":
        data = request.json
        input = data.get("input")

        output = get_chord_web(input)
        interval_notes, interval_strings = output

        return jsonify(notes=interval_notes, strings=interval_strings)
<<<<<<< HEAD

@app.route("/test_get/", methods="GET"])
def get_test():
        data = request.json
        input = data.get("input")

        output = get_chord_web(input)
        interval_notes, interval_strings = output

        return jsonify(notes=interval_notes, strings=interval_strings)
=======
"""
>>>>>>> ce251fb78203826cc6b4d20e772607604e21e6da

@app.route("/")
def index():
    return "<p>Currently listening on port 5000...</p>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
