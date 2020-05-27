import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages
import pandas as pd
import numpy as np


def generate_mac_d_values(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    json_data = retrieve_and_convert.get_stock_data(stock, start_date, end_date)
    price_dataframe = retrieve_and_convert.convert_to_dataframe(json_data)
    fast_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, fast_moving_average)
    slow_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, slow_moving_average)
    return slow_moving_average_df.subtract(fast_moving_average_df)


def generate_mac_d_signal(mac_d_dataframe):
    signals = [np.float64(0)]
    for i in range(mac_d_dataframe.shape[0]):
        if i == 0:
            continue
        current_mac_d_value = mac_d_dataframe.iloc[i]['adjClose']
        previous_mac_d_value = mac_d_dataframe.iloc[i-1]['adjClose']
        if previous_mac_d_value < 0 and current_mac_d_value >= 0:
            signals.append(np.float64(-1))
        elif previous_mac_d_value >= 0 and current_mac_d_value < 0:
            signals.append(np.float64(1))
        else:
            signals.append(np.float64(0))

    mac_d_dataframe['signal'] = signals
    return mac_d_dataframe
