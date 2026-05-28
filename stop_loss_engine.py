class StopLossEngine:

    # =========================
    # DYNAMIC STOP LOSS
    # =========================

    def dynamic_stop_loss(
        self,
        entry_price,
        side,
        volatility
    ):

        stop_percent = 2

        if volatility == "high":
            stop_percent = 3

        if volatility == "low":
            stop_percent = 1

        if side == "buy":

            stop = (
                entry_price
                * (
                    1 - (
                        stop_percent / 100
                    )
                )
            )

        else:

            stop = (
                entry_price
                * (
                    1 + (
                        stop_percent / 100
                    )
                )
            )

        return round(
            stop,
            2
        )

    # =========================
    # BREAK EVEN CHECK
    # =========================

    def move_to_break_even(
        self,
        pnl_percent
    ):

        return pnl_percent >= 1.5

    # =========================
    # TRAILING STOP
    # =========================

    def trailing_stop(
        self,
        highest_price,
        trailing_percent
    ):

        stop = (
            highest_price
            * (
                1 - (
                    trailing_percent / 100
                )
            )
        )

        return round(
            stop,
            2
        )

    # =========================
    # STOP LOSS HIT
    # =========================

    def stop_loss_hit(
        self,
        current_price,
        stop_price,
        side
    ):

        if side == "buy":
            return current_price <= stop_price

        return current_price >= stop_price