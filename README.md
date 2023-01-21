# Hisse filtreleme

Fibonacci Geri çekilmesi seviyelerine göre hisse filtreleme yapabilirsiniz.

Fibonachi 4. seviye ( **0.618** ) altında kalan hisseleri bulur

İyi bir internet hızınız varsa, her hissenin kontrolü ortalama 0,25 saniye sürer.

Sonuçlar Excel dosyası halinde verilir.

## Özellikler

* Otomatik kapanış açılış yüksek ve düşük değerlerini düzeltme
* Eksik veri ve karışıklıkları düzeltme
* Günlük aralıklarla veri çekilmesi
* Sorgunun yapılacağı mumların seçimi
* Borsalardan kaldırılmış hisseleri bulma seçeneği

## Kurulum

1. [python 3](https://www.python.org/downloads/) kur

1. **hisse-filtreleme.zip** dosyasını indir, bilgisayara aç.
1. *main.py* dosyasının olduğu klasörde bir terminal (komut satırı) aç.
1. `python -m pip install -r requirements.txt` komutu çalıştır.
1. Programı `python main.py -b de -p 5y` komutu ile çalıştır.

<details><summary>PIP olmadan gerekli paketlerin kurulumu İÇİN TIKLA</summary>
<p>

1. Sistemine *yfinance* eklemek için `pip install yfinance` çalıştır.
1. Sistemine *SciPy* eklemek için `pip install scipy` çalıştır.

</p>
</details>

## Kullanımı

`python .\main.py -b [borsa kodu] -p [periyod kodu]`

* Borsa seçmek için: `-b [kod]`
* Periyod seçmek için: `-p [kod]`

**Tercihen**

* Mum seçmek için: `-m [kod]`

---

**Örneğin**:

 `python .\main.py -b de -p 5y`

 Almanya borsasında 5 yıllık veriler içinde arama yapar, **data** klasörü içinde **uyumlu-de.csv** dosyasını oluşturup, içine sonuçları yazar.

---

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

### Geçerli Mum kodları

Verilerin hangi aralıklarla çekildiği Fibonacci için gerekli değil ancak ilerde gerekebilir.

| Mum  | kod|
|----------|---|
| Yarım Saat |30m|
| Saatlik |60m|
| Günlük  |1d |
| 5 Günlük   |5d |
| Haftalık |1wk |
| Aylık |1mo |
| 3 Aylık|3mo |

### Diğer bağlantılar

[yfinance dökümanları](https://openbase.com/python/yfinance/documentation)

Sembolleri bulmak için:
[Borsalardan işlem gören hisse listelerinin CSV halleri](https://www.nasdaq.com/market-activity/stocks/screener)

---

Yapılacaklar:

* 15 yıllık periyod seçimi eklenecek
