from .context import src
import unittest


class FunctionalTest(unittest.TestCase):

    def test_end_to_end(self):
        src.find_mac_d('AAPL', '2019-1-1', '2020-1-1')

    def test_mac_d(self):
        mac_d_values = src.mac_d.generate_mac_d_values('AAPL', '2019-1-1', '2020-1-1', 12, 26)
        src.mac_d.determine_mac_d_signal(mac_d_values)


if __name__ == '__main__':
    unittest.main()
