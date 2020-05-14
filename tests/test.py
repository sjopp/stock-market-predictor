from .context import src
import unittest
from unittest.mock import patch


class TestRetrievalOfData(unittest.TestCase):

    def test_return_AAPL_current_stock_data_from_api(self):
        response_body = [
            {"date": "2019-12-26T00:00:00.000Z", "close": 289.91, "high": 289.98, "low": 284.7, "open": 284.82,
             "volume": 23334004, "adjClose": 288.4514628933, "adjHigh": 288.5211107234, "adjLow": 283.2676744015,
             "adjOpen": 283.3870706815, "adjVolume": 23334004, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-27T00:00:00.000Z", "close": 289.8, "high": 293.97, "low": 288.12, "open": 291.12,
             "volume": 36592936, "adjClose": 288.3420163033, "adjHigh": 292.4910370348, "adjLow": 286.6704683827,
             "adjOpen": 289.6553753838, "adjVolume": 36592936, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-30T00:00:00.000Z", "close": 291.52, "high": 292.69, "low": 285.22, "open": 289.46,
             "volume": 36059614, "adjClose": 290.0533629839, "adjHigh": 291.2174767143, "adjLow": 283.7850582817,
             "adjOpen": 288.0037268432, "adjVolume": 36059614, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-31T00:00:00.000Z", "close": 293.65, "high": 293.68, "low": 289.52, "open": 289.93,
             "volume": 25247625, "adjClose": 292.1726469547, "adjHigh": 292.2024960247, "adjLow": 288.0634249832,
             "adjOpen": 288.4713622734, "adjVolume": 25247625, "divCash": 0.0, "splitFactor": 1.0}]

        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            mock_request.return_value.content = response_body
            self.assertEqual(src.get_stock_data('AAPL', '2019-12-25', '2020-1-1'), response_body)

    def test_return_MSFT_current_stock_data_from_api(self):
        response_body = [
            {"date": "2019-12-26T00:00:00.000Z", "close": 158.67, "high": 158.73, "low": 157.4, "open": 157.5511,
             "volume": 14526927, "adjClose": 158.2390840833, "adjHigh": 158.2989211353, "adjLow": 156.9725331487,
             "adjOpen": 157.1232227914, "adjVolume": 14526927, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-27T00:00:00.000Z", "close": 158.96, "high": 159.55, "low": 158.22, "open": 159.45,
             "volume": 18414352, "adjClose": 158.5282965014, "adjHigh": 159.1166941797, "adjLow": 157.7903061931,
             "adjOpen": 159.0169657596, "adjVolume": 18414352, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-30T00:00:00.000Z", "close": 157.59, "high": 159.02, "low": 156.73, "open": 158.9865,
             "volume": 16356720, "adjClose": 157.1620171468, "adjHigh": 158.5881335534, "adjLow": 156.3043527344,
             "adjOpen": 158.5547245327, "adjVolume": 16356720, "divCash": 0.0, "splitFactor": 1.0},
            {"date": "2019-12-31T00:00:00.000Z", "close": 157.7, "high": 157.77, "low": 156.45, "open": 156.77,
             "volume": 18393383, "adjClose": 157.2717184089, "adjHigh": 157.3415283029, "adjLow": 156.0251131583,
             "adjOpen": 156.3442441025, "adjVolume": 18393383, "divCash": 0.0, "splitFactor": 1.0}]

        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            mock_request.return_value.content = response_body
            self.assertEqual(src.get_stock_data('MSFT', '2019-12-25', '2020-1-1'), response_body)


if __name__ == '__main__':
    unittest.main()
