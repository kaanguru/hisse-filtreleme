import yfinance as yf
import pandas as pd
import sys
import getopt
from datetime import date, timedelta

borsa = None
aralik = None
kaldir = False
mum = "1d"
onBesYilOncesi = date.today() - timedelta(days=15*365)
bugun = date.today()
argv = sys.argv[1:]
sembolDosyasi = pd.read_csv("./data/semboller/"+borsa+".csv")
tumHisseler = sembolDosyasi["Symbol"]
uyumluHisseler = []
kaldirilmisHisseler = pd.read_csv("./data/kalkmis/kalkmis"+borsa+".csv")["Symbol"]

try:
    opts, args = getopt.getopt(argv, "b:p:m:k")
except:
    print("Seçenek Hatası")
for opt, arg in opts:
    if opt in ['-b']:
        borsa = arg
    elif opt in ['-p']:
        aralik = arg
    elif opt in ['-k']:
        kaldir = True
    elif opt in ['-m']:
        mum = arg

def fib_seviyeler_arasinda(hisse):
    try:
        if borsa == "tr":
            hisse = hisse + ".IS"
        if aralik == "15y":
            df = yf.download(
                hisse,
                start=onBesYilOncesi,
                end=bugun,
                auto_adjust=True,
                repair=True,
                interval=mum,
            )
        else:
            df = yf.download(
                hisse,
                period=aralik,
                auto_adjust=True,
                repair=True,
                interval=mum,
            )
        if hisse in kaldirilmisHisseler:
            return False

        max_deger = df["High"].max()
        min_deger = df["Low"].min()
        fark = max_deger - min_deger
        dorduncu_seviye = max_deger - fark * 0.618
        son_fiyat = df["Close"].iloc[-1]

        if son_fiyat < dorduncu_seviye:
            return True

    except:
        if kaldir:
            kaldirilmisHisseler.append(hisse)

for hisse in tumHisseler:
    if fib_seviyeler_arasinda(hisse):
        uyumluHisseler.append(hisse)

# Raporlama

print("Uyumlu hisseler:" + str(uyumluHisseler))
print(str(len(uyumluHisseler)) + " adet hisse fib uyumlu")
uyumluHisSerisi = pd.Series(uyumluHisseler)
uyumluHisSerisi.to_csv("./data/sonuclar/uyumlu-"+borsa+".csv")

if kaldir:
    print("Kaldirilanlar hisseler:" + str(kaldirilmisHisseler))
    print(str(len(kaldirilmisHisseler)) + " adet hisse kalkmis")
    kaldHisSerisi = pd.Series(kaldirilmisHisseler)
    kaldHisSerisi.to_csv("./data/kalkmis/kalkmis-"+borsa+".csv")
