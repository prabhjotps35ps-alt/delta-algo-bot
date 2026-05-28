class ProfitOptimizer:

    # =========================
    # PROFIT LOCK
    # =========================

    def profit_lock(
        self,
        pnl_percent
    ):

        return pnl_percent >= 2

    # =========================
    # PARTIAL BOOKING
    # =========================

    def partial_booking(
        self,
        pnl_percent
    ):

        return pnl_percent >= 1.5

    # =========================
    # EXTEND WINNER
    # =========================

    def extend_winner(
        self,
        trend_strength,
        volume_strength
    ):

        return (
            trend_strength == "strong"
            and volume_strength == "strong"
        )

    # =========================
    # EXIT WEAK TRADE
    # =========================

    def exit_weak_trade(
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
    # AUTO COMPOUND
    # =========================

    def auto_compound(
        self,
        balance
    ):

        if balance <= 1000:
            return 1

        if balance <= 3000:
            return 2

        if balance <= 5000:
            return 3

        return 5