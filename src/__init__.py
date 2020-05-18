import requests
import pandas as pd


def get_stock_data(stock_symbol, start_date, end_date):
    url = f'https://api.tiingo.com/tiingo/daily/{stock_symbol}/prices?'
    params = {
        'token': '387fd657063535f02ef5a5700aadd0b9286572e9',
        'startDate': start_date,
        'endDate': end_date
    }
    response = requests.get(url, params)
    print(response.content)
    return response.json()


def convert_to_dataframe(json_data):
    dataframe = pd.DataFrame(json_data).set_index('date')
    return dataframe


if __name__ == '__main__':
    aapl_data = get_stock_data('AAPL', '2019-12-25', '2020-1-1')
    print(aapl_data)
    appl_dataframe = convert_to_dataframe(aapl_data)
    print(appl_dataframe)

