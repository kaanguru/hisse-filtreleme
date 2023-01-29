import csv
borsalar = (
    "Ispanya",
    "Norvec",
    "Yunanistan",
    "NasdaqMega",
    "Almanya",
    "Turkiye",
    "NasdaqMedium",
    "NasdaqLarge",
    "XU050",
    "XU030",
    "XKTUM",
    "XK100",
    "XK050",
)
tumSemboller = []
for borsa in borsalar:
    with open("./data/HisseListeleri/" + borsa + ".csv") as sembolDosyasi:
        ilkSutun = []
        okuyucu = csv.reader(sembolDosyasi)
        for satir in okuyucu:
            ilkSutun.append(satir[0])
        tumSemboller = ilkSutun[1:]
    print(borsa+" = ")
    print(tumSemboller)