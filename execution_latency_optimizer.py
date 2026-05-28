import time
from datetime import datetime


class ExecutionLatencyOptimizer:

    def __init__(self):

        self.execution_times = []

        self.average_latency = 0

    # =========================
    # START TIMER
    # =========================

    def start_timer(self):

        return time.time()

    # =========================
    # END TIMER
    # =========================

    def end_timer(
        self,
        start
    ):

        latency = (
            time.time()
            - start
        ) * 1000

        self.execution_times.append(
            latency
        )

        self.average_latency = (

            sum(self.execution_times)

            / len(self.execution_times)

        )

        return round(
            latency,
            2
        )

    # =========================
    # LATENCY REPORT
    # =========================

    def latency_report(self):

        return {

            "time":
            str(datetime.now()),

            "average_latency_ms":
            round(
                self.average_latency,
                2
            ),

            "samples":
            len(self.execution_times)

        }