import asyncio
from datetime import datetime


class AsyncCore:

    def __init__(self):

        self.running = True

    # =========================
    # TASK 1
    # =========================

    async def market_monitor(self):

        while self.running:

            print(
                f"[{datetime.now()}] "
                f"Market monitor active"
            )

            await asyncio.sleep(5)

    # =========================
    # TASK 2
    # =========================

    async def trade_executor(self):

        while self.running:

            print(
                f"[{datetime.now()}] "
                f"Trade executor active"
            )

            await asyncio.sleep(5)

    # =========================
    # TASK 3
    # =========================

    async def risk_engine(self):

        while self.running:

            print(
                f"[{datetime.now()}] "
                f"Risk engine active"
            )

            await asyncio.sleep(5)

    # =========================
    # RUN ALL TASKS
    # =========================

    async def run_all_tasks(self):

        await asyncio.gather(

            self.market_monitor(),

            self.trade_executor(),

            self.risk_engine()

        )


if __name__ == "__main__":

    core = AsyncCore()

    asyncio.run(
        core.run_all_tasks()
    )