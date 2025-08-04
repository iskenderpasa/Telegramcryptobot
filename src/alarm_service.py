from src.models import Alarm
from src.crypto_service import get_crypto_price
from src.app import db
from telegram import Bot

CHAT_ID = 583677323
TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
bot = Bot(token=TOKEN)

def set_alarm(coin: str, target_price: float):
    alarm = Alarm(coin=coin.upper(), target_price=target_price)
    db.session.add(alarm)
    db.session.commit()

def check_alarms():
    alarms = Alarm.query.all()
    for alarm in alarms:
        current_price = get_crypto_price(alarm.coin)
        if current_price is not None and current_price >= alarm.target_price:
            msg = f"🚨 {alarm.coin} alarmı tetiklendi!\n📈 {current_price:.2f} USDT ≥ 🎯 {alarm.target_price:.2f} USDT"
            bot.send_message(chat_id=CHAT_ID, text=msg)
            db.session.delete(alarm)
    db.session.commit()
