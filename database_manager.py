import sqlite3
from datetime import datetime


class DatabaseManager:

    def __init__(self):

        self.db_name = (
            "omega_trading.db"
        )

        self.connection = sqlite3.connect(
            self.db_name,
            check_same_thread=False
        )

        self.cursor = (
            self.connection.cursor()
        )

        self.create_tables()

    # =========================
    # CREATE TABLES
    # =========================

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS trades (

                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                side TEXT,
                entry REAL,
                quantity REAL,
                status TEXT,
                created_at TEXT

            )
            """
        )

        self.connection.commit()

    # =========================
    # SAVE TRADE
    # =========================

    def save_trade(
        self,
        symbol,
        side,
        entry,
        quantity,
        status
    ):

        self.cursor.execute(
            """
            INSERT INTO trades (

                symbol,
                side,
                entry,
                quantity,
                status,
                created_at

            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                symbol,
                side,
                entry,
                quantity,
                status,
                str(datetime.now())
            )
        )

        self.connection.commit()

    # =========================
    # GET ALL TRADES
    # =========================

    def get_all_trades(self):

        self.cursor.execute(
            "SELECT * FROM trades"
        )

        return self.cursor.fetchall()