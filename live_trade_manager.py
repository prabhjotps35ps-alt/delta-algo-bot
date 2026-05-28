import time
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)

from indicator_engine import (
    IndicatorEngine
)

from live_order_executor import (
    LiveOrderExecutor
)


class LiveTradeManager:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.indicators = (
            IndicatorEngine()
        )

        self.executor = (
            LiveOrderExecutor()
        )

        self.symbol = "BTC/USDT"

    # =========================
    # MARKET ANALYSIS
    # =========================

    def analyze_market(self):

        candles = (
            self.market.fetch_ohlcv(
                symbol=self.symbol,
                timeframe="1m",
                limit=100
            )
        )

        closes = []

        for candle in candles:

            closes.append(
                candle[4]
            )

        ema_20 = (
            self.indicators.ema(
                closes,
                20
            )
        )

        ema_50 = (
            self.indicators.ema(
                closes,
                50
            )
        )

        rsi = (
            self.indicators.rsi(
                closes
            )
        )

        macd = (
            self.indicators.macd(
                closes
            )
        )

        return {

            "ema_20": ema_20,

            "ema_50": ema_50,

            "rsi": rsi,

            "macd": macd

        }

    # =========================
    # SIGNAL ENGINE
    # =========================

    def signal_engine(
        self,
        analysis
    ):

        if (

            analysis["ema_20"]
            > analysis["ema_50"]

            and

            analysis["rsi"] < 70

            and

            analysis["macd"]["macd"]
            >
            analysis["macd"]["signal"]

        ):

            return "buy"

        if (

            analysis["ema_20"]
            < analysis["ema_50"]

            and

            analysis["rsi"] > 30

        ):

            return "sell"

        return "wait"

    # =========================
    # LIVE EXECUTION
    # =========================

    def live_execution_cycle(self):

        try:

            analysis = (
                self.analyze_market()
            )

            signal = (
                self.signal_engine(
                    analysis
                )
            )

            print(
                f"[{datetime.now()}] "
                f"Signal: {signal}"
            )

            if signal == "buy":

                result = (
                    self.executor.execute_buy(
                        symbol=self.symbol,
                        amount=0.001
                    )
                )

                print(result)

            elif signal == "sell":

                result = (
                    self.executor.execute_sell(
                        symbol=self.symbol,
                        amount=0.001
                    )
                )

                print(result)

        except Exception as e:

            print(
                "Execution Error:",
                str(e)
            )

    # =========================
    # LIVE LOOP
    # =========================

    def start_live_trading(self):

        while True:

            self.live_execution_cycle()

            time.sleep(60)


if __name__ == "__main__":

    manager = (
        LiveTradeManager()
    )

    manager.start_live_trading()