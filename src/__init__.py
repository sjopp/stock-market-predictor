import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages


def plot_data(stock, start_date, end_date, window):
    json_data = retrieve_and_convert.get_stock_data(stock, start_date, end_date)
    stock_dataframe = retrieve_and_convert.convert_to_dataframe(json_data)
    simple_moving_averages = moving_averages.return_moving_average(stock_dataframe, window)
    moving_averages.plot_moving_averages_against_stock_price(stock_dataframe, simple_moving_averages)


if __name__ == '__main__':
    pass
