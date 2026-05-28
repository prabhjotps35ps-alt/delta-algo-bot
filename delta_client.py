import time
import hmac
import hashlib
import json
import requests

from config import (
    DELTA_API_KEY,
    DELTA_API_SECRET,
    DELTA_BASE_URL,
    REQUEST_TIMEOUT,
    MAX_API_RETRIES
)


class DeltaClient:

    def __init__(self):

        self.api_key = DELTA_API_KEY

        self.api_secret = DELTA_API_SECRET

    # =========================
    # SIGNATURE
    # =========================

    def _sign(
        self,
        payload,
        path,
        method,
        timestamp
    ):

        message = (
            method
            + timestamp
            + path
            + payload
        )

        return hmac.new(
            self.api_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    # =========================
    # HEADERS
    # =========================

    def _headers(
        self,
        payload,
        path,
        method
    ):

        timestamp = str(
            int(time.time())
        )

        signature = self._sign(
            payload,
            path,
            method,
            timestamp
        )

        return {
            "api-key": self.api_key,
            "timestamp": timestamp,
            "signature": signature,
            "Content-Type": "application/json"
        }

    # =========================
    # REQUEST WRAPPER
    # =========================

    def _request(
        self,
        method,
        path,
        payload=""
    ):

        headers = self._headers(
            payload,
            path,
            method
        )

        url = DELTA_BASE_URL + path

        for _ in range(MAX_API_RETRIES):

            try:

                if method == "GET":

                    response = requests.get(
                        url,
                        headers=headers,
                        timeout=REQUEST_TIMEOUT
                    )

                else:

                    response = requests.post(
                        url,
                        headers=headers,
                        data=payload,
                        timeout=REQUEST_TIMEOUT
                    )

                return response.json()

            except Exception:
                time.sleep(1)

        return {
            "success": False,
            "error": "API request failed"
        }

    # =========================
    # GET BALANCE
    # =========================

    def get_balance(self):

        path = "/v2/wallet/balances"

        return self._request(
            "GET",
            path
        )

    # =========================
    # GET POSITIONS
    # =========================

    def get_positions(self):

        path = "/v2/positions"

        return self._request(
            "GET",
            path
        )

    # =========================
    # GET TICKER
    # =========================

    def get_ticker(
        self,
        symbol
    ):

        path = f"/v2/tickers/{symbol}"

        return self._request(
            "GET",
            path
        )

    # =========================
    # PLACE MARKET ORDER
    # =========================

    def place_market_order(
        self,
        symbol,
        side,
        size,
        leverage=5
    ):

        path = "/v2/orders"

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "order_type": "market_order",
            "leverage": leverage
        })

        return self._request(
            "POST",
            path,
            payload
        )

    # =========================
    # PLACE LIMIT ORDER
    # =========================

    def place_limit_order(
        self,
        symbol,
        side,
        size,
        price,
        leverage=5
    ):

        path = "/v2/orders"

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "limit_price": price,
            "order_type": "limit_order",
            "leverage": leverage
        })

        return self._request(
            "POST",
            path,
            payload
        )

    # =========================
    # PLACE STOP LOSS
    # =========================

    def place_stop_loss(
        self,
        symbol,
        side,
        size,
        stop_price
    ):

        path = "/v2/orders"

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "stop_price": stop_price,
            "order_type": "stop_market_order"
        })

        return self._request(
            "POST",
            path,
            payload
        )

    # =========================
    # PLACE TAKE PROFIT
    # =========================

    def place_take_profit(
        self,
        symbol,
        side,
        size,
        target_price
    ):

        path = "/v2/orders"

        payload = json.dumps({
            "product_symbol": symbol,
            "size": size,
            "side": side,
            "limit_price": target_price,
            "order_type": "limit_order"
        })

        return self._request(
            "POST",
            path,
            payload
        )

    # =========================
    # CANCEL ORDER
    # =========================

    def cancel_order(
        self,
        order_id
    ):

        path = f"/v2/orders/{order_id}/cancel"

        return self._request(
            "POST",
            path
        )

    # =========================
    # GET OPEN ORDERS
    # =========================

    def get_open_orders(self):

        path = "/v2/orders"

        return self._request(
            "GET",
            path
        )

    # =========================
    # CLOSE POSITION
    # =========================

    def close_position(
        self,
        symbol
    ):

        positions = self.get_positions()

        result = positions.get(
            "result",
            []
        )

        for pos in result:

            if pos.get(
                "product_symbol"
            ) == symbol:

                size = abs(
                    float(
                        pos.get(
                            "size",
                            0
                        )
                    )
                )

                if size <= 0:
                    return {
                        "status": "no_position"
                    }

                side = (
                    "sell"
                    if float(
                        pos.get(
                            "size",
                            0
                        )
                    ) > 0
                    else "buy"
                )

                return self.place_market_order(
                    symbol=symbol,
                    side=side,
                    size=size
                )

        return {
            "status": "position_not_found"
        }