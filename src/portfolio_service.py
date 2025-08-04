import crypto_service

# Örnek portföy verisi (gerçek kullanımda DB'den okunacak)
portfolio = {
    "INJ": {
        "adet": 1.09,
        "alis": 13.75
    },
    "RNDR": {
        "adet": 8.57,
        "alis": 3.79
    },
    "PENDLE": {
        "adet": 2.5,
        "alis": 4.00
    }
}

def kar_zarar_ozeti():
    mesaj = "💼 *Portföy Özeti:*\n"
    toplam_kar_usdt = 0

    for coin, veri in portfolio.items():
        adet = veri["adet"]
        alis = veri["alis"]
        mevcut_fiyat = crypto_service.get_price(coin)
        if mevcut_fiyat is None:
            mesaj += f"{coin}: Fiyat alınamadı.\n"
            continue

        toplam_alis = adet * alis
        toplam_mevcut = adet * mevcut_fiyat
        kar = toplam_mevcut - toplam_alis
        yuzde = (kar / toplam_alis) * 100 if toplam_alis else 0
        toplam_kar_usdt += kar

        mesaj += (
            f"• {coin}:\n"
            f"  - Alış: {alis:.2f} × {adet} = {toplam_alis:.2f} USDT\n"
            f"  - Şimdi: {mevcut_fiyat:.2f} × {adet} = {toplam_mevcut:.2f} USDT\n"
            f"  - Kar/Zarar: {'+' if kar >= 0 else ''}{kar:.2f} USDT ({yuzde:.2f}%)\n"
        )

    mesaj += f"\n📊 *Toplam Kar/Zarar:* {'+' if toplam_kar_usdt >= 0 else ''}{toplam_kar_usdt:.2f} USDT"
    return mesaj
