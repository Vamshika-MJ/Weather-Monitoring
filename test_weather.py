import unittest
from unittest.mock import patch
from weather_api import get_weather_data

class TestWeatherApp(unittest.TestCase):

    @patch('weather_api.requests.get')
    def test_get_weather_data(self, mock_get):
        print("Mocking API response...")  # Debugging print
        
        mock_response = {
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 30, 'feels_like': 32},
            'dt': 1609459200
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        print("Calling get_weather_data...")  # Debugging print
        weather = get_weather_data('Delhi')
        print("Weather data fetched:", weather)  # Debugging print

        self.assertEqual(weather['city'], 'Delhi')
        self.assertEqual(weather['main'], 'Clear')
        self.assertEqual(weather['temp'], 30)

if __name__ == '__main__':
    print("Starting tests...")
    unittest.main()
