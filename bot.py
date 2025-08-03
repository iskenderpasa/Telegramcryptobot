import logging
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from crypto_service import get_crypto_price
from models import db, User
from scheduler import start_scheduler

# Bot token
TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
application = Application.builder().token(TOKEN).build()

# Komut: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = db.session.query(User).filter_by(chat_id=chat_id).first()
    if not user:
        new_user = User(chat_id=chat_id)
        db.session.add(new_user)
        db.session.commit()
    await update.message.reply_text("Botu başlattın. Komutlar için /help yaz.")

# Komut: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Botu başlat
/kar - Kar/Zarar durumu
/fiyat COIN - Coin fiyatı")

# Komut: /kar
async def kar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = db.session.query(User).filter_by(chat_id=chat_id).first()
    if user:
        await update.message.reply_text(f"Kar/Zarar durumu: {user.pnl}")
    else:
        await update.message.reply_text("Kullanıcı kaydı bulunamadı.")

# Komut: /fiyat
async def fiyat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        coin = context.args[0].lower()
        price = get_crypto_price(coin)
        if price:
            await update.message.reply_text(f"{coin.upper()} fiyatı: {price} USDT")
        else:
            await update.message.reply_text("Fiyat alınamadı.")
    else:
        await update.message.reply_text("Kullanım: /fiyat bitcoin")

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("kar", kar))
application.add_handler(CommandHandler("fiyat", fiyat))

def start_bot():
    start_scheduler()
    application.run_polling()
    @dp.message_handler(commands=['fiyat'])
def handle_fiyat(message: types.Message):
    try:
        coin_name = message.text.split()[1].upper()
    except IndexError:
        bot.send_message(message.chat.id, "Lütfen coin adını girin. Örn: /fiyat BTC")
        return

    from crypto_service import get_price
    price = get_price(coin_name)

    if price:
        bot.send_message(message.chat.id, f"{coin_name} fiyatı: {price} USDT")
    else:
        bot.send_message(message.chat.id, f"{coin_name} fiyatı alınamadı.")
        @dp.message_handler(commands=['kar'])
def handle_kar(message: types.Message):
    from models import get_user_assets
    from crypto_service import get_price

    user_id = message.chat.id
    assets = get_user_assets(user_id)

    if not assets:
        bot.send_message(user_id, "Kayıtlı varlık bulunamadı.")
        return

    response = "💰 Kar/Zarar Durumu:\n"
    for asset in assets:
        current_price = get_price(asset.coin)
        if current_price:
            total_value = asset.amount * current_price
            total_cost = asset.amount * asset.buy_price
            profit = total_value - total_cost
            response += f"\n{asset.coin}: {profit:.2f} USDT (Maliyet: {total_cost:.2f}, Değer: {total_value:.2f})"
        else:
            response += f"\n{asset.coin}: Fiyat alınamadı."

    bot.send_message(user_id, response)
