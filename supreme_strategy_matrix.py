import os
import json
import time
import random
import traceback
from datetime import datetime


class SupremeStrategyMatrix:

    def __init__(self):

        self.strategy_log = (
            "supreme_strategy_log.txt"
        )

        self.strategy_memory = (
            "supreme_strategy_memory.json"
        )

        self.strategy_mode = (
            "adaptive"
        )

        self.trade_history = []

        self.load_memory()

    # =========================
    # LOG WRITER
    # =========================

    def write_log(
        self,
        message
    ):

        timestamp = str(
            datetime.now()
        )

        final_message = (
            f"[{timestamp}] {message}\n"
        )

        with open(
            self.strategy_log,
            "a"
        ) as file:

            file.write(
                final_message
            )

    # =========================
    # LOAD MEMORY
    # =========================

    def load_memory(self):

        try:

            if not os.path.exists(
                self.strategy_memory
            ):

                with open(
                    self.strategy_memory,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.strategy_memory,
                "r"
            ) as file:

                self.trade_history = (
                    json.load(file)
                )

        except Exception as e:

            self.trade_history = []

            self.write_log(
                f"Memory error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.strategy_memory,
            "w"
        ) as file:

            json.dump(
                self.trade_history,
                file,
                indent=4
            )

    # =========================
    # TREND ANALYSIS
    # =========================

    def trend_analysis(
        self,
        ema_fast,
        ema_slow
    ):

        if ema_fast > ema_slow:
            return "bullish"

        if ema_fast < ema_slow:
            return "bearish"

        return "sideways"

    # =========================
    # MOMENTUM ANALYSIS
    # =========================

    def momentum_analysis(
        self,
        rsi
    ):

        if rsi >= 70:
            return "overbought"

        if rsi <= 30:
            return "oversold"

        return "neutral"

    # =========================
    # VOLUME ANALYSIS
    # =========================

    def volume_analysis(
        self,
        current_volume,
        average_volume
    ):

        if current_volume > average_volume:
            return "strong"

        return "weak"

    # =========================
    # BREAKOUT DETECTION
    # =========================

    def breakout_detection(
        self,
        current_price,
        resistance
    ):

        if current_price > resistance:
            return True

        return False

    # =========================
    # FAKE BREAKOUT FILTER
    # =========================

    def fake_breakout_filter(
        self,
        breakout,
        volume_strength
    ):

        if breakout and volume_strength == "weak":
            return "fake_breakout"

        return "valid_breakout"

    # =========================
    # MARKET REGIME
    # =========================

    def market_regime(
        self,
        volatility
    ):

        if volatility == "high":
            return "volatile_market"

        return "stable_market"

    # =========================
    # SIGNAL SCORE
    # =========================

    def signal_score(
        self,
        trend,
        momentum,
        volume
    ):

        score = 50

        if trend == "bullish":
            score += 20

        if momentum == "oversold":
            score += 15

        if volume == "strong":
            score += 15

        return min(
            score,
            100
        )

    # =========================
    # AI TRADE DECISION
    # =========================

    def ai_trade_decision(
        self,
        score,
        market_regime
    ):

        if score >= 85:

            if market_regime == "stable_market":
                return "strong_buy"

            return "safe_buy"

        if score >= 70:
            return "watch_trade"

        return "avoid_trade"

    # =========================
    # AUTO TARGET
    # =========================

    def auto_target(
        self,
        entry_price
    ):

        target = (
            entry_price
            * 1.03
        )

        return round(
            target,
            2
        )

    # =========================
    # AUTO STOPLOSS
    # =========================

    def auto_stoploss(
        self,
        entry_price
    ):

        stoploss = (
            entry_price
            * 0.985
        )

        return round(
            stoploss,
            2
        )

    # =========================
    # TRAILING MANAGEMENT
    # =========================

    def trailing_management(
        self,
        profit_percent
    ):

        if profit_percent >= 5:

            return {
                "trailing_active": True
            }

        return {
            "trailing_active": False
        }

    # =========================
    # TRADE STORAGE
    # =========================

    def store_trade(
        self,
        trade
    ):

        self.trade_history.append(
            trade
        )

        self.save_memory()

        return True

    # =========================
    # MARKET SIMULATOR
    # =========================

    def market_simulator(self):

        return {
            "price": random.randint(
                50000,
                70000
            ),
            "volume": random.randint(
                1000,
                5000
            ),
            "volatility": random.choice([
                "low",
                "medium",
                "high"
            ])
        }

    # =========================
    # FULL STRATEGY REPORT
    # =========================

    def full_report(self):

        report = {
            "strategy_mode": (
                self.strategy_mode
            ),
            "stored_trades": len(
                self.trade_history
            ),
            "market": (
                self.market_simulator()
            )
        }

        return report

    # =========================
    # LIVE STRATEGY LOOP
    # =========================

    def live_strategy_loop(self):

        while True:

            try:

                report = (
                    self.full_report()
                )

                self.write_log(
                    f"Strategy report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Strategy error: {str(e)}"
                )

    # =========================
    # CRITICAL LOGGER
    # =========================

    def critical_error(
        self,
        error
    ):

        traceback.print_exc()

        self.write_log(
            f"Critical Error: {str(error)}"
        )

        return {
            "critical_error": str(error)
        }


# =========================
# RUN STRATEGY MATRIX
# =========================

if __name__ == "__main__":

    matrix = SupremeStrategyMatrix()

    result = matrix.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )