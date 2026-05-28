import time


class LatencyManager:

    def latency(
        self,
        start_time
    ):

        return round(
            (
                time.time()
                - start_time
            ) * 1000,
            2
        )

    def acceptable(
        self,
        latency_ms
    ):

        return latency_ms < 500