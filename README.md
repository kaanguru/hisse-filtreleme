# Hisse filtreleme

Fibonacci Geri çekilmesi seviyelerine göre hisse filtreleme yapabilirsiniz.

Fibonachi 4. seviye ( **0.618** ) altında kalan hisseleri bulur.

İyi bir internet hızınız varsa, her hissenin kontrolü ortalama 0,25 saniye sürer.

## Kurulum

1. [python 3](https://www.python.org/downloads/) kur

1. **hisse-filtreleme.zip** dosyasını indir, bilgisayara aç.
1. main.py dosyasının olduğu klasörde bir terminal (komut satırı) aç.
1. Sistemine _yfinance_ eklemek için `pip install yfinance` çalıştır.
1. `python main.py` çalıştır.

**Varsayılan olarak:** 5 yıllık zaman dilimi içinde 4800 nasdaq hisseleri içinde arama yapar.

* Borsa seçmek için: `main -b [kod]`
* Periyod seçmek için: `main -p [kod]`

**Örneğin**: `python .\main.py -b de -p 5y` komutu tüm Almanya borsasında 5 yıllık veriler içinde arama yapar, **data** klasörü içinde **uyumlu-de.csv** dosyasını oluşturup, içine sonuçları yazar.

## Kodlar

### Ülke BORSA kodları

| ülke | kod|
-------|----|
| Norveç |no|
| İspanya | es |
| Yunanistan |gr |
| Almanya |de |
| BIST |tr |
| NASDAQ |nas |

### Geçerli periyodlar

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

### Diğer bağlantılar

[yfinance dökümanları](https://openbase.com/python/yfinance/documentation)

[Borsalardan işlem gören hisse listelerinin CSV halleri](https://www.nasdaq.com/market-activity/stocks/screener)

#### adjust all OHLC automatically

        # (optional, default is False)
        auto_adjust = True,

        # attempt repair of missing data or currency mixups e.g. $/cents
        repair = False,

---

TODO:

* 15 yıllık periyod seçimi ekle
