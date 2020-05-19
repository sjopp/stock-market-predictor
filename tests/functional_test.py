from .context import src
import unittest


class FunctionalTest(unittest.TestCase):

    def test_end_to_end(self):
        src.plot_data('AAPL', '2019-1-1', '2020-1-1', 10)


if __name__ == '__main__':
    unittest.main()
