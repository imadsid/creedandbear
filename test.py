import unittest
import requests


class BinanceTest(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"

    def test_latest_price(self):
        params = {'currency':'BNBUSDT'}
        response = requests.get(self.BASE_URL+'/get_latest_price',params=params)
        status = response.status_code
        print(status)
        self.assertEqual(status,200)

    def test_statistical_data(self):
        params = {'currency':'BTCUSDT'}
        response = requests.get(self.BASE_URL+'/get_statistical_data',params=params)
        status = response.status_code
        print(status)
        self.assertEqual(status,200)

    def test_historical_data(self):
        params = {'start': '2024-03-30 03:13:4', 'end': '2024-03-31 10:43:19'}
        response = requests.get(self.BASE_URL+'/get_historical_data',params=params)
        status = response.status_code
        print(status)
        self.assertEqual(status,200)

    def test_available_currencies(self):
        response = requests.get(self.BASE_URL+'/get_currencies')
        status = response.status_code
        print(status)
        self.assertEqual(status,200)


if __name__ == '__main__':
    unittest.main()