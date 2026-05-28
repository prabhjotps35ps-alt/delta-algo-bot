import os
import json
import time
import shutil
import traceback
from datetime import datetime


class NeuralGuardian:

    def __init__(self):

        self.guardian_log = (
            "neural_guardian_log.txt"
        )

        self.guardian_memory = (
            "neural_guardian_memory.json"
        )

        self.snapshot_folder = (
            "neural_snapshots"
        )

        self.guardian_mode = (
            "active"
        )

        self.ensure_snapshot_folder()

        self.load_memory()

    # =========================
    # ENSURE SNAPSHOT FOLDER
    # =========================

    def ensure_snapshot_folder(self):

        if not os.path.exists(
            self.snapshot_folder
        ):

            os.makedirs(
                self.snapshot_folder
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
    # LOAD MEMORY
    # =========================

    def load_memory(self):

        try:

            if not os.path.exists(
                self.guardian_memory
            ):

                with open(
                    self.guardian_memory,
                    "w"
                ) as file:

                    json.dump({}, file)

            with open(
                self.guardian_memory,
                "r"
            ) as file:

                self.memory = json.load(
                    file
                )

        except Exception as e:

            self.memory = {}

            self.write_log(
                f"Memory load error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.guardian_memory,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    # =========================
    # CREATE SNAPSHOT
    # =========================

    def create_snapshot(self):

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
        )

        snapshot_path = (
            f"{self.snapshot_folder}/"
            f"snapshot_{timestamp}"
        )

        os.makedirs(
            snapshot_path
        )

        for file in os.listdir():

            if (
                file.endswith(".py")
                or file.endswith(".txt")
            ):

                shutil.copy(
                    file,
                    snapshot_path
                )

        self.write_log(
            f"Snapshot created: {snapshot_path}"
        )

        return snapshot_path

    # =========================
    # PROJECT SCANNER
    # =========================

    def scan_project(self):

        report = {
            "total_files": 0,
            "healthy_files": 0,
            "broken_files": []
        }

        for file in os.listdir():

            if file.endswith(".py"):

                report[
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
    # AUTO HEAL SYSTEM
    # =========================

    def auto_heal(self):

        healed_files = []

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

                    content = content.replace(
                        "debug=True",
                        "debug=False"
                    )

                    with open(
                        file,
                        "w"
                    ) as code_file:

                        code_file.write(
                            content
                        )

                    healed_files.append(
                        file
                    )

                except Exception as e:

                    self.write_log(
                        f"Heal error in "
                        f"{file}: {str(e)}"
                    )

        self.write_log(
            "Auto heal completed"
        )

        return healed_files

    # =========================
    # INTELLIGENT RECOVERY
    # =========================

    def intelligent_recovery(self):

        report = self.scan_project()

        if report["broken_files"]:

            self.guardian_mode = (
                "recovery"
            )

            self.auto_heal()

            self.guardian_mode = (
                "protected"
            )

            return {
                "status": "recovered",
                "broken_files": (
                    report[
                        "broken_files"
                    ]
                )
            }

        return {
            "status": "healthy"
        }

    # =========================
    # AI MARKET DECISION
    # =========================

    def market_decision(
        self,
        signal_score,
        trend,
        volume
    ):

        if signal_score >= 85:

            if trend == "bullish":

                if volume == "strong":

                    return "aggressive_buy"

                return "safe_buy"

            if trend == "bearish":

                return "strong_sell"

        if signal_score >= 60:

            return "wait_confirmation"

        return "avoid_market"

    # =========================
    # RISK PROTECTION
    # =========================

    def risk_protection(
        self,
        drawdown
    ):

        if drawdown >= 20:

            return {
                "mode": "critical_protection"
            }

        if drawdown >= 10:

            return {
                "mode": "safe_protection"
            }

        return {
            "mode": "normal"
        }

    # =========================
    # LIVE GUARDIAN LOOP
    # =========================

    def live_guardian(self):

        while True:

            try:

                report = self.scan_project()

                if report["broken_files"]:

                    self.intelligent_recovery()

                self.write_log(
                    f"Guardian report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Guardian loop error: "
                    f"{str(e)}"
                )

    # =========================
    # FULL SYSTEM REPORT
    # =========================

    def full_report(self):

        report = {
            "guardian_mode": (
                self.guardian_mode
            ),
            "scan": self.scan_project(),
            "memory": self.memory
        }

        return report

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
# RUN GUARDIAN
# =========================

if __name__ == "__main__":

    guardian = NeuralGuardian()

    guardian.create_snapshot()

    result = guardian.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )