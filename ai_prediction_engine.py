import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)

from indicator_engine import (
    IndicatorEngine
)

from smart_money_engine import (
    SmartMoneyEngine
)

from multi_timeframe_ai import (
    MultiTimeframeAI
)

from orderbook_heatmap import (
    OrderbookHeatmap
)


class AIPredictionEngine:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.indicators = (
            IndicatorEngine()
        )

        self.smart_money = (
            SmartMoneyEngine()
        )

        self.multi_tf = (
            MultiTimeframeAI()
        )

        self.heatmap = (
            OrderbookHeatmap()
        )

        self.symbol = "BTC/USDT"

    # =========================
    # FETCH MARKET DATA
    # =========================

    def fetch_market_data(self):

        return (
            self.market.fetch_ohlcv(

                self.symbol,

                timeframe="5m",

                limit=100

            )
        )

    # =========================
    # TREND ANALYSIS
    # =========================

    def trend_analysis(self):

        try:

            candles = (
                self.fetch_market_data()
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

            trend = "neutral"

            strength = 50

            # =========================
            # BULLISH
            # =========================

            if (

                ema_fast > ema_slow

                and

                rsi > 55

            ):

                trend = "bullish"

                strength = 85

            # =========================
            # BEARISH
            # =========================

            elif (

                ema_fast < ema_slow

                and

                rsi < 45

            ):

                trend = "bearish"

                strength = 85

            return {

                "trend":
                trend,

                "strength":
                strength,

                "rsi":
                round(rsi, 2)

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "trend":
                "unknown",

                "strength":
                0

            }

    # =========================
    # BREAKOUT PROBABILITY
    # =========================

    def breakout_probability(self):

        try:

            smart_signal = (
                self.smart_money
                .smart_money_signal()
            )

            heatmap = (
                self.heatmap
                .status_report()
            )

            probability = 50

            # =========================
            # SMART MONEY BOOST
            # =========================

            if smart_signal == (
                "smart_buy"
            ):

                probability += 20

            if smart_signal == (
                "smart_sell"
            ):

                probability += 20

            # =========================
            # PRESSURE BOOST
            # =========================

            if heatmap["pressure"] == (
                "bullish_pressure"
            ):

                probability += 15

            if heatmap["pressure"] == (
                "bearish_pressure"
            ):

                probability += 15

            # =========================
            # SPOOFING PENALTY
            # =========================

            if heatmap["spoofing"]:

                probability -= 30

            return max(
                min(probability, 100),
                0
            )

        except Exception as e:

            traceback.print_exc()

            return 0

    # =========================
    # REVERSAL PROBABILITY
    # =========================

    def reversal_probability(self):

        try:

            trend = (
                self.trend_analysis()
            )

            probability = 20

            # =========================
            # RSI EXTREMES
            # =========================

            if trend["rsi"] >= 75:

                probability += 40

            if trend["rsi"] <= 25:

                probability += 40

            # =========================
            # MARKET PRESSURE
            # =========================

            pressure = (
                self.heatmap
                .market_pressure_analysis()
            )

            if (

                trend["trend"] == "bullish"

                and

                pressure == (
                    "bearish_pressure"
                )

            ):

                probability += 20

            if (

                trend["trend"] == "bearish"

                and

                pressure == (
                    "bullish_pressure"
                )

            ):

                probability += 20

            return max(
                min(probability, 100),
                0
            )

        except Exception as e:

            traceback.print_exc()

            return 0

    # =========================
    # CONTINUATION PROBABILITY
    # =========================

    def continuation_probability(self):

        try:

            trend = (
                self.trend_analysis()
            )

            multi_tf = (
                self.multi_tf
                .global_analysis()
            )

            probability = 40

            # =========================
            # TREND STRENGTH
            # =========================

            probability += (
                trend["strength"] * 0.3
            )

            # =========================
            # MULTI TF BOOST
            # =========================

            if multi_tf["confidence"] >= 90:

                probability += 20

            return max(
                min(
                    round(probability, 2),
                    100
                ),
                0
            )

        except Exception as e:

            traceback.print_exc()

            return 0

    # =========================
    # FINAL AI PREDICTION
    # =========================

    def final_prediction(self):

        try:

            trend = (
                self.trend_analysis()
            )

            breakout = (
                self.breakout_probability()
            )

            reversal = (
                self.reversal_probability()
            )

            continuation = (
                self.continuation_probability()
            )

            prediction = "wait"

            confidence = 50

            # =========================
            # BUY PREDICTION
            # =========================

            if (

                trend["trend"] == "bullish"

                and

                breakout >= 70

                and

                continuation >= 70

            ):

                prediction = "predict_buy"

                confidence = 90

            # =========================
            # SELL PREDICTION
            # =========================

            elif (

                trend["trend"] == "bearish"

                and

                breakout >= 70

                and

                continuation >= 70

            ):

                prediction = "predict_sell"

                confidence = 90

            # =========================
            # REVERSAL WARNING
            # =========================

            if reversal >= 80:

                prediction = (
                    "possible_reversal"
                )

                confidence = reversal

            return {

                "time":
                str(datetime.now()),

                "trend":
                trend,

                "breakout_probability":
                breakout,

                "reversal_probability":
                reversal,

                "continuation_probability":
                continuation,

                "prediction":
                prediction,

                "confidence":
                confidence

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "prediction":
                "error"

            }


if __name__ == "__main__":

    engine = (
        AIPredictionEngine()
    )

    print(
        engine.final_prediction()
    )