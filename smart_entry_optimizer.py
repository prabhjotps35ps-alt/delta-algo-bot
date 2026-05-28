class SmartEntryOptimizer:

    def __init__(self):

        self.minimum_confidence = 85

    # =========================
    # ENTRY QUALITY SCORE
    # =========================

    def entry_quality_score(
        self,
        confidence,
        liquidity_signal,
        volatility
    ):

        score = confidence

        # =========================
        # LIQUIDITY BOOST
        # =========================

        if liquidity_signal == (
            "bullish_liquidity"
        ):

            score += 5

        # =========================
        # VOLATILITY PENALTY
        # =========================

        if volatility == "high":

            score -= 15

        elif volatility == "medium":

            score -= 5

        return min(score, 100)

    # =========================
    # ENTRY FILTER
    # =========================

    def entry_filter(
        self,
        final_score
    ):

        return (
            final_score
            >= self.minimum_confidence
        )