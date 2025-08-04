import threading
import scheduler
import bot
from alarm_service import start_alarm_thread  # 🔔 Alarm sistemi

def run_bot():
    bot.run()

def run_scheduler():
    scheduler.start_scheduler()

def run_all():
    start_alarm_thread()  # 🔔 Fiyat alarm sistemi başlasın
    bot_thread = threading.Thread(target=run_bot)
    scheduler_thread = threading.Thread(target=run_scheduler)

    bot_thread.start()
    scheduler_thread.start()

    bot_thread.join()
    scheduler_thread.join()

if __name__ == "__main__":
    run_all()
