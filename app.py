from retrievers import get_chord_web

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS(app, resources={r'/.*': {'origins': 'http://localhost:3000/'}})
CORS(app)


@app.route("/test_get/", methods=["GET"])
def get_test():
    return jsonify(data="GET IS WORKING")


"""@app.route("/get_chord/", methods=["POST", "GET"])
def get_chord_post():
    if request.method == "POST":
        data = request.json
        user_input = data.get("input")

        output = None
        chord_objects = []

        for chord in user_input:
            output = get_chord_web(chord)
            for tup in output:
                root, interval_notes, interval_strings, keyboard_values = tup
                chord_object = \
                    jsonify(root=root, notes=interval_notes, strings=interval_strings, keyboard_values=keyboard_values)
                chord_objects.append(chord_object)

        return chord_objects"""


@app.route("/")
def index():
    return "<p>Currently listening on port 5000...</p>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
