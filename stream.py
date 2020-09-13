from alpaca_trade_api import StreamConn
from alpaca_trade_api.common import URL
from keys import API_KEY, API_SECRET_KEY
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

conn = StreamConn(
    API_KEY,
    API_SECRET_KEY,
    base_url=URL('https://paper-api.alpaca.markets'),
    data_url=URL('https://data.alpaca.markets'),
    data_stream='alpacadatav1'
)


@conn.on(r'^AM\..+$')
async def on_minute_bars(conn, channel, bar):
    print('bars', bar)


quote_count = 0  # don't print too much quotes
@conn.on(r'Q\..+')
async def on_quotes(conn, channel, quote):
    global quote_count
    if quote_count % 10 == 0:
        print('bars', quote)
    quote_count += 1


@conn.on(r'T\..+')
async def on_trades(conn, channel, trade):
    print('trade', trade)
