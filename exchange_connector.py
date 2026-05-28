import ccxt
import os


class ExchangeConnector:

    def __init__(self):

        self.exchange = ccxt.delta({

            "apiKey": os.getenv(
                "DELTA_API_KEY"
            ),

            "secret": os.getenv(
                "DELTA_API_SECRET"
            )

        })

    # =========================
    # BALANCE
    # =========================

    def fetch_balance(self):

        return self.exchange.fetch_balance()

    # =========================
    # PLACE ORDER
    # =========================

    def place_market_order(
        self,
        symbol,
        side,
        amount
    ):

        return self.exchange.create_market_order(
            symbol,
            side,
            amount
        )

    # =========================
    # OPEN POSITIONS
    # =========================

    def fetch_positions(self):

        return self.exchange.fetch_positions()