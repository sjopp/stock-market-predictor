def return_moving_average(dataframe):
    return dataframe.rolling(window=3).mean()

