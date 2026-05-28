from indicator_engine import IndicatorEngine
from market_tracker import MarketTracker
from volume_engine import VolumeEngine
from orderbook_engine import OrderbookEngine


class StrategyEngine:

    def __init__(self):

        self.indicator_engine = (
            IndicatorEngine()
        )

        self.market_tracker = (
            MarketTracker()
        )

        self.volume_engine = (
            VolumeEngine()
        )

        self.orderbook_engine = (
            OrderbookEngine()
        )

    # =========================
    # MARKET ANALYSIS
    # =========================

    def analyze_market(
        self,
        symbol,
        timeframe="1m"
    ):

        trend = (
            self.market_tracker
            .trend_analysis(symbol)
        )

        volatility = (
            self.market_tracker
            .volatility_analysis(symbol)
        )

        momentum = (
            self.market_tracker
            .momentum_analysis(symbol)
        )

        volume_strength = (
            self.volume_engine
            .volume_strength(symbol)
        )

        liquidity = (
            self.orderbook_engine
            .liquidity_analysis(symbol)
        )

        indicators = (
            self.indicator_engine
            .generate_indicator_signals(symbol)
        )

        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "trend": trend,
            "volatility": volatility,
            "momentum": momentum,
            "volume_strength": volume_strength,
            "liquidity": liquidity,
            "indicators": indicators
        }

    # =========================
    # ENTRY VALIDATION
    # =========================

    def validate_trade_setup(
        self,
        market_analysis
    ):

        trend = market_analysis.get(
            "trend"
        )

        volatility = market_analysis.get(
            "volatility"
        )

        volume_strength = market_analysis.get(
            "volume_strength"
        )

        if trend == "neutral":
            return False

        if volatility == "high":
            return False

        if volume_strength == "weak":
            return False

        return True

    # =========================
    # MARKET REGIME
    # =========================

    def market_regime(
        self,
        market_analysis
    ):

        trend = market_analysis.get(
            "trend"
        )

        volatility = market_analysis.get(
            "volatility"
        )

        if trend == "bullish":

            if volatility == "low":
                return "stable_uptrend"

            return "volatile_uptrend"

        if trend == "bearish":

            if volatility == "low":
                return "stable_downtrend"

            return "volatile_downtrend"

        return "sideways"

    # =========================
    # TRADE DECISION
    # =========================

    def trade_decision(
        self,
        market_analysis
    ):

        if not self.validate_trade_setup(
            market_analysis
        ):

            return "reject"

        trend = market_analysis.get(
            "trend"
        )

        if trend == "bullish":
            return "buy"

        if trend == "bearish":
            return "sell"

        return "wait"