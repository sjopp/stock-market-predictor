from .context import src, return_dataframe_resource
import unittest
import pandas.testing as pd_test


class TestRSICalculations(unittest.TestCase):
    dataframe_AAPL_12_2019 = return_dataframe_resource('AAPL/AAPL_12_2019.json', ['date', 'adjClose'])

    def test_we_return_price_difference_column_correctly(self):
        expected_dataframe = return_dataframe_resource('AAPL/AAPL_12_2019_RSI_ups_and_downs.json',
                                                       ['date', 'adjClose', 'difference'])
        actual_dataframe = src.rsi.append_price_difference(self.dataframe_AAPL_12_2019)
        pd_test.assert_frame_equal(actual_dataframe, expected_dataframe)


if __name__ == '__main__':
    unittest.main()
