class EmergencyRuleEngine:

    # =========================
    # FLASH CRASH RULE
    # =========================

    def flash_crash_rule(
        self,
        price_change_percent
    ):

        return (
            abs(price_change_percent)
            >= 10
        )

    # =========================
    # EXTREME VOLATILITY RULE
    # =========================

    def extreme_volatility_rule(
        self,
        volatility
    ):

        return volatility == "high"

    # =========================
    # API FAILURE RULE
    # =========================

    def api_failure_rule(
        self,
        api_status
    ):

        return not api_status

    # =========================
    # INTERNET FAILURE RULE
    # =========================

    def internet_failure_rule(
        self,
        internet_status
    ):

        return not internet_status

    # =========================
    # LIQUIDATION RISK RULE
    # =========================

    def liquidation_risk_rule(
        self,
        liquidation_distance
    ):

        return liquidation_distance < 5

    # =========================
    # SPREAD EXPLOSION RULE
    # =========================

    def spread_explosion_rule(
        self,
        spread
    ):

        return spread > 1.5

    # =========================
    # SLIPPAGE RULE
    # =========================

    def slippage_rule(
        self,
        slippage
    ):

        return slippage == "high"

    # =========================
    # FINAL EMERGENCY CHECK
    # =========================

    def emergency_trigger(
        self,
        volatility,
        api_status,
        internet_status,
        liquidation_distance,
        spread,
        slippage
    ):

        if self.extreme_volatility_rule(
            volatility
        ):

            return True

        if self.api_failure_rule(
            api_status
        ):

            return True

        if self.internet_failure_rule(
            internet_status
        ):

            return True

        if self.liquidation_risk_rule(
            liquidation_distance
        ):

            return True

        if self.spread_explosion_rule(
            spread
        ):

            return True

        if self.slippage_rule(
            slippage
        ):

            return True

        return False

    # =========================
    # EMERGENCY ACTION
    # =========================

    def emergency_action(
        self,
        reason
    ):

        return {
            "emergency": True,
            "action": "close_positions",
            "reason": reason
        }