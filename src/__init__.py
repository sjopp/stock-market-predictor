import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages


def find_mac_d(stock, start_date, end_date):
    json_data = retrieve_and_convert.get_stock_data(stock, start_date, end_date)
    stock_dataframe = retrieve_and_convert.convert_to_dataframe(json_data)
    exponential_moving_averages_12_day = moving_averages.get_exponential_moving_averages(stock_dataframe, 12)
    exponential_moving_averages_26_day = moving_averages.get_exponential_moving_averages(stock_dataframe, 26)
    moving_averages.plot_mac_d(stock_dataframe, exponential_moving_averages_12_day,
                               exponential_moving_averages_26_day)


if __name__ == '__main__':
    pass
