from flask import Flask, jsonify, request

app = Flask(__name__)

# =========================
# SAFE IMPORTS
# =========================

try:
    from delta_client import DeltaClient
except Exception as e:
    print("delta_client import error:", e)

try:
    from strategy_engine import StrategyEngine
except Exception as e:
    print("strategy_engine import error:", e)

try:
    from risk_manager import RiskManager
except Exception as e:
    print("risk_manager import error:", e)

try:
    from execution_engine import ExecutionEngine
except Exception as e:
    print("execution_engine import error:", e)

try:
    from signal_scoring import SignalScoring
except Exception as e:
    print("signal_scoring import error:", e)

try:
    from notifier import Notifier
except Exception as e:
    print("notifier import error:", e)

# =========================
# INITIALIZE
# =========================

delta = DeltaClient()

strategy_engine = StrategyEngine()

risk_manager = RiskManager()

execution_engine = ExecutionEngine()

signal_scoring = SignalScoring()

notifier = Notifier()

# =========================
# HOME
# =========================

@app.route("/")
def home():

    return jsonify({
        "status": "running",
        "bot": "institutional-engine"
    })

# =========================
# HEALTH
# =========================

@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

# =========================
# WEBHOOK
# =========================

@app.route("/webhook", methods=["POST"])
def webhook():

    try:

        data = request.get_json()

        symbol = data.get("symbol")

        side = data.get("side")

        if not symbol:
            return jsonify({
                "error": "symbol missing"
            }), 400

        if side not in ["buy", "sell"]:
            return jsonify({
                "error": "invalid side"
            }), 400

        market = strategy_engine.analyze_market(
            symbol
        )

        score = signal_scoring.calculate_score(
            market
        )

        balance_data = delta.get_balance()

        balance = risk_manager.extract_balance(
            balance_data
        )

        size = risk_manager.calculate_position_size(
            balance,
            score
        )

        order = execution_engine.execute_trade(
            delta=delta,
            symbol=symbol,
            side=side,
            size=size,
            leverage=5
        )

        notifier.send_trade_alert(
            symbol=symbol,
            side=side,
            size=size,
            leverage=5
        )

        return jsonify({
            "success": True,
            "score": score,
            "order": order
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )