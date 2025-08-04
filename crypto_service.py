import requests

def get_price(coin_name: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_name.lower()}&vs_currencies=usd"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if coin_name.lower() in data:
            price = data[coin_name.lower()]['usd']
            return f"{coin_name.capitalize()} şu anda {price} USD civarında işlem görüyor."
        else:
            return f"{coin_name.capitalize()} için fiyat verisi bulunamadı. İsmi doğru yazdığınızdan emin olun."

    except requests.exceptions.RequestException as e:
        return f"Fiyat alınırken bir hata oluştu: {e}"
