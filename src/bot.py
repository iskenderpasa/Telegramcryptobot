from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from src.crypto_service import get_crypto_price
from src.portfolio_service import calculate_portfolio_value
from src.alarm_service import set_alarm, check_alarms

TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"

application = ApplicationBuilder().token(TOKEN).build()

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Kripto botuna hoş geldin.")

# /fiyat komutu
async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Lütfen bir coin ismi girin. Örn: /fiyat BTC")
        return
    coin = context.args[0].upper()
    price = get_crypto_price(coin)
    if price:
        await update.message.reply_text(f"{coin} fiyatı: {price} USDT")
    else:
        await update.message.reply_text(f"{coin} için fiyat bulunamadı.")

# /kar komutu
async def kar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    summary = calculate_portfolio_value()
    await update.message.reply_text(summary)

# /alarm komutu
async def alarm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Kullanım: /alarm COIN HEDEF_FİYAT\nÖrn: /alarm INJ 13.50")
        return
    coin = context.args[0].upper()
    try:
        target = float(context.args[1])
        set_alarm(coin, target)
        await update.message.reply_text(f"{coin} için {target} USDT hedefli alarm kuruldu.")
    except ValueError:
        await update.message.reply_text("Hedef fiyat sayısal olmalıdır.")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("fiyat", fiyat))
application.add_handler(CommandHandler("kar", kar))
application.add_handler(CommandHandler("alarm", alarm))
