from .context import src
import unittest
from unittest.mock import patch


class TestRetrievalOfData(unittest.TestCase):

    def test_return_AAPL_current_stock_data_from_api(self):
        response_body = [
            {"adjClose": 315.01, "adjHigh": 317.05, "adjLow": 307.24, "adjOpen": 308.1, "adjVolume": 36486561,
             "close": 315.01, "date": "2020-05-11T00:00:00+00:00", "divCash": 0.0, "high": 317.05, "low": 307.24,
             "open": 308.1, "splitFactor": 1.0, "volume": 36486561}]

        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            mock_request.return_value.content = response_body
            self.assertEqual(src.get_stock_data('AAPL'), response_body)

    def test_return_MSFT_current_stock_data_from_api(self):
        response_body = [
            {"adjClose": 186.74, "adjHigh": 187.51, "adjLow": 182.85, "adjOpen": 183.15, "adjVolume": 30892660,
             "close": 186.74, "date": "2020-05-11T00:00:00+00:00", "divCash": 0.0, "high": 187.51, "low": 182.85,
             "open": 183.15, "splitFactor": 1.0, "volume": 30892660}]

        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            mock_request.return_value.content = response_body
            self.assertEqual(src.get_stock_data('MSFT'), response_body)


if __name__ == '__main__':
    unittest.main()
