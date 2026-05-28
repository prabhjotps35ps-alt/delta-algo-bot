import time


class CooldownManager:

    def __init__(self):

        self.cooldown_until = 0

    def activate(
        self,
        seconds
    ):

        self.cooldown_until = (
            time.time()
            + seconds
        )

    def active(self):

        return (
            time.time()
            < self.cooldown_until
        )

    def remaining(self):

        return max(
            0,
            round(
                self.cooldown_until
                - time.time(),
                2
            )
        )