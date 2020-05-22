from .context import src
import unittest


class FunctionalTest(unittest.TestCase):

    def test_end_to_end(self):
        src.find_mac_d('AAPL', '2019-1-1', '2020-1-1')


if __name__ == '__main__':
    unittest.main()
