
from flask import Flask, request, jsonify

from delta_client import DeltaClient
from position_manager import PositionManager
from risk_manager import RiskManager
from connectivity_monitor import ConnectivityMonitor
from recovery_manager import RecoveryManager
from strategy_engine import StrategyEngine
from execution_engine import ExecutionEngine
from trade_monitor import TradeMonitor
from emergency_exit import EmergencyExit
from trading_rule_engine import TradingRuleEngine
from signal_scoring import SignalScoring
from notifier import Notifier

app = Flask(__name__)

# =========================
# CORE ENGINES
# =========================

delta = DeltaClient()

position_manager = PositionManager()

risk_manager = RiskManager()

connectivity_monitor = ConnectivityMonitor()

recovery_manager = RecoveryManager()

strategy_engine = StrategyEngine()

execution_engine = ExecutionEngine()

trade_monitor = TradeMonitor()

emergency_exit = EmergencyExit()

trading_rules = TradingRuleEngine()

signal_scoring = SignalScoring()

notifier = Notifier()

# =========================
# HOME ROUTE
# =========================

@app.route("/")
def home():

    return jsonify({
        "status": "Institutional Bot Running",
        "system": "healthy"
    })

# =========================
# HEALTH CHECK
# =========================

@app.route("/health")
def health():

    try:

        internet_ok = connectivity_monitor.internet_check()

        delta_ok = connectivity_monitor.delta_api_check(
            delta
        )

        heartbeat = connectivity_monitor.heartbeat_status(
            internet_ok,
            delta_ok
        )

        return jsonify({
            "status": heartbeat,
            "internet_ok": internet_ok,
            "delta_ok": delta_ok
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

# =========================
# WEBHOOK
# =========================

@app.route("/webhook", methods=["POST"])
def webhook():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "error": "No JSON payload"
            }), 400

        # =========================
        # CONNECTIVITY CHECK
        # =========================

        internet_ok = connectivity_monitor.internet_check()

        delta_ok = connectivity_monitor.delta_api_check(
            delta
        )

        if recovery_manager.should_pause_trading(
            internet_ok,
            delta_ok
        ):

            return jsonify({
                "error": recovery_manager.recovery_message(
                    internet_ok,
                    delta_ok
                )
            }), 503

        # =========================
        # INPUT DATA
        # =========================

        symbol = data.get("symbol")

        side = data.get("side")

        timeframe = data.get(
            "timeframe",
            "1m"
        )

        if side not in ["buy", "sell"]:

            return jsonify({
                "error": "Invalid side"
            }), 400

        # =========================
        # POSITION CHECK
        # =========================

        if position_manager.has_open_position(
            symbol
        ):

            return jsonify({
                "error": "Open position already exists"
            }), 400

        # =========================
        # MARKET ANALYSIS
        # =========================

        market_analysis = strategy_engine.analyze_market(
            symbol,
            timeframe
        )

        # =========================
        # SIGNAL SCORING
        # =========================

        signal_score = signal_scoring.calculate_score(
            market_analysis
        )

        if signal_score < 70:

            return jsonify({
                "error": "Weak signal rejected",
                "signal_score": signal_score
            }), 400

        # =========================
        # TRADING RULE CHECK
        # =========================

        trade_allowed = trading_rules.allow_trade(
            market_analysis
        )

        if not trade_allowed:

            return jsonify({
                "error": "Trading rules rejected trade"
            }), 400

        # =========================
        # BALANCE CHECK
        # =========================

        balance_data = delta.get_balance()

        balance = risk_manager.extract_balance(
            balance_data
        )

        # =========================
        # POSITION SIZE
        # =========================

        size = risk_manager.calculate_position_size(
            balance,
            signal_score
        )

        if size <= 0:

            return jsonify({
                "error": "Insufficient balance"
            }), 400

        # =========================
        # LEVERAGE
        # =========================

        leverage = risk_manager.dynamic_leverage(
            signal_score
        )

        # =========================
        # EXECUTION
        # =========================

        order_result = execution_engine.execute_trade(
            delta=delta,
            symbol=symbol,
            side=side,
            size=size,
            leverage=leverage
        )

        # =========================
        # TRADE MONITOR
        # =========================

        trade_monitor.register_trade(
            symbol=symbol,
            side=side,
            size=size,
            leverage=leverage,
            signal_score=signal_score
        )

        # =========================
        # NOTIFICATION
        # =========================

        notifier.send_trade_alert(
            symbol=symbol,
            side=side,
            size=size,
            leverage=leverage
        )

        # =========================
        # RESPONSE
        # =========================

        return jsonify({
            "status": "success",
            "symbol": symbol,
            "side": side,
            "size": size,
            "leverage": leverage,
            "signal_score": signal_score,
            "order": order_result
        })

    except Exception as e:

        try:

            emergency_exit.handle_critical_error(
                str(e)
            )

        except Exception:
            pass

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# =========================
# EMERGENCY CLOSE
# =========================

@app.route("/emergency-close", methods=["POST"])
def emergency_close():

    try:

        data = request.get_json()

        symbol = data.get("symbol")

        result = emergency_exit.close_position(
            delta,
            symbol
        )

        return jsonify({
            "status": "closed",
            "result": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )