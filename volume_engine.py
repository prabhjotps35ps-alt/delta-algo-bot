import random


class VolumeEngine:

    # =========================
    # VOLUME STRENGTH
    # =========================

    def volume_strength(
        self,
        symbol
    ):

        volume = random.randint(
            1000,
            100000
        )

        if volume > 70000:
            return "strong"

        if volume > 30000:
            return "medium"

        return "weak"

    # =========================
    # VOLUME SPIKE
    # =========================

    def volume_spike_detection(
        self,
        current_volume,
        average_volume
    ):

        return (
            current_volume
            > average_volume * 2
        )

    # =========================
    # BUYING PRESSURE
    # =========================

    def buying_pressure(
        self,
        buy_volume,
        sell_volume
    ):

        if buy_volume > sell_volume:
            return "bullish"

        if sell_volume > buy_volume:
            return "bearish"

        return "neutral"

    # =========================
    # VOLUME TREND
    # =========================

    def volume_trend(
        self,
        current_volume,
        previous_volume
    ):

        if current_volume > previous_volume:
            return "increasing"

        if current_volume < previous_volume:
            return "decreasing"

        return "flat"

    # =========================
    # VOLUME CONFIRMATION
    # =========================

    def volume_confirmation(
        self,
        trend,
        volume_strength
    ):

        if (
            trend == "bullish"
            and volume_strength == "strong"
        ):

            return True

        if (
            trend == "bearish"
            and volume_strength == "strong"
        ):

            return True

        return False

    # =========================
    # VOLUME EXHAUSTION
    # =========================

    def volume_exhaustion(
        self,
        current_volume,
        average_volume
    ):

        return (
            current_volume
            < average_volume * 0.5
        )

    # =========================
    # WHALE ACTIVITY
    # =========================

    def whale_activity_detection(
        self,
        current_volume,
        average_volume
    ):

        return (
            current_volume
            > average_volume * 5
        )

    # =========================
    # SMART MONEY FLOW
    # =========================

    def smart_money_flow(
        self,
        buy_volume,
        sell_volume
    ):

        ratio = (
            buy_volume
            / max(sell_volume, 1)
        )

        if ratio > 1.5:
            return "strong_buying"

        if ratio < 0.7:
            return "strong_selling"

        return "balanced"

    # =========================
    # LIQUIDITY FLOW
    # =========================

    def liquidity_flow(
        self,
        inflow,
        outflow
    ):

        if inflow > outflow:
            return "positive"

        if outflow > inflow:
            return "negative"

        return "neutral"

    # =========================
    # VOLUME SNAPSHOT
    # =========================

    def volume_snapshot(
        self,
        symbol
    ):

        current_volume = random.randint(
            10000,
            100000
        )

        average_volume = random.randint(
            5000,
            50000
        )

        buy_volume = random.randint(
            1000,
            50000
        )

        sell_volume = random.randint(
            1000,
            50000
        )

        strength = self.volume_strength(
            symbol
        )

        spike = self.volume_spike_detection(
            current_volume,
            average_volume
        )

        pressure = self.buying_pressure(
            buy_volume,
            sell_volume
        )

        smart_money = self.smart_money_flow(
            buy_volume,
            sell_volume
        )

        return {
            "symbol": symbol,
            "volume_strength": strength,
            "volume_spike": spike,
            "buying_pressure": pressure,
            "smart_money_flow": smart_money
        }