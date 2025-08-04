from src.crypto_service import get_crypto_price
from telegram import Bot

# Telegram bildirim için ayarlar
CHAT_ID = 583677323
TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
bot = Bot(token=TOKEN)

# Portföy: coin sembolü -> (adet, alış fiyatı)
PORTFOLIO = {
    "inj": [(1.09, 13.75), (2.13, 12.692)],
    "rndr": [(8.57, 3.79), (7.14, 4.20), (6.97, 3.47)],
    "pendle": [(2.5, 4.00)],
}

def calculate_portfolio_value():
    total_buy_value = 0
    total_current_value = 0
    message = "📊 *Portföy Özeti:*\n\n"

    for coin, entries in PORTFOLIO.items():
        total_amount = sum(e[0] for e in entries)
        avg_buy_price = sum(e[0] * e[1] for e in entries) / total_amount
        current_price = get_crypto_price(coin)
        if current_price is None:
            continue
        current_value = total_amount * current_price
        buy_value = total_amount * avg_buy_price
        total_buy_value += buy_value
        total_current_value += current_value

        pnl = current_value - buy_value
        pnl_pct = (pnl / buy_value) * 100

        message += f"💰 {coin.upper()}: {total_amount:.2f} adet\n"
        message += f"   - Alış: {avg_buy_price:.2f} USDT\n"
        message += f"   - Şu an: {current_price:.2f} USDT\n"
        message += f"   - Kar/Zarar: {pnl:.2f} USDT ({pnl_pct:.2f}%)\n\n"

    total_pnl = total_current_value - total_buy_value
    total_pct = (total_pnl / total_buy_value) * 100 if total_buy_value > 0 else 0

    message += f"📈 *Genel Kar/Zarar:* {total_pnl:.2f} USDT ({total_pct:.2f}%)"
    return message

def send_portfolio_summary():
    summary = calculate_portfolio_value()
    bot.send_message(chat_id=CHAT_ID, text=summary, parse_mode="Markdown")
