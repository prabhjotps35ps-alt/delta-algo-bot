import os
import traceback
from datetime import datetime

from self_healing_core import (
    SelfHealingCore
)


class AutomaticRepairEngine:

    def __init__(self):

        self.healer = (
            SelfHealingCore()
        )

        self.repair_history = []

        self.detected_errors = []

    # =========================
    # ERROR DETECTOR
    # =========================

    def detect_runtime_errors(
        self,
        filepath
    ):

        try:

            with open(
                filepath,
                "r",
                errors="ignore"
            ) as file:

                code = file.read()

            compile(
                code,
                filepath,
                "exec"
            )

            return None

        except Exception as e:

            return str(e)

    # =========================
    # SCAN PROJECT
    # =========================

    def scan_project(self):

        errors = []

        for root, dirs, files in os.walk("."):

            for file in files:

                if file.endswith(".py"):

                    filepath = os.path.join(
                        root,
                        file
                    )

                    error = (
                        self.detect_runtime_errors(
                            filepath
                        )
                    )

                    if error:

                        errors.append({

                            "file":
                            filepath,

                            "error":
                            error

                        })

        self.detected_errors = errors

        return errors

    # =========================
    # AUTO REPAIR
    # =========================

    def automatic_repair(self):

        report = {

            "fixed": [],

            "failed": []

        }

        try:

            errors = (
                self.scan_project()
            )

            for item in errors:

                filepath = item["file"]

                repair = (
                    self.healer
                    .auto_repair_file(
                        filepath
                    )
                )

                if repair[
                    "status"
                ] == "repaired":

                    report[
                        "fixed"
                    ].append(
                        filepath
                    )

                else:

                    report[
                        "failed"
                    ].append({

                        "file":
                        filepath,

                        "error":
                        item["error"]

                    })

            self.repair_history.append(
                report
            )

            return report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "repair_engine_failed",

                "error":
                str(e)

            }

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "time":
            str(datetime.now()),

            "total_repairs":
            len(self.repair_history),

            "detected_errors":
            len(self.detected_errors)

        }

    # =========================
    # LIVE AUTO REPAIR LOOP
    # =========================

    def start_repair_loop(self):

        import time

        while True:

            try:

                report = (
                    self.automatic_repair()
                )

                print(report)

                time.sleep(180)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Repair Engine Error:",
                    str(e)
                )


if __name__ == "__main__":

    engine = (
        AutomaticRepairEngine()
    )

    print(
        engine.automatic_repair()
    )