class DynamicExitManager:

    # =========================
    # EXIT DECISION
    # =========================

    def should_exit(
        self,
        reversal,
        weak_volume,
        emergency
    ):

        if reversal:
            return True

        if weak_volume:
            return True

        if emergency:
            return True

        return False

    # =========================
    # REVERSAL CHECK
    # =========================

    def reversal_detected(
        self,
        trend,
        momentum
    ):

        if trend == "bearish":

            if momentum == "strong_bearish":
                return True

        return False

    # =========================
    # EMERGENCY EXIT
    # =========================

    def emergency_exit(
        self,
        volatility,
        api_failure
    ):

        if volatility == "high":
            return True

        if api_failure:
            return True

        return False

    # =========================
    # EXIT REASON
    # =========================

    def exit_reason(
        self,
        reversal,
        weak_volume,
        emergency
    ):

        if emergency:
            return "emergency_exit"

        if reversal:
            return "trend_reversal"

        if weak_volume:
            return "weak_volume"

        return "normal_exit"