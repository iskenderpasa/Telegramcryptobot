from app import app
from bot import application
from scheduler import run_scheduler
import threading

def run_all():
    # Flask sunucusunu ayrı bir thread'de çalıştır
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=10000)).start()

    # Zamanlayıcıyı başlat (örneğin sabah özet gönderimi vs.)
    run_scheduler()

    # Telegram botunu başlat
    application.run_polling()

if __name__ == "__main__":
    run_all()
