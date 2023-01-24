import pandas as pd
import sys
import getopt
import kontroller
class Secenekler:
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
        Secenekler.borsa = arg
    elif opt in ['-p']:
        Secenekler.aralik = arg
    elif opt in ['-k']:
        Secenekler.kaldir = True
    elif opt in ['-m']:
        Secenekler.mum = arg
    elif opt in ['-s']:
        Secenekler.seviye = arg

sembolDosyasi = pd.read_csv("./data/semboller/"+Secenekler.borsa+".csv")
tumHisseler = sembolDosyasi["Symbol"]
kaldirilmisHisselerDosyasi = pd.read_csv("./data/kalkmis/kalkmis-"+Secenekler.borsa+".csv")
kaldirilmisHisseler = kaldirilmisHisselerDosyasi["0"]

for hisse in tumHisseler:
    if kontroller.fibSeviyeAltinda(hisse, Secenekler):
        uyumluHisseler.append(hisse)

# Raporlama

print("Uyumlu hisseler:" + str(uyumluHisseler))
print(str(len(uyumluHisseler)) + " adet hisse fib uyumlu")
uyumluHisSerisi = pd.Series(uyumluHisseler)
uyumluHisSerisi.to_csv("./data/sonuclar/uyumlu-"+Secenekler.borsa+".csv")

if Secenekler.kaldir:
    print("Kaldirilanlar hisseler:" + str(kaldirilmisHisseler))
    print(str(len(kaldirilmisHisseler)) + " adet hisse kalkmis")
    kaldHisSerisi = pd.Series(kaldirilmisHisseler)
    kaldHisSerisi.to_csv("./data/kalkmis/kalkmis-"+Secenekler.borsa+".csv")
