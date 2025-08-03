from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.BigInteger, unique=True, nullable=False)
    pnl = db.Column(db.Float, default=0.0)