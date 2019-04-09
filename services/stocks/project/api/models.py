from project import db


class Stocks(db.Model):

    __tablename__ = "stocks"
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    stock_name = db.Column(db.String(128), nullable=False)
    opening_price = db.Column(db.String(128), nullable=False)
    highest_price = db.Column(db.String(128), nullable=False)
    lowest_price = db.Column(db.String(128), nullable=False)
    closing_price = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date)


    def __init__(self, stock_name, opening_price, highest_price, lowest_price, closing_price, date):
        self.stock_name = stock_name
        self.opening_price = opening_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.closing_price = closing_price
        self.date = date

    def to_json(self):
        return {
            'id': self.id,
            'stock_name': self.stock_name,
            'opening_price': self.opening_price,
            'highest_price': self.highest_price,
            'lowest_price': self.lowest_price,
            'closing_price': self.closing_price,
            'date': self.date,
        }
