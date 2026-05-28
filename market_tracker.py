import random


class MarketTracker:

    # =========================
    # TREND ANALYSIS
    # =========================

    def trend_analysis(
        self,
        symbol
    ):

        trend = random.choice([
            "bullish",
            "bearish",
            "neutral"
        ])

        return trend

    # =========================
    # VOLATILITY ANALYSIS
    # =========================

    def volatility_analysis(
        self,
        symbol
    ):

        volatility = random.uniform(
            0.5,
            6
        )

        if volatility > 4:
            return "high"

        if volatility < 1.5:
            return "low"

        return "medium"

    # =========================
    # MOMENTUM ANALYSIS
    # =========================

    def momentum_analysis(
        self,
        symbol
    ):

        momentum = random.uniform(
            -10,
            10
        )

        if momentum > 3:
            return "strong_bullish"

        if momentum < -3:
            return "strong_bearish"

        return "neutral"

    # =========================
    # MARKET REGIME
    # =========================

    def market_regime(
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

    # =========================
    # TREND STRENGTH
    # =========================

    def trend_strength(
        self,
        momentum
    ):

        if momentum in [
            "strong_bullish",
            "strong_bearish"
        ]:

            return "strong"

        return "weak"

    # =========================
    # MARKET STABILITY
    # =========================

    def market_stability(
        self,
        volatility
    ):

        return volatility != "high"

    # =========================
    # FAKE BREAKOUT DETECTION
    # =========================

    def fake_breakout_detection(
        self,
        candle_body,
        wick_size
    ):

        return wick_size > candle_body

    # =========================
    # LIQUIDITY CHECK
    # =========================

    def liquidity_check(
        self,
        liquidity_score
    ):

        return liquidity_score > 50

    # =========================
    # SPREAD ANALYSIS
    # =========================

    def spread_analysis(
        self,
        spread
    ):

        if spread > 1:
            return "bad"

        return "good"

    # =========================
    # SLIPPAGE ANALYSIS
    # =========================

    def slippage_analysis(
        self,
        slippage
    ):

        if slippage > 1:
            return "high"

        return "acceptable"

    # =========================
    # LIVE MARKET SNAPSHOT
    # =========================

    def live_market_snapshot(
        self,
        symbol
    ):

        trend = self.trend_analysis(
            symbol
        )

        volatility = (
            self.volatility_analysis(
                symbol
            )
        )

        momentum = (
            self.momentum_analysis(
                symbol
            )
        )

        regime = self.market_regime(
            trend,
            volatility
        )

        strength = self.trend_strength(
            momentum
        )

        stability = self.market_stability(
            volatility
        )

        return {
            "symbol": symbol,
            "trend": trend,
            "volatility": volatility,
            "momentum": momentum,
            "market_regime": regime,
            "trend_strength": strength,
            "stable_market": stability
        }