from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ana endpoint
@app.route('/')
def index():
    return "Telegram bot çalışıyor. ✅"

# Gerekirse diğer Flask route'larını routes.py içinde tanımlayıp import edebilirsin
