from delta_client import DeltaClient

delta = DeltaClient()


class PositionManager:
    def has_open_position(self, symbol):
        try:
            positions = delta.get_positions()

            if not positions:
                return False

            result = positions.get("result", [])

            for pos in result:
                if pos.get("product_symbol") == symbol:
                    size = abs(float(pos.get("size", 0)))
                    if size > 0:
                        return True

            return False

        except Exception:
            return False
from delta_client import DeltaClient

delta = DeltaClient()

class PositionManager:
    def has_open_position(self, symbol):
        try:
            positions = delta.get_positions()

            if not positions:
                return False

            result = positions.get("result", [])

            for pos in result:
                if pos.get("product_symbol") == symbol:
                    size = abs(float(pos.get("size", 0)))
                    if size > 0:
                        return True

            return False

        except Exception:
            return False