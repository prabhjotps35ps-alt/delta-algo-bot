import time


class StandbyManager:

    def __init__(self):

        self.standby_mode = False

        self.last_trade_time = 0

        self.cooldown_seconds = 60

    # =========================
    # ENABLE STANDBY
    # =========================

    def enable_standby(self):

        self.standby_mode = True

        return {
            "status": "standby_enabled"
        }

    # =========================
    # DISABLE STANDBY
    # =========================

    def disable_standby(self):

        self.standby_mode = False

        return {
            "status": "standby_disabled"
        }

    # =========================
    # STANDBY STATUS
    # =========================

    def standby_status(self):

        return self.standby_mode

    # =========================
    # UPDATE LAST TRADE TIME
    # =========================

    def update_trade_time(self):

        self.last_trade_time = time.time()

    # =========================
    # COOLDOWN CHECK
    # =========================

    def cooldown_complete(self):

        current_time = time.time()

        elapsed = (
            current_time
            - self.last_trade_time
        )

        return elapsed >= self.cooldown_seconds

    # =========================
    # WAIT MODE
    # =========================

    def wait_mode(self):

        if not self.cooldown_complete():

            remaining = (
                self.cooldown_seconds
                - (
                    time.time()
                    - self.last_trade_time
                )
            )

            return {
                "wait": True,
                "remaining_seconds": round(
                    remaining,
                    2
                )
            }

        return {
            "wait": False
        }

    # =========================
    # MARKET STANDBY
    # =========================

    def market_standby(
        self,
        volatility,
        volume_strength
    ):

        if volatility == "high":

            self.enable_standby()

            return {
                "standby": True,
                "reason": "High volatility"
            }

        if volume_strength == "weak":

            self.enable_standby()

            return {
                "standby": True,
                "reason": "Weak volume"
            }

        self.disable_standby()

        return {
            "standby": False,
            "reason": "Market stable"
        }

    # =========================
    # SAFE ENTRY CHECK
    # =========================

    def safe_entry_allowed(
        self,
        signal_score
    ):

        if signal_score < 70:
            return False

        if self.standby_mode:
            return False

        if not self.cooldown_complete():
            return False

        return True

    # =========================
    # STANDBY SNAPSHOT
    # =========================

    def snapshot(self):

        return {
            "standby_mode": (
                self.standby_mode
            ),
            "cooldown_seconds": (
                self.cooldown_seconds
            ),
            "last_trade_time": (
                self.last_trade_time
            )
        }