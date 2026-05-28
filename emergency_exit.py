class EmergencyExit:

    # =========================
    # CLOSE POSITION
    # =========================

    def close_position(
        self,
        delta,
        symbol
    ):

        try:

            result = (
                delta.close_position(
                    symbol
                )
            )

            return {
                "success": True,
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # FLASH CRASH DETECTION
    # =========================

    def flash_crash_detected(
        self,
        price_change_percent
    ):

        return (
            abs(price_change_percent)
            >= 10
        )

    # =========================
    # EXTREME VOLATILITY
    # =========================

    def extreme_volatility(
        self,
        volatility
    ):

        return volatility == "high"

    # =========================
    # LIQUIDATION RISK
    # =========================

    def liquidation_risk(
        self,
        liquidation_distance
    ):

        return liquidation_distance < 5

    # =========================
    # API FAILURE DETECTION
    # =========================

    def api_failure_detected(
        self,
        api_status
    ):

        return not api_status

    # =========================
    # INTERNET FAILURE
    # =========================

    def internet_failure_detected(
        self,
        internet_status
    ):

        return not internet_status

    # =========================
    # EMERGENCY CONDITION CHECK
    # =========================

    def emergency_condition(
        self,
        volatility,
        liquidation_distance,
        api_status,
        internet_status
    ):

        if self.extreme_volatility(
            volatility
        ):

            return True

        if self.liquidation_risk(
            liquidation_distance
        ):

            return True

        if self.api_failure_detected(
            api_status
        ):

            return True

        if self.internet_failure_detected(
            internet_status
        ):

            return True

        return False

    # =========================
    # HANDLE CRITICAL ERROR
    # =========================

    def handle_critical_error(
        self,
        error_message
    ):

        return {
            "critical_error": True,
            "message": error_message
        }

    # =========================
    # SAFE EXIT MODE
    # =========================

    def safe_exit_mode(
        self,
        delta,
        symbol
    ):

        result = self.close_position(
            delta,
            symbol
        )

        return {
            "safe_exit_triggered": True,
            "result": result
        }

    # =========================
    # FORCE EXIT ALL
    # =========================

    def force_exit_all_positions(
        self,
        delta
    ):

        try:

            positions = (
                delta.get_positions()
            )

            result = positions.get(
                "result",
                []
            )

            closed = []

            for pos in result:

                size = abs(
                    float(
                        pos.get(
                            "size",
                            0
                        )
                    )
                )

                if size > 0:

                    symbol = pos.get(
                        "product_symbol"
                    )

                    response = (
                        delta.close_position(
                            symbol
                        )
                    )

                    closed.append({
                        "symbol": symbol,
                        "response": response
                    })

            return {
                "success": True,
                "closed_positions": closed
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # EMERGENCY REPORT
    # =========================

    def emergency_report(
        self,
        reason
    ):

        return {
            "emergency": True,
            "reason": reason
        }