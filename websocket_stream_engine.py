import json
import websocket
import threading


class WebSocketStreamEngine:

    def __init__(self):

        self.ws_url = (
            "wss://socket.delta.exchange"
        )

        self.latest_price = None

    # =========================
    # MESSAGE HANDLER
    # =========================

    def on_message(
        self,
        ws,
        message
    ):

        data = json.loads(
            message
        )

        print(
            "Live Stream:",
            data
        )

        if "price" in str(data):

            self.latest_price = data

    # =========================
    # ERROR HANDLER
    # =========================

    def on_error(
        self,
        ws,
        error
    ):

        print(
            "WebSocket Error:",
            error
        )

    # =========================
    # CLOSE HANDLER
    # =========================

    def on_close(
        self,
        ws,
        close_status_code,
        close_msg
    ):

        print(
            "WebSocket Closed"
        )

    # =========================
    # OPEN HANDLER
    # =========================

    def on_open(
        self,
        ws
    ):

        payload = {

            "type": "subscribe",

            "payload": {

                "channels": [{
                    "name": "all_trades",
                    "symbols": [
                        "BTCUSDT"
                    ]
                }]
            }
        }

        ws.send(
            json.dumps(payload)
        )

    # =========================
    # START STREAM
    # =========================

    def start_stream(self):

        websocket.enableTrace(
            False
        )

        ws = websocket.WebSocketApp(

            self.ws_url,

            on_open=self.on_open,

            on_message=self.on_message,

            on_error=self.on_error,

            on_close=self.on_close

        )

        ws.run_forever()

    # =========================
    # BACKGROUND STREAM
    # =========================

    def start_background_stream(self):

        thread = threading.Thread(
            target=self.start_stream
        )

        thread.daemon = True

        thread.start()