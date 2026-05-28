import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class SmartLiquidityHunter:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

        self.liquidity_zones = []

        self.buy_walls = []

        self.sell_walls = []

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
    # DETECT LIQUIDITY WALLS
    # =========================

    def detect_liquidity_walls(self):

        try:

            orderbook = (
                self.fetch_orderbook()
            )

            bids = (
                orderbook["bids"][:20]
            )

            asks = (
                orderbook["asks"][:20]
            )

            self.buy_walls = []

            self.sell_walls = []

            # =========================
            # BUY WALLS
            # =========================

            for bid in bids:

                price = bid[0]

                volume = bid[1]

                if volume >= 5:

                    self.buy_walls.append({

                        "price": price,

                        "volume": volume

                    })

            # =========================
            # SELL WALLS
            # =========================

            for ask in asks:

                price = ask[0]

                volume = ask[1]

                if volume >= 5:

                    self.sell_walls.append({

                        "price": price,

                        "volume": volume

                    })

            return {

                "time":
                str(datetime.now()),

                "buy_walls":
                self.buy_walls,

                "sell_walls":
                self.sell_walls

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # LIQUIDITY SIGNAL
    # =========================

    def liquidity_signal(self):

        report = (
            self.detect_liquidity_walls()
        )

        if not report:

            return "neutral"

        total_buy = 0

        total_sell = 0

        for wall in self.buy_walls:

            total_buy += (
                wall["volume"]
            )

        for wall in self.sell_walls:

            total_sell += (
                wall["volume"]
            )

        if total_buy > total_sell:

            return "bullish_liquidity"

        if total_sell > total_buy:

            return "bearish_liquidity"

        return "neutral"