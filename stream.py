import alpaca_trade_api as tradeapi
import threading
from keys import API_KEY, API_SECRET_KEY


conn = tradeapi.stream2.StreamConn(
    key_id=API_KEY,
    secret_key=API_SECRET_KEY,
    base_url='https://paper-api.alpaca.markets',
    data_url='wss://data.alpaca.markets/stream'
)


# @conn.on(r'.*')
# async def on_data(conn, channel, data):
#     print(data)

conn.run(['account_updates'])

