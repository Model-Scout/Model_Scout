---
license: odc-by
task_categories:
- text-generation
language:
- en
- de
- fr
- pl
- es
- ru
- it
- ar
- pt
- tr
- el
- vi
- ro
- zh
- uk
- ko
- hi
- nl
pretty_name: FineNews-unfiltered
configs:
- config_name: CC-NEWS-2024-05
  data_files:
  - split: en
    path: data/CC-NEWS-2024-05/en/*
  - split: es
    path: data/CC-NEWS-2024-05/es/*
  - split: ru
    path: data/CC-NEWS-2024-05/ru/*
  - split: it
    path: data/CC-NEWS-2024-05/it/*
  - split: de
    path: data/CC-NEWS-2024-05/de/*
  - split: ar
    path: data/CC-NEWS-2024-05/ar/*
  - split: fr
    path: data/CC-NEWS-2024-05/fr/*
  - split: pl
    path: data/CC-NEWS-2024-05/pl/*
  - split: pt
    path: data/CC-NEWS-2024-05/pt/*
  - split: tr
    path: data/CC-NEWS-2024-05/tr/*
  - split: el
    path: data/CC-NEWS-2024-05/el/*
  - split: vi
    path: data/CC-NEWS-2024-05/vi/*
  - split: ro
    path: data/CC-NEWS-2024-05/ro/*
  - split: zh
    path: data/CC-NEWS-2024-05/zh/*
  - split: uk
    path: data/CC-NEWS-2024-05/uk/*
  - split: ko
    path: data/CC-NEWS-2024-05/ko/*
  - split: hi
    path: data/CC-NEWS-2024-05/hi/*
  - split: nl
    path: data/CC-NEWS-2024-05/nl/*
- config_name: CC-NEWS-2024-04
  data_files:
  - split: en
    path: data/CC-NEWS-2024-04/en/*
  - split: es
    path: data/CC-NEWS-2024-04/es/*
  - split: ru
    path: data/CC-NEWS-2024-04/ru/*
  - split: it
    path: data/CC-NEWS-2024-04/it/*
  - split: de
    path: data/CC-NEWS-2024-04/de/*
  - split: ar
    path: data/CC-NEWS-2024-04/ar/*
  - split: fr
    path: data/CC-NEWS-2024-04/fr/*
  - split: pl
    path: data/CC-NEWS-2024-04/pl/*
  - split: pt
    path: data/CC-NEWS-2024-04/pt/*
  - split: tr
    path: data/CC-NEWS-2024-04/tr/*
  - split: el
    path: data/CC-NEWS-2024-04/el/*
  - split: vi
    path: data/CC-NEWS-2024-04/vi/*
  - split: ro
    path: data/CC-NEWS-2024-04/ro/*
  - split: zh
    path: data/CC-NEWS-2024-04/zh/*
  - split: uk
    path: data/CC-NEWS-2024-04/uk/*
  - split: ko
    path: data/CC-NEWS-2024-04/ko/*
  - split: hi
    path: data/CC-NEWS-2024-04/hi/*
  - split: nl
    path: data/CC-NEWS-2024-04/nl/*
- config_name: CC-NEWS-2024-03
  data_files:
  - split: en
    path: data/CC-NEWS-2024-03/en/*
  - split: es
    path: data/CC-NEWS-2024-03/es/*
  - split: ru
    path: data/CC-NEWS-2024-03/ru/*
  - split: it
    path: data/CC-NEWS-2024-03/it/*
  - split: de
    path: data/CC-NEWS-2024-03/de/*
  - split: ar
    path: data/CC-NEWS-2024-03/ar/*
  - split: fr
    path: data/CC-NEWS-2024-03/fr/*
  - split: pl
    path: data/CC-NEWS-2024-03/pl/*
  - split: pt
    path: data/CC-NEWS-2024-03/pt/*
  - split: tr
    path: data/CC-NEWS-2024-03/tr/*
  - split: el
    path: data/CC-NEWS-2024-03/el/*
  - split: vi
    path: data/CC-NEWS-2024-03/vi/*
  - split: ro
    path: data/CC-NEWS-2024-03/ro/*
  - split: zh
    path: data/CC-NEWS-2024-03/zh/*
  - split: uk
    path: data/CC-NEWS-2024-03/uk/*
  - split: ko
    path: data/CC-NEWS-2024-03/ko/*
  - split: hi
    path: data/CC-NEWS-2024-03/hi/*
  - split: nl
    path: data/CC-NEWS-2024-03/nl/*
---

# FineNews
WIP. Like FineWeb, but built from [Common Crawl News](https://commoncrawl.org/news-crawl) instead of main web.
For languages not listed as a *split*, check the `data/` directory.

For now, it contains the 2024-05 (May),-04 (April),-03 (March) dumps.

This is the unfiltered version, with only URL filtering applied.

## Some initial stats
Total number of documents: 35M

|Dump|Number of docs|Disk size (compressed)|
|---|--:|--:|
|CC-NEWS-2024-05|11_715_084|11G|
|CC-NEWS-2024-04|11_546_298|11G|
|CC-NEWS-2024-03|11_723_542|11G|


Sizes of some example language: CC-NEWS-2024-05
|Language|Number of docs|Disk size (compressed)|
|---|--:|--:|
|en|3_743_387|4.1G|
|es|1_168_430|1.3G|
|it|743_788|0.7G|
|de|411_926|0.4G|
|fr|333_473|0.3G|
|pl|278_893|0.3G|
|nl|43_447|0.0G|

Top-20 top-level-domains: CC-NEWS-2024-05/en
|TLD|count|
|---|--:|
condesan-ecoandes.org|374080
webcatalog.io|127105
yahoo.com|99864
wise.com|86548
dailymail.co.uk|77523
indiatimes.com|56276
wkrb13.com|47591
tickerreport.com|42761
themarketsdaily.com|38557
nasdaq.com|37142
racenet.com.au|36946
goal.com|35318
theenterpriseleader.com|35239
einpresswire.com|34453
hindustantimes.com|31307
etfdailynews.com|28246
business-standard.com|27994
thehindu.com|27433
cbsnews.com|26197
westernjournal.com|23199

Top-20 top-level-domains: CC-NEWS-2024-05/de
|TLD|count|
|---|--:|
presseportal.de|19146
augsburger-allgemeine.de|15191
finanzen.net|13621
rp-online.de|11455
rheinpfalz.de|11422
mz.de|11222
volksstimme.de|11178
rhein-zeitung.de|10147
onvista.de|8773
wise.com|8713
tag24.de|8353
abendblatt.de|7098
krone.at|7022
saarbruecker-zeitung.de|6302
swr.de|6228
handball.net|5720
prosieben.de|5611
derwesten.de|5585
braunschweiger-zeitung.de|5536
kicker.de|5450
