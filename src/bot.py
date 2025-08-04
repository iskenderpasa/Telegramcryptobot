from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from portfolio_service import get_portfolio_summary, set_alarm_price
from crypto_service import get_price

TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
CHAT_ID = 583677323

application = ApplicationBuilder().token(TOKEN).build()

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba! Coin portföy takip botuna hoş geldin.")

# /kar komutu
async def kar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    summary = get_portfolio_summary()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=summary)

# /fiyat komutu
async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Kullanım: /fiyat COIN")
        return
    coin = context.args[0].upper()
    price = get_price(coin)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{coin} güncel fiyatı: {price} USDT")

# /alarm komutu
async def alarm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Kullanım: /alarm COIN FİYAT")
        return
    coin = context.args[0].upper()
    try:
        target_price = float(context.args[1])
    except ValueError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Fiyat geçerli değil.")
        return
    set_alarm_price(coin, target_price)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{coin} için {target_price} USDT fiyat alarmı ayarlandı.")

# Komutları ekle
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("kar", kar))
application.add_handler(CommandHandler("fiyat", fiyat))
application.add_handler(CommandHandler("alarm", alarm))
