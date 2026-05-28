from flask import Flask, jsonify

from delta_client import DeltaClient

app = Flask(__name__)

delta = DeltaClient()


@app.route("/")
def home():

    return "Bot Running"


@app.route("/health")
def health():

    return jsonify({
        "status": "ok"
    })


@app.route("/delta-test")
def delta_test():

    return jsonify(
        delta.test()
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )