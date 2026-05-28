import math
from datetime import datetime


class AdaptivePositionController:

    def __init__(self):

        # =========================
        # BASE SETTINGS
        # =========================

        self.base_risk_percent = 1.0

        self.max_risk_percent = 3.0

        self.min_risk_percent = 0.5

        self.max_positions = 1

        self.active_positions = 0

        # =========================
        # AI ADAPTIVE SETTINGS
        # =========================

        self.winrate_boost = True

        self.volatility_reduction = True

        self.drawdown_protection = True

        # =========================
        # PERFORMANCE MEMORY
        # =========================

        self.total_trades = 0

        self.wins = 0

        self.losses = 0

        self.current_drawdown = 0

    # =========================
    # WIN RATE
    # =========================

    def calculate_winrate(self):

        if self.total_trades == 0:

            return 0

        return round(

            (
                self.wins
                / self.total_trades
            ) * 100,

            2

        )

    # =========================
    # ADAPTIVE RISK ENGINE
    # =========================

    def adaptive_risk_engine(
        self,
        volatility,
        confidence
    ):

        risk = (
            self.base_risk_percent
        )

        # =========================
        # CONFIDENCE BOOST
        # =========================

        if confidence >= 90:

            risk += 1.0

        elif confidence >= 80:

            risk += 0.5

        # =========================
        # VOLATILITY REDUCTION
        # =========================

        if (
            self.volatility_reduction
            and volatility == "high"
        ):

            risk -= 0.5

        # =========================
        # DRAWDOWN PROTECTION
        # =========================

        if (
            self.drawdown_protection
            and self.current_drawdown >= 5
        ):

            risk -= 0.5

        # =========================
        # LIMITS
        # =========================

        risk = max(
            self.min_risk_percent,
            risk
        )

        risk = min(
            self.max_risk_percent,
            risk
        )

        return round(
            risk,
            2
        )

    # =========================
    # POSITION SIZE ENGINE
    # =========================

    def calculate_position_size(
        self,
        balance,
        entry_price,
        stoploss_percent,
        volatility,
        confidence
    ):

        risk_percent = (
            self.adaptive_risk_engine(
                volatility,
                confidence
            )
        )

        risk_amount = (
            balance
            * risk_percent
        ) / 100

        stop_distance = (
            entry_price
            * stoploss_percent
        ) / 100

        if stop_distance <= 0:

            return 0

        quantity = (
            risk_amount
            / stop_distance
        )

        return round(
            quantity,
            4
        )

    # =========================
    # POSITION VALIDATOR
    # =========================

    def validate_position_open(self):

        if (
            self.active_positions
            >= self.max_positions
        ):

            return False

        return True

    # =========================
    # REGISTER WIN
    # =========================

    def register_win(
        self,
        profit_percent
    ):

        self.total_trades += 1

        self.wins += 1

        if self.current_drawdown > 0:

            self.current_drawdown -= (
                profit_percent * 0.5
            )

            self.current_drawdown = max(
                0,
                self.current_drawdown
            )

    # =========================
    # REGISTER LOSS
    # =========================

    def register_loss(
        self,
        loss_percent
    ):

        self.total_trades += 1

        self.losses += 1

        self.current_drawdown += abs(
            loss_percent
        )

    # =========================
    # OPEN POSITION
    # =========================

    def open_position(self):

        self.active_positions += 1

    # =========================
    # CLOSE POSITION
    # =========================

    def close_position(self):

        if self.active_positions > 0:

            self.active_positions -= 1

    # =========================
    # COMPOUND ENGINE
    # =========================

    def compound_balance(
        self,
        balance,
        profit_percent
    ):

        new_balance = (

            balance

            + (

                balance
                * profit_percent
                / 100

            )

        )

        return round(
            new_balance,
            2
        )

    # =========================
    # AI TRADE SCORE
    # =========================

    def ai_trade_score(
        self,
        trend_strength,
        volume_strength,
        confidence
    ):

        score = 50

        score += (
            trend_strength * 0.2
        )

        score += (
            volume_strength * 0.2
        )

        score += (
            confidence * 0.3
        )

        return min(
            round(score, 2),
            100
        )

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "time":
            str(datetime.now()),

            "winrate":
            self.calculate_winrate(),

            "total_trades":
            self.total_trades,

            "wins":
            self.wins,

            "losses":
            self.losses,

            "drawdown":
            self.current_drawdown,

            "active_positions":
            self.active_positions

        }


if __name__ == "__main__":

    controller = (
        AdaptivePositionController()
    )

    report = (
        controller.status_report()
    )

    print(report)