class VolatilityShieldEngine:

    def __init__(self):

        self.high_volatility_limit = 3

        self.medium_volatility_limit = 1.5

    # =========================
    # DETECT VOLATILITY
    # =========================

    def detect_volatility(
        self,
        current_price,
        previous_price
    ):

        movement = abs(

            (
                current_price
                - previous_price
            )

            / previous_price

        ) * 100

        if movement >= (
            self.high_volatility_limit
        ):

            return "high"

        if movement >= (
            self.medium_volatility_limit
        ):

            return "medium"

        return "low"

    # =========================
    # VOLATILITY FILTER
    # =========================

    def volatility_filter(
        self,
        volatility
    ):

        if volatility == "high":

            return False

        return True