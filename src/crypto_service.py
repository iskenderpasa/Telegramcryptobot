import requests

def get_crypto_price(coin: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get(coin.lower(), {}).get("usd", None)
    except Exception as e:
        print(f"Hata: {e}")
        return None
