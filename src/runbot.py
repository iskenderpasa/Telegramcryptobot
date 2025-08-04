from src.bot import application
from src.scheduler import schedule_jobs

def run_all():
    schedule_jobs()
    application.run_polling(allowed_updates=application.resolve_used_update_types())
