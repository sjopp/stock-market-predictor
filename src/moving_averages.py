import matplotlib.pyplot as plt


def get_simple_moving_averages(dataframe, window):
    return dataframe.rolling(window=window).mean()


def get_exponential_moving_averages(dataframe, span):
    return dataframe.ewm(span=span, adjust=False).mean()


def plot_mac_d(stock_data, ema_12_day, ema_26_day):
    dates = stock_data.index.values
    plt.plot(dates, stock_data['adjClose'], label='prices')
    plt.plot(dates, ema_12_day['adjClose'], label='EMA 12 day')
    plt.plot(dates, ema_26_day['adjClose'], label='EMA 26 day')
    plt.legend()
    plt.show()
