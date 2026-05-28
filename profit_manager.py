class ProfitManager:

    def __init__(self):

        self.daily_profit = 0

        self.weekly_profit = 0

    # =========================
    # UPDATE DAILY PROFIT
    # =========================

    def update_daily_profit(
        self,
        profit
    ):

        self.daily_profit += profit

        return self.daily_profit

    # =========================
    # UPDATE WEEKLY PROFIT
    # =========================

    def update_weekly_profit(
        self,
        profit
    ):

        self.weekly_profit += profit

        return self.weekly_profit

    # =========================
    # DAILY TARGET HIT
    # =========================

    def daily_target_hit(
        self,
        target
    ):

        return (
            self.daily_profit
            >= target
        )

    # =========================
    # PROFIT LOCK
    # =========================

    def profit_lock(
        self,
        pnl_percent
    ):

        return pnl_percent >= 2

    # =========================
    # PROFIT SNAPSHOT
    # =========================

    def snapshot(self):

        return {
            "daily_profit": (
                self.daily_profit
            ),
            "weekly_profit": (
                self.weekly_profit
            )
        }