import unittest
from project import db
from project.api.models import Stocks
from project.tests.base import BaseTestCase


def add_stocks(**kwargs):
    stocks = Stocks(**kwargs)
    db.session.add(stocks)
    db.session.commit()
    return stocks

class TestStockModel(BaseTestCase):

    stock_data = {
        "stock_name": "PEPSI",
        "opening_price": "29.01",
        "highest_price": "29.11",
        "lowest_price": "29.13",
        "closing_price": "29.12",
        "date": "2019-01-05"
    }
    def test_add_user(self):
        stocks = add_stocks(**self.stock_data)

        self.assertTrue(stocks.id)
        self.assertEqual(stocks.stock_name, 'PEPSI')
        self.assertTrue(stocks.date)

    def test_to_json(self):
        stocks = add_stocks(**self.stock_data)
        self.assertTrue(isinstance(stocks.to_json(), dict))

if __name__ == '__main__':
    unittest.main()