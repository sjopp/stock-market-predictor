import numpy as np


def append_price_difference(price_dataframe):
    differences = [np.float64(0)]
    for i in range(1, price_dataframe.shape[0]):
        difference = price_dataframe.iloc[i]['adjClose'] - price_dataframe.iloc[i - 1]['adjClose']
        differences.append(difference)
    price_dataframe['difference'] = differences
    return price_dataframe
