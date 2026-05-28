import time


class TradeMonitor:

    def __init__(self):

        self.active_trades = {}

    # =========================
    # REGISTER TRADE
    # =========================

    def register_trade(
        self,
        symbol,
        side,
        size,
        leverage,
        signal_score
    ):

        self.active_trades[
            symbol
        ] = {
            "side": side,
            "size": size,
            "leverage": leverage,
            "signal_score": signal_score,
            "entry_time": time.time(),
            "status": "active"
        }

        return True

    # =========================
    # GET ACTIVE TRADE
    # =========================

    def get_trade(
        self,
        symbol
    ):

        return self.active_trades.get(
            symbol
        )

    # =========================
    # REMOVE TRADE
    # =========================

    def remove_trade(
        self,
        symbol
    ):

        if symbol in self.active_trades:

            del self.active_trades[
                symbol
            ]

            return True

        return False

    # =========================
    # TRADE EXISTS
    # =========================

    def trade_exists(
        self,
        symbol
    ):

        return (
            symbol
            in self.active_trades
        )

    # =========================
    # TOTAL ACTIVE TRADES
    # =========================

    def total_active_trades(self):

        return len(
            self.active_trades
        )

    # =========================
    # TRADE DURATION
    # =========================

    def trade_duration(
        self,
        symbol
    ):

        trade = self.get_trade(
            symbol
        )

        if not trade:
            return 0

        return round(
            time.time()
            - trade["entry_time"],
            2
        )

    # =========================
    # STALE TRADE CHECK
    # =========================

    def stale_trade_check(
        self,
        symbol,
        max_duration=3600
    ):

        duration = self.trade_duration(
            symbol
        )

        return duration > max_duration

    # =========================
    # UPDATE TRADE STATUS
    # =========================

    def update_trade_status(
        self,
        symbol,
        status
    ):

        if symbol not in self.active_trades:
            return False

        self.active_trades[
            symbol
        ]["status"] = status

        return True

    # =========================
    # PNL TRACKING
    # =========================

    def update_trade_pnl(
        self,
        symbol,
        pnl
    ):

        if symbol not in self.active_trades:
            return False

        self.active_trades[
            symbol
        ]["pnl"] = pnl

        return True

    # =========================
    # TRADE HEALTH
    # =========================

    def trade_health(
        self,
        symbol
    ):

        trade = self.get_trade(
            symbol
        )

        if not trade:

            return {
                "healthy": False,
                "reason": "Trade missing"
            }

        pnl = trade.get(
            "pnl",
            0
        )

        if pnl < -10:

            return {
                "healthy": False,
                "reason": "Heavy drawdown"
            }

        return {
            "healthy": True,
            "reason": "Trade stable"
        }

    # =========================
    # ACTIVE TRADE SNAPSHOT
    # =========================

    def active_trade_snapshot(self):

        return {
            "total_trades": (
                self.total_active_trades()
            ),
            "trades": self.active_trades
        }