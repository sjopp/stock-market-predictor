import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages


def generate_mac_d_values(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    json_data = retrieve_and_convert.get_stock_data(stock, start_date, end_date)
    price_dataframe = retrieve_and_convert.convert_to_dataframe(json_data)
    fast_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, fast_moving_average)
    slow_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, slow_moving_average)
    return slow_moving_average_df.subtract(fast_moving_average_df)


def determine_mac_d_signal(mac_d_dataframe):
    print(mac_d_dataframe.iloc[1])
