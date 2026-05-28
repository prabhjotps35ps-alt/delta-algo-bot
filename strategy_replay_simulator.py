import traceback
from datetime import datetime

from market_data_feed import (
    MarketDataFeed
)

from ai_prediction_engine import (
    AIPredictionEngine
)


class StrategyReplaySimulator:

    def __init__(self):

        self.market = (
            MarketDataFeed()
        )

        self.ai = (
            AIPredictionEngine()
        )

        self.symbol = "BTC/USDT"

        self.balance = 1000

        self.initial_balance = 1000

        self.position = None

        self.trade_history = []

        self.win_count = 0

        self.loss_count = 0

    # =========================
    # LOAD HISTORICAL DATA
    # =========================

    def load_historical_data(self):

        return (
            self.market.fetch_ohlcv(

                self.symbol,

                timeframe="5m",

                limit=200

            )
        )

    # =========================
    # OPEN POSITION
    # =========================

    def open_position(
        self,
        side,
        entry_price
    ):

        self.position = {

            "side": side,

            "entry_price": entry_price,

            "time":
            str(datetime.now())

        }

    # =========================
    # CLOSE POSITION
    # =========================

    def close_position(
        self,
        exit_price
    ):

        if not self.position:

            return

        side = (
            self.position["side"]
        )

        entry = (
            self.position["entry_price"]
        )

        # =========================
        # PNL
        # =========================

        if side == "buy":

            pnl = (

                (
                    exit_price
                    - entry
                )

                / entry

            ) * 100

        else:

            pnl = (

                (
                    entry
                    - exit_price
                )

                / entry

            ) * 100

        pnl = round(
            pnl,
            2
        )

        self.balance += (
            self.balance
            * pnl
            / 100
        )

        trade = {

            "side": side,

            "entry": entry,

            "exit": exit_price,

            "pnl": pnl

        }

        self.trade_history.append(
            trade
        )

        if pnl > 0:

            self.win_count += 1

        else:

            self.loss_count += 1

        self.position = None

    # =========================
    # AI DECISION
    # =========================

    def ai_decision(self):

        prediction = (
            self.ai.final_prediction()
        )

        return prediction["prediction"]

    # =========================
    # RUN SIMULATION
    # =========================

    def run_simulation(self):

        try:

            candles = (
                self.load_historical_data()
            )

            for candle in candles:

                current_price = (
                    candle[4]
                )

                signal = (
                    self.ai_decision()
                )

                # =========================
                # BUY
                # =========================

                if (

                    signal == "predict_buy"

                    and

                    not self.position

                ):

                    self.open_position(

                        "buy",

                        current_price

                    )

                # =========================
                # SELL
                # =========================

                elif (

                    signal == "predict_sell"

                    and

                    not self.position

                ):

                    self.open_position(

                        "sell",

                        current_price

                    )

                # =========================
                # CLOSE POSITION
                # =========================

                elif self.position:

                    self.close_position(
                        current_price
                    )

            return self.performance_report()

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "simulation_failed",

                "error":
                str(e)

            }

    # =========================
    # PERFORMANCE REPORT
    # =========================

    def performance_report(self):

        total_trades = len(
            self.trade_history
        )

        winrate = 0

        if total_trades > 0:

            winrate = round(

                (
                    self.win_count
                    / total_trades
                ) * 100,

                2

            )

        return {

            "initial_balance":
            self.initial_balance,

            "final_balance":
            round(self.balance, 2),

            "profit":
            round(

                self.balance
                - self.initial_balance,

                2

            ),

            "total_trades":
            total_trades,

            "wins":
            self.win_count,

            "losses":
            self.loss_count,

            "winrate":
            winrate,

            "trade_history":
            self.trade_history

        }


if __name__ == "__main__":

    simulator = (
        StrategyReplaySimulator()
    )

    print(
        simulator.run_simulation()
    )