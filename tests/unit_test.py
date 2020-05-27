from .context import src
from .context import return_json_test_resource
import unittest
import responses
import pandas.testing as pd_test
import pandas as pd
import numpy as np


def return_dataframe_resource(file_path):
    json_data = return_json_test_resource(file_path)
    return pd.DataFrame(json_data, columns=['date', 'adjClose'], dtype=np.float64).set_index('date')


class TestRetrievalOfData(unittest.TestCase):

    resource = return_json_test_resource('AAPL_12_2019.json')

    @responses.activate
    def test_return_AAPL_current_stock_data_from_api(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource, status=200)

        json_actual = src.retrieve_and_convert.get_stock_data('AAPL', '2019-12-1', '2020-1-1')

        self.assertEqual(self.resource, json_actual)

    def test_we_return_pandas_dataframe(self):
        dataframe_expected = return_dataframe_resource('AAPL_12_2019.json')

        actual_dataframe = src.retrieve_and_convert.convert_to_dataframe(self.resource)

        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    def test_simple_moving_averages(self):
        dataframe_expected = return_dataframe_resource('AAPL_12_2019_SMA_3_day.json')

        dataframe = src.retrieve_and_convert.convert_to_dataframe(self.resource)
        actual_moving_averages = src.moving_averages.get_simple_moving_averages(dataframe, 3)

        pd_test.assert_frame_equal(actual_moving_averages, dataframe_expected)

    def test_exponential_slow_moving_averages(self):
        dataframe_expected = return_dataframe_resource('AAPL_12_2019_EMA_9_day.json')

        dataframe = src.retrieve_and_convert.convert_to_dataframe(self.resource)
        actual_dataframe = src.moving_averages.get_exponential_moving_averages(dataframe, 9)

        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    def test_exponential_fast_moving_averages(self):
        dataframe_expected = return_dataframe_resource('AAPL_12_2019_EMA_4_day.json')

        dataframe = src.retrieve_and_convert.convert_to_dataframe(self.resource)
        actual_dataframe = src.moving_averages.get_exponential_moving_averages(dataframe, 4)

        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    def test_mac_d_values(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource, status=200)

        result = src.mac_d.generate_mac_d_values('AAPL', '2019-12-1', '2020-1-1', 4, 9)
        dataframe_expected = return_dataframe_resource('AAPL_MACD_values.json')
        pd_test.assert_frame_equal(result, dataframe_expected)

    def test_mac_d_signals(self):
        mac_d_values = return_dataframe_resource('AAPL_MACD_values.json')
        dataframe_expected = return_dataframe_resource('AAPL_MACD_signals.json')
        result = src.mac_d.generate_mac_d_signal(mac_d_values)
        pd_test.assert_frame_equal(result, dataframe_expected)


if __name__ == '__main__':
    unittest.main()
