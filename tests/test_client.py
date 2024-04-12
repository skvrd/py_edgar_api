import unittest
from unittest.mock import patch
from py_edgar_api import Client, Company  # Adjust import to your package structure

class TestClientClass(unittest.TestCase):

    @patch('requests.Session.get')
    def test_get_company_success(self, mock_get):
        # Mock the API response
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {
            "0": {"cik_str": "789019", "ticker": "MSFT", "title": "MICROSOFT CORP"},
            "1": {"cik_str": "320193", "ticker": "AAPL", "title": "Apple Inc."}
        }

        client = Client("Test Name", "test@example.com")  # Instantiate your class
        result = client.get_company("MSFT")
        self.assertIsInstance(result, Company)
        self.assertIsNotNone(result)
        self.assertEqual(result.cik, "789019")

    @patch('requests.Session.get')
    def test_get_company_not_found(self, mock_get):
        # Mock the API response to simulate ticker not found
        mock_response = mock_get.return_value
        mock_response.raise_for_status = lambda: None
        mock_response.json.return_value = {
            "0": {"cik_str": "789019", "ticker": "MSFT", "title": "MICROSOFT CORP"}
        }

        client = Client("Test Name", "test@example.com")
        result = client.get_company("GOOG")
        self.assertIsNone(result)

    @patch('requests.Session.get')
    def test_get_company_api_failure(self, mock_get):
        # Simulate an API failure
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = Exception("API Error")

        client = Client("Test Name", "test@example.com")
        with self.assertRaises(Exception):
            client.get_company("MSFT")