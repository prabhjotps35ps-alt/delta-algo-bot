import os
import json
import time
import shutil
import traceback
from datetime import datetime


class InfinityEngine:

    def __init__(self):

        self.infinity_log = (
            "infinity_engine_log.txt"
        )

        self.infinity_memory = (
            "infinity_memory.json"
        )

        self.snapshot_folder = (
            "infinity_snapshots"
        )

        self.engine_mode = (
            "booting"
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
            self.infinity_log,
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
                self.infinity_memory
            ):

                with open(
                    self.infinity_memory,
                    "w"
                ) as file:

                    json.dump({}, file)

            with open(
                self.infinity_memory,
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
            self.infinity_memory,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    # =========================
    # UPDATE MODE
    # =========================

    def update_mode(
        self,
        mode
    ):

        self.engine_mode = mode

        self.memory[
            "engine_mode"
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
    # SYSTEM SCANNER
    # =========================

    def scan_system(self):

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
                or file.endswith(".json")
            ):

                shutil.copy(
                    file,
                    snapshot_path
                )

        self.write_log(
            "Infinity snapshot created"
        )

        return snapshot_path

    # =========================
    # AUTO HEAL ENGINE
    # =========================

    def auto_heal_engine(self):

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
            "Auto healing completed"
        )

        return healed_files

    # =========================
    # SELF EVOLUTION
    # =========================

    def self_evolution(self):

        report = self.scan_system()

        if report["broken_files"]:

            self.update_mode(
                "self_repair"
            )

            self.auto_heal_engine()

            self.update_mode(
                "stable"
            )

            return {
                "status": "self_repaired",
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
    # MARKET INTELLIGENCE
    # =========================

    def market_intelligence(
        self,
        signal_score,
        trend,
        volatility,
        liquidity,
        volume
    ):

        if signal_score >= 90:

            if trend == "bullish":

                if (
                    volatility == "low"
                    and liquidity == "high"
                    and volume == "strong"
                ):

                    return "ultra_buy"

                return "safe_buy"

            if trend == "bearish":

                return "ultra_sell"

        if signal_score >= 70:

            return "watch_market"

        return "avoid_market"

    # =========================
    # RISK SHIELD
    # =========================

    def risk_shield(
        self,
        drawdown
    ):

        if drawdown >= 30:

            return {
                "shield_mode": "maximum_protection"
            }

        if drawdown >= 15:

            return {
                "shield_mode": "safe_protection"
            }

        return {
            "shield_mode": "normal"
        }

    # =========================
    # LIVE ENGINE LOOP
    # =========================

    def live_engine(self):

        while True:

            try:

                report = (
                    self.scan_system()
                )

                if report["broken_files"]:

                    self.self_evolution()

                self.write_log(
                    f"Infinity report: {report}"
                )

                time.sleep(60)

            except Exception as e:

                self.write_log(
                    f"Engine loop error: "
                    f"{str(e)}"
                )

    # =========================
    # FULL REPORT
    # =========================

    def full_report(self):

        report = {
            "engine_mode": (
                self.engine_mode
            ),
            "system_analysis": (
                self.scan_system()
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
# RUN INFINITY ENGINE
# =========================

if __name__ == "__main__":

    engine = InfinityEngine()

    engine.update_mode(
        "running"
    )

    engine.create_snapshot()

    result = engine.full_report()

    print(
        json.dumps(
            result,
            indent=4
        )
    )