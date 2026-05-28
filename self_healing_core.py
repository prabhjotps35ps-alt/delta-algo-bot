import os
import time
import shutil
import traceback
from datetime import datetime


class SelfHealingCore:

    def __init__(self):

        # =========================
        # HEALING SETTINGS
        # =========================

        self.backup_folder = (
            "system_backups"
        )

        self.healing_logs = []

        self.repair_count = 0

        self.max_backups = 10

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
    # BACKUP FILE
    # =========================

    def backup_file(
        self,
        filepath
    ):

        try:

            if not os.path.exists(
                filepath
            ):

                return False

            filename = os.path.basename(
                filepath
            )

            timestamp = int(time.time())

            backup_name = (

                f"{timestamp}_"

                f"{filename}"

            )

            destination = os.path.join(

                self.backup_folder,

                backup_name

            )

            shutil.copy2(
                filepath,
                destination
            )

            return True

        except Exception as e:

            traceback.print_exc()

            return False

    # =========================
    # FILE HEALTH CHECK
    # =========================

    def file_health_check(
        self,
        filepath
    ):

        try:

            with open(
                filepath,
                "r",
                errors="ignore"
            ) as file:

                content = file.read()

            # =========================
            # EMPTY FILE
            # =========================

            if len(content.strip()) == 0:

                return {

                    "healthy": False,

                    "reason": "empty_file"

                }

            # =========================
            # BASIC PYTHON CHECK
            # =========================

            if filepath.endswith(".py"):

                compile(
                    content,
                    filepath,
                    "exec"
                )

            return {

                "healthy": True

            }

        except Exception as e:

            return {

                "healthy": False,

                "reason": str(e)

            }

    # =========================
    # AUTO REPAIR FILE
    # =========================

    def auto_repair_file(
        self,
        filepath
    ):

        try:

            # =========================
            # BACKUP BEFORE REPAIR
            # =========================

            self.backup_file(
                filepath
            )

            with open(
                filepath,
                "r",
                errors="ignore"
            ) as file:

                content = file.read()

            # =========================
            # BASIC REPAIRS
            # =========================

            content = content.replace(
                "\t",
                "    "
            )

            content = content.replace(
                "debug=True",
                "debug=False"
            )

            content = content.replace(
                "print ",
                "print("
            )

            # =========================
            # AUTO CLOSE PRINT
            # =========================

            fixed_lines = []

            for line in content.splitlines():

                if (

                    "print(" in line

                    and

                    not line.strip().endswith(
                        ")"
                    )

                ):

                    line += ")"

                fixed_lines.append(line)

            content = "\n".join(
                fixed_lines
            )

            with open(
                filepath,
                "w"
            ) as file:

                file.write(content)

            self.repair_count += 1

            repair_report = {

                "time":
                str(datetime.now()),

                "file":
                filepath,

                "status":
                "repaired"

            }

            self.healing_logs.append(
                repair_report
            )

            return repair_report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "repair_failed",

                "error":
                str(e)

            }

    # =========================
    # HEAL ALL FILES
    # =========================

    def heal_system(self):

        report = {

            "healthy": [],

            "repaired": [],

            "failed": []

        }

        try:

            for root, dirs, files in os.walk("."):

                for file in files:

                    if not file.endswith(
                        ".py"
                    ):

                        continue

                    filepath = os.path.join(
                        root,
                        file
                    )

                    health = (
                        self.file_health_check(
                            filepath
                        )
                    )

                    # =========================
                    # HEALTHY
                    # =========================

                    if health["healthy"]:

                        report[
                            "healthy"
                        ].append(
                            filepath
                        )

                    # =========================
                    # REPAIR
                    # =========================

                    else:

                        repair = (
                            self.auto_repair_file(
                                filepath
                            )
                        )

                        if repair[
                            "status"
                        ] == "repaired":

                            report[
                                "repaired"
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
                                health[
                                    "reason"
                                ]

                            })

            return report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "healing_failed",

                "error":
                str(e)

            }

    # =========================
    # LIVE HEALING LOOP
    # =========================

    def start_healing_loop(self):

        while True:

            try:

                report = (
                    self.heal_system()
                )

                print(report)

                time.sleep(120)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Healing Error:",
                    str(e)
                )


if __name__ == "__main__":

    healer = (
        SelfHealingCore()
    )

    print(
        healer.heal_system()
    )