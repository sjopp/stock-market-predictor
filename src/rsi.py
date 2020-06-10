import numpy as np
import src.moving_averages as moving_averages


def append_price_difference(price_dataframe):
    ups = [np.float64(0)]
    downs = [np.float64(0)]
    for i in range(1, price_dataframe.shape[0]):
        difference = price_dataframe.iloc[i]['adjClose'] - price_dataframe.iloc[i - 1]['adjClose']
        if difference >= 0:
            ups.append(difference)
            downs.append(np.float64(0))
        else:
            ups.append(np.float64(0))
            downs.append(np.absolute(difference))
    price_dataframe['ups'] = ups
    price_dataframe['downs'] = downs
    return price_dataframe


def append_sma(price_difference_dataframe):
    sma_dataframe = moving_averages.get_simple_moving_averages(price_difference_dataframe, 9)
    price_difference_dataframe['smaUp'] = sma_dataframe['ups']
    price_difference_dataframe['smaDown'] = sma_dataframe['downs']
    return price_difference_dataframe


def append_ema(price_difference_dataframe):
    ema_dataframe = moving_averages.get_exponential_moving_averages(price_difference_dataframe, 9)
    price_difference_dataframe['emaUp'] = ema_dataframe['ups']
    price_difference_dataframe['emaDown'] = ema_dataframe['downs']
    return price_difference_dataframe


def append_relative_strength(price_difference_dataframe):
    relative_strengths = []
    for i in range(price_difference_dataframe.shape[0]):
        if price_difference_dataframe.iloc[i]['emaDown'] == 0:
            relative_strengths.append(np.float64(0))
        else:
            strength = price_difference_dataframe.iloc[i]['emaUp'] / price_difference_dataframe.iloc[i]['emaDown']
            relative_strengths.append(strength)
    price_difference_dataframe['rs'] = relative_strengths
    return price_difference_dataframe
