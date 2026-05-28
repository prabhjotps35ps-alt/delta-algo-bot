import traceback
from datetime import datetime

from exchange_connector import (
    ExchangeConnector
)

from database_manager import (
    DatabaseManager
)


class LiveOrderExecutor:

    def __init__(self):

        self.exchange = (
            ExchangeConnector()
        )

        self.database = (
            DatabaseManager()
        )

    # =========================
    # EXECUTE BUY
    # =========================

    def execute_buy(
        self,
        symbol,
        amount
    ):

        try:

            order = (
                self.exchange
                .place_market_order(
                    symbol=symbol,
                    side="buy",
                    amount=amount
                )
            )

            self.database.save_trade(
                symbol=symbol,
                side="buy",
                entry=(
                    order.get("price", 0)
                ),
                quantity=amount,
                status="executed"
            )

            return {
                "success": True,
                "order": order
            }

        except Exception as e:

            traceback.print_exc()

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # EXECUTE SELL
    # =========================

    def execute_sell(
        self,
        symbol,
        amount
    ):

        try:

            order = (
                self.exchange
                .place_market_order(
                    symbol=symbol,
                    side="sell",
                    amount=amount
                )
            )

            self.database.save_trade(
                symbol=symbol,
                side="sell",
                entry=(
                    order.get("price", 0)
                ),
                quantity=amount,
                status="executed"
            )

            return {
                "success": True,
                "order": order
            }

        except Exception as e:

            traceback.print_exc()

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # CLOSE POSITION
    # =========================

    def close_position(
        self,
        symbol,
        amount,
        side
    ):

        try:

            close_side = "sell"

            if side == "sell":

                close_side = "buy"

            order = (
                self.exchange
                .place_market_order(
                    symbol=symbol,
                    side=close_side,
                    amount=amount
                )
            )

            return {
                "success": True,
                "closed_order": order
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }