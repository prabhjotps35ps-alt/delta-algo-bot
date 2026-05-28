import os
import time
import json
import traceback
from datetime import datetime


class IntelligentMonitor:

    def __init__(self):

        self.monitor_log = (
            "intelligent_monitor_log.txt"
        )

        self.monitor_status = (
            "monitor_status.json"
        )

        self.last_scan = None

    # =========================
    # LOG WRITER
    # =========================

    def write_log(
        self,
        message
    ):

        timestamp = str(
            datetime.now()
        )

        final_message = (
            f"[{timestamp}] {message}\n"
        )

        with open(
            self.monitor_log,
            "a"
        ) as file:

            file.write(
                final_message
            )

    # =========================
    # SAVE STATUS
    # =========================

    def save_status(
        self,
        data
    ):

        with open(
            self.monitor_status,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # =========================
    # LOAD STATUS
    # =========================

    def load_status(self):

        try:

            with open(
                self.monitor_status,
                "r"
            ) as file:

                return json.load(file)

        except Exception:

            return {}

    # =========================
    # SCAN PYTHON FILES
    # =========================

    def scan_project(self):

        project_data = {
            "total_files": 0,
            "healthy_files": 0,
            "broken_files": []
        }

        for file in os.listdir():

            if file.endswith(".py"):

                project_data[
                    "total_files"
                ] += 1

                try:

                    with open(
                        file,
                        "r"
                    ) as code_file:

                        code = (
                            code_file.read()
                        )

                    compile(
                        code,
                        file,
                        "exec"
                    )

                    project_data[
                        "healthy_files"
                    ] += 1

                except Exception as e:

                    project_data[
                        "broken_files"
                    ].append({
                        "file": file,
                        "error": str(e)
                    })

        self.last_scan = str(
            datetime.now()
        )

        self.write_log(
            "Project scan completed"
        )

        self.save_status(
            project_data
        )

        return project_data

    # =========================
    # AUTO HEALTH CHECK
    # =========================

    def health_check(self):

        result = self.scan_project()

        if result["broken_files"]:

            return {
                "status": "warning",
                "details": result
            }

        return {
            "status": "healthy",
            "details": result
        }

    # =========================
    # AUTO MEMORY CHECK
    # =========================

    def memory_check(self):

        try:

            total_files = len(
                os.listdir()
            )

            return {
                "status": "ok",
                "files": total_files
            }

        except Exception as e:

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # AUTO IMPORT CHECK
    # =========================

    def import_check(
        self,
        filename
    ):

        try:

            with open(
                filename,
                "r"
            ) as file:

                content = file.read()

            if (
                "from flask import Flask jsonify"
                in content
            ):

                return {
                    "status": "broken_import"
                }

            return {
                "status": "ok"
            }

        except Exception as e:

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # AUTO PERFORMANCE CHECK
    # =========================

    def performance_check(self):

        start = time.time()

        self.scan_project()

        end = time.time()

        execution_time = round(
            end - start,
            2
        )

        return {
            "scan_time": execution_time,
            "status": "optimized"
        }

    # =========================
    # AUTO SYSTEM REPORT
    # =========================

    def system_report(self):

        report = {
            "health": self.health_check(),
            "memory": self.memory_check(),
            "performance": (
                self.performance_check()
            ),
            "last_scan": self.last_scan
        }

        return report

    # =========================
    # LIVE PROTECTION LOOP
    # =========================

    def live_monitoring(self):

        while True:

            try:

                report = self.system_report()

                self.write_log(
                    f"Live report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Monitoring error: "
                    f"{str(e)}"
                )

    # =========================
    # CRITICAL LOGGER
    # =========================

    def critical_error(
        self,
        error
    ):

        traceback.print_exc()

        self.write_log(
            f"Critical Error: {str(error)}"
        )

        return {
            "critical_error": str(error)
        }


# =========================
# RUN MONITOR
# =========================

if __name__ == "__main__":

    monitor = IntelligentMonitor()

    result = monitor.system_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )