from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from models import init_db, get_user_assets
from crypto_service import get_price

API_TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

init_db()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Merhaba! Ben kripto asistan botuyum.")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Komutlar:\n/start\n/help\n/fiyat COIN\n/kar")

@dp.message_handler(commands=['fiyat'])
async def handle_fiyat(message: types.Message):
    try:
        coin_name = message.text.split()[1].upper()
    except IndexError:
        await message.reply("Lütfen coin adını girin. Örn: /fiyat BTC")
        return

    price = get_price(coin_name)
    if price:
        await message.reply(f"{coin_name} fiyatı: {price} USDT")
    else:
        await message.reply(f"{coin_name} fiyatı alınamadı.")

@dp.message_handler(commands=['kar'])
async def handle_kar(message: types.Message):
    user_id = message.chat.id
    assets = get_user_assets(user_id)

    if not assets:
        await message.reply("Kayıtlı varlık bulunamadı.")
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

    await message.reply(response)

def start_bot():
    executor.start_polling(dp, skip_updates=True)
