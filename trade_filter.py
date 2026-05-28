class TradeFilter:

    def allow(
        self,
        signal_score,
        spread,
        volatility
    ):

        if signal_score < 70:
            return False

        if spread > 1:
            return False

        if volatility == "high":
            return False

        return True