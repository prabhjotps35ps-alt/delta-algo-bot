from flask import Flask, request, jsonify
import os
import time
import hmac
import hashlib
import requests
import json

app = Flask(__name__)

API_KEY = os.getenv("DELTA_API_KEY")
API_SECRET = os.getenv("DELTA_API_SECRET")
BASE_URL = "https://api.delta.exchange"

def sign(payload, path, method, timestamp):
    message = method + timestamp + path + payload
    return hmac.new(
        API_SECRET.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        symbol = data.get("symbol", "BTCUSDT")
        side = data.get("side", "buy")
        size = data.get("size", 1)

        path = "/v2/orders"
        method = "POST"
        timestamp = str(int(time.time()))

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "order_type": "market"
        })

        headers = {
            "api-key": API_KEY,
            "timestamp": timestamp,
            "signature": sign(payload, path, method, timestamp),
            "Content-Type": "application/json"
        }

        response = requests.post(BASE_URL + path, headers=headers, data=payload)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)