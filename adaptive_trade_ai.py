import os
import json
import time
import random
import traceback
from datetime import datetime


class AdaptiveTradeAI:

    def __init__(self):

        self.ai_memory = (
            "ai_memory.json"
        )

        self.ai_log = (
            "adaptive_trade_ai_log.txt"
        )

        self.learning_data = []

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
            self.ai_log,
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
                self.ai_memory
            ):

                with open(
                    self.ai_memory,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.ai_memory,
                "r"
            ) as file:

                self.learning_data = (
                    json.load(file)
                )

        except Exception as e:

            self.write_log(
                f"Memory load error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.ai_memory,
            "w"
        ) as file:

            json.dump(
                self.learning_data,
                file,
                indent=4
            )

    # =========================
    # STORE TRADE RESULT
    # =========================

    def learn_from_trade(
        self,
        symbol,
        side,
        result,
        pnl
    ):

        trade_data = {
            "timestamp": str(
                datetime.now()
            ),
            "symbol": symbol,
            "side": side,
            "result": result,
            "pnl": pnl
        }

        self.learning_data.append(
            trade_data
        )

        self.save_memory()

        self.write_log(
            f"Learned trade: {symbol}"
        )

        return True

    # =========================
    # WIN RATE ANALYSIS
    # =========================

    def analyze_win_rate(self):

        if not self.learning_data:

            return 0

        wins = 0

        for trade in self.learning_data:

            if trade["result"] == "win":

                wins += 1

        return round(
            (
                wins
                / len(
                    self.learning_data
                )
            ) * 100,
            2
        )

    # =========================
    # STRATEGY SCORE
    # =========================

    def strategy_score(self):

        win_rate = (
            self.analyze_win_rate()
        )

        if win_rate >= 80:
            return "excellent"

        if win_rate >= 60:
            return "good"

        if win_rate >= 40:
            return "average"

        return "weak"

    # =========================
    # MARKET ADAPTATION
    # =========================

    def market_adaptation(
        self,
        volatility,
        volume
    ):

        if volatility == "high":

            return {
                "risk": "low",
                "mode": "safe"
            }

        if volume == "strong":

            return {
                "risk": "medium",
                "mode": "aggressive"
            }

        return {
            "risk": "normal",
            "mode": "balanced"
        }

    # =========================
    # AI DECISION ENGINE
    # =========================

    def ai_trade_decision(
        self,
        signal_score,
        trend
    ):

        if signal_score >= 80:

            if trend == "bullish":

                return "strong_buy"

            if trend == "bearish":

                return "strong_sell"

        if signal_score >= 60:
            return "moderate_trade"

        return "avoid_trade"

    # =========================
    # RISK ADAPTATION
    # =========================

    def adaptive_risk(
        self,
        drawdown
    ):

        if drawdown >= 20:

            return {
                "risk_mode": "critical"
            }

        if drawdown >= 10:

            return {
                "risk_mode": "protected"
            }

        return {
            "risk_mode": "normal"
        }

    # =========================
    # AI CONFIDENCE
    # =========================

    def confidence_level(
        self,
        signal_score,
        volume_strength
    ):

        confidence = signal_score

        if volume_strength == "strong":

            confidence += 10

        return min(
            confidence,
            100
        )

    # =========================
    # SELF IMPROVEMENT
    # =========================

    def self_improvement(self):

        score = self.strategy_score()

        self.write_log(
            f"Current strategy score: {score}"
        )

        return {
            "strategy_score": score,
            "win_rate": (
                self.analyze_win_rate()
            )
        }

    # =========================
    # AUTO MARKET SIMULATION
    # =========================

    def market_simulation(self):

        trends = [
            "bullish",
            "bearish",
            "sideways"
        ]

        volumes = [
            "strong",
            "medium",
            "weak"
        ]

        volatility = [
            "low",
            "medium",
            "high"
        ]

        return {
            "trend": random.choice(
                trends
            ),
            "volume": random.choice(
                volumes
            ),
            "volatility": random.choice(
                volatility
            )
        }

    # =========================
    # FULL AI REPORT
    # =========================

    def ai_report(self):

        report = {
            "win_rate": (
                self.analyze_win_rate()
            ),
            "strategy_score": (
                self.strategy_score()
            ),
            "total_trades": len(
                self.learning_data
            ),
            "simulation": (
                self.market_simulation()
            )
        }

        return report

    # =========================
    # LIVE AI LOOP
    # =========================

    def live_ai_system(self):

        while True:

            try:

                report = self.ai_report()

                self.write_log(
                    f"AI Report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"AI Loop Error: {str(e)}"
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
# RUN AI
# =========================

if __name__ == "__main__":

    ai = AdaptiveTradeAI()

    result = ai.ai_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )