import time
from datetime import datetime


# =========================
# CURRENT TIMESTAMP
# =========================

def current_timestamp():

    return str(
        datetime.now()
    )


# =========================
# ROUND PRICE
# =========================

def round_price(
    price,
    digits=2
):

    return round(
        price,
        digits
    )


# =========================
# PERCENTAGE CHANGE
# =========================

def percentage_change(
    old_price,
    new_price
):

    try:

        return round(
            (
                (
                    new_price
                    - old_price
                )
                / old_price
            ) * 100,
            2
        )

    except Exception:
        return 0


# =========================
# SLEEP
# =========================

def wait(seconds):

    time.sleep(seconds)


# =========================
# SAFE DIVISION
# =========================

def safe_divide(
    a,
    b
):

    try:

        return a / b

    except Exception:
        return 0


# =========================
# BOOL TO STATUS
# =========================

def bool_status(value):

    return (
        "enabled"
        if value
        else "disabled"
    )


# =========================
# FORMAT PNL
# =========================

def format_pnl(
    pnl
):

    return f"{round(pnl, 2)}%"