import yfinance as yf
import pandas as pd
import sys
import getopt
borsa = None
donem = None
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "b:p:")

except:
    print("Error")

for opt, arg in opts:
    if opt in ['-b']:
        borsa = arg
    elif opt in ['-p']:
        aralik = arg

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
        kaldirilmisHisseler.append(hisse)


for hisse in tum_hisseler:
    if fib_seviyeler_arasinda(hisse):
        uyumluHisseler.append(hisse)

# Raporlama

print("Uyumlu hisseler:" + str(uyumluHisseler))
print(str(len(uyumluHisseler)) + " adet hisse fib uyumlu")
print("Kaldirilanlar hisseler:" + str(kaldirilmisHisseler))
print(str(len(kaldirilmisHisseler)) + " adet hisse kalkmis")

uyumluHisSerisi = pd.Series(uyumluHisseler)
uyumluHisSerisi.to_csv("./data/uyumlu-"+borsa+".csv")
kaldHisSerisi = pd.Series(kaldirilmisHisseler)
kaldHisSerisi.to_csv("./data/kalkmis-"+borsa+".csv")
