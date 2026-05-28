import json
import os


class AILearningEngine:

    def __init__(self):

        self.memory_file = (
            "ai_learning_memory.json"
        )

        self.memory = []

        self.load_memory()

    # =========================
    # LOAD MEMORY
    # =========================

    def load_memory(self):

        if not os.path.exists(
            self.memory_file
        ):

            with open(
                self.memory_file,
                "w"
            ) as file:

                json.dump([], file)

        with open(
            self.memory_file,
            "r"
        ) as file:

            self.memory = json.load(
                file
            )

    # =========================
    # SAVE MEMORY
    # =========================

    def save_memory(self):

        with open(
            self.memory_file,
            "w"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4
            )

    # =========================
    # LEARN TRADE
    # =========================

    def learn_trade(
        self,
        trade
    ):

        self.memory.append(
            trade
        )

        self.save_memory()

    # =========================
    # WIN RATE
    # =========================

    def calculate_winrate(self):

        if len(self.memory) == 0:

            return 0

        wins = 0

        for trade in self.memory:

            if trade.get(
                "profit",
                0
            ) > 0:

                wins += 1

        return round(

            (wins / len(self.memory)) * 100,

            2

        )