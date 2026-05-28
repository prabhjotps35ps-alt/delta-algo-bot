import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)


class DeepLiquidityScanner:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.symbol = "BTC/USDT"

        self.deep_buy_liquidity = []

        self.deep_sell_liquidity = []

        self.hidden_liquidity = False

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
    # DEEP SCAN
    # =========================

    def deep_scan(self):

        try:

            orderbook = (
                self.fetch_orderbook()
            )

            bids = (
                orderbook["bids"][:100]
            )

            asks = (
                orderbook["asks"][:100]
            )

            self.deep_buy_liquidity = []

            self.deep_sell_liquidity = []

            # =========================
            # BUY LIQUIDITY
            # =========================

            for bid in bids:

                if bid[1] >= 10:

                    self.deep_buy_liquidity.append({

                        "price": bid[0],

                        "volume": bid[1]

                    })

            # =========================
            # SELL LIQUIDITY
            # =========================

            for ask in asks:

                if ask[1] >= 10:

                    self.deep_sell_liquidity.append({

                        "price": ask[0],

                        "volume": ask[1]

                    })

            return {

                "time":
                str(datetime.now()),

                "buy_liquidity":
                self.deep_buy_liquidity,

                "sell_liquidity":
                self.deep_sell_liquidity

            }

        except Exception as e:

            traceback.print_exc()

            return None

    # =========================
    # HIDDEN LIQUIDITY
    # =========================

    def hidden_liquidity_detector(self):

        try:

            scan = (
                self.deep_scan()
            )

            if not scan:

                return False

            buy_total = 0

            sell_total = 0

            for item in (
                self.deep_buy_liquidity
            ):

                buy_total += (
                    item["volume"]
                )

            for item in (
                self.deep_sell_liquidity
            ):

                sell_total += (
                    item["volume"]
                )

            difference = abs(
                buy_total - sell_total
            )

            self.hidden_liquidity = (
                difference <= 20
            )

            return self.hidden_liquidity

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # LIQUIDITY DIRECTION
    # =========================

    def liquidity_direction(self):

        buy_total = 0

        sell_total = 0

        for item in (
            self.deep_buy_liquidity
        ):

            buy_total += (
                item["volume"]
            )

        for item in (
            self.deep_sell_liquidity
        ):

            sell_total += (
                item["volume"]
            )

        if buy_total > sell_total:

            return "bullish"

        if sell_total > buy_total:

            return "bearish"

        return "neutral"