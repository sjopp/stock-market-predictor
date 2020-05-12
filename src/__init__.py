import requests


def get_stock_data(stock_symbol):
    url = f'https://api.tiingo.com/tiingo/daily/{stock_symbol}/prices'
    return requests.get(url).content
