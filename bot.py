import json
from stream import conn


class AlpacaTradingBot:
    def __init__(self, websocket, trade_symbols, strategy=None):
        self.websocket = websocket
        self.trade_symbols = trade_symbols
        self.strategy = strategy

    def start(self):
        self.websocket.run(self.trade_symbols)


if __name__ == '__main__':
    AlpacaTradingBot(conn, ['AM.AAPL']).start()
