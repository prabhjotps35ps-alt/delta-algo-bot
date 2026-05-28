import os
import json
import time
import random
import traceback
from datetime import datetime


class EliteTradeBrain:

    def __init__(self):

        self.memory_file = (
            "elite_trade_memory.json"
        )

        self.log_file = (
            "elite_trade_brain_log.txt"
        )

        self.trade_mode = (
            "learning"
        )

        self.trade_memory = []

        self.load_memory()

    # =========================
    # LOG SYSTEM
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
            self.log_file,
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
                self.memory_file
            ):

                with open(
                    self.memory_file,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.memory_file,
                "r"
            ) as file:

                self.trade_memory = (
                    json.load(file)
                )

        except Exception as e:

            self.trade_memory = []

            self.write_log(
                f"Memory load error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.memory_file,
            "w"
        ) as file:

            json.dump(
                self.trade_memory,
                file,
                indent=4
            )

    # =========================
    # LEARN FROM TRADE
    # =========================

    def learn_trade(
        self,
        symbol,
        side,
        entry,
        exit_price,
        profit
    ):

        trade = {
            "time": str(
                datetime.now()
            ),
            "symbol": symbol,
            "side": side,
            "entry": entry,
            "exit": exit_price,
            "profit": profit
        }

        self.trade_memory.append(
            trade
        )

        self.save_memory()

        self.write_log(
            f"Learned trade: {symbol}"
        )

        return True

    # =========================
    # WIN RATE
    # =========================

    def calculate_win_rate(self):

        if not self.trade_memory:

            return 0

        wins = 0

        for trade in self.trade_memory:

            if trade["profit"] > 0:

                wins += 1

        return round(
            (
                wins
                / len(
                    self.trade_memory
                )
            ) * 100,
            2
        )

    # =========================
    # AI MARKET ANALYSIS
    # =========================

    def market_analysis(self):

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

        liquidity = [
            "high",
            "medium",
            "low"
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
            ),
            "liquidity": random.choice(
                liquidity
            )
        }

    # =========================
    # SIGNAL GENERATOR
    # =========================

    def generate_signal(
        self,
        signal_score,
        trend,
        volume
    ):

        if signal_score >= 90:

            if trend == "bullish":

                if volume == "strong":

                    return "strong_buy"

                return "safe_buy"

            if trend == "bearish":

                return "strong_sell"

        if signal_score >= 70:

            return "wait_confirmation"

        return "avoid_trade"

    # =========================
    # RISK CONTROL
    # =========================

    def risk_control(
        self,
        drawdown
    ):

        if drawdown >= 25:

            return {
                "mode": "emergency_stop"
            }

        if drawdown >= 15:

            return {
                "mode": "safe_mode"
            }

        return {
            "mode": "normal"
        }

    # =========================
    # PROFIT OPTIMIZER
    # =========================

    def profit_optimizer(
        self,
        current_profit
    ):

        if current_profit >= 10:

            return {
                "action": "partial_book"
            }

        if current_profit >= 20:

            return {
                "action": "secure_profit"
            }

        return {
            "action": "hold_trade"
        }

    # =========================
    # AUTO TRADE DECISION
    # =========================

    def auto_trade_decision(
        self,
        signal_score,
        trend,
        volume,
        volatility
    ):

        if signal_score >= 85:

            if (
                trend == "bullish"
                and volume == "strong"
                and volatility != "high"
            ):

                return "buy"

            if (
                trend == "bearish"
                and volume == "strong"
            ):

                return "sell"

        return "wait"

    # =========================
    # SELF IMPROVEMENT
    # =========================

    def self_improvement(self):

        win_rate = (
            self.calculate_win_rate()
        )

        if win_rate >= 80:

            self.trade_mode = (
                "aggressive"
            )

        elif win_rate >= 60:

            self.trade_mode = (
                "balanced"
            )

        else:

            self.trade_mode = (
                "safe"
            )

        return {
            "mode": self.trade_mode,
            "win_rate": win_rate
        }

    # =========================
    # LIVE BRAIN LOOP
    # =========================

    def live_brain(self):

        while True:

            try:

                report = {
                    "market": (
                        self.market_analysis()
                    ),
                    "improvement": (
                        self.self_improvement()
                    )
                }

                self.write_log(
                    f"Brain report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Brain error: {str(e)}"
                )

    # =========================
    # FULL REPORT
    # =========================

    def full_report(self):

        report = {
            "mode": self.trade_mode,
            "win_rate": (
                self.calculate_win_rate()
            ),
            "memory_size": len(
                self.trade_memory
            ),
            "market": (
                self.market_analysis()
            )
        }

        return report

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
# RUN ELITE BRAIN
# =========================

if __name__ == "__main__":

    brain = EliteTradeBrain()

    result = brain.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )