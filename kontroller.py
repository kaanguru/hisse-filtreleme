import yfinance as yf
from datetime import date, timedelta
import pandas as pd
onBesYilOncesi = date.today() - timedelta(days=15*365)
bugun = date.today()

def fibSeviyeAltinda(hisse, Filtreler):
    try:
        if Filtreler.borsa == "Turkiye" or Filtreler.borsa.startswith("XK"):
            hisse = hisse + ".IS"
        if Filtreler.borsa == "Norvec":
            hisse = hisse + ".OL"
        if Filtreler.aralik == "15y":
            df = yf.download(
                hisse,
                start=onBesYilOncesi,
                end=bugun,
                auto_adjust=True,
                repair=True,
                interval=Filtreler.mum,
            )
        else:
            df = yf.download(
                hisse,
                period=Filtreler.aralik,
                auto_adjust=True,
                repair=True,
                interval=Filtreler.mum,
            )
        max_deger = df["High"].max()
        min_deger = df["Low"].min()
        fark = max_deger - min_deger
        istenenSeviye = max_deger - fark * float("0."+Filtreler.seviye)
        son_fiyat = df["Close"].iloc[-1]
        if son_fiyat < istenenSeviye:
            return True
    except:
        pass
