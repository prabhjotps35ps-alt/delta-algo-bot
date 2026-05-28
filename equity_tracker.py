class EquityTracker:

    def __init__(self):

        self.peak_balance = 0

        self.current_balance = 0

    # =========================
    # UPDATE EQUITY
    # =========================

    def update_equity(
        self,
        balance
    ):

        self.current_balance = balance

        if balance > self.peak_balance:

            self.peak_balance = balance

    # =========================
    # DRAWDOWN
    # =========================

    def drawdown_percent(self):

        if self.peak_balance <= 0:
            return 0

        drawdown = (
            (
                self.peak_balance
                - self.current_balance
            )
            / self.peak_balance
        ) * 100

        return round(
            drawdown,
            2
        )

    # =========================
    # EQUITY STATUS
    # =========================

    def equity_status(self):

        drawdown = (
            self.drawdown_percent()
        )

        if drawdown < 10:
            return "healthy"

        if drawdown < 20:
            return "warning"

        return "danger"

    # =========================
    # EQUITY SNAPSHOT
    # =========================

    def snapshot(self):

        return {
            "peak_balance": (
                self.peak_balance
            ),
            "current_balance": (
                self.current_balance
            ),
            "drawdown_percent": (
                self.drawdown_percent()
            ),
            "status": (
                self.equity_status()
            )
        }