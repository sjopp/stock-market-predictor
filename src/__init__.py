import requests


def get_stock_data(stock_symbol, start_date, end_date):
    url = f'https://api.tiingo.com/tiingo/daily/{stock_symbol}/prices?'
    params = {
        'startDate': start_date,
        'endDate': end_date
    }
    return requests.get(url, params).content
