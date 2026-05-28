class RiskManagementEngine:

    def __init__(self):

        self.max_risk_per_trade = 2

        self.max_daily_loss = 10

    # =========================
    # POSITION SIZE
    # =========================

    def calculate_position_size(
        self,
        balance,
        stoploss_percent
    ):

        risk_amount = (
            balance
            * self.max_risk_per_trade
        ) / 100

        size = (
            risk_amount
            / stoploss_percent
        )

        return round(
            size,
            4
        )

    # =========================
    # DAILY LOSS CHECK
    # =========================

    def daily_loss_check(
        self,
        daily_loss
    ):

        if daily_loss >= (
            self.max_daily_loss
        ):

            return False

        return True

    # =========================
    # LEVERAGE CHECK
    # =========================

    def leverage_check(
        self,
        leverage
    ):

        if leverage > 5:

            return False

        return True