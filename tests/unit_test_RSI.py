from .context import src, return_dataframe_resource
import unittest
import pandas.testing as pd_test


class TestRSICalculations(unittest.TestCase):
    dataframe_AAPL_12_2019 = return_dataframe_resource('AAPL/AAPL_12_2019.json', ['date', 'adjClose'])

    def test_we_return_ups_and_downs_correctly(self):
        ups_total, downs_total = src.rsi.return_ups(self.dataframe_AAPL_12_2019)
        assert ups_total == 39.152030163999996
        assert downs_total == 9.810394343500036


if __name__ == '__main__':
    unittest.main()
