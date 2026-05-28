from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "status": "running",
        "message": "Bot Running Successfully"
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "ok",
        "server": "active"
    })


@app.route("/ping")
def ping():

    return jsonify({
        "response": "pong"
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=False
    )