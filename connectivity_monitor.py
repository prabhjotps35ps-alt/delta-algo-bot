import requests
import time

from config import (
    REQUEST_TIMEOUT,
    HEARTBEAT_INTERVAL
)


class ConnectivityMonitor:

    # =========================
    # INTERNET CHECK
    # =========================

    def internet_check(self):

        try:

            requests.get(
                "https://www.google.com",
                timeout=5
            )

            return True

        except Exception:
            return False

    # =========================
    # DELTA API CHECK
    # =========================

    def delta_api_check(
        self,
        delta_client
    ):

        try:

            response = (
                delta_client.get_balance()
            )

            if not response:
                return False

            if response.get("success") is False:
                return False

            return True

        except Exception:
            return False

    # =========================
    # HEARTBEAT STATUS
    # =========================

    def heartbeat_status(
        self,
        internet_ok,
        delta_ok
    ):

        if internet_ok and delta_ok:
            return "healthy"

        if internet_ok and not delta_ok:
            return "delta_api_down"

        if not internet_ok:
            return "internet_down"

        return "system_error"

    # =========================
    # LATENCY CHECK
    # =========================

    def latency_check(self):

        try:

            start = time.time()

            requests.get(
                "https://www.google.com",
                timeout=REQUEST_TIMEOUT
            )

            end = time.time()

            latency = (
                end - start
            ) * 1000

            return round(
                latency,
                2
            )

        except Exception:
            return -1

    # =========================
    # CONNECTION QUALITY
    # =========================

    def connection_quality(
        self,
        latency
    ):

        if latency < 0:
            return "offline"

        if latency < 100:
            return "excellent"

        if latency < 300:
            return "good"

        if latency < 600:
            return "average"

        return "poor"

    # =========================
    # API RESPONSE VALIDATION
    # =========================

    def validate_api_response(
        self,
        response
    ):

        try:

            if not response:
                return False

            if isinstance(
                response,
                dict
            ):

                if response.get(
                    "error"
                ):
                    return False

            return True

        except Exception:
            return False

    # =========================
    # SYSTEM HEALTH SNAPSHOT
    # =========================

    def system_health_snapshot(
        self,
        delta_client
    ):

        internet_ok = (
            self.internet_check()
        )

        delta_ok = (
            self.delta_api_check(
                delta_client
            )
        )

        latency = (
            self.latency_check()
        )

        quality = (
            self.connection_quality(
                latency
            )
        )

        heartbeat = (
            self.heartbeat_status(
                internet_ok,
                delta_ok
            )
        )

        return {
            "heartbeat": heartbeat,
            "internet_ok": internet_ok,
            "delta_ok": delta_ok,
            "latency_ms": latency,
            "connection_quality": quality
        }

    # =========================
    # WAIT FOR RECOVERY
    # =========================

    def wait_for_recovery(self):

        time.sleep(
            HEARTBEAT_INTERVAL
        )

    # =========================
    # AUTO RECONNECT
    # =========================

    def auto_reconnect(
        self,
        retries=3
    ):

        for _ in range(retries):

            if self.internet_check():
                return True

            time.sleep(2)

        return False