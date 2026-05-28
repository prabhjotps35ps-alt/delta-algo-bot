class SignalScoring:

    # =========================
    # TREND SCORE
    # =========================

    def trend_score(
        self,
        trend
    ):

        if trend == "bullish":
            return 25

        if trend == "bearish":
            return 25

        return 5

    # =========================
    # VOLUME SCORE
    # =========================

    def volume_score(
        self,
        volume_strength
    ):

        if volume_strength == "strong":
            return 20

        if volume_strength == "medium":
            return 10

        return 0

    # =========================
    # MOMENTUM SCORE
    # =========================

    def momentum_score(
        self,
        momentum
    ):

        if momentum in [
            "strong_bullish",
            "strong_bearish"
        ]:

            return 20

        if momentum == "neutral":
            return 5

        return 0

    # =========================
    # VOLATILITY SCORE
    # =========================

    def volatility_score(
        self,
        volatility
    ):

        if volatility == "low":
            return 15

        if volatility == "medium":
            return 10

        return 0

    # =========================
    # LIQUIDITY SCORE
    # =========================

    def liquidity_score(
        self,
        liquidity
    ):

        if liquidity == "high":
            return 10

        if liquidity == "medium":
            return 5

        return 0

    # =========================
    # INDICATOR SCORE
    # =========================

    def indicator_score(
        self,
        indicators
    ):

        score = 0

        trend = indicators.get(
            "trend"
        )

        adx = indicators.get(
            "adx_strength"
        )

        if trend in [
            "bullish",
            "bearish"
        ]:

            score += 10

        if adx == "strong":
            score += 10

        return score

    # =========================
    # FINAL SCORE
    # =========================

    def calculate_score(
        self,
        market_analysis
    ):

        trend = market_analysis.get(
            "trend"
        )

        volume_strength = (
            market_analysis.get(
                "volume_strength"
            )
        )

        momentum = market_analysis.get(
            "momentum"
        )

        volatility = (
            market_analysis.get(
                "volatility"
            )
        )

        liquidity = market_analysis.get(
            "liquidity"
        )

        indicators = market_analysis.get(
            "indicators",
            {}
        )

        total_score = 0

        total_score += self.trend_score(
            trend
        )

        total_score += self.volume_score(
            volume_strength
        )

        total_score += self.momentum_score(
            momentum
        )

        total_score += self.volatility_score(
            volatility
        )

        total_score += self.liquidity_score(
            liquidity
        )

        total_score += self.indicator_score(
            indicators
        )

        return min(
            total_score,
            100
        )

    # =========================
    # SIGNAL QUALITY
    # =========================

    def signal_quality(
        self,
        score
    ):

        if score >= 85:
            return "excellent"

        if score >= 70:
            return "good"

        if score >= 50:
            return "weak"

        return "reject"

    # =========================
    # TRADE RECOMMENDATION
    # =========================

    def trade_recommendation(
        self,
        score
    ):

        if score >= 85:
            return "strong_trade"

        if score >= 70:
            return "allowed_trade"

        return "avoid_trade"