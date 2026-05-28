import time
import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)

from indicator_engine import (
    IndicatorEngine
)

from adaptive_position_controller import (
    AdaptivePositionController
)

from institutional_risk_firewall import (
    InstitutionalRiskFirewall
)

from auto_trade_guardian import (
    AutoTradeGuardian
)

from live_order_executor import (
    LiveOrderExecutor
)


class NeuralTradeCommander:

    def __init__(self):

        # =========================
        # CORE SYSTEMS
        # =========================

        self.market = (
            MarketDataFeed()
        )

        self.indicators = (
            IndicatorEngine()
        )

        self.position_controller = (
            AdaptivePositionController()
        )

        self.firewall = (
            InstitutionalRiskFirewall()
        )

        self.guardian = (
            AutoTradeGuardian()
        )

        self.executor = (
            LiveOrderExecutor()
        )

        # =========================
        # SETTINGS
        # =========================

        self.symbol = "BTC/USDT"

        self.timeframe = "1m"

        self.balance = 1000

        self.leverage = 3

        self.confidence_threshold = 85

        # =========================
        # AI MEMORY
        # =========================

        self.last_signal = None

        self.trade_cooldown = False

    # =========================
    # MARKET ANALYSIS
    # =========================

    def market_analysis(self):

        candles = (
            self.market.fetch_ohlcv(

                symbol=self.symbol,

                timeframe=self.timeframe,

                limit=150

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

        return {

            "ema_fast": ema_fast,

            "ema_slow": ema_slow,

            "rsi": rsi,

            "macd": macd

        }

    # =========================
    # AI SIGNAL ENGINE
    # =========================

    def ai_signal_engine(
        self,
        analysis
    ):

        confidence = 50

        signal = "wait"

        # =========================
        # BULLISH LOGIC
        # =========================

        if (

            analysis["ema_fast"]
            >
            analysis["ema_slow"]

        ):

            confidence += 20

        if (

            analysis["rsi"] > 55

            and

            analysis["rsi"] < 70

        ):

            confidence += 15

        if (

            analysis["macd"]["macd"]
            >
            analysis["macd"]["signal"]

        ):

            confidence += 20

        # =========================
        # BUY SIGNAL
        # =========================

        if confidence >= (
            self.confidence_threshold
        ):

            signal = "buy"

        # =========================
        # SELL LOGIC
        # =========================

        bearish_score = 0

        if (

            analysis["ema_fast"]
            <
            analysis["ema_slow"]

        ):

            bearish_score += 30

        if analysis["rsi"] < 40:

            bearish_score += 20

        if (

            analysis["macd"]["macd"]
            <
            analysis["macd"]["signal"]

        ):

            bearish_score += 30

        if bearish_score >= 70:

            signal = "sell"

            confidence = bearish_score

        return {

            "signal": signal,

            "confidence": confidence

        }

    # =========================
    # EXECUTE TRADE
    # =========================

    def execute_trade(
        self,
        signal_data
    ):

        signal = (
            signal_data["signal"]
        )

        confidence = (
            signal_data["confidence"]
        )

        # =========================
        # POSITION VALIDATION
        # =========================

        validation = (
            self.firewall.validate_trade(

                leverage=self.leverage,

                position_size=1

            )
        )

        if not validation["allowed"]:

            print(
                "Firewall Blocked:",
                validation["reason"]
            )

            return

        if signal == "wait":

            print(
                "No Trade Signal"
            )

            return

        ticker = (
            self.market.fetch_ticker(
                self.symbol
            )
        )

        entry_price = (
            ticker["last"]
        )

        quantity = (
            self.position_controller
            .calculate_position_size(

                balance=self.balance,

                entry_price=entry_price,

                stoploss_percent=1,

                volatility="medium",

                confidence=confidence

            )
        )

        if quantity <= 0:

            print(
                "Invalid Quantity"
            )

            return

        # =========================
        # BUY EXECUTION
        # =========================

        if signal == "buy":

            result = (
                self.executor.execute_buy(

                    symbol=self.symbol,

                    amount=quantity

                )
            )

        else:

            result = (
                self.executor.execute_sell(

                    symbol=self.symbol,

                    amount=quantity

                )
            )

        print(
            f"Trade Executed: "
            f"{signal}"
        )

        print(result)

        self.position_controller.open_position()

        self.firewall.register_position_open()

    # =========================
    # LIVE AI LOOP
    # =========================

    def live_ai_loop(self):

        while True:

            try:

                # =========================
                # TRACK ACTIVE TRADE
                # =========================

                self.guardian.live_trade_tracker()

                # =========================
                # MARKET ANALYSIS
                # =========================

                analysis = (
                    self.market_analysis()
                )

                signal_data = (
                    self.ai_signal_engine(
                        analysis
                    )
                )

                print(

                    f"[{datetime.now()}] "

                    f"Signal: "

                    f"{signal_data['signal']} "

                    f"| Confidence: "

                    f"{signal_data['confidence']}"

                )

                # =========================
                # EXECUTE TRADE
                # =========================

                if not self.guardian.active_trade:

                    self.execute_trade(
                        signal_data
                    )

                time.sleep(30)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Commander Error:",
                    str(e)
                )


if __name__ == "__main__":

    commander = (
        NeuralTradeCommander()
    )

    commander.live_ai_loop()