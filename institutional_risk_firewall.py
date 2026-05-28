import time
import traceback
from datetime import datetime


class InstitutionalRiskFirewall:

    def __init__(self):

        # =========================
        # RISK LIMITS
        # =========================

        self.max_daily_loss = 5.0

        self.max_consecutive_losses = 3

        self.max_open_positions = 1

        self.max_drawdown = 10.0

        self.max_leverage = 5

        # =========================
        # TRACKERS
        # =========================

        self.daily_loss = 0

        self.consecutive_losses = 0

        self.open_positions = 0

        self.total_profit = 0

        self.total_loss = 0

        self.trade_history = []

        self.firewall_active = True

        self.pause_trading = False

        self.last_reset_day = (
            datetime.now().day
        )

    # =========================
    # RESET DAILY LIMITS
    # =========================

    def reset_daily_limits(self):

        current_day = (
            datetime.now().day
        )

        if current_day != (
            self.last_reset_day
        ):

            self.daily_loss = 0

            self.consecutive_losses = 0

            self.last_reset_day = (
                current_day
            )

            print(
                "Daily Risk Reset Completed"
            )

    # =========================
    # VALIDATE TRADE
    # =========================

    def validate_trade(
        self,
        leverage,
        position_size
    ):

        self.reset_daily_limits()

        # =========================
        # FIREWALL STATUS
        # =========================

        if not self.firewall_active:

            return {
                "allowed": False,
                "reason": "Firewall Disabled"
            }

        # =========================
        # TRADING PAUSED
        # =========================

        if self.pause_trading:

            return {
                "allowed": False,
                "reason": "Trading Paused"
            }

        # =========================
        # DAILY LOSS LIMIT
        # =========================

        if self.daily_loss >= (
            self.max_daily_loss
        ):

            self.pause_trading = True

            return {
                "allowed": False,
                "reason": "Daily Loss Limit Hit"
            }

        # =========================
        # CONSECUTIVE LOSSES
        # =========================

        if self.consecutive_losses >= (
            self.max_consecutive_losses
        ):

            self.pause_trading = True

            return {
                "allowed": False,
                "reason": (
                    "Consecutive Loss Limit"
                )
            }

        # =========================
        # OPEN POSITION LIMIT
        # =========================

        if self.open_positions >= (
            self.max_open_positions
        ):

            return {
                "allowed": False,
                "reason": (
                    "Max Open Positions"
                )
            }

        # =========================
        # LEVERAGE LIMIT
        # =========================

        if leverage > self.max_leverage:

            return {
                "allowed": False,
                "reason": (
                    "Leverage Too High"
                )
            }

        # =========================
        # POSITION SIZE CHECK
        # =========================

        if position_size <= 0:

            return {
                "allowed": False,
                "reason": (
                    "Invalid Position Size"
                )
            }

        return {
            "allowed": True,
            "reason": "Approved"
        }

    # =========================
    # REGISTER OPEN POSITION
    # =========================

    def register_position_open(self):

        self.open_positions += 1

    # =========================
    # REGISTER CLOSED POSITION
    # =========================

    def register_position_close(
        self,
        pnl_percent
    ):

        if self.open_positions > 0:

            self.open_positions -= 1

        trade = {

            "time": str(
                datetime.now()
            ),

            "pnl_percent": pnl_percent

        }

        self.trade_history.append(
            trade
        )

        # =========================
        # WIN / LOSS TRACKING
        # =========================

        if pnl_percent > 0:

            self.total_profit += (
                pnl_percent
            )

            self.consecutive_losses = 0

        else:

            self.total_loss += abs(
                pnl_percent
            )

            self.daily_loss += abs(
                pnl_percent
            )

            self.consecutive_losses += 1

    # =========================
    # EMERGENCY SHUTDOWN
    # =========================

    def emergency_shutdown(self):

        self.pause_trading = True

        self.firewall_active = False

        print(
            "EMERGENCY SHUTDOWN ACTIVATED"
        )

    # =========================
    # RESUME TRADING
    # =========================

    def resume_trading(self):

        self.pause_trading = False

        self.firewall_active = True

        print(
            "Trading Resumed"
        )

    # =========================
    # FIREWALL STATUS
    # =========================

    def firewall_status(self):

        return {

            "firewall_active":
            self.firewall_active,

            "pause_trading":
            self.pause_trading,

            "daily_loss":
            self.daily_loss,

            "consecutive_losses":
            self.consecutive_losses,

            "open_positions":
            self.open_positions,

            "total_profit":
            self.total_profit,

            "total_loss":
            self.total_loss

        }

    # =========================
    # LIVE FIREWALL LOOP
    # =========================

    def start_firewall_loop(self):

        while True:

            try:

                self.reset_daily_limits()

                print(
                    f"[{datetime.now()}] "
                    f"Firewall Active"
                )

                time.sleep(60)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Firewall Error:",
                    str(e)
                )


if __name__ == "__main__":

    firewall = (
        InstitutionalRiskFirewall()
    )

    firewall.start_firewall_loop()