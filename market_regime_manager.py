class MarketRegimeManager:

    def detect(
        self,
        trend,
        volatility
    ):

        if trend == "bullish":

            if volatility == "low":
                return "stable_bull"

            return "volatile_bull"

        if trend == "bearish":

            if volatility == "low":
                return "stable_bear"

            return "volatile_bear"

        return "sideways"