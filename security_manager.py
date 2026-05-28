import os
import hashlib


class SecurityManager:

    def __init__(self):

        self.allowed_ips = [
            "127.0.0.1"
        ]

    # =========================
    # HASH SECRET
    # =========================

    def hash_secret(
        self,
        secret
    ):

        return hashlib.sha256(
            secret.encode()
        ).hexdigest()

    # =========================
    # VERIFY IP
    # =========================

    def verify_ip(
        self,
        ip
    ):

        return (
            ip in self.allowed_ips
        )

    # =========================
    # ENV CHECK
    # =========================

    def env_check(self):

        required = [

            "DELTA_API_KEY",

            "DELTA_API_SECRET"

        ]

        missing = []

        for key in required:

            if not os.getenv(key):

                missing.append(key)

        return {
            "missing": missing
        }