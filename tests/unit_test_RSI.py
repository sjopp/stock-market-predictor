from .context import src, return_dataframe_resource
import unittest
import pandas.testing as pd_test


class TestRSICalculations(unittest.TestCase):

    dataframe_AAPL_12_2019 = return_dataframe_resource('AAPL/AAPL_12_2019.json', ['date', 'adjClose'])
    dataframe_AAPL_12_2019_price_differences = return_dataframe_resource('AAPL/AAPL_12_2019_RSI.json',
                                                                         ['date', 'adjClose', 'ups', 'downs'])

    def test_we_return_price_difference_column_correctly(self):
        expected_dataframe = self.dataframe_AAPL_12_2019_price_differences
        actual_dataframe = src.rsi.append_price_difference(self.dataframe_AAPL_12_2019)
        pd_test.assert_frame_equal(actual_dataframe, expected_dataframe)

    def test_we_return_simple_moving_averages_ups_and_downs_column_correctly(self):
        expected_dataframe = return_dataframe_resource('AAPL/AAPL_12_2019_RSI.json',
                                                       ['date', 'adjClose', 'ups', 'downs', 'smaUp', 'smaDown'])
        actual_dataframe = src.rsi.append_sma(self.dataframe_AAPL_12_2019_price_differences)
        pd_test.assert_frame_equal(actual_dataframe, expected_dataframe)


if __name__ == '__main__':
    unittest.main()
