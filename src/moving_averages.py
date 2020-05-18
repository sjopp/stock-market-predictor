import matplotlib.pyplot as plt


def return_moving_average(dataframe, window):
    return dataframe.rolling(window=window).mean()


def plot_moving_averages_against_stock_price(stock_data, moving_averages):
    dates = stock_data.index.values
    plt.plot(dates, stock_data['adjClose'])
    plt.plot(dates, moving_averages['adjClose'])
    plt.show()
