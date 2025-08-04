from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import portfolio_service
import crypto_service

TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Merhaba! Portföy takip botuna hoş geldin. Komutlar için /help yazabilirsin.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Botu başlat\n"
        "/help - Yardım al\n"
        "/kar - Portföydeki kar/zarar durumunu göster\n"
        "/fiyat [coin] - Coin fiyatını göster (örn: /fiyat BTC)\n"
    )

async def kar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = portfolio_service.kar_zarar_ozeti()
    await update.message.reply_text(mesaj)

async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Lütfen bir coin girin. Örn: /fiyat BTC")
        return
    coin = context.args[0]
    fiyat = crypto_service.get_price(coin)
    if fiyat:
        await update.message.reply_text(f"{coin.upper()} fiyatı: {fiyat} USD")
    else:
        await update.message.reply_text("Coin bulunamadı.")

def run():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("kar", kar))
    app.add_handler(CommandHandler("fiyat", fiyat))

    print("Bot çalışıyor...")
    from alarm_service import alarm_ekle

async def alarm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Kullanım: /alarm COIN FİYAT\nÖrn: /alarm INJ 14.00")
        return
    coin = context.args[0]
    fiyat = context.args[1]
    cevap = alarm_ekle(coin, fiyat)
    await update.message.reply_text(cevap)

app.add_handler(CommandHandler("alarm", alarm))
