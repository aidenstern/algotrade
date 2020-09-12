import alpaca_trade_api as tradeapi
from keys import API_KEY, API_SECRET_KEY

if __name__ == '__main__':
    api = tradeapi.REST(API_KEY, API_SECRET_KEY, base_url='https://paper-api.alpaca.markets')
    account = api.get_account()
    print(account)
    api.list_positions()
