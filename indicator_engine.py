import random


class IndicatorEngine:

    # =========================
    # EMA SIGNAL
    # =========================

    def ema_signal(
        self,
        ema_fast,
        ema_slow
    ):

        if ema_fast > ema_slow:
            return "bullish"

        if ema_fast < ema_slow:
            return "bearish"

        return "neutral"

    # =========================
    # RSI SIGNAL
    # =========================

    def rsi_signal(
        self,
        rsi
    ):

        if rsi > 70:
            return "overbought"

        if rsi < 30:
            return "oversold"

        return "neutral"

    # =========================
    # MACD SIGNAL
    # =========================

    def macd_signal(
        self,
        macd,
        signal
    ):

        if macd > signal:
            return "bullish"

        if macd < signal:
            return "bearish"

        return "neutral"

    # =========================
    # ADX STRENGTH
    # =========================

    def adx_strength(
        self,
        adx
    ):

        if adx >= 25:
            return "strong"

        return "weak"

    # =========================
    # ATR VOLATILITY
    # =========================

    def atr_volatility(
        self,
        atr
    ):

        if atr > 3:
            return "high"

        if atr < 1:
            return "low"

        return "medium"

    # =========================
    # SUPERTREND
    # =========================

    def supertrend_signal(
        self,
        trend
    ):

        if trend:
            return "bullish"

        return "bearish"

    # =========================
    # BOLLINGER SIGNAL
    # =========================

    def bollinger_signal(
        self,
        price,
        upper,
        lower
    ):

        if price >= upper:
            return "overbought"

        if price <= lower:
            return "oversold"

        return "neutral"

    # =========================
    # MOMENTUM SIGNAL
    # =========================

    def momentum_signal(
        self,
        momentum
    ):

        if momentum > 0:
            return "bullish"

        if momentum < 0:
            return "bearish"

        return "neutral"

    # =========================
    # TREND CONFIRMATION
    # =========================

    def trend_confirmation(
        self,
        ema_signal,
        macd_signal,
        supertrend_signal
    ):

        bullish_count = 0

        bearish_count = 0

        signals = [
            ema_signal,
            macd_signal,
            supertrend_signal
        ]

        for signal in signals:

            if signal == "bullish":
                bullish_count += 1

            if signal == "bearish":
                bearish_count += 1

        if bullish_count >= 2:
            return "bullish"

        if bearish_count >= 2:
            return "bearish"

        return "neutral"

    # =========================
    # FAKE BREAKOUT FILTER
    # =========================

    def fake_breakout_filter(
        self,
        candle_body,
        wick_size
    ):

        return candle_body > wick_size

    # =========================
    # VOLUME CONFIRMATION
    # =========================

    def volume_confirmation(
        self,
        current_volume,
        average_volume
    ):

        return current_volume > average_volume

    # =========================
    # GENERATE SIGNALS
    # =========================

    def generate_indicator_signals(
        self,
        symbol
    ):

        # Temporary demo values
        ema_fast = random.randint(100, 120)

        ema_slow = random.randint(90, 110)

        rsi = random.randint(30, 70)

        macd = random.uniform(1, 5)

        signal = random.uniform(1, 5)

        adx = random.randint(15, 40)

        atr = random.uniform(0.5, 5)

        supertrend = random.choice(
            [True, False]
        )

        ema_result = self.ema_signal(
            ema_fast,
            ema_slow
        )

        rsi_result = self.rsi_signal(
            rsi
        )

        macd_result = self.macd_signal(
            macd,
            signal
        )

        adx_result = self.adx_strength(
            adx
        )

        atr_result = self.atr_volatility(
            atr
        )

        supertrend_result = (
            self.supertrend_signal(
                supertrend
            )
        )

        trend = self.trend_confirmation(
            ema_result,
            macd_result,
            supertrend_result
        )

        return {
            "symbol": symbol,
            "ema_signal": ema_result,
            "rsi_signal": rsi_result,
            "macd_signal": macd_result,
            "adx_strength": adx_result,
            "atr_volatility": atr_result,
            "supertrend_signal": (
                supertrend_result
            ),
            "trend": trend
        }
import pandas as pd
import ta


class IndicatorEngine:

    def __init__(self):

        pass

    # =========================
    # EMA
    # =========================

    def ema(
        self,
        close_prices,
        period=20
    ):

        series = pd.Series(
            close_prices
        )

        ema_value = ta.trend.ema_indicator(
            series,
            window=period
        )

        return float(
            ema_value.iloc[-1]
        )

    # =========================
    # RSI
    # =========================

    def rsi(
        self,
        close_prices,
        period=14
    ):

        series = pd.Series(
            close_prices
        )

        rsi_value = ta.momentum.rsi(
            series,
            window=period
        )

        return float(
            rsi_value.iloc[-1]
        )

    # =========================
    # MACD
    # =========================

    def macd(
        self,
        close_prices
    ):

        series = pd.Series(
            close_prices
        )

        macd = ta.trend.macd(
            series
        )

        signal = ta.trend.macd_signal(
            series
        )

        return {
            "macd": float(
                macd.iloc[-1]
            ),
            "signal": float(
                signal.iloc[-1]
            )
        }