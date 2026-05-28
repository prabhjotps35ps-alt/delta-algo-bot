from config import (
    MIN_BALANCE_INR,
    MAX_RISK_PER_TRADE,
    MIN_LEVERAGE,
    MAX_LEVERAGE,
    DEFAULT_LEVERAGE,
    DEFAULT_STOP_LOSS_PERCENT,
    DEFAULT_TAKE_PROFIT_PERCENT,
    MAX_DAILY_LOSS_PERCENT,
    MAX_DRAWDOWN_PERCENT
)


class RiskManager:

    # =========================
    # EXTRACT BALANCE
    # =========================

    def extract_balance(
        self,
        balance_data
    ):

        try:

            result = balance_data.get(
                "result",
                []
            )

            if not result:
                return 0

            balance = float(
                result[0].get(
                    "balance",
                    0
                )
            )

            return balance

        except Exception:
            return 0

    # =========================
    # POSITION SIZE
    # =========================

    def calculate_position_size(
        self,
        balance,
        signal_score
    ):

        try:

            if balance < MIN_BALANCE_INR:
                return 0

            risk_factor = (
                signal_score / 100
            )

            capital = (
                balance
                * (
                    MAX_RISK_PER_TRADE
                    / 100
                )
            )

            adjusted_size = (
                capital
                * risk_factor
            )

            if adjusted_size <= 0:
                return 0

            if adjusted_size < 1:
                return 1

            return round(
                adjusted_size,
                2
            )

        except Exception:
            return 0

    # =========================
    # DYNAMIC LEVERAGE
    # =========================

    def dynamic_leverage(
        self,
        signal_score
    ):

        try:

            if signal_score >= 90:
                return MAX_LEVERAGE

            if signal_score >= 80:
                return 8

            if signal_score >= 70:
                return DEFAULT_LEVERAGE

            return MIN_LEVERAGE

        except Exception:
            return DEFAULT_LEVERAGE

    # =========================
    # STOP LOSS
    # =========================

    def calculate_stop_loss(
        self,
        entry_price,
        side
    ):

        try:

            stop_percent = (
                DEFAULT_STOP_LOSS_PERCENT
                / 100
            )

            if side == "buy":

                stop_loss = (
                    entry_price
                    * (
                        1 - stop_percent
                    )
                )

            else:

                stop_loss = (
                    entry_price
                    * (
                        1 + stop_percent
                    )
                )

            return round(
                stop_loss,
                2
            )

        except Exception:
            return 0

    # =========================
    # TAKE PROFIT
    # =========================

    def calculate_take_profit(
        self,
        entry_price,
        side
    ):

        try:

            target_percent = (
                DEFAULT_TAKE_PROFIT_PERCENT
                / 100
            )

            if side == "buy":

                target = (
                    entry_price
                    * (
                        1 + target_percent
                    )
                )

            else:

                target = (
                    entry_price
                    * (
                        1 - target_percent
                    )
                )

            return round(
                target,
                2
            )

        except Exception:
            return 0

    # =========================
    # RISK REWARD
    # =========================

    def risk_reward_ratio(
        self,
        entry_price,
        stop_loss,
        target
    ):

        try:

            risk = abs(
                entry_price
                - stop_loss
            )

            reward = abs(
                target
                - entry_price
            )

            if risk <= 0:
                return 0

            return round(
                reward / risk,
                2
            )

        except Exception:
            return 0

    # =========================
    # BREAK EVEN CHECK
    # =========================

    def should_move_to_breakeven(
        self,
        pnl_percent
    ):

        return pnl_percent >= 1.5

    # =========================
    # DAILY LOSS LIMIT
    # =========================

    def daily_loss_limit_hit(
        self,
        daily_loss_percent
    ):

        return (
            daily_loss_percent
            >= MAX_DAILY_LOSS_PERCENT
        )

    # =========================
    # DRAWDOWN CHECK
    # =========================

    def drawdown_limit_hit(
        self,
        drawdown_percent
    ):

        return (
            drawdown_percent
            >= MAX_DRAWDOWN_PERCENT
        )

    # =========================
    # CAPITAL PRESERVATION
    # =========================

    def capital_preservation_mode(
        self,
        balance,
        peak_balance
    ):

        try:

            if peak_balance <= 0:
                return False

            drawdown = (
                (
                    peak_balance
                    - balance
                )
                / peak_balance
            ) * 100

            return drawdown >= 15

        except Exception:
            return False

    # =========================
    # SAFE TRADE VALIDATION
    # =========================

    def validate_trade_risk(
        self,
        balance,
        leverage,
        signal_score
    ):

        try:

            if balance < MIN_BALANCE_INR:
                return False

            if leverage > MAX_LEVERAGE:
                return False

            if signal_score < 70:
                return False

            return True

        except Exception:
            return False

    # =========================
    # PARTIAL BOOKING
    # =========================

    def should_partial_book(
        self,
        pnl_percent
    ):

        return pnl_percent >= 2

    # =========================
    # TRAILING ACTIVATION
    # =========================

    def should_activate_trailing(
        self,
        pnl_percent
    ):

        return pnl_percent >= 1

    # =========================
    # AUTO COMPOUND
    # =========================

    def auto_compound_size(
        self,
        balance
    ):

        try:

            if balance <= 1000:
                return 1

            if balance <= 3000:
                return 2

            if balance <= 5000:
                return 3

            if balance <= 10000:
                return 5

            return 10

        except Exception:
            return 1