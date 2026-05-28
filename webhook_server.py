from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "status": "Webhook Active"
    })


@app.route(
    "/webhook",
    methods=["POST"]
)
def webhook():

    data = request.json

    print(
        "Webhook Signal:",
        data
    )

    return jsonify({
        "success": True,
        "data": data
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=False
    )