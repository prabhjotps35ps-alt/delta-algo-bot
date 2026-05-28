import requests
import traceback
from datetime import datetime


class TelegramAlertEngine:

    def __init__(self):

        # =========================
        # TELEGRAM SETTINGS
        # =========================

        self.bot_token = (
            "YOUR_BOT_TOKEN"
        )

        self.chat_id = (
            "YOUR_CHAT_ID"
        )

        self.base_url = (

            f"https://api.telegram.org/bot"

            f"{self.bot_token}"

        )

    # =========================
    # SEND MESSAGE
    # =========================

    def send_message(
        self,
        message
    ):

        try:

            url = (
                f"{self.base_url}"
                f"/sendMessage"
            )

            payload = {

                "chat_id":
                self.chat_id,

                "text":
                message

            }

            response = requests.post(

                url,

                json=payload,

                timeout=10

            )

            return response.json()

        except Exception as e:

            traceback.print_exc()

            return {

                "success":
                False,

                "error":
                str(e)

            }

    # =========================
    # ENTRY ALERT
    # =========================

    def send_entry_alert(
        self,
        symbol,
        side,
        entry,
        confidence
    ):

        message = (

            f"🚀 TRADE ENTRY\n\n"

            f"Symbol: {symbol}\n"

            f"Side: {side}\n"

            f"Entry: {entry}\n"

            f"Confidence: {confidence}%\n"

            f"Time: {datetime.now()}"

        )

        return self.send_message(
            message
        )

    # =========================
    # EXIT ALERT
    # =========================

    def send_exit_alert(
        self,
        symbol,
        pnl,
        reason
    ):

        message = (

            f"✅ TRADE EXIT\n\n"

            f"Symbol: {symbol}\n"

            f"PNL: {pnl}%\n"

            f"Reason: {reason}\n"

            f"Time: {datetime.now()}"

        )

        return self.send_message(
            message
        )

    # =========================
    # EMERGENCY ALERT
    # =========================

    def send_emergency_alert(
        self,
        message_text
    ):

        message = (

            f"⚠️ EMERGENCY ALERT\n\n"

            f"{message_text}\n\n"

            f"Time: {datetime.now()}"

        )

        return self.send_message(
            message
        )

    # =========================
    # SYSTEM STATUS ALERT
    # =========================

    def send_system_status(
        self,
        status
    ):

        message = (

            f"🧠 SYSTEM STATUS\n\n"

            f"Status: {status}\n"

            f"Time: {datetime.now()}"

        )

        return self.send_message(
            message
        )


if __name__ == "__main__":

    telegram = (
        TelegramAlertEngine()
    )

    print(

        telegram.send_system_status(
            "OMEGA AI ACTIVE"
        )

    )