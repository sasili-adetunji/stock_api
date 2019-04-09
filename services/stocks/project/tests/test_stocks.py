import json
import unittest
from project import db
from project.tests.base import BaseTestCase
from project.api.models import Stocks

def add_stocks(**kwargs):
    stocks = Stocks(**kwargs)
    db.session.add(stocks)
    db.session.commit()
    return stocks

class TestStocksService(BaseTestCase):
    """Tests for the Stocks Service."""

    stock_data = {
        "stock_name": "PEPSI",
        "opening_price": "29.01",
        "highest_price": "29.11",
        "lowest_price": "29.13",
        "closing_price": "29.12",
        "date": "2019-01-05"
    }
    def test_get_all_stocks(self):
        """Ensure get all stock behaves correctly."""
        add_stocks(**self.stock_data)
        with self.client:
            response = self.client.get('/stocks/')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']), 1)
            self.assertEqual(
                self.stock_data['stock_name'],
                data['data'][0]['stocks']['stock_name'])

    def test_post_stocks(self):
        """Ensure a new stocks can be added to the database."""
        with self.client:
            response = self.client.post(
                '/stocks/',
                data=json.dumps(self.stock_data),
                content_type='application/json',
                headers=({'Authorization': 'Bearer test'})
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('New stocks was recorded', data['message'])
            self.assertIn('success', data['status'])

    def test_add_stocks_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/stocks/',
                data=json.dumps({}),
                content_type='application/json',
                headers=({'Authorization': 'Bearer test'})
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_stocks_no_header(self):
        """Ensure error is thrown if 'Authorization' header is empty."""
        response = self.client.post(
            '/stocks/',
            data=json.dumps(self.stock_data),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 403)
        self.assertIn('Kindly provide a valid auth token.', data['message'])
        self.assertIn('error', data['status'])


if __name__ == '__main__':
    unittest.main()
