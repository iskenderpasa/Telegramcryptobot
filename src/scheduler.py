from apscheduler.schedulers.background import BackgroundScheduler
import portfolio_service
import requests

BOT_TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
CHAT_ID = 583677323  # Kullanıcının Telegram chat ID'si

def gonder_rapor():
    mesaj = portfolio_service.kar_zarar_ozeti()
    send_message(mesaj)

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def start_scheduler():
    scheduler = BackgroundScheduler()

    # Günde 4 kez belirli saatlerde rapor gönder
    scheduler.add_job(gonder_rapor, 'cron', hour=10, minute=0)
    scheduler.add_job(gonder_rapor, 'cron', hour=14, minute=0)
    scheduler.add_job(gonder_rapor, 'cron', hour=18, minute=0)
    scheduler.add_job(gonder_rapor, 'cron', hour=22, minute=0)

    scheduler.start()
    print("Zamanlayıcı başlatıldı.")
