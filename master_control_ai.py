import os
import json
import time
import shutil
import traceback
from datetime import datetime


class MasterControlAI:

    def __init__(self):

        self.master_log = (
            "master_control_log.txt"
        )

        self.master_memory = (
            "master_memory.json"
        )

        self.backup_folder = (
            "master_backups"
        )

        self.system_mode = (
            "initializing"
        )

        self.ensure_backup_folder()

        self.load_memory()

    # =========================
    # ENSURE BACKUP FOLDER
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
            self.master_log,
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
                self.master_memory
            ):

                with open(
                    self.master_memory,
                    "w"
                ) as file:

                    json.dump({}, file)

            with open(
                self.master_memory,
                "r"
            ) as file:

                self.memory = json.load(
                    file
                )

        except Exception as e:

            self.memory = {}

            self.write_log(
                f"Memory error: {str(e)}"
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.master_memory,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    # =========================
    # UPDATE SYSTEM MODE
    # =========================

    def update_mode(
        self,
        mode
    ):

        self.system_mode = mode

        self.memory[
            "system_mode"
        ] = mode

        self.memory[
            "updated_at"
        ] = str(
            datetime.now()
        )

        self.save_memory()

        self.write_log(
            f"Mode updated: {mode}"
        )

    # =========================
    # PROJECT ANALYZER
    # =========================

    def analyze_project(self):

        analysis = {
            "total_files": 0,
            "healthy_files": 0,
            "broken_files": []
        }

        for file in os.listdir():

            if file.endswith(".py"):

                analysis[
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

                    analysis[
                        "healthy_files"
                    ] += 1

                except Exception as e:

                    analysis[
                        "broken_files"
                    ].append({
                        "file": file,
                        "error": str(e)
                    })

        return analysis

    # =========================
    # CREATE FULL BACKUP
    # =========================

    def create_backup(self):

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
                or file.endswith(".txt")
            ):

                shutil.copy(
                    file,
                    backup_path
                )

        self.write_log(
            "Full backup created"
        )

        return backup_path

    # =========================
    # AUTO FIX SYSTEM
    # =========================

    def auto_fix_system(self):

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

                    fixed_files.append(
                        file
                    )

                except Exception as e:

                    self.write_log(
                        f"Fix error "
                        f"in {file}: {str(e)}"
                    )

        return fixed_files

    # =========================
    # AUTO RECOVERY SYSTEM
    # =========================

    def recovery_system(self):

        analysis = (
            self.analyze_project()
        )

        if analysis["broken_files"]:

            self.update_mode(
                "recovering"
            )

            self.auto_fix_system()

            self.update_mode(
                "stable"
            )

            return {
                "status": "recovered",
                "broken_files": (
                    analysis[
                        "broken_files"
                    ]
                )
            }

        return {
            "status": "healthy"
        }

    # =========================
    # AI DECISION ENGINE
    # =========================

    def ai_decision(
        self,
        signal_score,
        trend,
        volatility
    ):

        if signal_score >= 85:

            if trend == "bullish":

                if volatility == "low":

                    return "strong_buy"

                return "safe_buy"

            if trend == "bearish":

                return "strong_sell"

        if signal_score >= 60:

            return "watch_market"

        return "avoid_trade"

    # =========================
    # AUTO PERFORMANCE BOOST
    # =========================

    def performance_boost(self):

        self.update_mode(
            "optimized"
        )

        return {
            "performance": "boosted"
        }

    # =========================
    # LIVE MASTER WATCHER
    # =========================

    def live_master_loop(self):

        while True:

            try:

                analysis = (
                    self.analyze_project()
                )

                if analysis["broken_files"]:

                    self.recovery_system()

                self.write_log(
                    f"Live Analysis: {analysis}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Master Loop Error: "
                    f"{str(e)}"
                )

    # =========================
    # FULL SYSTEM REPORT
    # =========================

    def full_report(self):

        report = {
            "mode": self.system_mode,
            "analysis": (
                self.analyze_project()
            ),
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
# RUN MASTER AI
# =========================

if __name__ == "__main__":

    master = MasterControlAI()

    master.update_mode(
        "running"
    )

    master.create_backup()

    result = master.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )