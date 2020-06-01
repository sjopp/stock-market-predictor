import src.retrieve_convert as retrieve_and_convert
import src.moving_averages as moving_averages
import matplotlib.pyplot as plt
import numpy as np


def generate_mac_d_values(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    price_dataframe, fast_moving_average_df, slow_moving_average_df = get_moving_averages(stock, start_date, end_date,
                                                                                          fast_moving_average,
                                                                                          slow_moving_average)
    return slow_moving_average_df.subtract(fast_moving_average_df)


def generate_mac_d_signal(mac_d_dataframe):
    signals = [np.float64(0)]
    for i in range(1, mac_d_dataframe.shape[0]):
        current_mac_d_value = mac_d_dataframe.iloc[i]['adjClose']
        previous_mac_d_value = mac_d_dataframe.iloc[i - 1]['adjClose']
        if previous_mac_d_value < 0 and current_mac_d_value >= 0:
            signals.append(np.float64(-1))
        elif previous_mac_d_value >= 0 and current_mac_d_value < 0:
            signals.append(np.float64(1))
        else:
            signals.append(np.float64(0))

    mac_d_dataframe['signal'] = signals
    return mac_d_dataframe


def plot_mac_d(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    price_dataframe, fast_moving_average_df, slow_moving_average_df = get_moving_averages(stock, start_date, end_date,
                                                                                          fast_moving_average,
                                                                                          slow_moving_average)
    dates = price_dataframe.index.values
    plt.plot(dates, price_dataframe['adjClose'], label='Price')
    plt.plot(dates, fast_moving_average_df['adjClose'], label='Fast Moving Average')
    plt.plot(dates, slow_moving_average_df['adjClose'], label='Slow Moving Average')
    plt.legend()
    plt.show()


def get_moving_averages(stock, start_date, end_date, fast_moving_average, slow_moving_average):
    price_dataframe = retrieve_and_convert.get_stock_dataframe(stock, start_date, end_date)
    fast_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, fast_moving_average)
    slow_moving_average_df = moving_averages.get_exponential_moving_averages(price_dataframe, slow_moving_average)
    return price_dataframe, fast_moving_average_df, slow_moving_average_df
