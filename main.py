import os
import logging
import threading
import asyncio
from app import app

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def start_flask_app():
    logger.info("Starting Flask web application...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

def start_telegram_bot():
    try:
        from bot import start_bot
        logger.info("Starting Telegram bot...")
        asyncio.set_event_loop(asyncio.new_event_loop())
        start_bot()
    except Exception as e:
        logger.error(f"Failed to start Telegram bot: {e}")

def main():
    logger.info("Starting Kripto Bot - Flask web application and Telegram bot")
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token or bot_token == "your-bot-token-here":
        logger.warning("TELEGRAM_BOT_TOKEN not provided. Starting only Flask web application.")
        start_flask_app()
        return

    try:
        flask_thread = threading.Thread(target=start_flask_app, daemon=True)
        flask_thread.start()
        logger.info("Flask web application started in background thread")
        start_telegram_bot()
    except KeyboardInterrupt:
        logger.info("Shutting down Kripto Bot...")
    except Exception as e:
        logger.error(f"Error in main application: {e}")
        logger.info("Falling back to Flask-only mode...")
        start_flask_app()

if __name__ == "__main__":
    main()