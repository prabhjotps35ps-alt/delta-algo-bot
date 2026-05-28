import time
import traceback
from datetime import datetime

from quantum_execution_hub import (
    QuantumExecutionHub
)

from institutional_risk_firewall import (
    InstitutionalRiskFirewall
)

from adaptive_position_controller import (
    AdaptivePositionController
)

from ai_learning_engine import (
    AILearningEngine
)

from market_data_feed import (
    MarketDataFeed
)


class OmegaSentinelAI:

    def __init__(self):

        # =========================
        # CORE SYSTEMS
        # =========================

        self.execution_hub = (
            QuantumExecutionHub()
        )

        self.firewall = (
            InstitutionalRiskFirewall()
        )

        self.position_controller = (
            AdaptivePositionController()
        )

        self.ai_learning = (
            AILearningEngine()
        )

        self.market = (
            MarketDataFeed()
        )

        # =========================
        # SYSTEM SETTINGS
        # =========================

        self.system_mode = (
            "OMEGA_SENTINEL"
        )

        self.symbol = "BTC/USDT"

        self.active = True

        # =========================
        # AI INTELLIGENCE MEMORY
        # =========================

        self.market_regime = (
            "neutral"
        )

        self.volatility_state = (
            "medium"
        )

        self.last_market_price = 0

        self.market_health_score = 100

        # =========================
        # PERFORMANCE MEMORY
        # =========================

        self.total_cycles = 0

        self.emergency_events = 0

        self.successful_cycles = 0

    # =========================
    # MARKET REGIME DETECTION
    # =========================

    def market_regime_detection(self):

        try:

            ticker = (
                self.market.fetch_ticker(
                    self.symbol
                )
            )

            current_price = (
                ticker["last"]
            )

            if self.last_market_price == 0:

                self.last_market_price = (
                    current_price
                )

                return "neutral"

            movement = abs(

                (
                    current_price
                    - self.last_market_price
                )

                / self.last_market_price

            ) * 100

            self.last_market_price = (
                current_price
            )

            # =========================
            # VOLATILITY CLASSIFICATION
            # =========================

            if movement >= 2:

                self.volatility_state = (
                    "high"
                )

            elif movement >= 1:

                self.volatility_state = (
                    "medium"
                )

            else:

                self.volatility_state = (
                    "low"
                )

            # =========================
            # MARKET REGIME
            # =========================

            if movement >= 1.5:

                self.market_regime = (
                    "trending"
                )

            else:

                self.market_regime = (
                    "sideways"
                )

            return self.market_regime

        except Exception as e:

            traceback.print_exc()

            return "unknown"

    # =========================
    # MARKET HEALTH ENGINE
    # =========================

    def market_health_engine(self):

        score = 100

        # =========================
        # VOLATILITY PENALTY
        # =========================

        if self.volatility_state == "high":

            score -= 30

        elif self.volatility_state == "medium":

            score -= 10

        # =========================
        # FIREWALL CHECK
        # =========================

        firewall = (
            self.firewall.firewall_status()
        )

        if firewall["pause_trading"]:

            score -= 50

        self.market_health_score = (
            max(score, 0)
        )

        return self.market_health_score

    # =========================
    # EMERGENCY DEFENSE
    # =========================

    def emergency_defense_system(self):

        # =========================
        # CRITICAL HEALTH
        # =========================

        if self.market_health_score <= 40:

            self.firewall.emergency_shutdown()

            self.emergency_events += 1

            print(
                "Emergency Defense Activated"
            )

            return True

        return False

    # =========================
    # AI ADAPTIVE ENGINE
    # =========================

    def ai_adaptive_engine(self):

        report = (
            self.execution_hub
            .status_report()
        )

        # =========================
        # LOSS STREAK DEFENSE
        # =========================

        if report["loss_streak"] >= 3:

            self.firewall.pause_trading = (
                True
            )

            print(
                "Loss Streak Protection"
            )

        # =========================
        # WIN STREAK BOOST
        # =========================

        if report["win_streak"] >= 3:

            self.position_controller.max_risk_percent = (
                4.0
            )

        else:

            self.position_controller.max_risk_percent = (
                3.0
            )

    # =========================
    # GLOBAL STATUS REPORT
    # =========================

    def global_status_report(self):

        return {

            "mode":
            self.system_mode,

            "market_regime":
            self.market_regime,

            "volatility":
            self.volatility_state,

            "market_health":
            self.market_health_score,

            "total_cycles":
            self.total_cycles,

            "emergency_events":
            self.emergency_events,

            "successful_cycles":
            self.successful_cycles,

            "execution_hub":
            self.execution_hub
            .status_report()

        }

    # =========================
    # LIVE SENTINEL LOOP
    # =========================

    def live_sentinel_loop(self):

        print(
            "Omega Sentinel AI Started"
        )

        self.execution_hub.start_stream_engine()

        while self.active:

            try:

                self.total_cycles += 1

                # =========================
                # MARKET DETECTION
                # =========================

                self.market_regime_detection()

                # =========================
                # HEALTH ENGINE
                # =========================

                self.market_health_engine()

                # =========================
                # EMERGENCY DEFENSE
                # =========================

                emergency = (
                    self.emergency_defense_system()
                )

                if emergency:

                    time.sleep(30)

                    continue

                # =========================
                # ADAPTIVE AI
                # =========================

                self.ai_adaptive_engine()

                # =========================
                # EXECUTION LOOP
                # =========================

                self.execution_hub.live_execution_loop()

                self.successful_cycles += 1

                # =========================
                # STATUS REPORT
                # =========================

                print(
                    self.global_status_report()
                )

                time.sleep(10)

            except Exception as e:

                traceback.print_exc()

                print(
                    "Sentinel Error:",
                    str(e)
                )

                time.sleep(5)


if __name__ == "__main__":

    sentinel = (
        OmegaSentinelAI()
    )

    sentinel.live_sentinel_loop()