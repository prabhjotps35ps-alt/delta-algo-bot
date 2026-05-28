import os
import time
import psutil
import socket
import traceback
from datetime import datetime


class VPSMonitorEngine:

    def __init__(self):

        # =========================
        # LIMIT SETTINGS
        # =========================

        self.cpu_limit = 85

        self.ram_limit = 85

        self.disk_limit = 90

        self.internet_timeout = 5

        # =========================
        # SYSTEM STATUS
        # =========================

        self.server_status = (
            "healthy"
        )

        self.internet_status = (
            "connected"
        )

        self.last_ping = None

        self.system_reports = []

    # =========================
    # CPU MONITOR
    # =========================

    def cpu_monitor(self):

        cpu = psutil.cpu_percent(
            interval=1
        )

        status = "normal"

        if cpu >= self.cpu_limit:

            status = "critical"

        return {

            "cpu_usage":
            cpu,

            "cpu_status":
            status

        }

    # =========================
    # RAM MONITOR
    # =========================

    def ram_monitor(self):

        ram = psutil.virtual_memory()

        usage = ram.percent

        status = "normal"

        if usage >= self.ram_limit:

            status = "critical"

        return {

            "ram_usage":
            usage,

            "ram_status":
            status

        }

    # =========================
    # DISK MONITOR
    # =========================

    def disk_monitor(self):

        disk = psutil.disk_usage("/")

        usage = disk.percent

        status = "normal"

        if usage >= self.disk_limit:

            status = "critical"

        return {

            "disk_usage":
            usage,

            "disk_status":
            status

        }

    # =========================
    # INTERNET CHECK
    # =========================

    def internet_check(self):

        try:

            socket.setdefaulttimeout(
                self.internet_timeout
            )

            host = socket.gethostbyname(
                "google.com"
            )

            connection = socket.create_connection(

                (host, 80),

                self.internet_timeout

            )

            connection.close()

            self.internet_status = (
                "connected"
            )

            return {

                "internet":
                "connected"

            }

        except Exception:

            self.internet_status = (
                "disconnected"
            )

            return {

                "internet":
                "disconnected"

            }

    # =========================
    # PROCESS MONITOR
    # =========================

    def process_monitor(self):

        processes = []

        for process in psutil.process_iter(

            ["pid", "name"]

        ):

            try:

                processes.append({

                    "pid":
                    process.info["pid"],

                    "name":
                    process.info["name"]

                })

            except Exception:

                continue

        return {

            "total_processes":
            len(processes)

        }

    # =========================
    # SYSTEM HEALTH ENGINE
    # =========================

    def system_health_engine(self):

        cpu = (
            self.cpu_monitor()
        )

        ram = (
            self.ram_monitor()
        )

        disk = (
            self.disk_monitor()
        )

        internet = (
            self.internet_check()
        )

        health = "healthy"

        if (

            cpu["cpu_status"]
            == "critical"

            or

            ram["ram_status"]
            == "critical"

            or

            disk["disk_status"]
            == "critical"

        ):

            health = "warning"

        if internet["internet"] == (
            "disconnected"
        ):

            health = "critical"

        self.server_status = (
            health
        )

        report = {

            "time":
            str(datetime.now()),

            "health":
            health,

            "cpu":
            cpu,

            "ram":
            ram,

            "disk":
            disk,

            "internet":
            internet

        }

        self.system_reports.append(
            report
        )

        return report

    # =========================
    # AUTO RECOVERY ENGINE
    # =========================

    def auto_recovery_engine(self):

        try:

            if self.internet_status == (
                "disconnected"
            ):

                print(
                    "Internet Recovery Attempt"
                )

                os.system(
                    "ping -c 1 google.com"
                )

            if self.server_status == (
                "warning"
            ):

                print(
                    "Resource Optimization Triggered"
                )

            return {

                "recovery":
                "completed"

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "recovery":
                "failed",

                "error":
                str(e)

            }

    # =========================
    # LIVE MONITOR LOOP
    # =========================

    def start_monitor_loop(self):

        while True:

            try:

                report = (
                    self.system_health_engine()
                )

                print(report)

                if report["health"] != (
                    "healthy"
                ):

                    self.auto_recovery_engine()

                time.sleep(30)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Monitor Error:",
                    str(e)
                )


if __name__ == "__main__":

    monitor = (
        VPSMonitorEngine()
    )

    monitor.start_monitor_loop()