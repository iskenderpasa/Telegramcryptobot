import requests

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usdt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get(symbol, {}).get("usdt")
    except Exception:
        return None