from flask import request, jsonify
from src.app import app, db
from src.models import Alarm

@app.route("/")
def index():
    return "Bot çalışıyor!"

@app.route("/alarms", methods=["GET"])
def get_alarms():
    alarms = Alarm.query.all()
    return jsonify([
        {"coin": alarm.coin, "target_price": alarm.target_price}
        for alarm in alarms
    ])

@app.route("/set_alarm", methods=["POST"])
def create_alarm():
    data = request.get_json()
    coin = data.get("coin")
    target_price = data.get("target_price")
    if not coin or not target_price:
        return jsonify({"error": "Eksik veri"}), 400
    alarm = Alarm(coin=coin.upper(), target_price=target_price)
    db.session.add(alarm)
    db.session.commit()
    return jsonify({"message": f"{coin.upper()} için alarm kuruldu!"}), 201
