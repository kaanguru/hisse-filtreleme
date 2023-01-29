# Hisse filtreleme

Fibonacci Geri çekilmesi seviyelerine göre hisse filtreleme yapabilirsiniz.

Fibonachi seviyeleri altında kalan hisseleri bulur.

![screen](./img/screen.gif)

_İyi bir internet hızınız varsa_, her hissenin kontrolü ortalama 0,2 saniye sürer.

Sonuçlar Excel (CSV) dosyası halinde verilir.

## İçindekiler

- [Özellikler](#ozellikler)
- [Kurulum](#kurulum)
- [Seçenek Kodları](#kodlar)
  - [Ülke BORSA kodları](#ulke)
  - [Periyodlar](#periyodlar)
  - [Mumlar](#mumlar)
- [Linkler](#linkler)

<h2 id="ozellikler">Özellikler</h2>

- Otomatik kapanış açılış yüksek ve düşük değerlerini düzeltme
- Eksik veri ve karışıklıkları düzeltme
- Günlük aralıklarla veri çekilmesi
- Sorgunun yapılacağı mumların seçimi
- Borsalardan kaldırılmış hisseleri bulma seçeneği

<a target="new" href="https://pypi.python.org/pypi/yfinance"><img border=0 src="https://img.shields.io/badge/python-3,%203.1+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://github.com/kaanguru/hisse-filtreleme"><img border=0 src="https://img.shields.io/github/stars/kaanguru/hisse-filtreleme.svg?style=social&label=Star&maxAge=60" alt="Star this repo"></a>

## Kurulum

Windows

1. [python 3](https://www.python.org/downloads/) kur. `python --version` ile kurulumu kontrol et.
1. [hisse-filtreleme.zip](https://github.com/kaanguru/hisse-filtreleme/archive/refs/heads/master.zip) dosyasını indir, bilgisayara aç.
1. _main_ dosyasının olduğu klasörde bir terminal (komut satırı) aç.
1. `python -m pip install -r requirements.txt` komutu çalıştır.
1. Programı `python main.py` komutu ile çalıştır.

<details><summary>MacOS ve Linux İÇİN TIKLA</summary>
<p>

1. [python 3](https://www.python.org/downloads/) kur. `python3 --version` ile kurulumu kontrol et.
1. [hisse-filtreleme.zip](https://github.com/kaanguru/hisse-filtreleme/archive/refs/heads/master.zip) dosyasını indir, bilgisayara aç.
1. _main_ dosyasının olduğu klasörde bir terminal (komut satırı) aç.
1. `python3 -m pip install -r requirements.txt` komutu çalıştır.
1. Programı `python3 main.py` komutu ile çalıştır.

</p>
</details>

---

## Kodlar

<h3 id="ulke"> Ülke/BORSA kodları</h3>

| Ülke | kod|adet|
-------|----|----|
| Norveç |no|22|
| İspanya | es |6|
| Yunanistan |gr |35|
| Almanya |de |25|
| BIST |tr |518|
| NASDAQ |nas |4689|
| Tüm Hisseler ! |all |8025|

**NOT**: _all_ seçeneğinin sonuç bulması yaklaşık 45 dakika sürüyor

### Periyodlar

| Aralık | kod|
|----------|----|
| Günlük   |1d|
| 5 Günlük | 5d |
| Aylık    |1mo |
| 3 Aylık  |3mo |
| 6 Aylık  |6mo |
| Yıllık   |1y |
| 2 Yıllık |2y |
| 5 Yıllık |5y |
| 10 Yıllık|10y |
| 15 Yıllık|15y |
| geçen yıl bu zamandan itibaren |ytd |
| Tüm geçmiş veriler |max |

### Mumlar

_Verilerin hangi aralıklarla çekildiği Fibonacci için gerekli değil ancak ilerde gerekebilir._

| Mum  | kod|
|----------|---|
| Yarım Saat |30m|
| Saatlik |60m|
| 1,5 Saatlik |90m|
| Günlük  |1d |
| 5 Günlük   |5d |
| Haftalık |1wk |
| Aylık |1mo |
| 3 Aylık|3mo |

### Linkler

[yfinance dökümanları](https://openbase.com/python/yfinance/documentation)

Sembolleri bulmak için:
[Borsalardan işlem gören hisse listelerinin CSV halleri](https://www.nasdaq.com/market-activity/stocks/screener)

TODO:

[RSI hesaplama](https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/)

pyinstaller -wF main.py
