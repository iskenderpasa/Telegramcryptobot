from src.bot import application

def start_bot():
    application.run_polling(allowed_updates=application.resolve_used_update_types())

if __name__ == "__main__":
    start_bot()
