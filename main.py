from app import app
from bot import application
from scheduler import run_scheduler
import threading

def run_all():
    # Flask sunucusunu paralel başlat
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()

    # Zamanlayıcıyı başlat (APS)
    run_scheduler()

    # Telegram botu başlat
    application.run_polling()

if __name__ == "__main__":
    run_all()
