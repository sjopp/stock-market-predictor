import numpy as np


def return_ups(price_dataframe):
    ups_count = 0
    downs_count = 0
    for i in range(1, price_dataframe.shape[0]):
        price_difference = price_dataframe.iloc[i]['adjClose'] - price_dataframe.iloc[i - 1]['adjClose']
        if price_difference >= 0:
            ups_count += price_difference
        else:
            downs_count += np.absolute(price_difference)
    return ups_count, downs_count
