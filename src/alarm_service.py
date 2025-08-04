import requests
import time
from threading import Thread
from crypto_service import get_price

BOT_TOKEN = "8049173481:AAEb19lLTxrMc7LJcstsxLMKW3fYMGfFybo"
CHAT_ID = 583677323

# Basit alarm yapısı: { "coin": "INJ", "fiyat": 14.00 }
alarmlar = []

def alarm_ekle(coin, fiyat):
    try:
        fiyat = float(fiyat)
        alarmlar.append({"coin": coin.upper(), "fiyat": fiyat})
        return f"🔔 Alarm ayarlandı: {coin.upper()} > {fiyat} USDT"
    except:
        return "Hatalı fiyat girdisi. Örn: /alarm INJ 14.00"

def alarm_kontrol():
    while True:
        for alarm in alarmlar[:]:
            coin = alarm["coin"]
            hedef_fiyat = alarm["fiyat"]
            anlik_fiyat = get_price(coin)

            if anlik_fiyat and anlik_fiyat >= hedef_fiyat:
                mesaj = f"🚨 {coin} fiyatı {anlik_fiyat:.2f} USDT’ye ulaştı (Alarm: {hedef_fiyat})"
                send_message(mesaj)
                alarmlar.remove(alarm)

        time.sleep(60)  # 1 dakikada bir kontrol

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

def start_alarm_thread():
    t = Thread(target=alarm_kontrol)
    t.daemon = True
    t.start()
