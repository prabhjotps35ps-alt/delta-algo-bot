import os
import traceback
from datetime import datetime


class AutoErrorFixEngine:

    def __init__(self):

        self.fixed_files = []

        self.error_reports = []

        self.common_fixes = {

            "\t": "    ",

            "debug=True": "debug=False",

            "app=Flask(__name__)":
            "app = Flask(__name__)",

            "print ": "print("

        }

    # =========================
    # SCAN PYTHON FILES
    # =========================

    def scan_python_files(self):

        files = []

        for file in os.listdir():

            if file.endswith(".py"):

                files.append(file)

        return files

    # =========================
    # SYNTAX TEST
    # =========================

    def syntax_test(
        self,
        filepath
    ):

        try:

            with open(
                filepath,
                "r"
            ) as file:

                code = file.read()

            compile(
                code,
                filepath,
                "exec"
            )

            return {

                "status":
                "healthy"

            }

        except Exception as e:

            return {

                "status":
                "error",

                "error":
                str(e)

            }

    # =========================
    # AUTO FIX ENGINE
    # =========================

    def auto_fix_file(
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
            # APPLY FIXES
            # =========================

            for bad, good in (
                self.common_fixes.items()
            ):

                content = content.replace(
                    bad,
                    good
                )

            with open(
                filepath,
                "w"
            ) as file:

                file.write(content)

            self.fixed_files.append(
                filepath
            )

            return {

                "status":
                "fixed",

                "file":
                filepath

            }

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "failed",

                "error":
                str(e)

            }

    # =========================
    # FULL AUTO TEST
    # =========================

    def full_auto_test(self):

        report = {

            "healthy": [],

            "fixed": [],

            "failed": []

        }

        try:

            files = (
                self.scan_python_files()
            )

            for file in files:

                test = (
                    self.syntax_test(
                        file
                    )
                )

                # =========================
                # HEALTHY
                # =========================

                if test["status"] == (
                    "healthy"
                ):

                    report[
                        "healthy"
                    ].append(file)

                # =========================
                # FIX ERROR
                # =========================

                else:

                    fix = (
                        self.auto_fix_file(
                            file
                        )
                    )

                    if fix["status"] == (
                        "fixed"
                    ):

                        report[
                            "fixed"
                        ].append(file)

                    else:

                        report[
                            "failed"
                        ].append({

                            "file":
                            file,

                            "error":
                            test["error"]

                        })

            self.error_reports.append(
                report
            )

            return report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "engine_failed",

                "error":
                str(e)

            }

    # =========================
    # LIVE AUTO FIX LOOP
    # =========================

    def start_auto_fix_loop(self):

        import time

        while True:

            try:

                report = (
                    self.full_auto_test()
                )

                print(report)

                time.sleep(60)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Auto Fix Error:",
                    str(e)
                )

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "time":
            str(datetime.now()),

            "fixed_files":
            len(self.fixed_files),

            "reports":
            len(self.error_reports)

        }


if __name__ == "__main__":

    engine = (
        AutoErrorFixEngine()
    )

    print(
        engine.full_auto_test()
    )