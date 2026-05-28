class ExecutionEngine:

    # =========================
    # EXECUTE TRADE
    # =========================

    def execute_trade(
        self,
        delta,
        symbol,
        side,
        size,
        leverage
    ):

        try:

            order = (
                delta.place_market_order(
                    symbol=symbol,
                    side=side,
                    size=size,
                    leverage=leverage
                )
            )

            return {
                "success": True,
                "order": order
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # LIMIT ORDER EXECUTION
    # =========================

    def execute_limit_order(
        self,
        delta,
        symbol,
        side,
        size,
        price,
        leverage
    ):

        try:

            order = (
                delta.place_limit_order(
                    symbol=symbol,
                    side=side,
                    size=size,
                    price=price,
                    leverage=leverage
                )
            )

            return {
                "success": True,
                "order": order
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # STOP LOSS EXECUTION
    # =========================

    def place_stop_loss(
        self,
        delta,
        symbol,
        side,
        size,
        stop_price
    ):

        try:

            order = (
                delta.place_stop_loss(
                    symbol=symbol,
                    side=side,
                    size=size,
                    stop_price=stop_price
                )
            )

            return {
                "success": True,
                "stop_loss": order
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # TAKE PROFIT EXECUTION
    # =========================

    def place_take_profit(
        self,
        delta,
        symbol,
        side,
        size,
        target_price
    ):

        try:

            order = (
                delta.place_take_profit(
                    symbol=symbol,
                    side=side,
                    size=size,
                    target_price=target_price
                )
            )

            return {
                "success": True,
                "take_profit": order
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # SLIPPAGE CHECK
    # =========================

    def slippage_check(
        self,
        expected_price,
        market_price
    ):

        slippage = abs(
            market_price
            - expected_price
        )

        slippage_percent = (
            slippage
            / expected_price
        ) * 100

        return slippage_percent < 1

    # =========================
    # SPREAD CHECK
    # =========================

    def spread_check(
        self,
        spread
    ):

        return spread < 1

    # =========================
    # EXECUTION VALIDATION
    # =========================

    def validate_execution(
        self,
        signal_score,
        spread,
        slippage_ok
    ):

        if signal_score < 70:
            return False

        if spread > 1:
            return False

        if not slippage_ok:
            return False

        return True

    # =========================
    # RETRY EXECUTION
    # =========================

    def retry_execution(
        self,
        execute_function,
        retries=3
    ):

        for _ in range(retries):

            result = execute_function()

            if result.get("success"):
                return result

        return {
            "success": False,
            "error": "Execution failed"
        }

    # =========================
    # EXECUTION REPORT
    # =========================

    def execution_report(
        self,
        symbol,
        side,
        size,
        leverage
    ):

        return {
            "symbol": symbol,
            "side": side,
            "size": size,
            "leverage": leverage,
            "status": "executed"
        }