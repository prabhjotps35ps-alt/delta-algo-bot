import os
import json
import time
import random
import traceback
from datetime import datetime


class InfinityMasterController:

    def __init__(self):

        self.controller_log = (
            "infinity_master_controller_log.txt"
        )

        self.controller_memory = (
            "infinity_master_controller_memory.json"
        )

        self.controller_mode = (
            "master_control"
        )

        self.controller_history = []

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
            self.controller_log,
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
                self.controller_memory
            ):

                with open(
                    self.controller_memory,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.controller_memory,
                "r"
            ) as file:

                self.controller_history = (
                    json.load(file)
                )

        except Exception as e:

            self.controller_history = []

            self.write_log(
                f"Memory load error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.controller_memory,
            "w"
        ) as file:

            json.dump(
                self.controller_history,
                file,
                indent=4
            )

    # =========================
    # GLOBAL AI MARKET ENGINE
    # =========================

    def global_ai_market_engine(self):

        return {
            "trend": random.choice([
                "bullish",
                "bearish",
                "sideways"
            ]),
            "volume": random.choice([
                "strong",
                "medium",
                "weak"
            ]),
            "volatility": random.choice([
                "low",
                "medium",
                "high"
            ]),
            "liquidity": random.choice([
                "high",
                "medium",
                "low"
            ]),
            "momentum": random.randint(
                50,
                100
            ),
            "sentiment": random.choice([
                "fear",
                "neutral",
                "greed"
            ]),
            "spread": round(
                random.uniform(
                    0.1,
                    2.0
                ),
                2
            )
        }

    # =========================
    # MASTER AI SCORE
    # =========================

    def master_ai_score(
        self,
        market
    ):

        score = 50

        if market["trend"] == "bullish":
            score += 20

        if market["volume"] == "strong":
            score += 15

        if market["volatility"] == "low":
            score += 10

        if market["liquidity"] == "high":
            score += 10

        if market["sentiment"] == "greed":
            score += 10

        score += int(
            market["momentum"] / 10
        )

        return min(
            score,
            100
        )

    # =========================
    # MASTER TRADE DECISION
    # =========================

    def master_trade_decision(
        self,
        score,
        trend,
        volatility
    ):

        if score >= 95:

            if (
                trend == "bullish"
                and volatility != "high"
            ):

                return "infinity_buy"

            if trend == "bearish":

                return "infinity_sell"

        if score >= 85:
            return "prepare_trade"

        if score >= 70:
            return "monitor_trade"

        return "avoid_trade"

    # =========================
    # CAPITAL MANAGER
    # =========================

    def capital_manager(
        self,
        balance,
        risk_percent
    ):

        amount = (
            balance
            * risk_percent
        ) / 100

        return round(
            amount,
            2
        )

    # =========================
    # AUTO TARGET ENGINE
    # =========================

    def auto_target_engine(
        self,
        entry_price,
        score
    ):

        multiplier = 1.03

        if score >= 95:

            multiplier = 1.10

        elif score >= 85:

            multiplier = 1.07

        return round(
            entry_price
            * multiplier,
            2
        )

    # =========================
    # AUTO STOPLOSS ENGINE
    # =========================

    def auto_stoploss_engine(
        self,
        entry_price,
        volatility
    ):

        multiplier = 0.985

        if volatility == "high":

            multiplier = 0.970

        return round(
            entry_price
            * multiplier,
            2
        )

    # =========================
    # TRAILING PROFIT ENGINE
    # =========================

    def trailing_profit_engine(
        self,
        current_profit
    ):

        if current_profit >= 5:

            return {
                "trailing_enabled": True
            }

        return {
            "trailing_enabled": False
        }

    # =========================
    # PROFIT LOCK ENGINE
    # =========================

    def profit_lock_engine(
        self,
        current_profit
    ):

        if current_profit >= 15:

            return {
                "profit_locked": True
            }

        return {
            "profit_locked": False
        }

    # =========================
    # RISK DEFENSE ENGINE
    # =========================

    def risk_defense_engine(
        self,
        drawdown
    ):

        if drawdown >= 25:

            return {
                "trading_disabled": True
            }

        if drawdown >= 15:

            return {
                "safe_mode": True
            }

        return {
            "safe_mode": False
        }

    # =========================
    # EXECUTION FILTER
    # =========================

    def execution_filter(
        self,
        score,
        spread,
        liquidity
    ):

        if score < 80:
            return False

        if spread > 1.5:
            return False

        if liquidity == "low":
            return False

        return True

    # =========================
    # STORE REPORT
    # =========================

    def store_report(
        self,
        report
    ):

        self.controller_history.append(
            report
        )

        self.save_memory()

        return True

    # =========================
    # SYSTEM HEALTH CHECK
    # =========================

    def system_health_check(self):

        files = os.listdir()

        python_files = []

        for file in files:

            if file.endswith(".py"):

                python_files.append(
                    file
                )

        return {
            "python_files": len(
                python_files
            ),
            "system_status": "healthy"
        }

    # =========================
    # LIVE MASTER LOOP
    # =========================

    def live_master_loop(self):

        while True:

            try:

                market = (
                    self.global_ai_market_engine()
                )

                score = (
                    self.master_ai_score(
                        market
                    )
                )

                decision = (
                    self.master_trade_decision(
                        score,
                        market["trend"],
                        market["volatility"]
                    )
                )

                report = {
                    "time": str(
                        datetime.now()
                    ),
                    "market": market,
                    "score": score,
                    "decision": decision,
                    "health": (
                        self.system_health_check()
                    )
                }

                self.store_report(
                    report
                )

                self.write_log(
                    f"Master report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Master loop error: "
                    f"{str(e)}"
                )

    # =========================
    # FULL REPORT
    # =========================

    def full_report(self):

        market = (
            self.global_ai_market_engine()
        )

        score = (
            self.master_ai_score(
                market
            )
        )

        decision = (
            self.master_trade_decision(
                score,
                market["trend"],
                market["volatility"]
            )
        )

        return {
            "mode": self.controller_mode,
            "market": market,
            "score": score,
            "decision": decision,
            "health": (
                self.system_health_check()
            ),
            "stored_reports": len(
                self.controller_history
            )
        }

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
# RUN MASTER CONTROLLER
# =========================

if __name__ == "__main__":

    controller = (
        InfinityMasterController()
    )

    result = (
        controller.full_report()
    )

    print(
        json.dumps(
            result,
            indent=4
        )
    )