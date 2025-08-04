import requests

# Sembol-ID eşleştirmesi (gerekirse genişletilir)
COIN_ID_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "INJ": "injective-protocol",
    "RNDR": "render-token",
    "SOL": "solana",
    "AVAX": "avalanche-2",
    "ADA": "cardano",
    "DOT": "polkadot",
    "XRP": "ripple",
    "DOGE": "dogecoin",
    "SHIB": "shiba-inu",
    "OP": "optimism",
    "PENDLE": "pendle"
}

def get_price(coin_symbol):
    try:
        coin_id = COIN_ID_MAP.get(coin_symbol.upper())
        if not coin_id:
            return f"{coin_symbol.upper()} için ID bulunamadı."

        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": coin_id,
                "vs_currencies": "usd"
            }
        )
        data = response.json()
        return data[coin_id]["usd"]
    except Exception as e:
        print(f"Hata: {e}")
        return None
