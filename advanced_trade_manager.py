class AdvancedTradeManager:

    def __init__(self):

        self.trailing_active = False

        self.break_even_active = False

    # =========================
    # TRAILING STOP ACTIVATION
    # =========================

    def activate_trailing(
        self,
        pnl_percent
    ):

        if pnl_percent >= 1:

            self.trailing_active = True

            return True

        return False

    # =========================
    # BREAK EVEN ACTIVATION
    # =========================

    def activate_break_even(
        self,
        pnl_percent
    ):

        if pnl_percent >= 1.5:

            self.break_even_active = True

            return True

        return False

    # =========================
    # PARTIAL PROFIT BOOKING
    # =========================

    def partial_profit_booking(
        self,
        pnl_percent
    ):

        return pnl_percent >= 2

    # =========================
    # TARGET EXTENSION
    # =========================

    def extend_target(
        self,
        strong_trend,
        strong_volume
    ):

        if strong_trend and strong_volume:
            return True

        return False

    # =========================
    # EARLY EXIT DETECTION
    # =========================

    def early_exit_signal(
        self,
        momentum,
        volume_strength
    ):

        if momentum == "weak":
            return True

        if volume_strength == "weak":
            return True

        return False

    # =========================
    # REVERSAL DETECTION
    # =========================

    def reversal_detected(
        self,
        trend,
        momentum
    ):

        if trend == "bearish":

            if momentum == "strong_bearish":
                return True

        return False

    # =========================
    # TRADE MANAGEMENT DECISION
    # =========================

    def manage_trade(
        self,
        pnl_percent,
        trend,
        momentum,
        volume_strength
    ):

        trailing = self.activate_trailing(
            pnl_percent
        )

        breakeven = self.activate_break_even(
            pnl_percent
        )

        partial_book = (
            self.partial_profit_booking(
                pnl_percent
            )
        )

        early_exit = self.early_exit_signal(
            momentum,
            volume_strength
        )

        reversal = self.reversal_detected(
            trend,
            momentum
        )

        return {
            "activate_trailing": trailing,
            "activate_break_even": breakeven,
            "partial_booking": partial_book,
            "early_exit": early_exit,
            "reversal_detected": reversal
        }

    # =========================
    # PROFIT LOCK SYSTEM
    # =========================

    def profit_lock(
        self,
        pnl_percent
    ):

        return pnl_percent >= 3

    # =========================
    # EMERGENCY EXIT CHECK
    # =========================

    def emergency_exit_needed(
        self,
        volatility,
        slippage
    ):

        if volatility == "high":
            return True

        if slippage == "high":
            return True

        return False