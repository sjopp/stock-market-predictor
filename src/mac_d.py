import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages
import pandas as pd


def generate_mac_d_values(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    json_data = retrieve_and_convert.get_stock_data(stock, start_date, end_date)
    price_dataframe = retrieve_and_convert.convert_to_dataframe(json_data)
    fast_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, fast_moving_average)
    slow_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, slow_moving_average)
    return slow_moving_average_df.subtract(fast_moving_average_df)


def generate_mac_d_signal(mac_d_dataframe):
    for i in range(mac_d_dataframe.shape[0]):
        if i == 0:
            mac_d_dataframe.iloc[i].append(pd.Series({'signal': 'NONE'}), ignore_index=True)
            break
        current_mac_d_value = mac_d_dataframe.iloc[i]
        previous_mac_d_value = mac_d_dataframe.iloc[i-1]
        if previous_mac_d_value < 0 and current_mac_d_value > 0:
            mac_d_dataframe.iloc[i].append(pd.Series({'signal': "SELL"}), ignore_index=True)
        elif previous_mac_d_value > 0 and current_mac_d_value < 0:
            mac_d_dataframe.iloc[i].append(pd.Series({'signal': "BUY"}), ignore_index=True)
        else:
            mac_d_dataframe.iloc[i].append(pd.Series({'signal': "NONE"}), ignore_index=True)

    return mac_d_dataframe
