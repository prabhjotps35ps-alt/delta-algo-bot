class TradingRuleEngine:

    # =========================
    # TREND RULE
    # =========================

    def trend_rule(
        self,
        trend
    ):

        return trend in [
            "bullish",
            "bearish"
        ]

    # =========================
    # VOLUME RULE
    # =========================

    def volume_rule(
        self,
        volume_strength
    ):

        return volume_strength in [
            "strong",
            "medium"
        ]

    # =========================
    # VOLATILITY RULE
    # =========================

    def volatility_rule(
        self,
        volatility
    ):

        return volatility != "high"

    # =========================
    # MOMENTUM RULE
    # =========================

    def momentum_rule(
        self,
        momentum
    ):

        return momentum in [
            "strong_bullish",
            "strong_bearish",
            "neutral"
        ]

    # =========================
    # LIQUIDITY RULE
    # =========================

    def liquidity_rule(
        self,
        liquidity
    ):

        return liquidity != "low"

    # =========================
    # INDICATOR RULE
    # =========================

    def indicator_rule(
        self,
        indicators
    ):

        trend = indicators.get(
            "trend"
        )

        return trend in [
            "bullish",
            "bearish"
        ]

    # =========================
    # FAKE BREAKOUT RULE
    # =========================

    def fake_breakout_rule(
        self,
        fake_breakout
    ):

        return not fake_breakout

    # =========================
    # SPREAD RULE
    # =========================

    def spread_rule(
        self,
        spread
    ):

        return spread < 1

    # =========================
    # SLIPPAGE RULE
    # =========================

    def slippage_rule(
        self,
        slippage
    ):

        return slippage != "high"

    # =========================
    # MARKET REGIME RULE
    # =========================

    def market_regime_rule(
        self,
        market_regime
    ):

        return market_regime != "sideways"

    # =========================
    # FINAL TRADE VALIDATION
    # =========================

    def allow_trade(
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

        volatility = (
            market_analysis.get(
                "volatility"
            )
        )

        momentum = market_analysis.get(
            "momentum"
        )

        liquidity = market_analysis.get(
            "liquidity"
        )

        indicators = market_analysis.get(
            "indicators",
            {}
        )

        if not self.trend_rule(
            trend
        ):

            return False

        if not self.volume_rule(
            volume_strength
        ):

            return False

        if not self.volatility_rule(
            volatility
        ):

            return False

        if not self.momentum_rule(
            momentum
        ):

            return False

        if not self.liquidity_rule(
            liquidity
        ):

            return False

        if not self.indicator_rule(
            indicators
        ):

            return False

        return True

    # =========================
    # RISK LOCK RULE
    # =========================

    def risk_lock_rule(
        self,
        daily_loss_hit,
        drawdown_hit
    ):

        return not (
            daily_loss_hit
            or drawdown_hit
        )

    # =========================
    # COOL DOWN RULE
    # =========================

    def cooldown_rule(
        self,
        cooldown_active
    ):

        return not cooldown_active

    # =========================
    # OVERTRADING RULE
    # =========================

    def overtrading_rule(
        self,
        total_trades
    ):

        return total_trades < 10

    # =========================
    # FINAL SYSTEM STATUS
    # =========================

    def system_trade_status(
        self,
        trade_allowed
    ):

        if trade_allowed:
            return "trading_enabled"

        return "trading_blocked"