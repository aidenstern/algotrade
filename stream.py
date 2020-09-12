import alpaca_trade_api as tradeapi
from keys import API_KEY, API_SECRET_KEY

if __name__ == '__main__':
    api = tradeapi.REST(API_KEY, API_SECRET_KEY, base_url='https://paper-api.alpaca.markets')

    # Get daily price data for AAPL over the last 5 trading days.
    barset = api.get_barset('AAPL', 'day', limit=5)
    aapl_bars = barset['AAPL']

    print(aapl_bars)
