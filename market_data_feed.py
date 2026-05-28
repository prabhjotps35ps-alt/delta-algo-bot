import ccxt


class MarketDataFeed:

    def __init__(self):

        self.exchange = ccxt.delta()

    # =========================
    # FETCH TICKER
    # =========================

    def fetch_ticker(
        self,
        symbol="BTC/USDT"
    ):

        return (
            self.exchange.fetch_ticker(
                symbol
            )
        )

    # =========================
    # FETCH OHLCV
    # =========================

    def fetch_ohlcv(
        self,
        symbol="BTC/USDT",
        timeframe="1m",
        limit=100
    ):

        return (
            self.exchange.fetch_ohlcv(
                symbol,
                timeframe,
                limit=limit
            )
        )

    # =========================
    # FETCH ORDERBOOK
    # =========================

    def fetch_orderbook(
        self,
        symbol="BTC/USDT"
    ):

        return (
            self.exchange.fetch_order_book(
                symbol
            )
        )