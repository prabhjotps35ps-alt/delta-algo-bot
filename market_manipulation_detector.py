import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class MarketManipulationDetector:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

    # =========================
    # PUMP DETECTOR
    # =========================

    def pump_detector(self):

        try:

            candles = (
                self.market.fetch_ohlcv(

                    self.symbol,

                    timeframe="1m",

                    limit=5

                )
            )

            first = candles[0][4]

            last = candles[-1][4]

            movement = (

                (
                    last - first
                )

                / first

            ) * 100

            return movement >= 3

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # DUMP DETECTOR
    # =========================

    def dump_detector(self):

        try:

            candles = (
                self.market.fetch_ohlcv(

                    self.symbol,

                    timeframe="1m",

                    limit=5

                )
            )

            first = candles[0][4]

            last = candles[-1][4]

            movement = (

                (
                    first - last
                )

                / first

            ) * 100

            return movement >= 3

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # SPOOF DETECTOR
    # =========================

    def spoof_detector(self):

        try:

            orderbook = (
                self.market.fetch_orderbook(
                    self.symbol
                )
            )

            spoof_orders = 0

            for bid in orderbook["bids"][:20]:

                if bid[1] >= 25:

                    spoof_orders += 1

            for ask in orderbook["asks"][:20]:

                if ask[1] >= 25:

                    spoof_orders += 1

            return spoof_orders >= 4

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # FINAL MANIPULATION REPORT
    # =========================

    def manipulation_report(self):

        pump = (
            self.pump_detector()
        )

        dump = (
            self.dump_detector()
        )

        spoof = (
            self.spoof_detector()
        )

        market_safe = not (
            pump
            or dump
            or spoof
        )

        return {

            "time":
            str(datetime.now()),

            "pump_detected":
            pump,

            "dump_detected":
            dump,

            "spoof_detected":
            spoof,

            "market_safe":
            market_safe

        }