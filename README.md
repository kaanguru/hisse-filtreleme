# Hisse filtreleme

Fibonacci Geri çekilmesi seviyelerine göre hisse filtreleme yapabilirsiniz.

Fibonachi 4. seviye ( **0.618** ) altında kalan hisseleri bulur.

_İyi bir internet hızınız varsa_, her hissenin kontrolü ortalama 0,25 saniye sürer.

Sonuçlar Excel dosyası halinde verilir.

## İçindekiler

- [Özellikler](#ozellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanim)
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

1. [python 3](https://www.python.org/downloads/) kur

1. **hisse-filtreleme.zip** dosyasını indir, bilgisayara aç.
1. _main.py_ dosyasının olduğu klasörde bir terminal (komut satırı) aç.
1. `python -m pip install -r requirements.txt` komutu çalıştır.
1. Programı `python main.py -b de -p 5y` komutu ile çalıştır.

<details><summary>PIP olmadan gerekli paketlerin kurulumu İÇİN TIKLA</summary>
<p>

1. Sistemine _yfinance_ eklemek için `pip install yfinance` çalıştır.
1. Sistemine _SciPy_ eklemek için `pip install scipy` çalıştır.

</p>
</details>

<h2 id="kullanim">Kullanım</h2>

`python .\main.py -b [borsa kodu] -p [periyod kodu]`

- Borsa seçmek için: `-b [kod]`
- Periyod seçmek için: `-p [kod]`

**Tercihen**

- Mum seçmek için: `-m [kod]`

---

**Örneğin**:

 `python .\main.py -b de -p 5y`

 Almanya borsasında 5 yıllık veriler içinde arama yapar, **data** klasörü içinde **uyumlu-de.csv** dosyasını oluşturup, içine sonuçları yazar.

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
| geçen yıl bu zamandan itibaren |ytd |
| Tüm geçmiş veriler |max |

### Mumlar

_Verilerin hangi aralıklarla çekildiği Fibonacci için gerekli değil ancak ilerde gerekebilir._

| Mum  | kod|
|----------|---|
| Yarım Saat |30m|
| Saatlik |60m|
| Günlük  |1d |
| 5 Günlük   |5d |
| Haftalık |1wk |
| Aylık |1mo |
| 3 Aylık|3mo |

### Linkler

[yfinance dökümanları](https://openbase.com/python/yfinance/documentation)

Sembolleri bulmak için:
[Borsalardan işlem gören hisse listelerinin CSV halleri](https://www.nasdaq.com/market-activity/stocks/screener)

---

Yapılacaklar:

- 15 yıllık periyod seçimi eklenecek
