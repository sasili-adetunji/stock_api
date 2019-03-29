from project import db

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
