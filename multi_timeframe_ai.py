import traceback

from market_data_feed import (
    MarketDataFeed
)

from indicator_engine import (
    IndicatorEngine
)


class MultiTimeframeAI:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.indicators = (
            IndicatorEngine()
        )

        self.symbol = "BTC/USDT"

        self.timeframes = [

            "1m",

            "5m",

            "15m",

            "1h"

        ]

    # =========================
    # ANALYZE TIMEFRAME
    # =========================

    def analyze_timeframe(
        self,
        timeframe
    ):

        try:

            candles = (
                self.market.fetch_ohlcv(

                    symbol=self.symbol,

                    timeframe=timeframe,

                    limit=100

                )
            )

            closes = []

            for candle in candles:

                closes.append(
                    candle[4]
                )

            ema_fast = (
                self.indicators.ema(
                    closes,
                    20
                )
            )

            ema_slow = (
                self.indicators.ema(
                    closes,
                    50
                )
            )

            rsi = (
                self.indicators.rsi(
                    closes,
                    14
                )
            )

            macd = (
                self.indicators.macd(
                    closes
                )
            )

            trend = "neutral"

            # =========================
            # BULLISH
            # =========================

            if (

                ema_fast > ema_slow

                and

                rsi > 55

                and

                macd["macd"]
                >
                macd["signal"]

            ):

                trend = "bullish"

            # =========================
            # BEARISH
            # =========================

            elif (

                ema_fast < ema_slow

                and

                rsi < 45

                and

                macd["macd"]
                <
                macd["signal"]

            ):

                trend = "bearish"

            return {

                "timeframe":
                timeframe,

                "trend":
                trend,

                "ema_fast":
                round(ema_fast, 2),

                "ema_slow":
                round(ema_slow, 2),

                "rsi":
                round(rsi, 2),

                "macd":
                round(
                    macd["macd"],
                    2
                ),

                "signal":
                round(
                    macd["signal"],
                    2
                )

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "timeframe":
                timeframe,

                "trend":
                "error"

            }

    # =========================
    # GLOBAL ANALYSIS
    # =========================

    def global_analysis(self):

        report = []

        bullish = 0

        bearish = 0

        for timeframe in self.timeframes:

            result = (
                self.analyze_timeframe(
                    timeframe
                )
            )

            report.append(
                result
            )

            if result["trend"] == (
                "bullish"
            ):

                bullish += 1

            elif result["trend"] == (
                "bearish"
            ):

                bearish += 1

        # =========================
        # FINAL DECISION
        # =========================

        final_signal = "wait"

        confidence = 50

        if bullish >= 3:

            final_signal = "multi_buy"

            confidence = 90

        elif bearish >= 3:

            final_signal = "multi_sell"

            confidence = 90

        elif bullish == 2:

            final_signal = "weak_buy"

            confidence = 70

        elif bearish == 2:

            final_signal = "weak_sell"

            confidence = 70

        return {

            "timeframes":
            report,

            "bullish_count":
            bullish,

            "bearish_count":
            bearish,

            "final_signal":
            final_signal,

            "confidence":
            confidence

        }

    # =========================
    # AI FILTER
    # =========================

    def ai_filter(
        self,
        signal
    ):

        report = (
            self.global_analysis()
        )

        # =========================
        # BLOCK WRONG BUY
        # =========================

        if (

            signal == "buy"

            and

            report["final_signal"]
            in [

                "multi_sell",

                "weak_sell"

            ]

        ):

            return "wait"

        # =========================
        # BLOCK WRONG SELL
        # =========================

        if (

            signal == "sell"

            and

            report["final_signal"]
            in [

                "multi_buy",

                "weak_buy"

            ]

        ):

            return "wait"

        # =========================
        # BOOST SIGNALS
        # =========================

        if (

            signal == "buy"

            and

            report["final_signal"]
            == "multi_buy"

        ):

            return "strong_buy"

        if (

            signal == "sell"

            and

            report["final_signal"]
            == "multi_sell"

        ):

            return "strong_sell"

        return signal


if __name__ == "__main__":

    ai = (
        MultiTimeframeAI()
    )

    print(
        ai.global_analysis()
    )