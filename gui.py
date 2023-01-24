import PySimpleGUI as sg
borsalar = ["tr", "de", "no", "es", "gr", "nas"]
periyodlar = ["1y", "2y", "5y", "10y", "ytd", "15y", "max"]
mumlar = ["60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Fibonachi 4. seviye ( 0.618 ) altında kalan hisseleri bulur.')],
          [sg.HorizontalSeparator()],
          [sg.Text('Borsa', size=(12, 1), pad=(2, 2)), sg.Drop(
              borsalar, key="secilenBorsa", size=(4, 6), default_value="tr")],
          [sg.Text('Zaman Aralığı', size=(12, 1), pad=(2, 2)), sg.Drop(
              periyodlar, key="secilenPeriyod", default_value="10y")],
          [sg.Text('Mum', size=(12, 1), pad=(2, 2)), sg.Drop(
              mumlar, key="secilenMum", default_value="1d")],
          [sg.Text(size=(40,2), key='-OUTPUT-')],
          [sg.Ok('Ara', size=(12, 1), pad=(2, 2)), sg.Cancel('İptal', size=(12, 1), pad=(2, 2))]]

# Create the Window
window = sg.Window('Hisse filtreleme', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'İptal':  # if user closes window or clicks cancel
        break
    window['-OUTPUT-'].update(values["secilenBorsa"] + ' Borsası içinde ve ' + values["secilenPeriyod"]+ " zaman aralığında \n arama yapılıyor")

window.close()
