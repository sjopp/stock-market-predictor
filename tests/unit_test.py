from .context import src
from .context import return_json_test_resource
import unittest
import responses
import pandas.testing as pd_test
import pandas as pd


class TestRetrievalOfData(unittest.TestCase):

    json_expected = return_json_test_resource('AAPL_12_2019.json')

    dataframe_expected = pd.DataFrame(json_expected,
                                      columns=['date', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen',
                                               'adjVolume']).set_index('date')

    @responses.activate
    def test_return_AAPL_current_stock_data_from_api(self):
        responses.add(responses.GET,
                      'https://api.tiingo.com/tiingo/daily/AAPL/prices?token'
                      '=387fd657063535f02ef5a5700aadd0b9286572e9&startDate=2019-12-25&endDate=2020-1-1',
                      json=self.json_expected, status=200)

        json_actual = src.retrieve_and_convert.get_stock_data('AAPL', '2019-12-25', '2020-1-1')

        self.assertEqual(self.json_expected, json_actual)

    def test_we_return_pandas_dataframe(self):
        actual_dataframe = src.retrieve_and_convert.convert_to_dataframe(self.json_expected)
        print(actual_dataframe)
        pd_test.assert_frame_equal(actual_dataframe, self.dataframe_expected)

    def test_we_find_the_correct_moving_averages_with_window_3(self):
        expected_moving_averages = self.dataframe_expected.rolling(window=3).mean()
        dataframe = src.retrieve_and_convert.convert_to_dataframe(self.json_expected)
        actual_moving_averages = src.moving_averages.return_moving_average(dataframe, 3)
        pd_test.assert_frame_equal(actual_moving_averages, expected_moving_averages)

    def test_we_find_the_correct_moving_averages_with_window_5(self):
        expected_moving_averages = self.dataframe_expected.rolling(window=5).mean()
        dataframe = src.retrieve_and_convert.convert_to_dataframe(self.json_expected)
        actual_moving_averages = src.moving_averages.return_moving_average(dataframe, 5)
        pd_test.assert_frame_equal(actual_moving_averages, expected_moving_averages)


if __name__ == '__main__':
    unittest.main()
