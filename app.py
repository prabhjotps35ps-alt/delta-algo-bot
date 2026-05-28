from flask import Flask, request, jsonify
from delta_client import DeltaClient
from config import WEBHOOK_SECRET

app = Flask(__name__)
delta = DeltaClient()


@app.route("/")
def home():
    return jsonify({
        "status": "bot running"
    })


@app.route("/health")
def health():
    try:
        balance = delta.get_balance()
        return jsonify({
            "status": "healthy",
            "delta_connected": True,
            "balance_check": balance
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "delta_connected": False,
            "error": str(e)
        }), 500


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON payload"}), 400

        if data.get("secret") != WEBHOOK_SECRET:
            return jsonify({"error": "Unauthorized"}), 401

        balance_data = delta.get_balance()

balance = 1000

try:
    result = balance_data.get("result", [])
    if result:
        balance = float(result[0].get("balance", 1000))
except Exception:
    pass

size = risk_manager.calculate_position_size(balance)
        side = data.get("side")
        size = data.get("size", 1)
if position_manager.has_open_position(symbol):
    return jsonify({
        "error": "Open position already exists"
    }), 400

        if side not in ["buy", "sell"]:
            return jsonify({"error": "Invalid side"}), 400

        result = delta.place_market_order(symbol, side, size)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from position_manager import PositionManager

position_manager = PositionManager()

from risk_manager import RiskManager

risk_manager = RiskManager()
position_manager = PositionManager()
