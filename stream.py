from keys import API_KEY, API_SECRET_KEY
import websocket
import json


def on_open(ws):
    print("[CONNECTION OPENED]")
    auth_data = {
        "action": "authenticate",
        "data": {
            "key_id": API_KEY,
            "secret_key": API_SECRET_KEY
        }
    }

    ws.send(json.dumps(auth_data))

    trade_symbols = ["T.NFLX", "T.GE"]
    listen_message = {
        "action": "listen",
        "data": {
            "streams": trade_symbols
        }
    }

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    message = json.loads(message)
    print(message['data'])


def on_close(ws):
    print("[CONNECTION CLOSED]")


socket = "wss://data.alpaca.markets/stream"
alpaca_ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)

alpaca_ws.run_forever()
