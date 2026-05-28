import json
import os


class StateStore:

    def __init__(self):

        self.file_path = (
            "bot_state.json"
        )

        if not os.path.exists(
            self.file_path
        ):

            with open(
                self.file_path,
                "w"
            ) as file:

                json.dump({}, file)

    # =========================
    # LOAD STATE
    # =========================

    def load_state(self):

        try:

            with open(
                self.file_path,
                "r"
            ) as file:

                return json.load(file)

        except Exception:
            return {}

    # =========================
    # SAVE STATE
    # =========================

    def save_state(
        self,
        state
    ):

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                state,
                file,
                indent=4
            )

    # =========================
    # UPDATE STATE
    # =========================

    def update_state(
        self,
        key,
        value
    ):

        state = self.load_state()

        state[key] = value

        self.save_state(state)

        return True

    # =========================
    # GET VALUE
    # =========================

    def get_value(
        self,
        key,
        default=None
    ):

        state = self.load_state()

        return state.get(
            key,
            default
        )

    # =========================
    # CLEAR STATE
    # =========================

    def clear_state(self):

        self.save_state({})

        return True

    # =========================
    # STATE SNAPSHOT
    # =========================

    def snapshot(self):

        return self.load_state()