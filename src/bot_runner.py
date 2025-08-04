from bot import application
from telegram.ext import CommandHandler
from scheduler import schedule_jobs
from routes import alarm

def run_all():
    application.add_handler(CommandHandler("alarm", alarm))
    schedule_jobs()
    application.run_polling()
