import pandas as pd
import sys
import getopt
import kontroller

class Filtreler:
    borsa = None
    aralik = None
    mum = "1d"
    seviye = "618"
    kaldir = False
argv = sys.argv[1:]
uyumluHisseler = []

try:
    opts, args = getopt.getopt(argv, "b:p:m:k:s")
except:
    print("Seçenek Hatası")
for opt, arg in opts:
    if opt in ['-b']:
        Filtreler.borsa = arg
    elif opt in ['-p']:
        Filtreler.aralik = arg
    elif opt in ['-k']:
        Filtreler.kaldir = True
    elif opt in ['-m']:
        Filtreler.mum = arg
    elif opt in ['-s']:
        Filtreler.seviye = arg

sembolDosyasi = pd.read_csv("./data/semboller/"+Filtreler.borsa+".csv")
tumSemboller = sembolDosyasi["Symbol"]
kaldirilmisHisselerDosyasi = pd.read_csv("./data/kalkmis/kalkmis-"+Filtreler.borsa+".csv")
kaldirilmisHisseler = kaldirilmisHisselerDosyasi["0"]

for hisse in tumSemboller:
    if kontroller.fibSeviyeAltinda(hisse, Filtreler):
        uyumluHisseler.append(hisse)

# Raporlama

print("Uyumlu hisseler:" + str(uyumluHisseler))
print(str(len(uyumluHisseler)) + " adet hisse fib uyumlu")
uyumluHisSerisi = pd.Series(uyumluHisseler)
uyumluHisSerisi.to_csv("./data/sonuclar/uyumlu-"+Filtreler.borsa+".csv")

if Filtreler.kaldir:
    print("Kaldirilanlar hisseler:" + str(kaldirilmisHisseler))
    print(str(len(kaldirilmisHisseler)) + " adet hisse kalkmis")
    kaldHisSerisi = pd.Series(kaldirilmisHisseler)
    kaldHisSerisi.to_csv("./data/kalkmis/kalkmis-"+Filtreler.borsa+".csv")
