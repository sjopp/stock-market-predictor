import matplotlib.pyplot as plt


def get_simple_moving_averages(dataframe, window):
    return dataframe.rolling(window=window).mean()


def get_exponential_moving_averages(dataframe, span):
    return dataframe.ewm(span=span, adjust=False).mean()


def plot_moving_averages_against_stock_price(stock_data, moving_averages):
    dates = stock_data.index.values
    plt.plot(dates, stock_data['adjClose'])
    plt.plot(dates, moving_averages['adjClose'])
    plt.show()
