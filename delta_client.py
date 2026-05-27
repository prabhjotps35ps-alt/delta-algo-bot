import time
import hmac
import hashlib
import json
import requests
from config import (
    DELTA_API_KEY,
    DELTA_API_SECRET,
    DELTA_BASE_URL,
    REQUEST_TIMEOUT
)


class DeltaClient:
    def __init__(self):
        self.api_key = DELTA_API_KEY
        self.api_secret = DELTA_API_SECRET

    def _sign(self, payload, path, method, timestamp):
        message = method + timestamp + path + payload
        return hmac.new(
            self.api_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def _headers(self, payload, path, method):
        timestamp = str(int(time.time()))
        signature = self._sign(payload, path, method, timestamp)

        return {
            "api-key": self.api_key,
            "timestamp": timestamp,
            "signature": signature,
            "Content-Type": "application/json"
        }

    def get_balance(self):
        path = "/v2/wallet/balances"
        method = "GET"
        payload = ""

        headers = self._headers(payload, path, method)

        response = requests.get(
            DELTA_BASE_URL + path,
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )

        return response.json()

    def place_market_order(self, symbol, side, size):
        path = "/v2/orders"
        method = "POST"

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "order_type": "market"
        })

        headers = self._headers(payload, path, method)

        response = requests.post(
            DELTA_BASE_URL + path,
            headers=headers,
            data=payload,
            timeout=REQUEST_TIMEOUT
        )

        return response.json()
def get_positions(self):
    path = "/v2/positions"
    method = "GET"
    payload = ""

    headers = self._headers(payload, path, method)

    response = requests.get(
        DELTA_BASE_URL + path,
        headers=headers,
        timeout=REQUEST_TIMEOUT
    )

    return response.json()