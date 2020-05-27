def get_simple_moving_averages(dataframe, window):
    return dataframe.rolling(window=window).mean()


def get_exponential_moving_averages(dataframe, span):
    return dataframe.ewm(span=span, adjust=False).mean()
