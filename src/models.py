from src.app import db

class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin = db.Column(db.String(10), nullable=False)
    target_price = db.Column(db.Float, nullable=False)
