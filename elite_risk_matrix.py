import os
import json
import time
import traceback
from datetime import datetime


class EliteRiskMatrix:

    def __init__(self):

        self.risk_log = (
            "elite_risk_matrix_log.txt"
        )

        self.risk_memory = (
            "elite_risk_memory.json"
        )

        self.risk_mode = (
            "protected"
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
            self.risk_log,
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
                self.risk_memory
            ):

                with open(
                    self.risk_memory,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.risk_memory,
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
            self.risk_memory,
            "w"
        ) as file:

            json.dump(
                self.trade_memory,
                file,
                indent=4
            )

    # =========================
    # MAX RISK CONTROL
    # =========================

    def max_risk_control(
        self,
        balance,
        risk_percent
    ):

        risk_amount = (
            balance
            * risk_percent
        ) / 100

        return round(
            risk_amount,
            2
        )

    # =========================
    # DRAWDOWN PROTECTION
    # =========================

    def drawdown_protection(
        self,
        drawdown
    ):

        if drawdown >= 25:

            self.risk_mode = (
                "emergency"
            )

            return {
                "trade_allowed": False,
                "mode": "emergency_stop"
            }

        if drawdown >= 15:

            self.risk_mode = (
                "safe"
            )

            return {
                "trade_allowed": True,
                "mode": "safe_mode"
            }

        return {
            "trade_allowed": True,
            "mode": "normal"
        }

    # =========================
    # POSITION LIMITER
    # =========================

    def position_limiter(
        self,
        open_positions,
        max_positions
    ):

        if open_positions >= max_positions:

            return {
                "allow_trade": False
            }

        return {
            "allow_trade": True
        }

    # =========================
    # DAILY LOSS LIMIT
    # =========================

    def daily_loss_limit(
        self,
        daily_loss,
        max_daily_loss
    ):

        if daily_loss >= max_daily_loss:

            return {
                "trading": "blocked"
            }

        return {
            "trading": "active"
        }

    # =========================
    # VOLATILITY FILTER
    # =========================

    def volatility_filter(
        self,
        volatility
    ):

        if volatility == "high":

            return {
                "trade_mode": "avoid"
            }

        return {
            "trade_mode": "allowed"
        }

    # =========================
    # CAPITAL PRESERVATION
    # =========================

    def capital_preservation(
        self,
        account_balance
    ):

        if account_balance <= 50:

            return {
                "mode": "capital_protection"
            }

        return {
            "mode": "normal"
        }

    # =========================
    # AUTO HEDGE MODE
    # =========================

    def auto_hedge(
        self,
        market_trend
    ):

        if market_trend == "uncertain":

            return {
                "hedge": True
            }

        return {
            "hedge": False
        }

    # =========================
    # SMART RISK SCORE
    # =========================

    def smart_risk_score(
        self,
        signal_score,
        volatility,
        liquidity
    ):

        risk_score = signal_score

        if volatility == "high":

            risk_score -= 20

        if liquidity == "low":

            risk_score -= 15

        return max(
            risk_score,
            0
        )

    # =========================
    # SAFE ENTRY VALIDATION
    # =========================

    def safe_entry_validation(
        self,
        signal_score,
        volatility,
        spread
    ):

        if signal_score < 75:
            return False

        if volatility == "high":
            return False

        if spread > 1:
            return False

        return True

    # =========================
    # TRADE MEMORY
    # =========================

    def store_trade(
        self,
        trade_data
    ):

        self.trade_memory.append(
            trade_data
        )

        self.save_memory()

        return True

    # =========================
    # FULL RISK REPORT
    # =========================

    def full_report(self):

        return {
            "risk_mode": self.risk_mode,
            "stored_trades": len(
                self.trade_memory
            ),
            "status": "active"
        }

    # =========================
    # LIVE RISK LOOP
    # =========================

    def live_risk_loop(self):

        while True:

            try:

                report = (
                    self.full_report()
                )

                self.write_log(
                    f"Risk report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Risk loop error: {str(e)}"
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
# RUN RISK MATRIX
# =========================

if __name__ == "__main__":

    matrix = EliteRiskMatrix()

    result = matrix.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )