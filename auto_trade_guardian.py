import time
import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)

from live_order_executor import (
    LiveOrderExecutor
)

from database_manager import (
    DatabaseManager
)


class AutoTradeGuardian:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.executor = (
            LiveOrderExecutor()
        )

        self.database = (
            DatabaseManager()
        )

        # =========================
        # TRADE STATE
        # =========================

        self.active_trade = None

        self.trade_start_time = None

        # =========================
        # RISK SETTINGS
        # =========================

        self.trailing_stop_percent = 0.5

        self.emergency_stop_percent = 2.0

        self.take_profit_percent = 3.0

        self.max_trade_duration = 900

        self.cooldown_time = 60

        self.last_exit_time = 0

        # =========================
        # PERFORMANCE MEMORY
        # =========================

        self.total_trades = 0

        self.total_profit = 0

        self.total_loss = 0

    # =========================
    # OPEN TRADE
    # =========================

    def open_trade(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            ticker = (
                self.market.fetch_ticker(
                    symbol
                )
            )

            entry_price = (
                ticker["last"]
            )

            # =========================
            # EXECUTE BUY
            # =========================

            if side == "buy":

                result = (
                    self.executor.execute_buy(
                        symbol=symbol,
                        amount=quantity
                    )
                )

            else:

                result = (
                    self.executor.execute_sell(
                        symbol=symbol,
                        amount=quantity
                    )
                )

            self.active_trade = {

                "symbol": symbol,

                "side": side,

                "entry_price": entry_price,

                "quantity": quantity,

                "highest_pnl": 0

            }

            self.trade_start_time = (
                time.time()
            )

            print(
                f"Trade Opened: {side}"
            )

            return result

        except Exception as e:

            traceback.print_exc()

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # CLOSE TRADE
    # =========================

    def close_trade(
        self,
        reason
    ):

        try:

            if not self.active_trade:

                return

            symbol = (
                self.active_trade["symbol"]
            )

            side = (
                self.active_trade["side"]
            )

            quantity = (
                self.active_trade["quantity"]
            )

            result = (
                self.executor.close_position(
                    symbol=symbol,
                    amount=quantity,
                    side=side
                )
            )

            print(
                f"Trade Closed: {reason}"
            )

            self.active_trade = None

            self.last_exit_time = (
                time.time()
            )

            return result

        except Exception as e:

            traceback.print_exc()

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # LIVE TRADE TRACKER
    # =========================

    def live_trade_tracker(self):

        try:

            if not self.active_trade:

                return

            symbol = (
                self.active_trade["symbol"]
            )

            ticker = (
                self.market.fetch_ticker(
                    symbol
                )
            )

            current_price = (
                ticker["last"]
            )

            entry_price = (
                self.active_trade[
                    "entry_price"
                ]
            )

            side = (
                self.active_trade["side"]
            )

            # =========================
            # PNL CALCULATION
            # =========================

            if side == "buy":

                pnl = (
                    (
                        current_price
                        - entry_price
                    )
                    / entry_price
                ) * 100

            else:

                pnl = (
                    (
                        entry_price
                        - current_price
                    )
                    / entry_price
                ) * 100

            pnl = round(
                pnl,
                2
            )

            print(
                f"[{datetime.now()}] "
                f"PNL: {pnl}%"
            )

            # =========================
            # HIGHEST PNL MEMORY
            # =========================

            if pnl > self.active_trade[
                "highest_pnl"
            ]:

                self.active_trade[
                    "highest_pnl"
                ] = pnl

            highest_pnl = (
                self.active_trade[
                    "highest_pnl"
                ]
            )

            # =========================
            # TAKE PROFIT
            # =========================

            if pnl >= (
                self.take_profit_percent
            ):

                self.close_trade(
                    "Take Profit"
                )

                return

            # =========================
            # TRAILING STOP
            # =========================

            if highest_pnl >= 1:

                drawdown = (
                    highest_pnl - pnl
                )

                if drawdown >= (
                    self.trailing_stop_percent
                ):

                    self.close_trade(
                        "Trailing Stop"
                    )

                    return

            # =========================
            # EMERGENCY EXIT
            # =========================

            if pnl <= (
                -self.emergency_stop_percent
            ):

                self.close_trade(
                    "Emergency Exit"
                )

                return

            # =========================
            # TIME EXIT
            # =========================

            duration = (
                time.time()
                - self.trade_start_time
            )

            if duration >= (
                self.max_trade_duration
            ):

                self.close_trade(
                    "Time Exit"
                )

                return

        except Exception as e:

            traceback.print_exc()

            print(
                "Tracker Error:",
                str(e)
            )

    # =========================
    # COOLDOWN CHECK
    # =========================

    def cooldown_check(self):

        current = time.time()

        if (
            current
            - self.last_exit_time
        ) < self.cooldown_time:

            return False

        return True

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "active_trade":
            self.active_trade,

            "total_trades":
            self.total_trades,

            "total_profit":
            self.total_profit,

            "total_loss":
            self.total_loss

        }

    # =========================
    # LIVE LOOP
    # =========================

    def start_guardian_loop(self):

        while True:

            try:

                self.live_trade_tracker()

                time.sleep(5)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Guardian Loop Error:",
                    str(e)
                )


if __name__ == "__main__":

    guardian = (
        AutoTradeGuardian()
    )

    guardian.start_guardian_loop()