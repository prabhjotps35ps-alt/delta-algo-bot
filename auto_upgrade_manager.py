import os
import shutil
import traceback
from datetime import datetime


class AutoUpgradeManager:

    def __init__(self):

        self.backup_folder = "backup_files"

        self.log_file = "upgrade_log.txt"

        self.ensure_backup_folder()

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

        log_message = (
            f"[{timestamp}] {message}\n"
        )

        with open(
            self.log_file,
            "a"
        ) as file:

            file.write(log_message)

    # =========================
    # BACKUP FILE
    # =========================

    def backup_file(
        self,
        filename
    ):

        try:

            if not os.path.exists(
                filename
            ):

                return False

            backup_name = (
                f"{self.backup_folder}/"
                f"{filename}.bak"
            )

            shutil.copy(
                filename,
                backup_name
            )

            self.write_log(
                f"Backup created for {filename}"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Backup error: {str(e)}"
            )

            return False

    # =========================
    # AUTO UPGRADE FILE
    # =========================

    def auto_upgrade(
        self,
        filename,
        new_content
    ):

        try:

            self.backup_file(
                filename
            )

            with open(
                filename,
                "w"
            ) as file:

                file.write(
                    new_content
                )

            self.write_log(
                f"{filename} upgraded successfully"
            )

            return {
                "status": "success",
                "file": filename
            }

        except Exception as e:

            self.write_log(
                f"Upgrade error: {str(e)}"
            )

            return {
                "status": "failed",
                "error": str(e)
            }

    # =========================
    # AUTO FIX IMPORTS
    # =========================

    def fix_imports(
        self,
        filename
    ):

        try:

            with open(
                filename,
                "r"
            ) as file:

                content = file.read()

            fixed_content = content.replace(
                "from flask import Flask jsonify",
                "from flask import Flask, jsonify"
            )

            with open(
                filename,
                "w"
            ) as file:

                file.write(
                    fixed_content
                )

            self.write_log(
                f"Imports fixed in {filename}"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Import fix error: {str(e)}"
            )

            return False

    # =========================
    # SYNTAX CHECK
    # =========================

    def syntax_check(
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

            self.write_log(
                f"Syntax OK: {filename}"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Syntax Error in {filename}: {str(e)}"
            )

            return False

    # =========================
    # AUTO RECOVERY
    # =========================

    def auto_recovery(
        self,
        filename
    ):

        try:

            backup_name = (
                f"{self.backup_folder}/"
                f"{filename}.bak"
            )

            if not os.path.exists(
                backup_name
            ):

                return False

            shutil.copy(
                backup_name,
                filename
            )

            self.write_log(
                f"Recovered {filename}"
            )

            return True

        except Exception as e:

            self.write_log(
                f"Recovery error: {str(e)}"
            )

            return False

    # =========================
    # FULL PROJECT SCAN
    # =========================

    def full_scan(self):

        results = []

        for file in os.listdir():

            if file.endswith(".py"):

                syntax = self.syntax_check(
                    file
                )

                results.append({
                    "file": file,
                    "syntax_ok": syntax
                })

        return results

    # =========================
    # AUTO OPTIMIZER
    # =========================

    def optimize_project(self):

        self.write_log(
            "Project optimization started"
        )

        results = self.full_scan()

        self.write_log(
            "Project optimization completed"
        )

        return results

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
# RUN MANAGER
# =========================

if __name__ == "__main__":

    manager = AutoUpgradeManager()

    result = manager.optimize_project()

    print(result)