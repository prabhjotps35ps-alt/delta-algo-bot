import traceback

from market_data_feed import (
    MarketDataFeed
)


class MarketRegimeAnalyzer:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

    # =========================
    # REGIME ANALYSIS
    # =========================

    def analyze_regime(self):

        try:

            candles = (
                self.market.fetch_ohlcv(

                    self.symbol,

                    timeframe="5m",

                    limit=50

                )
            )

            closes = []

            for candle in candles:

                closes.append(
                    candle[4]
                )

            highest = max(closes)

            lowest = min(closes)

            current = closes[-1]

            movement = (

                (
                    highest - lowest
                )

                / current

            ) * 100

            if movement >= 5:

                return "trending"

            if movement >= 2:

                return "volatile"

            return "sideways"

        except Exception as e:

            traceback.print_exc()

            return "unknown"