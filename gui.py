import PySimpleGUI as sg
import pandas as pd
import kontroller

borsalar = ("Turkiye", "Almanya", "Norvec", "Ispanya",
            "Yunanistan", "NASDAQ-Large", "NASDAQ-Medium", "XKTUM", "XK100", "XK050")
periyodlar = ("1y", "2y", "5y", "10y", "15y", "ytd",  "max")
mumlar = ("60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo")
# seviyeler = ("0.382","0.5" "0,618","0.786")
uyumluHisseler = []
csv_yap = False


class Filtreler:
    borsa = None
    aralik = None
    mum = "1d"
    seviye = "618"


sg.theme('Material1')
layout = [[sg.Text('Fibonachi 4. seviye ( 0.618 ) altında kalan hisseleri bulur.')],
          [sg.HorizontalSeparator()],
          [sg.Text('Borsa', size=(12, 1), pad=(2, 2)), sg.Drop(
              borsalar, key="secilenBorsa", default_value="Turkiye")],
          [sg.Text('Zaman Aralığı', size=(12, 1), pad=(2, 2)), sg.Drop(
              periyodlar, key="secilenPeriyod", default_value="10y")],
          [sg.Text('Mum', size=(12, 1), pad=(2, 2)), sg.Drop(
              mumlar, key="secilenMum", default_value="1d")],
          [sg.InputText(uyumluHisseler, use_readonly_for_disable=True,
                        disabled=True, key='-OUTPUT-', focus=True,
                         expand_y=True, expand_x=True)],
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
        sayac = 0
        hisseAdeti = len(tumSemboller)
        for hisse in tumSemboller:
            sayac = sayac + 1
            if kontroller.fibSeviyeAltinda(hisse, Filtreler):
                uyumluHisseler.append(hisse)
            if not sg.one_line_progress_meter('Bekleyin', sayac+1, hisseAdeti, Filtreler.borsa+" Borsasında kontrol edilen: " + str(hisse), grab_anywhere=True) and sayac+1 != hisseAdeti:
                sg.popup_auto_close('Arama iptal ediliyor.')
                break
        uyumluHisSerisi = pd.Series(uyumluHisseler)
        uyumluHisSerisi.to_csv(
            "./data/sonuclar/uyumlu-"+Filtreler.borsa+".csv")
        window['-OUTPUT-'].update(uyumluHisseler)
        sg.popup(f' {len(uyumluHisseler)} adet uyumlu hisse bulundu,',
                 str(uyumluHisseler))

window.close()
