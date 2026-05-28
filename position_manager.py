from config import (
    MAX_OPEN_TRADES
)

from delta_client import DeltaClient


delta = DeltaClient()


class PositionManager:

    # =========================
    # CHECK OPEN POSITION
    # =========================

    def has_open_position(
        self,
        symbol
    ):

        try:

            positions = delta.get_positions()

            if not positions:
                return False

            result = positions.get(
                "result",
                []
            )

            for pos in result:

                if pos.get(
                    "product_symbol"
                ) == symbol:

                    size = abs(
                        float(
                            pos.get(
                                "size",
                                0
                            )
                        )
                    )

                    if size > 0:
                        return True

            return False

        except Exception:
            return False

    # =========================
    # GET OPEN POSITIONS
    # =========================

    def get_open_positions(self):

        try:

            positions = delta.get_positions()

            if not positions:
                return []

            return positions.get(
                "result",
                []
            )

        except Exception:
            return []

    # =========================
    # TOTAL OPEN TRADES
    # =========================

    def total_open_positions(self):

        try:

            positions = self.get_open_positions()

            active_positions = 0

            for pos in positions:

                size = abs(
                    float(
                        pos.get(
                            "size",
                            0
                        )
                    )
                )

                if size > 0:
                    active_positions += 1

            return active_positions

        except Exception:
            return 0

    # =========================
    # CHECK TRADE LIMIT
    # =========================

    def can_open_new_trade(self):

        active_positions = (
            self.total_open_positions()
        )

        return (
            active_positions
            < MAX_OPEN_TRADES
        )

    # =========================
    # GET POSITION DETAILS
    # =========================

    def get_position_details(
        self,
        symbol
    ):

        try:

            positions = self.get_open_positions()

            for pos in positions:

                if pos.get(
                    "product_symbol"
                ) == symbol:

                    return {
                        "symbol": symbol,
                        "size": float(
                            pos.get(
                                "size",
                                0
                            )
                        ),
                        "entry_price": float(
                            pos.get(
                                "entry_price",
                                0
                            )
                        ),
                        "unrealized_pnl": float(
                            pos.get(
                                "unrealized_pnl",
                                0
                            )
                        ),
                        "liquidation_price": float(
                            pos.get(
                                "liquidation_price",
                                0
                            )
                        )
                    }

            return None

        except Exception:
            return None

    # =========================
    # CHECK DUPLICATE POSITION
    # =========================

    def duplicate_position_check(
        self,
        symbol,
        side
    ):

        try:

            positions = self.get_open_positions()

            for pos in positions:

                if pos.get(
                    "product_symbol"
                ) == symbol: