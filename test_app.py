import unittest
from unittest.mock import patch
import requests
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.get')
    def test_get_cell_data_success(self, mocked_get):
        # Mock data
        mock_response = {
            'discharge_capacity': 2000,
            'nominal_capacity': 3000,
            'time_data': [1, 2, 3],
            'current_data': [5, 10, 15],
            'voltage_data': [3.7, 3.8, 3.9],
            'capacity_data': [1800, 1900, 2000],
            'temperature_data': [30, 31, 32]
        }
        mocked_get.return_value.json.return_value = mock_response
        response = self.app.get('/cell_data/5308', headers={'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})  # admin:password123 in base64
        self.assertEqual(response.status_code, 200)
        self.assertIn('discharge_capacity', response.get_json())

    @patch('requests.get')
    def test_get_cell_data_failure(self, mocked_get):
        mocked_get.side_effect = requests.exceptions.RequestException
        response = self.app.get('/cell_data/5308', headers={'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
