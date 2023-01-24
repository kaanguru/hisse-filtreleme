import yfinance as yf
from datetime import date, timedelta
import pandas as pd
onBesYilOncesi = date.today() - timedelta(days=15*365)
bugun = date.today()


def fibSeviyeAltinda(hisse, Secenekler):
    try:
        kaldirilmisHisselerDosyasi = pd.read_csv(
        "./data/kalkmis/kalkmis-"+Secenekler.borsa+".csv")
        kaldirilmisHisseler = kaldirilmisHisselerDosyasi["0"]
        if Secenekler.borsa == "tr":
            hisse = hisse + ".IS"
        if Secenekler.borsa == "no":
            hisse = hisse + ".OL"
        if Secenekler.aralik == "15y":
            df = yf.download(
                hisse,
                start=onBesYilOncesi,
                end=bugun,
                auto_adjust=True,
                repair=True,
                interval=Secenekler.mum,
            )
        else:
            df = yf.download(
                hisse,
                period=Secenekler.aralik,
                auto_adjust=True,
                repair=True,
                interval=Secenekler.mum,
            )
        if hisse in kaldirilmisHisseler:
            return False

        max_deger = df["High"].max()
        min_deger = df["Low"].min()
        fark = max_deger - min_deger
        istenenSeviye = max_deger - fark * float("0."+Secenekler.seviye)
        son_fiyat = df["Close"].iloc[-1]

        if son_fiyat < istenenSeviye:
            return True
    except:
        if Secenekler.kaldir:
            kaldirilmisHisseler.append(hisse)
