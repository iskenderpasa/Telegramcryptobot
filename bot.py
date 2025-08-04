from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from crypto_service import get_price
import os

# Bot Token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo")

# /start komutu
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Merhaba! Ben kripto asistan botuyum.\n"
        "/start - Başlat\n"
        "/kar - Kar-Zarar\n"
        "/fiyat <coin> - Fiyat Sorgula\n"
        "/help - Yardım"
    )

# /help komutu
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Komutlar:\n"
        "/start - Botu başlatır\n"
        "/kar - Kar/Zarar durumunu gösterir\n"
        "/fiyat <coin> - Belirttiğiniz coinin güncel fiyatını gösterir"
    )

# /fiyat komutu
def fiyat(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Lütfen bir coin ismi girin. Örnek: /fiyat BTC")
        return

    coin = context.args[0].lower()
    price = get_price(coin)
    if price is not None:
        update.message.reply_text(f"{coin.upper()} fiyatı: {price} USDT")
    else:
        update.message.reply_text("Fiyat alınamadı. Lütfen geçerli bir coin girin.")

# /kar komutu
def kar(update: Update, context: CallbackContext):
    update.message.reply_text("Kar/Zarar özelliği yakında aktif edilecek.")

# Botu başlat
def start_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("fiyat", fiyat))
    dp.add_handler(CommandHandler("kar", kar))

    updater.start_polling()
    updater.idle()
