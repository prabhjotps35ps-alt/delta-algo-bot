import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class OrderbookHeatmap:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

        # =========================
        # HEATMAP MEMORY
        # =========================

        self.buy_heat_zones = []

        self.sell_heat_zones = []

        self.spoofing_detected = False

        self.absorption_detected = False

    # =========================
    # FETCH ORDERBOOK
    # =========================

    def fetch_orderbook(self):

        return (
            self.market.fetch_orderbook(
                self.symbol
            )
        )

    # =========================
    # BUILD HEATMAP
    # =========================

    def build_heatmap(self):

        try:

            orderbook = (
                self.fetch_orderbook()
            )

            bids = (
                orderbook["bids"][:50]
            )

            asks = (
                orderbook["asks"][:50]
            )

            self.buy_heat_zones = []

            self.sell_heat_zones = []

            # =========================
            # BUY HEAT ZONES
            # =========================

            for bid in bids:

                price = bid[0]

                volume = bid[1]

                if volume >= 5:

                    self.buy_heat_zones.append({

                        "price": price,

                        "volume": volume

                    })

            # =========================
            # SELL HEAT ZONES
            # =========================

            for ask in asks:

                price = ask[0]

                volume = ask[1]

                if volume >= 5:

                    self.sell_heat_zones.append({

                        "price": price,

                        "volume": volume

                    })

            return {

                "time":
                str(datetime.now()),

                "buy_heat_zones":
                self.buy_heat_zones,

                "sell_heat_zones":
                self.sell_heat_zones

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # SPOOFING DETECTOR
    # =========================

    def spoofing_detector(self):

        try:

            heatmap = (
                self.build_heatmap()
            )

            if not heatmap:

                return False

            spoof_count = 0

            # =========================
            # BUY SIDE SPOOFING
            # =========================

            for zone in self.buy_heat_zones:

                if zone["volume"] >= 20:

                    spoof_count += 1

            # =========================
            # SELL SIDE SPOOFING
            # =========================

            for zone in self.sell_heat_zones:

                if zone["volume"] >= 20:

                    spoof_count += 1

            self.spoofing_detected = (
                spoof_count >= 3
            )

            return self.spoofing_detected

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # ABSORPTION DETECTOR
    # =========================

    def absorption_detector(self):

        try:

            heatmap = (
                self.build_heatmap()
            )

            if not heatmap:

                return False

            buy_total = 0

            sell_total = 0

            for zone in self.buy_heat_zones:

                buy_total += (
                    zone["volume"]
                )

            for zone in self.sell_heat_zones:

                sell_total += (
                    zone["volume"]
                )

            difference = abs(
                buy_total - sell_total
            )

            self.absorption_detected = (
                difference <= 10
            )

            return self.absorption_detected

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # MARKET PRESSURE
    # =========================

    def market_pressure_analysis(self):

        try:

            buy_total = 0

            sell_total = 0

            for zone in self.buy_heat_zones:

                buy_total += (
                    zone["volume"]
                )

            for zone in self.sell_heat_zones:

                sell_total += (
                    zone["volume"]
                )

            if buy_total > sell_total:

                return "bullish_pressure"

            if sell_total > buy_total:

                return "bearish_pressure"

            return "neutral"

        except Exception as e:

            traceback.print_exc()

            return "unknown"

    # =========================
    # AI SIGNAL FILTER
    # =========================

    def ai_signal_filter(
        self,
        signal
    ):

        spoofing = (
            self.spoofing_detector()
        )

        absorption = (
            self.absorption_detector()
        )

        pressure = (
            self.market_pressure_analysis()
        )

        # =========================
        # BLOCK SPOOFING MARKET
        # =========================

        if spoofing:

            return "wait"

        # =========================
        # ABSORPTION FILTER
        # =========================

        if absorption:

            return "wait"

        # =========================
        # PRESSURE BOOST
        # =========================

        if (

            signal == "buy"

            and

            pressure == (
                "bullish_pressure"
            )

        ):

            return "strong_buy"

        if (

            signal == "sell"

            and

            pressure == (
                "bearish_pressure"
            )

        ):

            return "strong_sell"

        return signal

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "spoofing":
            self.spoofing_detected,

            "absorption":
            self.absorption_detected,

            "pressure":
            self.market_pressure_analysis(),

            "buy_zones":
            len(self.buy_heat_zones),

            "sell_zones":
            len(self.sell_heat_zones)

        }


if __name__ == "__main__":

    heatmap = (
        OrderbookHeatmap()
    )

    print(
        heatmap.build_heatmap()
    )

    print(
        heatmap.status_report()
    )