import time
import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class LiveOrderFlowTracker:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

        # =========================
        # ORDERFLOW MEMORY
        # =========================

        self.last_bid_volume = 0

        self.last_ask_volume = 0

        self.last_price = 0

        self.market_pressure = (
            "neutral"
        )

        self.order_shift = (
            "stable"
        )

        self.liquidity_state = (
            "normal"
        )

        self.order_imbalance = 0

        self.buy_pressure_score = 0

        self.sell_pressure_score = 0

    # =========================
    # FETCH ORDERBOOK
    # =========================

    def fetch_orderbook(self):

        try:

            return (
                self.market.fetch_orderbook(
                    self.symbol
                )
            )

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # ANALYZE ORDERFLOW
    # =========================

    def analyze_orderflow(self):

        try:

            orderbook = (
                self.fetch_orderbook()
            )

            if not orderbook:

                return None

            bids = (
                orderbook["bids"][:10]
            )

            asks = (
                orderbook["asks"][:10]
            )

            total_bid_volume = 0

            total_ask_volume = 0

            # =========================
            # BID ANALYSIS
            # =========================

            for bid in bids:

                total_bid_volume += (
                    bid[1]
                )

            # =========================
            # ASK ANALYSIS
            # =========================

            for ask in asks:

                total_ask_volume += (
                    ask[1]
                )

            # =========================
            # IMBALANCE
            # =========================

            total_volume = (

                total_bid_volume
                + total_ask_volume

            )

            if total_volume > 0:

                imbalance = (

                    (
                        total_bid_volume
                        - total_ask_volume
                    )

                    / total_volume

                ) * 100

            else:

                imbalance = 0

            self.order_imbalance = round(
                imbalance,
                2
            )

            # =========================
            # MARKET PRESSURE
            # =========================

            if imbalance >= 20:

                self.market_pressure = (
                    "strong_buying"
                )

                self.buy_pressure_score += 1

            elif imbalance <= -20:

                self.market_pressure = (
                    "strong_selling"
                )

                self.sell_pressure_score += 1

            else:

                self.market_pressure = (
                    "neutral"
                )

            # =========================
            # ORDER SHIFT DETECTION
            # =========================

            bid_change = (

                total_bid_volume
                - self.last_bid_volume

            )

            ask_change = (

                total_ask_volume
                - self.last_ask_volume

            )

            if bid_change > ask_change:

                self.order_shift = (
                    "buyers_increasing"
                )

            elif ask_change > bid_change:

                self.order_shift = (
                    "sellers_increasing"
                )

            else:

                self.order_shift = (
                    "stable"
                )

            # =========================
            # LIQUIDITY ANALYSIS
            # =========================

            if total_volume >= 100:

                self.liquidity_state = (
                    "high"
                )

            elif total_volume >= 50:

                self.liquidity_state = (
                    "medium"
                )

            else:

                self.liquidity_state = (
                    "low"
                )

            # =========================
            # STORE PREVIOUS VALUES
            # =========================

            self.last_bid_volume = (
                total_bid_volume
            )

            self.last_ask_volume = (
                total_ask_volume
            )

            return {

                "time":
                str(datetime.now()),

                "bid_volume":
                round(
                    total_bid_volume,
                    2
                ),

                "ask_volume":
                round(
                    total_ask_volume,
                    2
                ),

                "imbalance":
                self.order_imbalance,

                "market_pressure":
                self.market_pressure,

                "order_shift":
                self.order_shift,

                "liquidity":
                self.liquidity_state

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # AI ADJUSTMENT ENGINE
    # =========================

    def ai_adjustment_engine(
        self,
        signal
    ):

        report = (
            self.analyze_orderflow()
        )

        if not report:

            return signal

        # =========================
        # BLOCK WEAK BUY
        # =========================

        if (

            signal == "buy"

            and

            report["market_pressure"]
            == "strong_selling"

        ):

            return "wait"

        # =========================
        # BLOCK WEAK SELL
        # =========================

        if (

            signal == "sell"

            and

            report["market_pressure"]
            == "strong_buying"

        ):

            return "wait"

        # =========================
        # BUY BOOST
        # =========================

        if (

            signal == "buy"

            and

            report["order_shift"]
            == "buyers_increasing"

        ):

            return "strong_buy"

        # =========================
        # SELL BOOST
        # =========================

        if (

            signal == "sell"

            and

            report["order_shift"]
            == "sellers_increasing"

        ):

            return "strong_sell"

        return signal

    # =========================
    # LIVE TRACKING LOOP
    # =========================

    def start_tracking_loop(self):

        while True:

            try:

                report = (
                    self.analyze_orderflow()
                )

                print(
                    report
                )

                time.sleep(5)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Tracking Error:",
                    str(e)
                )


if __name__ == "__main__":

    tracker = (
        LiveOrderFlowTracker()
    )

    tracker.start_tracking_loop()