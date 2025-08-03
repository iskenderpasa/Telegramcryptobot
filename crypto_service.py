import requests

def get_price(coin_symbol):
    try:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_symbol}&vs_currencies=usd'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if coin_symbol in data and 'usd' in data[coin_symbol]:
                return data[coin_symbol]['usd']
            else:
                return None
        else:
            return None
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None
