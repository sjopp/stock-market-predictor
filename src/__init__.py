import requests


def get_stock_data(stock_symbol, start_date, end_date):
    url = f'https://api.tiingo.com/tiingo/daily/{stock_symbol}/prices?'
    params = {
        'token': '387fd657063535f02ef5a5700aadd0b9286572e9',
        'startDate': start_date,
        'endDate': end_date
    }
    return requests.get(url, params).content


if __name__ == '__main__':
    aapl_data = get_stock_data('AAPL', '2019-12-25', '2020-1-1')
    print(aapl_data)

