from .context import src, return_dataframe_resource
from .context import return_json_test_resource
import unittest
import responses
import pandas.testing as pd_test


class TestMACDCalculations(unittest.TestCase):

    resource_AAPL_12_2019 = return_json_test_resource('AAPL/AAPL_12_2019.json')
    resource_MSFT_2019 = return_json_test_resource('MSFT/MSFT_2019.json')

    @responses.activate
    def test_return_AAPL_current_stock_data_from_api(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)

        json_actual = src.retrieve_and_convert.get_stock_data('AAPL', '2019-12-1', '2020-1-1')

        self.assertEqual(self.resource_AAPL_12_2019, json_actual)

    @responses.activate
    def test_we_return_pandas_dataframe(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)

        dataframe_expected = return_dataframe_resource('AAPL/AAPL_12_2019.json', ['date', 'adjClose'])

        actual_dataframe = src.retrieve_and_convert.get_stock_dataframe('AAPL', '2019-12-1', '2020-1-1')

        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    @responses.activate
    def test_simple_moving_averages(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)

        dataframe_expected = return_dataframe_resource('AAPL/AAPL_12_2019_SMA_3_day.json', ['date', 'adjClose'])

        dataframe = src.retrieve_and_convert.get_stock_dataframe('AAPL', '2019-12-1', '2020-1-1')
        actual_moving_averages = src.moving_averages.get_simple_moving_averages(dataframe, 3)

        pd_test.assert_frame_equal(actual_moving_averages, dataframe_expected)

    @responses.activate
    def test_exponential_slow_moving_averages(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)

        dataframe_expected = return_dataframe_resource('AAPL/AAPL_12_2019_EMA_9_day.json', ['date', 'adjClose'])

        dataframe = src.retrieve_and_convert.get_stock_dataframe('AAPL', '2019-12-1', '2020-1-1')
        actual_dataframe = src.moving_averages.get_exponential_moving_averages(dataframe, 9)

        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    @responses.activate
    def test_exponential_fast_moving_averages(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)
        dataframe_expected = return_dataframe_resource('AAPL/AAPL_12_2019_EMA_4_day.json', ['date', 'adjClose'])

        dataframe = src.retrieve_and_convert.get_stock_dataframe('AAPL', '2019-12-1', '2020-1-1')
        actual_dataframe = src.moving_averages.get_exponential_moving_averages(dataframe, 4)

        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, dataframe_expected)

    @responses.activate
    def test_mac_d_values(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-1&endDate=2020-1-1',
                      json=self.resource_AAPL_12_2019, status=200)

        result = src.mac_d.generate_mac_d_values('AAPL', '2019-12-1', '2020-1-1', 4, 9)
        dataframe_expected = return_dataframe_resource('AAPL/AAPL_MACD_values.json', ['date', 'adjClose'])
        pd_test.assert_frame_equal(result, dataframe_expected)

    def test_mac_d_signals(self):
        mac_d_values = return_dataframe_resource('AAPL/AAPL_MACD_all_types_values.json', ['date', 'adjClose', 'signal'])
        dataframe_expected = return_dataframe_resource('AAPL/AAPL_MACD_all_types_signals.json',
                                                       ['date', 'adjClose', 'signal'])
        result = src.mac_d.generate_mac_d_signal(mac_d_values)
        pd_test.assert_frame_equal(result, dataframe_expected)

    @responses.activate
    def test_plot_mac_d_lines(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/MSFT/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-1-1&endDate=2020-1-1',
                      json=self.resource_MSFT_2019, status=200)
        src.mac_d.plot_mac_d('MSFT', '2019-1-1', '2020-1-1', 12, 26)


if __name__ == '__main__':
    unittest.main()
