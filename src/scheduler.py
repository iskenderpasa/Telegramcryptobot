from apscheduler.schedulers.background import BackgroundScheduler
from src.alarm_service import check_alarms
from src.portfolio_service import send_portfolio_summary
import pytz

def schedule_jobs():
    scheduler = BackgroundScheduler(timezone=pytz.timezone('Europe/Istanbul'))

    # Her 10 dakikada bir alarm kontrolü
    scheduler.add_job(check_alarms, 'interval', minutes=10)

    # Günde 4 kez portföy özeti gönderimi: 10:00, 14:00, 18:00, 22:00
    scheduler.add_job(send_portfolio_summary, 'cron', hour='10,14,18,22', minute=0)

    scheduler.start()
