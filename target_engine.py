class TargetEngine:

    # =========================
    # DYNAMIC TARGET
    # =========================

    def dynamic_target(
        self,
        entry_price,
        side,
        trend_strength,
        volatility
    ):

        target_percent = 2

        if trend_strength == "strong":
            target_percent = 4

        if volatility == "high":
            target_percent = 1.5

        if side == "buy":

            target = (
                entry_price
                * (
                    1 + (
                        target_percent / 100
                    )
                )
            )

        else:

            target = (
                entry_price
                * (
                    1 - (
                        target_percent / 100
                    )
                )
            )

        return round(
            target,
            2
        )

    # =========================
    # PARTIAL TARGETS
    # =========================

    def partial_targets(
        self,
        entry_price,
        side
    ):

        if side == "buy":

            tp1 = entry_price * 1.01

            tp2 = entry_price * 1.02

            tp3 = entry_price * 1.04

        else:

            tp1 = entry_price * 0.99

            tp2 = entry_price * 0.98

            tp3 = entry_price * 0.96

        return {
            "tp1": round(tp1, 2),
            "tp2": round(tp2, 2),
            "tp3": round(tp3, 2)
        }

    # =========================
    # TARGET EXTENSION
    # =========================

    def should_extend_target(
        self,
        strong_volume,
        strong_momentum
    ):

        return (
            strong_volume
            and strong_momentum
        )

    # =========================
    # EARLY PROFIT EXIT
    # =========================

    def early_profit_exit(
        self,
        weak_momentum,
        weak_volume
    ):

        return (
            weak_momentum
            or weak_volume
        )

    # =========================
    # TARGET HIT CHECK
    # =========================

    def target_hit(
        self,
        current_price,
        target_price,
        side
    ):

        if side == "buy":
            return current_price >= target_price

        return current_price <= target_price