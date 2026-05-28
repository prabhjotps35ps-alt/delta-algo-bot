import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class SmartMoneyEngine:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

        self.last_high = 0

        self.last_low = 0

        self.market_structure = (
            "neutral"
        )

    # =========================
    # FETCH CANDLES
    # =========================

    def fetch_candles(self):

        return (
            self.market.fetch_ohlcv(

                self.symbol,

                timeframe="5m",

                limit=50

            )
        )

    # =========================
    # STRUCTURE ANALYSIS
    # =========================

    def structure_analysis(self):

        try:

            candles = (
                self.fetch_candles()
            )

            highs = []

            lows = []

            closes = []

            for candle in candles:

                highs.append(
                    candle[2]
                )

                lows.append(
                    candle[3]
                )

                closes.append(
                    candle[4]
                )

            current_high = max(highs)

            current_low = min(lows)

            current_close = closes[-1]

            # =========================
            # BREAK OF STRUCTURE
            # =========================

            bos = False

            choch = False

            if current_close > (
                self.last_high
            ):

                bos = True

                self.market_structure = (
                    "bullish"
                )

            if current_close < (
                self.last_low
            ):

                choch = True

                self.market_structure = (
                    "bearish"
                )

            self.last_high = (
                current_high
            )

            self.last_low = (
                current_low
            )

            return {

                "time":
                str(datetime.now()),

                "bos":
                bos,

                "choch":
                choch,

                "market_structure":
                self.market_structure,

                "high":
                current_high,

                "low":
                current_low,

                "close":
                current_close

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # LIQUIDITY SWEEP
    # =========================

    def liquidity_sweep_detection(self):

        try:

            candles = (
                self.fetch_candles()
            )

            latest = candles[-1]

            previous = candles[-2]

            latest_high = latest[2]

            previous_high = previous[2]

            latest_low = latest[3]

            previous_low = previous[3]

            sweep = "none"

            if latest_high > previous_high:

                sweep = "buy_side_liquidity"

            if latest_low < previous_low:

                sweep = "sell_side_liquidity"

            return {

                "time":
                str(datetime.now()),

                "sweep":
                sweep

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # SMART MONEY SIGNAL
    # =========================

    def smart_money_signal(self):

        structure = (
            self.structure_analysis()
        )

        sweep = (
            self.liquidity_sweep_detection()
        )

        if not structure:

            return "wait"

        if (

            structure["market_structure"]
            == "bullish"

            and

            sweep["sweep"]
            == "sell_side_liquidity"

        ):

            return "smart_buy"

        if (

            structure["market_structure"]
            == "bearish"

            and

            sweep["sweep"]
            == "buy_side_liquidity"

        ):

            return "smart_sell"

        return "wait"


if __name__ == "__main__":

    engine = (
        SmartMoneyEngine()
    )

    print(
        engine.smart_money_signal()
    )