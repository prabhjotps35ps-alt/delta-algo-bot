import os

# =========================
# DELTA API CONFIG
# =========================

DELTA_API_KEY = os.getenv(
    "DELTA_API_KEY"
)

DELTA_API_SECRET = os.getenv(
    "DELTA_API_SECRET"
)

DELTA_BASE_URL = (
    "https://api.delta.exchange"
)

# =========================
# WEBHOOK SECURITY
# =========================

WEBHOOK_SECRET = os.getenv(
    "WEBHOOK_SECRET",
    "change_this_secret"
)

# =========================
# RISK MANAGEMENT
# =========================

MIN_BALANCE_INR = 1000

MAX_RISK_PER_TRADE = 2

MAX_DAILY_LOSS_PERCENT = 10

MAX_DRAWDOWN_PERCENT = 20

MAX_CONSECUTIVE_LOSSES = 3

# =========================
# LEVERAGE SETTINGS
# =========================

MIN_LEVERAGE = 5

MAX_LEVERAGE = 10

DEFAULT_LEVERAGE = 5

# =========================
# STOP LOSS SETTINGS
# =========================

DEFAULT_STOP_LOSS_PERCENT = 2.0

TRAILING_STOP_PERCENT = 1.0

BREAK_EVEN_TRIGGER_PERCENT = 1.5

# =========================
# TARGET SETTINGS
# =========================

DEFAULT_TAKE_PROFIT_PERCENT = 2.0

EXTENDED_TARGET_PERCENT = 5.0

PARTIAL_BOOK_PERCENT = 50

# =========================
# SIGNAL SETTINGS
# =========================

MIN_SIGNAL_SCORE = 70

STRONG_SIGNAL_SCORE = 85

# =========================
# VOLATILITY FILTER
# =========================

MAX_ALLOWED_VOLATILITY = 5

MIN_VOLUME_THRESHOLD = 100000

# =========================
# ORDERBOOK FILTER
# =========================

MIN_ORDERBOOK_IMBALANCE = 1.2

# =========================
# CONNECTIVITY
# =========================

REQUEST_TIMEOUT = 10

MAX_API_RETRIES = 3

HEARTBEAT_INTERVAL = 30

# =========================
# MARKET SETTINGS
# =========================

DEFAULT_TIMEFRAME = "1m"

HIGHER_TIMEFRAME = "5m"

TREND_TIMEFRAME = "15m"

# =========================
# TRADE SETTINGS
# =========================

MAX_OPEN_TRADES = 1

ALLOW_SCALPING = True

ALLOW_SHORTS = True

ALLOW_LONGS = True

# =========================
# EMERGENCY RULES
# =========================

ENABLE_EMERGENCY_EXIT = True

ENABLE_AUTO_RECOVERY = True

ENABLE_AUTO_RECONNECT = True

ENABLE_COOLDOWN_MODE = True

# =========================
# TELEGRAM ALERTS
# =========================

ENABLE_TELEGRAM_ALERTS = False

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID"
)

# =========================
# LOGGING
# =========================

ENABLE_TRADE_LOGGING = True

ENABLE_ERROR_LOGGING = True

ENABLE_JOURNAL = True

# =========================
# FUND MANAGEMENT
# =========================

ENABLE_AUTO_COMPOUNDING = True

CAPITAL_PRESERVATION_MODE = True

SAFE_MODE_TRIGGER_PERCENT = 15

# =========================
# SYSTEM MODES
# =========================

ENABLE_PAPER_TRADING = False

ENABLE_LIVE_TRADING = True

SYSTEM_NAME = (
    "Institutional Adaptive Trading Engine"
)