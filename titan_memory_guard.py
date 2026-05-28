import os
import json
import time
import shutil
import traceback
from datetime import datetime


class TitanMemoryGuard:

    def __init__(self):

        self.guard_log = (
            "titan_memory_guard_log.txt"
        )

        self.guard_memory = (
            "titan_memory_guard_memory.json"
        )

        self.backup_folder = (
            "titan_backups"
        )

        self.guard_mode = (
            "memory_protection"
        )

        self.memory_history = []

        self.ensure_backup_folder()

        self.load_memory()

    # =========================
    # CREATE BACKUP FOLDER
    # =========================

    def ensure_backup_folder(self):

        if not os.path.exists(
            self.backup_folder
        ):

            os.makedirs(
                self.backup_folder
            )

    # =========================
    # LOG SYSTEM
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
            self.guard_log,
            "a"
        ) as file:

            file.write(
                final_message
            )

    # =========================
    # LOAD MEMORY
    # =========================

    def load_memory(self):

        try:

            if not os.path.exists(
                self.guard_memory
            ):

                with open(
                    self.guard_memory,
                    "w"
                ) as file:

                    json.dump([], file)

            with open(
                self.guard_memory,
                "r"
            ) as file:

                self.memory_history = (
                    json.load(file)
                )

        except Exception as e:

            self.memory_history = []

            self.write_log(
                f"Memory load error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.guard_memory,
            "w"
        ) as file:

            json.dump(
                self.memory_history,
                file,
                indent=4
            )

    # =========================
    # AUTO BACKUP ENGINE
    # =========================

    def auto_backup_engine(self):

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )

        backup_path = (
            f"{self.backup_folder}/"
            f"backup_{timestamp}"
        )

        os.makedirs(
            backup_path
        )

        for file in os.listdir():

            if (
                file.endswith(".py")
                or file.endswith(".json")
                or file.endswith(".txt")
            ):

                shutil.copy(
                    file,
                    backup_path
                )

        self.write_log(
            f"Backup created: "
            f"{backup_path}"
        )

        return backup_path

    # =========================
    # SYSTEM SCANNER
    # =========================

    def system_scanner(self):

        report = {
            "total_python_files": 0,
            "healthy_files": 0,
            "broken_files": []
        }

        for file in os.listdir():

            if file.endswith(".py"):

                report[
                    "total_python_files"
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

                    report[
                        "healthy_files"
                    ] += 1

                except Exception as e:

                    report[
                        "broken_files"
                    ].append({
                        "file": file,
                        "error": str(e)
                    })

        return report

    # =========================
    # AUTO FIX ENGINE
    # =========================

    def auto_fix_engine(self):

        fixed_files = []

        for file in os.listdir():

            if file.endswith(".py"):

                try:

                    with open(
                        file,
                        "r"
                    ) as code_file:

                        content = (
                            code_file.read()
                        )

                    content = content.replace(
                        "debug=True",
                        "debug=False"
                    )

                    content = content.replace(
                        "app=Flask(__name__)",
                        "app = Flask(__name__)"
                    )

                    with open(
                        file,
                        "w"
                    ) as code_file:

                        code_file.write(
                            content
                        )

                    fixed_files.append(
                        file
                    )

                except Exception as e:

                    self.write_log(
                        f"Fix error in "
                        f"{file}: {str(e)}"
                    )

        self.write_log(
            "Auto fix completed"
        )

        return fixed_files

    # =========================
    # MEMORY OPTIMIZER
    # =========================

    def memory_optimizer(self):

        if len(
            self.memory_history
        ) > 1000:

            self.memory_history = (
                self.memory_history[-500:]
            )

            self.save_memory()

            return {
                "optimized": True
            }

        return {
            "optimized": False
        }

    # =========================
    # PERFORMANCE ENGINE
    # =========================

    def performance_engine(
        self,
        cpu_usage,
        ram_usage
    ):

        if cpu_usage > 90:

            return {
                "cpu_status": "critical"
            }

        if ram_usage > 90:

            return {
                "ram_status": "critical"
            }

        return {
            "system_status": "stable"
        }

    # =========================
    # RISK SHIELD
    # =========================

    def risk_shield(
        self,
        drawdown
    ):

        if drawdown >= 25:

            return {
                "trading_disabled": True
            }

        if drawdown >= 15:

            return {
                "safe_mode": True
            }

        return {
            "safe_mode": False
        }

    # =========================
    # LIVE GUARD LOOP
    # =========================

    def live_guard_loop(self):

        while True:

            try:

                report = (
                    self.system_scanner()
                )

                if report["broken_files"]:

                    self.auto_fix_engine()

                self.write_log(
                    f"Guard report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Guard loop error: "
                    f"{str(e)}"
                )

    # =========================
    # FULL REPORT
    # =========================

    def full_report(self):

        return {
            "mode": self.guard_mode,
            "scan": (
                self.system_scanner()
            ),
            "stored_memory": len(
                self.memory_history
            )
        }

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
# RUN TITAN MEMORY GUARD
# =========================

if __name__ == "__main__":

    guard = TitanMemoryGuard()

    guard.auto_backup_engine()

    result = guard.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )