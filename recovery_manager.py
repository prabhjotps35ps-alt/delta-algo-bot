import time

from config import (
    ENABLE_AUTO_RECOVERY,
    ENABLE_AUTO_RECONNECT,
    ENABLE_COOLDOWN_MODE,
    HEARTBEAT_INTERVAL
)


class RecoveryManager:

    def __init__(self):

        self.cooldown_mode = False

        self.recovery_attempts = 0

    # =========================
    # SHOULD PAUSE TRADING
    # =========================

    def should_pause_trading(
        self,
        internet_ok,
        delta_ok
    ):

        if not internet_ok:
            return True

        if not delta_ok:
            return True

        return False

    # =========================
    # RECOVERY MESSAGE
    # =========================

    def recovery_message(
        self,
        internet_ok,
        delta_ok
    ):

        if not internet_ok:
            return (
                "Internet disconnected"
            )

        if not delta_ok:
            return (
                "Delta API unavailable"
            )

        return "System healthy"

    # =========================
    # ENABLE COOLDOWN
    # =========================

    def activate_cooldown(self):

        if ENABLE_COOLDOWN_MODE:

            self.cooldown_mode = True

            return True

        return False

    # =========================
    # DISABLE COOLDOWN
    # =========================

    def deactivate_cooldown(self):

        self.cooldown_mode = False

        return True

    # =========================
    # CHECK COOLDOWN
    # =========================

    def is_cooldown_active(self):

        return self.cooldown_mode

    # =========================
    # AUTO RECOVERY
    # =========================

    def auto_recovery(self):

        if not ENABLE_AUTO_RECOVERY:
            return False

        self.recovery_attempts += 1

        time.sleep(
            HEARTBEAT_INTERVAL
        )

        return True

    # =========================
    # AUTO RECONNECT
    # =========================

    def auto_reconnect(
        self,
        connectivity_monitor
    ):

        if not ENABLE_AUTO_RECONNECT:
            return False

        return (
            connectivity_monitor
            .auto_reconnect()
        )

    # =========================
    # RESET RECOVERY STATE
    # =========================

    def reset_recovery_state(self):

        self.cooldown_mode = False

        self.recovery_attempts = 0

        return True

    # =========================
    # RECOVERY STATUS
    # =========================

    def recovery_status(self):

        return {
            "cooldown_mode": (
                self.cooldown_mode
            ),
            "recovery_attempts": (
                self.recovery_attempts
            )
        }

    # =========================
    # SYSTEM STABILIZATION
    # =========================

    def stabilize_system(self):

        time.sleep(2)

        return {
            "status": "stabilized"
        }

    # =========================
    # EMERGENCY RECOVERY
    # =========================

    def emergency_recovery(self):

        self.activate_cooldown()

        self.auto_recovery()

        return {
            "status": "emergency_recovery_triggered"
        }

    # =========================
    # API FAILURE HANDLER
    # =========================

    def handle_api_failure(self):

        self.activate_cooldown()

        return {
            "status": "api_failure_handled"
        }

    # =========================
    # INTERNET FAILURE HANDLER
    # =========================

    def handle_internet_failure(self):

        self.activate_cooldown()

        return {
            "status": "internet_failure_handled"
        }

    # =========================
    # SAFE MODE ACTIVATION
    # =========================

    def activate_safe_mode(self):

        self.cooldown_mode = True

        return {
            "status": "safe_mode_activated"
        }

    # =========================
    # SYSTEM HEALTH EVALUATION
    # =========================

    def evaluate_system_health(
        self,
        internet_ok,
        delta_ok
    ):

        if internet_ok and delta_ok:

            self.deactivate_cooldown()

            return {
                "healthy": True,
                "mode": "normal"
            }

        self.activate_cooldown()

        return {
            "healthy": False,
            "mode": "recovery"
        }