import time
import traceback
from datetime import datetime

from neural_trade_commander import (
    NeuralTradeCommander
)

from websocket_stream_engine import (
    WebSocketStreamEngine
)

from institutional_risk_firewall import (
    InstitutionalRiskFirewall
)

from adaptive_position_controller import (
    AdaptivePositionController
)

from auto_trade_guardian import (
    AutoTradeGuardian
)

from ai_learning_engine import (
    AILearningEngine
)


class QuantumExecutionHub:

    def __init__(self):

        # =========================
        # CORE SYSTEMS
        # =========================

        self.commander = (
            NeuralTradeCommander()
        )

        self.websocket_engine = (
            WebSocketStreamEngine()
        )

        self.firewall = (
            InstitutionalRiskFirewall()
        )

        self.position_controller = (
            AdaptivePositionController()
        )

        self.guardian = (
            AutoTradeGuardian()
        )

        self.ai_learning = (
            AILearningEngine()
        )

        # =========================
        # EXECUTION SETTINGS
        # =========================

        self.execution_mode = (
            "LIVE_PRODUCTION"
        )

        self.active = True

        self.trade_counter = 0

        self.last_trade_time = 0

        self.cooldown_seconds = 30

        # =========================
        # AI PERFORMANCE MEMORY
        # =========================

        self.total_profit = 0

        self.total_loss = 0

        self.win_streak = 0

        self.loss_streak = 0

    # =========================
    # START LIVE STREAM
    # =========================

    def start_stream_engine(self):

        try:

            self.websocket_engine.start_background_stream()

            print(
                "WebSocket Stream Started"
            )

        except Exception as e:

            print(
                "Stream Error:",
                str(e)
            )

    # =========================
    # AI EXECUTION FILTER
    # =========================

    def ai_execution_filter(
        self,
        signal_data
    ):

        signal = (
            signal_data["signal"]
        )

        confidence = (
            signal_data["confidence"]
        )

        # =========================
        # BASIC FILTER
        # =========================

        if signal == "wait":

            return False

        if confidence < 85:

            return False

        # =========================
        # FIREWALL FILTER
        # =========================

        validation = (
            self.firewall.validate_trade(

                leverage=3,

                position_size=1

            )
        )

        if not validation["allowed"]:

            print(
                "Firewall Block:",
                validation["reason"]
            )

            return False

        return True

    # =========================
    # TRADE EXECUTION ENGINE
    # =========================

    def trade_execution_engine(
        self,
        signal_data
    ):

        try:

            current_time = time.time()

            # =========================
            # COOLDOWN SYSTEM
            # =========================

            if (

                current_time
                - self.last_trade_time

            ) < self.cooldown_seconds:

                print(
                    "Cooldown Active"
                )

                return

            # =========================
            # EXECUTE TRADE
            # =========================

            self.commander.execute_trade(
                signal_data
            )

            self.last_trade_time = (
                current_time
            )

            self.trade_counter += 1

            print(
                f"Trade Count: "
                f"{self.trade_counter}"
            )

        except Exception as e:

            traceback.print_exc()

            print(
                "Execution Engine Error:",
                str(e)
            )

    # =========================
    # AI LEARNING UPDATE
    # =========================

    def ai_learning_update(
        self,
        profit
    ):

        trade_data = {

            "profit": profit,

            "time": str(
                datetime.now()
            )

        }

        self.ai_learning.learn_trade(
            trade_data
        )

        # =========================
        # WIN TRACKING
        # =========================

        if profit > 0:

            self.total_profit += profit

            self.win_streak += 1

            self.loss_streak = 0

        else:

            self.total_loss += abs(
                profit
            )

            self.loss_streak += 1

            self.win_streak = 0

    # =========================
    # STATUS REPORT
    # =========================

    def status_report(self):

        return {

            "mode":
            self.execution_mode,

            "active":
            self.active,

            "trade_counter":
            self.trade_counter,

            "total_profit":
            self.total_profit,

            "total_loss":
            self.total_loss,

            "win_streak":
            self.win_streak,

            "loss_streak":
            self.loss_streak,

            "winrate":
            self.ai_learning
            .calculate_winrate()

        }

    # =========================
    # LIVE EXECUTION LOOP
    # =========================

    def live_execution_loop(self):

        self.start_stream_engine()

        while self.active:

            try:

                # =========================
                # TRACK ACTIVE POSITION
                # =========================

                self.guardian.live_trade_tracker()

                # =========================
                # MARKET ANALYSIS
                # =========================

                analysis = (
                    self.commander
                    .market_analysis()
                )

                signal_data = (
                    self.commander
                    .ai_signal_engine(
                        analysis
                    )
                )

                print(

                    f"[{datetime.now()}] "

                    f"Signal: "

                    f"{signal_data['signal']} "

                    f"| Confidence: "

                    f"{signal_data['confidence']}"

                )

                # =========================
                # EXECUTION FILTER
                # =========================

                approved = (
                    self.ai_execution_filter(
                        signal_data
                    )
                )

                # =========================
                # EXECUTE TRADE
                # =========================

                if (

                    approved

                    and

                    not self.guardian
                    .active_trade

                ):

                    self.trade_execution_engine(
                        signal_data
                    )

                # =========================
                # STATUS OUTPUT
                # =========================

                print(
                    self.status_report()
                )

                time.sleep(15)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Hub Error:",
                    str(e)
                )

                time.sleep(5)


if __name__ == "__main__":

    hub = (
        QuantumExecutionHub()
    )

    hub.live_execution_loop()