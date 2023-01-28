import csv
import PySimpleGUI as sg

import kontroller

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
periyodlar = ("1y", "2y", "5y", "10y", "15y", "ytd", "max")
mumlar = ("60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo")
seviyeler = ("236", "382", "5", "618", "786")
uyumluHisseler = []

class Filtreler:
    borsa = None
    aralik = None
    mum = "1d"
    seviye = "618"

sg.theme("Material1")
layout = [
    [sg.Text("Fibonachi seviyeleri altında kalan hisseleri bulur.")],
    [sg.Image(filename="./fibo.png")],
    [sg.HorizontalSeparator()],
    [
        sg.Text("Borsa", size=(16, 1), pad=(2, 2)),
        sg.Drop(borsalar, key="secilenBorsa", default_value="Turkiye"),
    ],
    [
        sg.Text("Zaman Aralığı", size=(16, 1), pad=(2, 2)),
        sg.Drop(periyodlar, key="secilenPeriyod", default_value="10y"),
    ],
    [
        sg.Text("Mum", size=(16, 1), pad=(2, 2)),
        sg.Drop(mumlar, key="secilenMum", default_value="1d"),
    ],
    [
        sg.Text("Fibo. Seviyesi        0.", size=(16, 1), pad=(2, 2)),
        sg.Drop(seviyeler, key="secilenSeviye", default_value="618"),
    ],
    [
        sg.InputText(
            uyumluHisseler,
            use_readonly_for_disable=True,
            disabled=True,
            key="-OUTPUT-",
            focus=True,
            expand_y=True,
            expand_x=True,
        )
    ],
    [
        sg.B("Ara", size=(16, 1), pad=(2, 2)),
        sg.Cancel("İptal", size=(16, 1), pad=(2, 2)),
    ],
]
window = sg.Window("Hisse Filtreleme", layout)
while True:
    event, values = window.read()
    if event == event == "Ara":
        Filtreler.borsa = values["secilenBorsa"]
        Filtreler.aralik = values["secilenPeriyod"]
        Filtreler.mum = values["secilenMum"]
        Filtreler.seviye = values["secilenSeviye"]
        tumSemboller = []
        with open("./data/semboller/" + Filtreler.borsa + ".csv") as sembolDosyasi:
            ilkSutun = []
            reader = csv.reader(sembolDosyasi)
            for row in reader:
                ilkSutun.append(row[0])
            tumSemboller = ilkSutun[1:]
        # sembolDosyasi = pd.read_csv("./data/semboller/" + Filtreler.borsa + ".csv")
        # tumSemboller = sembolDosyasi["Symbol"]
        sayac = 0
        hisseAdeti = len(tumSemboller)
        for hisse in tumSemboller:
            sayac = sayac + 1
            uyumluHisseler.clear
            if kontroller.fibSeviyeAltinda(hisse, Filtreler):
                uyumluHisseler.append(hisse)
            if (
                not sg.one_line_progress_meter(
                    "Bekleyin",
                    sayac + 1,
                    hisseAdeti,
                    Filtreler.borsa + " Borsasında kontrol edilen: " + str(hisse),
                    grab_anywhere=True,
                )
                and sayac + 1 != hisseAdeti
            ):
                sg.popup_auto_close("Arama iptal ediliyor.")
                break
        # uyumluHisSerisi = pd.Series(uyumluHisseler)
        # uyumluHisSerisi.to_csv("./data/sonuclar/Fib-Uyumlu-" + Filtreler.borsa + ".csv")
        window["-OUTPUT-"].update(uyumluHisseler)
        sg.clipboard_set(new_value=str(uyumluHisseler))
        sg.popup(
            f" {len(uyumluHisseler)} adet uyumlu hisse bulundu,yapıştırabilirsiniz",
            str(uyumluHisseler),
        )
    if event == sg.WIN_CLOSED or event == "İptal":
        break
window.close()
