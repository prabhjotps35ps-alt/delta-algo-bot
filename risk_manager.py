from config import (
    DEFAULT_STOP_LOSS_PERCENT,
    DEFAULT_TAKE_PROFIT_PERCENT,
    MIN_BALANCE_INR
)

class RiskManager:

    def calculate_sl_tp(self, entry_price, side):
        sl_percent = DEFAULT_STOP_LOSS_PERCENT / 100
        tp_percent = DEFAULT_TAKE_PROFIT_PERCENT / 100

        if side == "buy":
            stop_loss = entry_price * (1 - sl_percent)
            take_profit = entry_price * (1 + tp_percent)

        else:
            stop_loss = entry_price * (1 + sl_percent)
            take_profit = entry_price * (1 - tp_percent)

        return {
            "stop_loss": round(stop_loss, 2),
            "take_profit": round(take_profit, 2)
        }

    def calculate_position_size(self, balance):
        if balance < MIN_BALANCE_INR:
            return 0

        # simple scaling logic
        if balance <= 1000:
            return 1

        elif balance <= 2000:
            return 2

        elif balance <= 5000:
            return 3

        else:
            return 5