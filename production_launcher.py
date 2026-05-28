import threading

from websocket_stream_engine import (
    WebSocketStreamEngine
)

from live_trade_manager import (
    LiveTradeManager
)

from apex_autonomous_core import (
    ApexAutonomousCore
)


class ProductionLauncher:

    def __init__(self):

        self.websocket_engine = (
            WebSocketStreamEngine()
        )

        self.trade_manager = (
            LiveTradeManager()
        )

        self.autonomous_core = (
            ApexAutonomousCore()
        )

    # =========================
    # START WEBSOCKET
    # =========================

    def start_websocket(self):

        self.websocket_engine.start_background_stream()

    # =========================
    # START LIVE TRADING
    # =========================

    def start_trading(self):

        self.trade_manager.start_live_trading()

    # =========================
    # START AI CORE
    # =========================

    def start_ai_core(self):

        self.autonomous_core.live_core_loop()

    # =========================
    # START ALL SYSTEMS
    # =========================

    def start_all_systems(self):

        websocket_thread = threading.Thread(
            target=self.start_websocket
        )

        trading_thread = threading.Thread(
            target=self.start_trading
        )

        ai_thread = threading.Thread(
            target=self.start_ai_core
        )

        websocket_thread.start()

        trading_thread.start()

        ai_thread.start()

        websocket_thread.join()

        trading_thread.join()

        ai_thread.join()


if __name__ == "__main__":

    launcher = (
        ProductionLauncher()
    )

    launcher.start_all_systems()