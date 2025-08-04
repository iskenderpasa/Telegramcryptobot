from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes import *
from src.runbot import run_all

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alarms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    run_all()
    app.run(host="0.0.0.0", port=10000)
