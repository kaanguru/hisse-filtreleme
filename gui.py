import PySimpleGUI as sg
import pandas as pd
import kontroller

borsalar = ("Turkiye", "Almanya", "Norvec", "Ispanya",
            "Yunanistan", "NASDAQ-Large", "NASDAQ-Medium")
periyodlar = ("1y", "2y", "5y", "10y", "15y", "ytd",  "max")
mumlar = ("60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo")
# seviyeler = ("0.382","0.5" "0,618","0.786")
class Filtreler:
    borsa = None
    aralik = None
    mum = "1d"
    seviye = "618"
uyumluHisseler = [""]

sg.theme('DarkAmber')  
layout = [[sg.Text('Fibonachi 4. seviye ( 0.618 ) altında kalan hisseleri bulur.')],
          [sg.HorizontalSeparator()],
          [sg.Text('Borsa', size=(12, 1), pad=(2, 2)), sg.Drop(
              borsalar, key="secilenBorsa", enable_events=True)],
          [sg.Text('Zaman Aralığı', size=(12, 1), pad=(2, 2)), sg.Drop(
              periyodlar, key="secilenPeriyod", default_value="10y")],
          [sg.Text('Mum', size=(12, 1), pad=(2, 2)), sg.Drop(
              mumlar, key="secilenMum", default_value="1d")],
          [sg.Table(uyumluHisseler,size=(40, 2), key='-OUTPUT-')],
          [sg.B('Ara', size=(12, 1), pad=(2, 2)), sg.Cancel('İptal', size=(12, 1), pad=(2, 2))]]
window = sg.Window('Hisse filtreleme', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'İptal': 
        break
    if event == event == "Ara":
        Filtreler.borsa = values["secilenBorsa"]
        Filtreler.aralik = values["secilenPeriyod"]
        Filtreler.mum = values["secilenMum"]
        sembolDosyasi = pd.read_csv("./data/semboller/"+Filtreler.borsa+".csv")
        tumSemboller = sembolDosyasi["Symbol"]
        print(Filtreler.borsa)
        print(Filtreler.aralik)
        print(Filtreler.mum)
        for hisse in tumSemboller:
            if kontroller.fibSeviyeAltinda(hisse, Filtreler):
                uyumluHisseler.append(hisse)
        window['-OUTPUT-'].update(values = uyumluHisseler)
        print(uyumluHisseler)

window.close()
