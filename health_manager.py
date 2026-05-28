class HealthManager:

    def system_health(
        self,
        internet_ok,
        api_ok,
        cooldown
    ):

        if not internet_ok:
            return "internet_down"

        if not api_ok:
            return "api_down"

        if cooldown:
            return "cooldown_mode"

        return "healthy"

    def healthy(
        self,
        status
    ):

        return status == "healthy"