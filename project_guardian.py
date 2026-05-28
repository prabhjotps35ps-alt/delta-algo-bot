import os
import time
import json
import shutil
import traceback
from datetime import datetime


class ProjectGuardian:

    def __init__(self):

        self.project_status_file = (
            "project_status.json"
        )

        self.guardian_log = (
            "guardian_log.txt"
        )

        self.backup_folder = (
            "guardian_backups"
        )

        self.ensure_backup_folder()

    # =========================
    # BACKUP FOLDER
    # =========================

    def ensure_backup_folder(self):

        if not os.path.exists(
            self.backup_folder
        ):

            os.makedirs(
                self.backup_folder
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
            self.guardian_log,
            "a"
        ) as file:

            file.write(
                final_message
            )

    # =========================
    # SAVE PROJECT STATUS
    # =========================

    def save_status(
        self,
        status
    ):

        with open(
            self.project_status_file,
            "w"
        ) as file:

            json.dump(
                status,
                file,
                indent=4
            )

    # =========================
    # LOAD PROJECT STATUS
    # =========================

    def load_status(self):

        try:

            with open(
                self.project_status_file,
                "r"
            ) as file:

                return json.load(file)

        except Exception:

            return {}

    # =========================
    # AUTO BACKUP
    # =========================

    def backup_project(self):

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

            if file.endswith(".py"):

                shutil.copy(
                    file,
                    backup_path
                )

        self.write_log(
            "Project backup completed"
        )

        return backup_path

    # =========================
    # FILE MONITOR
    # =========================

    def monitor_files(self):

        files = []

        for file in os.listdir():

            if file.endswith(".py"):

                size = os.path.getsize(
                    file
                )

                files.append({
                    "file": file,
                    "size": size
                })

        return files

    # =========================
    # SYNTAX VALIDATOR
    # =========================

    def validate_syntax(
        self,
        filename
    ):

        try:

            with open(
                filename,
                "r"
            ) as file:

                code = file.read()

            compile(
                code,
                filename,
                "exec"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Syntax error in "
                f"{filename}: {str(e)}"
            )

            return False

    # =========================
    # AUTO FIX COMMON ERRORS
    # =========================

    def auto_fix_common_errors(
        self,
        filename
    ):

        try:

            with open(
                filename,
                "r"
            ) as file:

                content = file.read()

            content = content.replace(
                "from flask import Flask jsonify",
                "from flask import Flask, jsonify"
            )

            content = content.replace(
                "app=Flask(__name__)",
                "app = Flask(__name__)"
            )

            with open(
                filename,
                "w"
            ) as file:

                file.write(
                    content
                )

            self.write_log(
                f"Common fixes applied "
                f"to {filename}"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Fix error: {str(e)}"
            )

            return False

    # =========================
    # PROJECT HEALTH CHECK
    # =========================

    def health_check(self):

        files = self.monitor_files()

        valid_files = 0

        invalid_files = 0

        for item in files:

            file = item["file"]

            valid = self.validate_syntax(
                file
            )

            if valid:

                valid_files += 1

            else:

                invalid_files += 1

        status = {
            "valid_files": valid_files,
            "invalid_files": invalid_files,
            "timestamp": str(
                datetime.now()
            )
        }

        self.save_status(
            status
        )

        return status

    # =========================
    # AUTO RECOVERY
    # =========================

    def auto_recovery(self):

        latest_backup = None

        backups = sorted(
            os.listdir(
                self.backup_folder
            )
        )

        if backups:

            latest_backup = backups[-1]

        if not latest_backup:

            return False

        backup_path = (
            f"{self.backup_folder}/"
            f"{latest_backup}"
        )

        for file in os.listdir(
            backup_path
        ):

            shutil.copy(
                f"{backup_path}/{file}",
                file
            )

        self.write_log(
            "Project auto recovery completed"
        )

        return True

    # =========================
    # AUTO OPTIMIZATION
    # =========================

    def optimize_project(self):

        self.write_log(
            "Optimization started"
        )

        status = self.health_check()

        self.write_log(
            "Optimization completed"
        )

        return status

    # =========================
    # AUTO LOOP PROTECTION
    # =========================

    def protection_loop(self):

        while True:

            try:

                self.optimize_project()

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Protection loop error: "
                    f"{str(e)}"
                )

    # =========================
    # CRITICAL ERROR LOGGER
    # =========================

    def critical_error(
        self,
        error
    ):

        traceback.print_exc()

        self.write_log(
            f"Critical error: {str(error)}"
        )

        return {
            "critical_error": str(error)
        }


# =========================
# RUN PROJECT GUARDIAN
# =========================

if __name__ == "__main__":

    guardian = ProjectGuardian()

    result = guardian.optimize_project()

    print(result)