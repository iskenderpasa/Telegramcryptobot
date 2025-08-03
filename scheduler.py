import schedule
import time
import threading
from routes import send_summary_to_all_users

def job():
    print("Scheduler: Sending summary to all users.")
    send_summary_to_all_users()

def start_scheduler():
    schedule.every().day.at("08:00").do(job)
    schedule.every().day.at("18:00").do(job)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()