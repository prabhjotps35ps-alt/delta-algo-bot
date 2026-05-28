import os
import time
import signal
import psutil
import traceback
from datetime import datetime


class RuntimeRecoveryEngine:

    def __init__(self):

        # =========================
        # CORE MODULES
        # =========================

        self.critical_processes = [

            "python",

            "gunicorn"

        ]

        self.restart_attempts = 0

        self.max_restart_attempts = 5

        self.recovery_log = []

        self.runtime_status = (
            "stable"
        )

    # =========================
    # PROCESS SCANNER
    # =========================

    def process_scanner(self):

        active_processes = []

        try:

            for process in psutil.process_iter(

                ["pid", "name"]

            ):

                try:

                    process_name = (
                        process.info["name"]
                    )

                    active_processes.append(
                        process_name
                    )

                except Exception:

                    continue

            return active_processes

        except Exception as e:

            traceback.print_exc()

            return []

    # =========================
    # CRITICAL CHECK
    # =========================

    def critical_process_check(self):

        processes = (
            self.process_scanner()
        )

        missing = []

        for critical in (
            self.critical_processes
        ):

            found = False

            for process in processes:

                if critical.lower() in (
                    process.lower()
                ):

                    found = True

                    break

            if not found:

                missing.append(
                    critical
                )

        return missing

    # =========================
    # AUTO RESTART ENGINE
    # =========================

    def auto_restart_engine(self):

        try:

            missing = (
                self.critical_process_check()
            )

            if not missing:

                return {

                    "status":
                    "healthy"

                }

            self.runtime_status = (
                "recovering"
            )

            self.restart_attempts += 1

            # =========================
            # MAX LIMIT
            # =========================

            if self.restart_attempts > (
                self.max_restart_attempts
            ):

                self.runtime_status = (
                    "critical_failure"
                )

                return {

                    "status":
                    "max_restart_limit"

                }

            # =========================
            # RESTART APP
            # =========================

            print(
                "Restarting Runtime..."
            )

            os.system(
                "python app.py &"
            )

            report = {

                "time":
                str(datetime.now()),

                "missing":
                missing,

                "restart_attempt":
                self.restart_attempts,

                "status":
                "restart_triggered"

            }

            self.recovery_log.append(
                report
            )

            self.runtime_status = (
                "stable"
            )

            return report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "restart_failed",

                "error":
                str(e)

            }

    # =========================
    # MEMORY CLEANER
    # =========================

    def memory_cleaner(self):

        try:

            memory = (
                psutil.virtual_memory()
            )

            if memory.percent >= 85:

                print(
                    "High Memory Usage Detected"
                )

            return {

                "memory_usage":
                memory.percent

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "memory":
                "error"

            }

    # =========================
    # CPU PROTECTION
    # =========================

    def cpu_protection(self):

        try:

            cpu = psutil.cpu_percent(
                interval=1
            )

            if cpu >= 90:

                print(
                    "High CPU Usage Detected"
                )

            return {

                "cpu_usage":
                cpu

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "cpu":
                "error"

            }

    # =========================
    # SYSTEM STATUS
    # =========================

    def runtime_report(self):

        return {

            "time":
            str(datetime.now()),

            "runtime_status":
            self.runtime_status,

            "restart_attempts":
            self.restart_attempts,

            "recovery_logs":
            len(self.recovery_log)

        }

    # =========================
    # LIVE RECOVERY LOOP
    # =========================

    def start_runtime_loop(self):

        while True:

            try:

                missing = (
                    self.critical_process_check()
                )

                if missing:

                    print(
                        "Critical Process Missing:",
                        missing
                    )

                    self.auto_restart_engine()

                self.memory_cleaner()

                self.cpu_protection()

                print(
                    self.runtime_report()
                )

                time.sleep(20)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Recovery Engine Error:",
                    str(e)
                )


if __name__ == "__main__":

    engine = (
        RuntimeRecoveryEngine()
    )

    engine.start_runtime_loop()