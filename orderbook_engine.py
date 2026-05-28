import random


class OrderbookEngine:

    # =========================
    # LIQUIDITY ANALYSIS
    # =========================

    def liquidity_analysis(
        self,
        symbol
    ):

        liquidity = random.randint(
            1,
            100
        )

        if liquidity >= 70:
            return "high"

        if liquidity >= 40:
            return "medium"

        return "low"

    # =========================
    # BUYER SELLER PRESSURE
    # =========================

    def buyer_seller_pressure(
        self,
        bids,
        asks
    ):

        if bids > asks:
            return "buyers_dominant"

        if asks > bids:
            return "sellers_dominant"

        return "balanced"

    # =========================
    # ORDERBOOK IMBALANCE
    # =========================

    def orderbook_imbalance(
        self,
        bids,
        asks
    ):

        if asks == 0:
            return 0

        imbalance = bids / asks

        return round(
            imbalance,
            2
        )

    # =========================
    # LIQUIDITY WALL DETECTION
    # =========================

    def liquidity_wall_detection(
        self,
        wall_size
    ):

        return wall_size > 100000

    # =========================
    # SPOOF DETECTION
    # =========================

    def spoof_detection(
        self,
        sudden_cancel_orders
    ):

        return sudden_cancel_orders > 50

    # =========================
    # MARKET DEPTH
    # =========================

    def market_depth(
        self,
        total_bids,
        total_asks
    ):

        total = (
            total_bids
            + total_asks
        )

        if total > 1000000:
            return "deep"

        if total > 300000:
            return "medium"

        return "shallow"

    # =========================
    # SPREAD CALCULATION
    # =========================

    def spread_calculation(
        self,
        best_bid,
        best_ask
    ):

        spread = (
            best_ask
            - best_bid
        )

        return round(
            spread,
            4
        )

    # =========================
    # SLIPPAGE RISK
    # =========================

    def slippage_risk(
        self,
        spread
    ):

        if spread > 1:
            return "high"

        if spread > 0.5:
            return "medium"

        return "low"

    # =========================
    # SMART ORDER FLOW
    # =========================

    def smart_order_flow(
        self,
        aggressive_buys,
        aggressive_sells
    ):

        if aggressive_buys > aggressive_sells:
            return "bullish_flow"

        if aggressive_sells > aggressive_buys:
            return "bearish_flow"

        return "neutral_flow"

    # =========================
    # ORDERBOOK SNAPSHOT
    # =========================

    def orderbook_snapshot(
        self,
        symbol
    ):

        bids = random.randint(
            10000,
            100000
        )

        asks = random.randint(
            10000,
            100000
        )

        total_bids = random.randint(
            100000,
            1000000
        )

        total_asks = random.randint(
            100000,
            1000000
        )

        best_bid = random.uniform(
            100,
            200
        )

        best_ask = (
            best_bid
            + random.uniform(
                0.1,
                1.5
            )
        )

        pressure = (
            self.buyer_seller_pressure(
                bids,
                asks
            )
        )

        imbalance = (
            self.orderbook_imbalance(
                bids,
                asks
            )
        )

        depth = self.market_depth(
            total_bids,
            total_asks
        )

        spread = (
            self.spread_calculation(
                best_bid,
                best_ask
            )
        )

        slippage = (
            self.slippage_risk(
                spread
            )
        )

        return {
            "symbol": symbol,
            "pressure": pressure,
            "imbalance": imbalance,
            "depth": depth,
            "spread": spread,
            "slippage_risk": slippage
        }