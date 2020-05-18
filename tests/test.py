from .context import src
import unittest
import responses
import pandas.testing as pd_test
import pandas as pd


class TestRetrievalOfData(unittest.TestCase):
    json_expected = [
        {'date': '2019-12-26T00:00:00.000Z', 'close': 289.91, 'high': 289.98, 'low': 284.7, 'open': 284.82,
         'volume': 23334004, 'adjClose': 288.4514628933, 'adjHigh': 288.5211107234, 'adjLow': 283.2676744015,
         'adjOpen': 283.3870706815, 'adjVolume': 23334004, 'divCash': 0.0, 'splitFactor': 1.0},
        {'date': '2019-12-27T00:00:00.000Z', 'close': 289.8, 'high': 293.97, 'low': 288.12, 'open': 291.12,
         'volume': 36592936, 'adjClose': 288.3420163033, 'adjHigh': 292.4910370348, 'adjLow': 286.6704683827,
         'adjOpen': 289.6553753838, 'adjVolume': 36592936, 'divCash': 0.0, 'splitFactor': 1.0},
        {'date': '2019-12-30T00:00:00.000Z', 'close': 291.52, 'high': 292.69, 'low': 285.22, 'open': 289.46,
         'volume': 36059614, 'adjClose': 290.0533629839, 'adjHigh': 291.2174767143, 'adjLow': 283.7850582817,
         'adjOpen': 288.0037268432, 'adjVolume': 36059614, 'divCash': 0.0, 'splitFactor': 1.0},
        {'date': '2019-12-31T00:00:00.000Z', 'close': 293.65, 'high': 293.68, 'low': 289.52, 'open': 289.93,
         'volume': 25247625, 'adjClose': 292.1726469547, 'adjHigh': 292.2024960247, 'adjLow': 288.0634249832,
         'adjOpen': 288.4713622734, 'adjVolume': 25247625, 'divCash': 0.0, 'splitFactor': 1.0}]

    dataframe_expected = pd.DataFrame(json_expected,
                                      columns=['date', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen',
                                               'adjVolume']).set_index('date')

    @responses.activate
    def test_return_AAPL_current_stock_data_from_api(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-25&endDate=2020-1-1',
                      json=self.json_expected, status=200)

        json_actual = src.get_stock_data('AAPL', '2019-12-25', '2020-1-1')

        self.assertEqual(self.json_expected, json_actual)

    def test_we_return_pandas_dataframe(self):
        actual_dataframe = src.convert_to_dataframe(self.json_expected)
        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, self.dataframe_expected)


if __name__ == '__main__':
    unittest.main()
