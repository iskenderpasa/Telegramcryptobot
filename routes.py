from models import db, User
from telegram import Bot

TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
bot = Bot(token=TOKEN)

def send_summary_to_all_users():
    users = db.session.query(User).all()
    for user in users:
        try:
            message = f"Günlük rapor: Kar/Zarar: {user.pnl}"
            bot.send_message(chat_id=user.chat_id, text=message)
        except Exception as e:
            print(f"Mesaj gönderilemedi: {e}")