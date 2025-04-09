from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"])
def echo():
    return jsonify({"headers": dict(request.headers)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)