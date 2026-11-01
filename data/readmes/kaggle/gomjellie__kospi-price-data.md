# Kospi Stock Price

Korean Stock Kospi Prices

# Context

I got all these .csv files using `pandas data reader` but getting every single kospi data through `pandas data reader` is annoying. so I decided to share this files.

# Content

### Files

kospi.csv contains average kospi price. you can use this for checking whether if korean stock is day-off or not.
xxxxxx.csv contains each single price records. xxxxxx is it's unique ticker.

### Columns

Date

```
format - \d{4}-\d{2}-\d{2}
```

Open

```
format - \d{1,}\.\d{1}
```

High

```
format - \d{1,}\.\d{1}
```

Low

```
format - \d{1,}\.\d{1}
```

Close

```
format - \d{1,}\.\d{1}
```

 Adj Close

```
format - \d{1,}\.\d{1}
```

Volume

```
format - \d+
```

# Acknowledgements

[blog post](https://gomjellie.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/pandas/%EC%A3%BC%EC%8B%9D/2017/06/09/pandas-datareader-stock.html) which describes how i got these data's. you might need this to update csv files.

[git repository](https://github.com/gomjellie/kospi-kosdaq-csv) git repository 


# Inspiration

Good luck.

출처: Kaggle (gomjellie/kospi-price-data)
태그: business, finance, economics, investing
라이선스: CC0: Public Domain
수정일: 2017-09-30T16:34:39.083Z
