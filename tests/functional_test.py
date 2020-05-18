from .context import src
import unittest


class FunctionalTest(unittest.TestCase):

    def test_end_to_end(self):
        json_stock_data = src.retrieve_and_convert.get_stock_data('AAPL', '2019-1-1', '2020-1-1')
        print(json_stock_data)
        stock_dataframe = src.retrieve_and_convert.convert_to_dataframe(json_stock_data)
        print(stock_dataframe)
        moving_averages = src.moving_averages.return_moving_average(stock_dataframe, 5)
        print(moving_averages)
        src.moving_averages.plot_moving_averages_against_stock_price(stock_dataframe, moving_averages)


if __name__ == '__main__':
    unittest.main()
