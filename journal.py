import json
import os
from datetime import datetime


class Journal:

    def __init__(self):

        self.file_path = (
            "trade_journal.json"
        )

        if not os.path.exists(
            self.file_path
        ):

            with open(
                self.file_path,
                "w"
            ) as file:

                json.dump([], file)

    # =========================
    # LOAD JOURNAL
    # =========================

    def load_journal(self):

        try:

            with open(
                self.file_path,
                "r"
            ) as file:

                return json.load(file)

        except Exception:
            return []

    # =========================
    # SAVE JOURNAL
    # =========================

    def save_journal(
        self,
        data
    ):

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # =========================
    # ADD TRADE ENTRY
    # =========================

    def add_trade(
        self,
        symbol,
        side,
        entry_price,
        exit_price,
        pnl,
        signal_score
    ):

        journal = self.load_journal()

        trade_entry = {
            "timestamp": str(
                datetime.now()
            ),
            "symbol": symbol,
            "side": side,
            "entry_price": entry_price,
            "exit_price": exit_price,
            "pnl": pnl,
            "signal_score": signal_score
        }

        journal.append(
            trade_entry
        )

        self.save_journal(
            journal
        )

        return True

    # =========================
    # TOTAL TRADES
    # =========================

    def total_trades(self):

        journal = self.load_journal()

        return len(journal)

    # =========================
    # WIN RATE
    # =========================

    def win_rate(self):

        journal = self.load_journal()

        if not journal:
            return 0

        wins = 0

        for trade in journal:

            if trade["pnl"] > 0:
                wins += 1

        return round(
            (
                wins
                / len(journal)
            ) * 100,
            2
        )

    # =========================
    # TOTAL PNL
    # =========================

    def total_pnl(self):

        journal = self.load_journal()

        total = 0

        for trade in journal:

            total += trade["pnl"]

        return round(total, 2)

    # =========================
    # LAST TRADE
    # =========================

    def last_trade(self):

        journal = self.load_journal()

        if not journal:
            return None

        return journal[-1]

    # =========================
    # JOURNAL SNAPSHOT
    # =========================

    def snapshot(self):

        return {
            "total_trades": (
                self.total_trades()
            ),
            "win_rate": (
                self.win_rate()
            ),
            "total_pnl": (
                self.total_pnl()
            ),
            "last_trade": (
                self.last_trade()
            )
        }