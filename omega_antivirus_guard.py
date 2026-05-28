import os
import hashlib
import traceback
from datetime import datetime


class OmegaAntivirusGuard:

    def __init__(self):

        # =========================
        # SECURITY SETTINGS
        # =========================

        self.quarantine_folder = (
            "quarantine"
        )

        self.suspicious_patterns = [

            "os.system(",

            "subprocess.Popen",

            "eval(",

            "exec(",

            "rm -rf",

            "shutdown",

            "forkbomb",

            "socket.connect",

            "pickle.loads",

            "__import__"

        ]

        self.safe_extensions = [

            ".py",

            ".json",

            ".txt",

            ".yml",

            ".yaml",

            ".env"

        ]

        self.scan_reports = []

        self.ensure_quarantine()

    # =========================
    # CREATE QUARANTINE
    # =========================

    def ensure_quarantine(self):

        if not os.path.exists(
            self.quarantine_folder
        ):

            os.makedirs(
                self.quarantine_folder
            )

    # =========================
    # FILE HASH
    # =========================

    def file_hash(
        self,
        filepath
    ):

        try:

            sha256 = hashlib.sha256()

            with open(
                filepath,
                "rb"
            ) as file:

                while True:

                    chunk = file.read(4096)

                    if not chunk:

                        break

                    sha256.update(chunk)

            return sha256.hexdigest()

        except Exception:

            return None

    # =========================
    # FILE SCANNER
    # =========================

    def file_scanner(
        self,
        filepath
    ):

        try:

            suspicious = []

            with open(
                filepath,
                "r",
                errors="ignore"
            ) as file:

                content = file.read()

            for pattern in (
                self.suspicious_patterns
            ):

                if pattern in content:

                    suspicious.append(
                        pattern
                    )

            return suspicious

        except Exception as e:

            traceback.print_exc()

            return [str(e)]

    # =========================
    # QUARANTINE FILE
    # =========================

    def quarantine_file(
        self,
        filepath
    ):

        try:

            filename = os.path.basename(
                filepath
            )

            destination = (

                f"{self.quarantine_folder}/"

                f"{filename}"

            )

            with open(
                filepath,
                "rb"
            ) as source:

                data = source.read()

            with open(
                destination,
                "wb"
            ) as target:

                target.write(data)

            os.remove(filepath)

            return {

                "status":
                "quarantined",

                "file":
                filename

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
    # FULL SYSTEM SCAN
    # =========================

    def full_system_scan(self):

        report = {

            "safe_files": [],

            "infected_files": []

        }

        try:

            for root, dirs, files in os.walk("."):

                for file in files:

                    extension = os.path.splitext(
                        file
                    )[1]

                    if extension not in (
                        self.safe_extensions
                    ):

                        continue

                    filepath = os.path.join(
                        root,
                        file
                    )

                    suspicious = (
                        self.file_scanner(
                            filepath
                        )
                    )

                    if suspicious:

                        quarantine = (
                            self.quarantine_file(
                                filepath
                            )
                        )

                        report[
                            "infected_files"
                        ].append({

                            "file":
                            filepath,

                            "patterns":
                            suspicious,

                            "action":
                            quarantine

                        })

                    else:

                        report[
                            "safe_files"
                        ].append(
                            filepath
                        )

            self.scan_reports.append(
                report
            )

            return report

        except Exception as e:

            traceback.print_exc()

            return {

                "status":
                "scan_failed",

                "error":
                str(e)

            }

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "time":
            str(datetime.now()),

            "total_scans":
            len(self.scan_reports),

            "quarantine_folder":
            self.quarantine_folder

        }


if __name__ == "__main__":

    antivirus = (
        OmegaAntivirusGuard()
    )

    print(
        antivirus.full_system_scan()
    )