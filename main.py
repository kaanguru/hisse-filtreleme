import yfinance as yf
import pandas as pd
import sys
import getopt
borsa = None
donem = None
kaldir = False
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "b:p:k")

except:
    print("Seçenek Hatası")

for opt, arg in opts:
    if opt in ['-b']:
        borsa = arg
    elif opt in ['-p']:
        aralik = arg
    elif opt in ['-k']:
        kaldir = True

tickers_dosya = pd.read_csv("./data/"+borsa+".csv")
tum_hisseler = tickers_dosya["Symbol"]
uyumluHisseler = []
kaldirilmisHisseler = [
    "ALXN",
    "ANTM",
    "BF.B",
    "BLL",
    "BRK.B",
    "CERN",
    "COG",
    "CTXS",
    "CXO",
    "DISCA",
    "DISCK",
    "FB",
    "FLIR",
    "HFC",
    "INFO",
    "KSU",
    "LB",
    "MXIM",
    "NLOK",
    "NLSN",
    "PBCT",
    "TIF",
    "VAR",
    "VIAC",
    "WLTW",
    "XLNX",
]


def fib_seviyeler_arasinda(hisse):
    # hisse için bir yıllık verileri çek
    try:
        if borsa == "tr":
            hisse = hisse + ".IS"
        df = yf.download(
            hisse,
            period=aralik,
            auto_adjust=True,
            repair=True,
        )
        if hisse in kaldirilmisHisseler:
            return False

        # Fibonacci sabitleri
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


for hisse in tum_hisseler:
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
