import requests

from config import (
    ENABLE_TELEGRAM_ALERTS,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)


class Notifier:

    # =========================
    # SEND TELEGRAM MESSAGE
    # =========================

    def send_message(
        self,
        message
    ):

        try:

            if not ENABLE_TELEGRAM_ALERTS:
                return {
                    "success": False,
                    "message": "Telegram alerts disabled"
                }

            url = (
                f"https://api.telegram.org/bot"
                f"{TELEGRAM_BOT_TOKEN}"
                f"/sendMessage"
            )

            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            }

            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

            return {
                "success": True,
                "response": response.json()
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # TRADE ALERT
    # =========================

    def send_trade_alert(
        self,
        symbol,
        side,
        size,
        leverage
    ):

        message = (
            f"🚀 Trade Executed\n\n"
            f"Symbol: {symbol}\n"
            f"Side: {side}\n"
            f"Size: {size}\n"
            f"Leverage: {leverage}x"
        )

        return self.send_message(
            message
        )

    # =========================
    # PROFIT ALERT
    # =========================

    def send_profit_alert(
        self,
        symbol,
        pnl
    ):

        message = (
            f"💰 Profit Update\n\n"
            f"Symbol: {symbol}\n"
            f"PnL: {pnl}%"
        )

        return self.send_message(
            message
        )

    # =========================
    # LOSS ALERT
    # =========================

    def send_loss_alert(
        self,
        symbol,
        pnl
    ):

        message = (
            f"⚠️ Loss Alert\n\n"
            f"Symbol: {symbol}\n"
            f"PnL: {pnl}%"
        )

        return self.send_message(
            message
        )

    # =========================
    # EMERGENCY ALERT
    # =========================

    def send_emergency_alert(
        self,
        reason
    ):

        message = (
            f"🚨 Emergency Alert\n\n"
            f"Reason: {reason}"
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
            f"🖥️ System Status\n\n"
            f"Status: {status}"
        )

        return self.send_message(
            message
        )

    # =========================
    # DAILY REPORT
    # =========================

    def send_daily_report(
        self,
        total_trades,
        total_profit,
        win_rate
    ):

        message = (
            f"📊 Daily Trading Report\n\n"
            f"Trades: {total_trades}\n"
            f"Profit: {total_profit}\n"
            f"Win Rate: {win_rate}%"
        )

        return self.send_message(
            message
        )