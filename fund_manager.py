class FundManager:

    def __init__(self):

        self.total_balance = 0

        self.used_margin = 0

        self.free_balance = 0

    # =========================
    # UPDATE BALANCE
    # =========================

    def update_balance(
        self,
        balance,
        used_margin
    ):

        self.total_balance = balance

        self.used_margin = used_margin

        self.free_balance = (
            balance - used_margin
        )

        return True

    # =========================
    # FREE MARGIN
    # =========================

    def available_margin(self):

        return round(
            self.free_balance,
            2
        )

    # =========================
    # CAPITAL PROTECTION
    # =========================

    def capital_protection(
        self,
        drawdown_percent
    ):

        return drawdown_percent < 20

    # =========================
    # SAFE MODE
    # =========================

    def safe_mode_needed(
        self,
        drawdown_percent
    ):

        return drawdown_percent >= 15

    # =========================
    # EXPOSURE CHECK
    # =========================

    def exposure_check(
        self,
        exposure_percent
    ):

        return exposure_percent <= 50

    # =========================
    # FUND SNAPSHOT
    # =========================

    def snapshot(self):

        return {
            "total_balance": (
                self.total_balance
            ),
            "used_margin": (
                self.used_margin
            ),
            "free_balance": (
                self.free_balance
            )
        }