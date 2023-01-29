import csv
borsalar = (
    "Ispanya",
    "Norvec",
    "Yunanistan",
    "NASDAQ-Mega",
    "Almanya",
    "Turkiye",
    "NASDAQ-Large",
    "NASDAQ-Medium",
    "XKTUM"
)
tumSemboller = []
for borsa in borsalar:
    with open("./data/semboller/" + borsa + ".csv") as sembolDosyasi:
        ilkSutun = []
        okuyucu = csv.reader(sembolDosyasi)
        for satir in okuyucu:
            ilkSutun.append(satir[0])
        tumSemboller = ilkSutun[1:]
    print(borsa+" = ")
    print(tumSemboller)