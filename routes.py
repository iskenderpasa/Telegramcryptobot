from flask import request
from app import app
from crypto_service import get_price

@app.route('/fiyat', methods=['GET'])
def fiyat_endpoint():
    coin = request.args.get('coin', default='bitcoin', type=str)
    price = get_price(coin)

    if price is None:
        return {"error": "Geçersiz coin ismi veya veri alınamadı."}, 400

    return {"coin": coin, "fiyat_usd": price}
