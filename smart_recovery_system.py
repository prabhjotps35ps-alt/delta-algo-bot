import os
import json
import shutil
import traceback
from datetime import datetime


class SmartRecoverySystem:

    def __init__(self):

        self.recovery_folder = (
            "smart_recovery"
        )

        self.recovery_log = (
            "smart_recovery_log.txt"
        )

        self.ensure_folder()

    # =========================
    # ENSURE RECOVERY FOLDER
    # =========================

    def ensure_folder(self):

        if not os.path.exists(
            self.recovery_folder
        ):

            os.makedirs(
                self.recovery_folder
            )

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
            self.recovery_log,
            "a"
        ) as file:

            file.write(
                final_message
            )

    # =========================
    # CREATE SNAPSHOT
    # =========================

    def create_snapshot(self):

        try:

            timestamp = (
                datetime.now()
                .strftime("%Y%m%d_%H%M%S")
            )

            snapshot_folder = (
                f"{self.recovery_folder}/"
                f"snapshot_{timestamp}"
            )

            os.makedirs(
                snapshot_folder
            )

            for file in os.listdir():

                if file.endswith(".py"):

                    shutil.copy(
                        file,
                        snapshot_folder
                    )

            self.write_log(
                "Snapshot created successfully"
            )

            return {
                "status": "success",
                "snapshot": snapshot_folder
            }

        except Exception as e:

            self.write_log(
                f"Snapshot error: {str(e)}"
            )

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # RESTORE SNAPSHOT
    # =========================

    def restore_snapshot(
        self,
        snapshot_name
    ):

        try:

            snapshot_path = (
                f"{self.recovery_folder}/"
                f"{snapshot_name}"
            )

            if not os.path.exists(
                snapshot_path
            ):

                return {
                    "status": "failed",
                    "message": "Snapshot not found"
                }

            for file in os.listdir(
                snapshot_path
            ):

                shutil.copy(
                    f"{snapshot_path}/{file}",
                    file
                )

            self.write_log(
                f"Restored snapshot "
                f"{snapshot_name}"
            )

            return {
                "status": "success"
            }

        except Exception as e:

            self.write_log(
                f"Restore error: {str(e)}"
            )

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # CHECK BROKEN FILES
    # =========================

    def detect_broken_files(self):

        broken_files = []

        for file in os.listdir():

            if file.endswith(".py"):

                try:

                    with open(
                        file,
                        "r"
                    ) as code_file:

                        code = code_file.read()

                    compile(
                        code,
                        file,
                        "exec"
                    )

                except Exception:

                    broken_files.append(
                        file
                    )

        return broken_files

    # =========================
    # AUTO FIX FILES
    # =========================

    def auto_fix_files(self):

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
                        "from flask import Flask jsonify",
                        "from flask import Flask, jsonify"
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

        return fixed_files

    # =========================
    # SYSTEM HEALTH
    # =========================

    def system_health(self):

        broken = (
            self.detect_broken_files()
        )

        if broken:

            return {
                "status": "warning",
                "broken_files": broken
            }

        return {
            "status": "healthy"
        }

    # =========================
    # AUTO SELF HEALING
    # =========================

    def self_healing(self):

        try:

            broken_files = (
                self.detect_broken_files()
            )

            if broken_files:

                self.auto_fix_files()

                self.write_log(
                    "Self healing completed"
                )

                return {
                    "status": "fixed",
                    "files": broken_files
                }

            return {
                "status": "healthy"
            }

        except Exception as e:

            self.write_log(
                f"Self healing error: {str(e)}"
            )

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # FULL PROJECT REPORT
    # =========================

    def project_report(self):

        report = {
            "health": self.system_health(),
            "snapshots": os.listdir(
                self.recovery_folder
            )
        }

        return report

    # =========================
    # CRITICAL ERROR LOGGER
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
# RUN SYSTEM
# =========================

if __name__ == "__main__":

    recovery = SmartRecoverySystem()

    recovery.create_snapshot()

    result = recovery.self_healing()

    print(result)