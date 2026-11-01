---
license: other
license_name: basis-data-license-1.0
license_link: LICENSE
language:
- af
- ak
- am
- ar
- as
- az
- bg
- bn
- bs
- ceb
- cnr
- cs
- da
- de
- el
- en
- es
- et
- fi
- fil
- fr
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ky
- lg
- ln
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- nb
- ne
- nl
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- rw
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tk
- tr
- uk
- ur
- uz
- vi
- wo
- xh
- yue
- zh
- zu
language_creators:
- crowdsourced
multilinguality: multilingual
source_datasets:
- original
extra_gated_heading: Request access
extra_gated_description: Listen to samples at https://withbasis.co/open/global-emotions. Requests are reviewed by a person.
extra_gated_prompt: This dataset contains recordings of real people. By requesting access you agree not to try to identify, locate or contact any speaker, not to use the data to impersonate a specific person, not to reconstruct anything that was removed, and to use it under the terms in the LICENSE file.
extra_gated_fields:
  Name: text
  Institution: text
  Work email: text
  Role/position: text
  I agree to the terms above: checkbox
extra_gated_button_content: Request access
pretty_name: Basis Global Emotions
task_categories:
- text-to-speech
- audio-classification
task_ids:
- audio-emotion-recognition
tags:
- audio
- multilingual
- emotional-speech
- expressive-speech
- emotion
- delivery-style
- paired-recordings
- speech
- speech-emotion-recognition
- nonverbal-vocalizations
size_categories:
- 100K<n<1M
configs:
- config_name: af-ZA
  data_files:
  - split: train
    path: data/af-ZA/train-*.parquet
- config_name: ak-GH
  data_files:
  - split: train
    path: data/ak-GH/train-*.parquet
- config_name: am-ET
  data_files:
  - split: train
    path: data/am-ET/train-*.parquet
- config_name: ar-DZ
  data_files:
  - split: train
    path: data/ar-DZ/train-*.parquet
- config_name: ar-EG
  data_files:
  - split: train
    path: data/ar-EG/train-*.parquet
- config_name: ar-JO
  data_files:
  - split: train
    path: data/ar-JO/train-*.parquet
- config_name: ar-LB
  data_files:
  - split: train
    path: data/ar-LB/train-*.parquet
- config_name: ar-LY
  data_files:
  - split: train
    path: data/ar-LY/train-*.parquet
- config_name: ar-MA
  data_files:
  - split: train
    path: data/ar-MA/train-*.parquet
- config_name: ar-SA
  data_files:
  - split: train
    path: data/ar-SA/train-*.parquet
- config_name: ar-TN
  data_files:
  - split: train
    path: data/ar-TN/train-*.parquet
- config_name: as-IN
  data_files:
  - split: train
    path: data/as-IN/train-*.parquet
- config_name: az-AZ
  data_files:
  - split: train
    path: data/az-AZ/train-*.parquet
- config_name: bg-BG
  data_files:
  - split: train
    path: data/bg-BG/train-*.parquet
- config_name: bn-BD
  data_files:
  - split: train
    path: data/bn-BD/train-*.parquet
- config_name: bn-IN
  data_files:
  - split: train
    path: data/bn-IN/train-*.parquet
- config_name: bs-BA
  data_files:
  - split: train
    path: data/bs-BA/train-*.parquet
- config_name: ceb-PH
  data_files:
  - split: train
    path: data/ceb-PH/train-*.parquet
- config_name: cnr-ME
  data_files:
  - split: train
    path: data/cnr-ME/train-*.parquet
- config_name: cs-CZ
  data_files:
  - split: train
    path: data/cs-CZ/train-*.parquet
- config_name: da-DK
  data_files:
  - split: train
    path: data/da-DK/train-*.parquet
- config_name: de-DE
  data_files:
  - split: train
    path: data/de-DE/train-*.parquet
- config_name: el-CY
  data_files:
  - split: train
    path: data/el-CY/train-*.parquet
- config_name: el-GR
  data_files:
  - split: train
    path: data/el-GR/train-*.parquet
- config_name: en-AU
  data_files:
  - split: train
    path: data/en-AU/train-*.parquet
- config_name: en-CA
  data_files:
  - split: train
    path: data/en-CA/train-*.parquet
- config_name: en-GB
  data_files:
  - split: train
    path: data/en-GB/train-*.parquet
- config_name: en-NZ
  data_files:
  - split: train
    path: data/en-NZ/train-*.parquet
- config_name: en-US
  data_files:
  - split: train
    path: data/en-US/train-*.parquet
- config_name: es-AR
  data_files:
  - split: train
    path: data/es-AR/train-*.parquet
- config_name: es-CL
  data_files:
  - split: train
    path: data/es-CL/train-*.parquet
- config_name: es-CO
  data_files:
  - split: train
    path: data/es-CO/train-*.parquet
- config_name: es-DO
  data_files:
  - split: train
    path: data/es-DO/train-*.parquet
- config_name: es-EC
  data_files:
  - split: train
    path: data/es-EC/train-*.parquet
- config_name: es-ES
  data_files:
  - split: train
    path: data/es-ES/train-*.parquet
- config_name: es-GT
  data_files:
  - split: train
    path: data/es-GT/train-*.parquet
- config_name: es-MX
  data_files:
  - split: train
    path: data/es-MX/train-*.parquet
- config_name: es-PE
  data_files:
  - split: train
    path: data/es-PE/train-*.parquet
- config_name: et-EE
  data_files:
  - split: train
    path: data/et-EE/train-*.parquet
- config_name: fi-FI
  data_files:
  - split: train
    path: data/fi-FI/train-*.parquet
- config_name: fil-PH
  data_files:
  - split: train
    path: data/fil-PH/train-*.parquet
- config_name: fr-FR
  data_files:
  - split: train
    path: data/fr-FR/train-*.parquet
- config_name: gu-IN
  data_files:
  - split: train
    path: data/gu-IN/train-*.parquet
- config_name: he-IL
  data_files:
  - split: train
    path: data/he-IL/train-*.parquet
- config_name: hi-IN
  data_files:
  - split: train
    path: data/hi-IN/train-*.parquet
- config_name: hr-HR
  data_files:
  - split: train
    path: data/hr-HR/train-*.parquet
- config_name: hu-HU
  data_files:
  - split: train
    path: data/hu-HU/train-*.parquet
- config_name: hy-AM
  data_files:
  - split: train
    path: data/hy-AM/train-*.parquet
- config_name: id-ID
  data_files:
  - split: train
    path: data/id-ID/train-*.parquet
- config_name: it-IT
  data_files:
  - split: train
    path: data/it-IT/train-*.parquet
- config_name: ja-JP
  data_files:
  - split: train
    path: data/ja-JP/train-*.parquet
- config_name: jv-ID
  data_files:
  - split: train
    path: data/jv-ID/train-*.parquet
- config_name: ka-GE
  data_files:
  - split: train
    path: data/ka-GE/train-*.parquet
- config_name: kk-KZ
  data_files:
  - split: train
    path: data/kk-KZ/train-*.parquet
- config_name: km-KH
  data_files:
  - split: train
    path: data/km-KH/train-*.parquet
- config_name: kn-IN
  data_files:
  - split: train
    path: data/kn-IN/train-*.parquet
- config_name: ko-KR
  data_files:
  - split: train
    path: data/ko-KR/train-*.parquet
- config_name: ky-KG
  data_files:
  - split: train
    path: data/ky-KG/train-*.parquet
- config_name: lg-UG
  data_files:
  - split: train
    path: data/lg-UG/train-*.parquet
- config_name: ln-CD
  data_files:
  - split: train
    path: data/ln-CD/train-*.parquet
- config_name: lo-LA
  data_files:
  - split: train
    path: data/lo-LA/train-*.parquet
- config_name: lt-LT
  data_files:
  - split: train
    path: data/lt-LT/train-*.parquet
- config_name: lv-LV
  data_files:
  - split: train
    path: data/lv-LV/train-*.parquet
- config_name: mg-MG
  data_files:
  - split: train
    path: data/mg-MG/train-*.parquet
- config_name: mk-MK
  data_files:
  - split: train
    path: data/mk-MK/train-*.parquet
- config_name: ml-IN
  data_files:
  - split: train
    path: data/ml-IN/train-*.parquet
- config_name: mn-MN
  data_files:
  - split: train
    path: data/mn-MN/train-*.parquet
- config_name: mr-IN
  data_files:
  - split: train
    path: data/mr-IN/train-*.parquet
- config_name: ms-MY
  data_files:
  - split: train
    path: data/ms-MY/train-*.parquet
- config_name: nb-NO
  data_files:
  - split: train
    path: data/nb-NO/train-*.parquet
- config_name: ne-NP
  data_files:
  - split: train
    path: data/ne-NP/train-*.parquet
- config_name: nl-NL
  data_files:
  - split: train
    path: data/nl-NL/train-*.parquet
- config_name: om-ET
  data_files:
  - split: train
    path: data/om-ET/train-*.parquet
- config_name: or-IN
  data_files:
  - split: train
    path: data/or-IN/train-*.parquet
- config_name: pa-IN
  data_files:
  - split: train
    path: data/pa-IN/train-*.parquet
- config_name: pl-PL
  data_files:
  - split: train
    path: data/pl-PL/train-*.parquet
- config_name: ps-PK
  data_files:
  - split: train
    path: data/ps-PK/train-*.parquet
- config_name: pt-BR
  data_files:
  - split: train
    path: data/pt-BR/train-*.parquet
- config_name: pt-PT
  data_files:
  - split: train
    path: data/pt-PT/train-*.parquet
- config_name: ro-RO
  data_files:
  - split: train
    path: data/ro-RO/train-*.parquet
- config_name: ru-BY
  data_files:
  - split: train
    path: data/ru-BY/train-*.parquet
- config_name: ru-KZ
  data_files:
  - split: train
    path: data/ru-KZ/train-*.parquet
- config_name: rw-RW
  data_files:
  - split: train
    path: data/rw-RW/train-*.parquet
- config_name: si-LK
  data_files:
  - split: train
    path: data/si-LK/train-*.parquet
- config_name: sk-SK
  data_files:
  - split: train
    path: data/sk-SK/train-*.parquet
- config_name: sl-SI
  data_files:
  - split: train
    path: data/sl-SI/train-*.parquet
- config_name: so-SO
  data_files:
  - split: train
    path: data/so-SO/train-*.parquet
- config_name: sq-AL
  data_files:
  - split: train
    path: data/sq-AL/train-*.parquet
- config_name: sq-XK
  data_files:
  - split: train
    path: data/sq-XK/train-*.parquet
- config_name: sr-RS
  data_files:
  - split: train
    path: data/sr-RS/train-*.parquet
- config_name: su-ID
  data_files:
  - split: train
    path: data/su-ID/train-*.parquet
- config_name: sv-SE
  data_files:
  - split: train
    path: data/sv-SE/train-*.parquet
- config_name: sw-KE
  data_files:
  - split: train
    path: data/sw-KE/train-*.parquet
- config_name: sw-TZ
  data_files:
  - split: train
    path: data/sw-TZ/train-*.parquet
- config_name: ta-IN
  data_files:
  - split: train
    path: data/ta-IN/train-*.parquet
- config_name: te-IN
  data_files:
  - split: train
    path: data/te-IN/train-*.parquet
- config_name: th-TH
  data_files:
  - split: train
    path: data/th-TH/train-*.parquet
- config_name: tk-TM
  data_files:
  - split: train
    path: data/tk-TM/train-*.parquet
- config_name: tr-TR
  data_files:
  - split: train
    path: data/tr-TR/train-*.parquet
- config_name: uk-UA
  data_files:
  - split: train
    path: data/uk-UA/train-*.parquet
- config_name: ur-PK
  data_files:
  - split: train
    path: data/ur-PK/train-*.parquet
- config_name: uz-UZ
  data_files:
  - split: train
    path: data/uz-UZ/train-*.parquet
- config_name: vi-VN
  data_files:
  - split: train
    path: data/vi-VN/train-*.parquet
- config_name: wo-SN
  data_files:
  - split: train
    path: data/wo-SN/train-*.parquet
- config_name: xh-ZA
  data_files:
  - split: train
    path: data/xh-ZA/train-*.parquet
- config_name: yue-HK
  data_files:
  - split: train
    path: data/yue-HK/train-*.parquet
- config_name: zh-TW
  data_files:
  - split: train
    path: data/zh-TW/train-*.parquet
- config_name: zu-ZA
  data_files:
  - split: train
    path: data/zu-ZA/train-*.parquet
---
# Basis Global Emotions

<img src="basis-global-emotions.gif" alt="Basis Global Emotions" style="border-radius: 16px;" />

[![Blog + Samples](https://img.shields.io/badge/%F0%9F%93%B0-Blog%20%2B%20Samples-0ea5e9)](https://withbasis.co/open/global-emotions)
[![Basis](https://img.shields.io/badge/%F0%9F%8F%A0-Basis-8b5cf6)](https://withbasis.co)
[![Contact](https://img.shields.io/badge/%E2%9C%89%EF%B8%8F-Contact-green)](mailto:data@withbasis.co)

**Listen first: [speech samples](https://withbasis.co/open/global-emotions)**

## Overview

**525.17 hours · 137,696 recordings · 54,575 series · 10,420 speakers · 108 locales**

Each recording is one native speaker performing a line in a described situation according to a steer, which is an emotion (e.g. happy, frustrated) or a direction (e.g., whispering, screaming). Recordings are organized into what we call series: the same speaker reads the same line multiple times to control for speaker identity and lexical content. An emotion series has three readings (neutral, medium, full); a delivery series has two (neutral, full). Every reading of every series is included; `series_id` groups them and `intensity` orders them.

### Languages

| Locale | Language | Country | Hours | Recordings | Series | Speakers |
|---|---|---|---:|---:|---:|---:|
| pt-BR | Portuguese | Brazil | 9.97 | 2,382 | 946 | 80 |
| ja-JP | Japanese | Japan | 8.84 | 2,322 | 939 | 73 |
| pl-PL | Polish | Poland | 8.49 | 2,168 | 857 | 88 |
| en-US | English | United States | 8.46 | 2,497 | 995 | 209 |
| uk-UA | Ukrainian | Ukraine | 8.30 | 1,938 | 778 | 88 |
| it-IT | Italian | Italy | 8.13 | 2,042 | 805 | 71 |
| es-CL | Spanish | Chile | 8.06 | 2,199 | 888 | 81 |
| am-ET | Amharic | Ethiopia | 7.89 | 2,250 | 915 | 118 |
| bg-BG | Bulgarian | Bulgaria | 7.85 | 1,922 | 766 | 97 |
| es-MX | Spanish | Mexico | 7.73 | 2,092 | 827 | 86 |
| sr-RS | Serbian | Serbia | 7.67 | 1,838 | 735 | 86 |
| id-ID | Indonesian | Indonesia | 7.47 | 1,824 | 722 | 194 |
| cs-CZ | Czech | Czechia | 7.38 | 1,999 | 794 | 131 |
| es-PE | Spanish | Peru | 7.31 | 1,940 | 769 | 125 |
| ro-RO | Romanian | Romania | 7.11 | 1,976 | 793 | 82 |
| mg-MG | Malagasy | Madagascar | 7.01 | 1,860 | 751 | 129 |
| ka-GE | Georgian | Georgia | 6.93 | 1,899 | 751 | 159 |
| ru-BY | Russian | Belarus | 6.85 | 1,658 | 648 | 70 |
| bs-BA | Bosnian | Bosnia and Herzegovina | 6.81 | 1,710 | 662 | 112 |
| zu-ZA | Zulu | South Africa | 6.71 | 2,570 | 1,010 | 144 |
| ru-KZ | Russian | Kazakhstan | 6.70 | 1,572 | 612 | 63 |
| el-GR | Greek | Greece | 6.66 | 1,875 | 752 | 120 |
| or-IN | Odia | India | 6.56 | 1,600 | 636 | 163 |
| es-ES | Spanish | Spain | 6.54 | 1,671 | 676 | 128 |
| fr-FR | French | France | 6.51 | 1,857 | 755 | 103 |
| mk-MK | Macedonian | North Macedonia | 6.50 | 1,588 | 622 | 99 |
| es-GT | Spanish | Guatemala | 6.39 | 1,687 | 674 | 117 |
| as-IN | Assamese | India | 6.35 | 1,612 | 651 | 107 |
| sk-SK | Slovak | Slovakia | 6.32 | 1,514 | 587 | 82 |
| ko-KR | Korean | South Korea | 6.21 | 1,536 | 598 | 77 |
| ar-MA | Arabic | Morocco | 6.18 | 1,580 | 633 | 52 |
| ceb-PH | Cebuano | Philippines | 6.13 | 1,426 | 580 | 98 |
| tr-TR | Turkish | Turkey | 6.12 | 1,601 | 643 | 72 |
| mn-MN | Mongolian | Mongolia | 5.98 | 1,593 | 641 | 114 |
| ml-IN | Malayalam | India | 5.93 | 1,349 | 537 | 162 |
| uz-UZ | Uzbek | Uzbekistan | 5.91 | 1,381 | 547 | 143 |
| sl-SI | Slovenian | Slovenia | 5.90 | 1,716 | 677 | 74 |
| ms-MY | Malay | Malaysia | 5.88 | 1,501 | 593 | 122 |
| lt-LT | Lithuanian | Lithuania | 5.83 | 1,502 | 576 | 87 |
| su-ID | Sundanese | Indonesia | 5.80 | 1,493 | 591 | 123 |
| ne-NP | Nepali | Nepal | 5.76 | 1,317 | 536 | 132 |
| sq-AL | Albanian | Albania | 5.73 | 1,606 | 650 | 107 |
| es-EC | Spanish | Ecuador | 5.73 | 1,381 | 556 | 68 |
| ar-JO | Arabic | Jordan | 5.71 | 1,443 | 572 | 72 |
| hr-HR | Croatian | Croatia | 5.66 | 1,377 | 539 | 98 |
| sw-TZ | Swahili | Tanzania | 5.64 | 1,276 | 509 | 122 |
| cnr-ME | Montenegrin | Montenegro | 5.61 | 1,301 | 507 | 90 |
| sv-SE | Swedish | Sweden | 5.47 | 1,371 | 542 | 117 |
| fil-PH | Filipino | Philippines | 5.26 | 1,290 | 517 | 114 |
| az-AZ | Azerbaijani | Azerbaijan | 5.24 | 1,407 | 561 | 142 |
| es-CO | Spanish | Colombia | 5.16 | 1,333 | 532 | 82 |
| pt-PT | Portuguese | Portugal | 5.09 | 1,389 | 538 | 54 |
| hu-HU | Hungarian | Hungary | 5.09 | 1,352 | 544 | 115 |
| mr-IN | Marathi | India | 4.96 | 1,213 | 471 | 88 |
| af-ZA | Afrikaans | South Africa | 4.89 | 1,284 | 509 | 99 |
| bn-BD | Bengali | Bangladesh | 4.73 | 1,113 | 436 | 136 |
| xh-ZA | Xhosa | South Africa | 4.64 | 1,652 | 653 | 101 |
| ar-DZ | Arabic | Algeria | 4.64 | 1,341 | 528 | 187 |
| kn-IN | Kannada | India | 4.62 | 1,071 | 420 | 93 |
| en-CA | English | Canada | 4.58 | 1,325 | 507 | 97 |
| bn-IN | Bengali | India | 4.53 | 1,095 | 429 | 99 |
| lv-LV | Latvian | Latvia | 4.51 | 1,125 | 433 | 78 |
| jv-ID | Javanese | Indonesia | 4.30 | 1,205 | 485 | 176 |
| ur-PK | Urdu | Pakistan | 4.29 | 1,113 | 450 | 116 |
| es-AR | Spanish | Argentina | 4.27 | 1,106 | 447 | 70 |
| fi-FI | Finnish | Finland | 4.24 | 1,109 | 445 | 74 |
| te-IN | Telugu | India | 4.23 | 906 | 360 | 132 |
| de-DE | German | Germany | 4.17 | 1,159 | 455 | 50 |
| gu-IN | Gujarati | India | 4.12 | 1,060 | 417 | 122 |
| en-GB | English | United Kingdom | 4.11 | 1,022 | 398 | 58 |
| sw-KE | Swahili | Kenya | 4.10 | 936 | 367 | 88 |
| ar-TN | Arabic | Tunisia | 4.08 | 1,339 | 540 | 163 |
| rw-RW | Kinyarwanda | Rwanda | 4.02 | 1,077 | 420 | 132 |
| he-IL | Hebrew | Israel | 4.01 | 1,043 | 404 | 78 |
| kk-KZ | Kazakh | Kazakhstan | 3.92 | 1,047 | 426 | 54 |
| nl-NL | Dutch | Netherlands | 3.90 | 1,075 | 415 | 59 |
| hy-AM | Armenian | Armenia | 3.86 | 1,047 | 415 | 95 |
| ar-SA | Arabic | Saudi Arabia | 3.68 | 927 | 368 | 43 |
| ar-LB | Arabic | Lebanon | 3.66 | 956 | 391 | 116 |
| si-LK | Sinhala | Sri Lanka | 3.57 | 1,016 | 401 | 126 |
| ar-EG | Arabic | Egypt | 3.54 | 858 | 340 | 45 |
| es-DO | Spanish | Dominican Republic | 3.50 | 911 | 363 | 105 |
| vi-VN | Vietnamese | Vietnam | 3.49 | 1,067 | 411 | 101 |
| ta-IN | Tamil | India | 3.44 | 845 | 325 | 79 |
| hi-IN | Hindi | India | 3.41 | 857 | 339 | 47 |
| lg-UG | Luganda | Uganda | 3.37 | 811 | 315 | 95 |
| ar-LY | Arabic | Libya | 3.27 | 918 | 373 | 160 |
| et-EE | Estonian | Estonia | 3.12 | 774 | 298 | 60 |
| ky-KG | Kyrgyz | Kyrgyzstan | 3.11 | 798 | 307 | 96 |
| th-TH | Thai | Thailand | 2.98 | 1,260 | 516 | 189 |
| el-CY | Greek | Cyprus | 2.98 | 843 | 328 | 98 |
| pa-IN | Punjabi | India | 2.73 | 650 | 254 | 140 |
| nb-NO | Norwegian | Norway | 2.59 | 749 | 292 | 51 |
| om-ET | Oromo | Ethiopia | 2.10 | 549 | 206 | 45 |
| da-DK | Danish | Denmark | 1.60 | 436 | 171 | 67 |
| lo-LA | Lao | Laos | 1.55 | 614 | 245 | 70 |
| yue-HK | Cantonese | Hong Kong | 1.44 | 429 | 164 | 78 |
| sq-XK | Albanian | Kosovo | 1.30 | 368 | 147 | 47 |
| zh-TW | Mandarin | Taiwan | 1.28 | 337 | 130 | 50 |
| ak-GH | Akan | Ghana | 1.26 | 344 | 131 | 87 |
| ln-CD | Lingala | DR Congo | 1.16 | 271 | 103 | 70 |
| km-KH | Khmer | Cambodia | 1.00 | 418 | 164 | 36 |
| ps-PK | Pashto | Pakistan | 1.00 | 301 | 112 | 56 |
| so-SO | Somali | Somalia | 1.00 | 283 | 111 | 73 |
| en-AU | English | Australia | 1.00 | 275 | 107 | 31 |
| tk-TM | Turkmen | Turkmenistan | 1.00 | 247 | 95 | 48 |
| en-NZ | English | New Zealand | 1.00 | 244 | 92 | 17 |
| wo-SN | Wolof | Senegal | 0.78 | 294 | 111 | 47 |

## How to Use

Each locale is a configuration named by its code. Install `datasets[audio]` and FFmpeg first.

```python
from datasets import load_dataset

ds = load_dataset("basis-ai/basis-global-emotions", "ja-JP", split="train")
row = ds[0]
row["audio"], row["steer"], row["intensity"], row["given_line"]
```

Rows are recordings. Group them by `series_id` and order `intensity` as neutral, medium, full to get one speaker's readings of one line. Join `speaker_id` to `speaker` in `speakers.jsonl` for speaker-disjoint splits. For every locale at once, loop over the configurations or read `data/*/*.parquet` directly.
## Dataset Structure

```text
README.md                        this card
FIELDS.md                        every column and field
LICENSE                          the terms
dataset_info.json                statistics for the release and for every locale
locales.json                     every locale code with its language and country names
speakers.jsonl                   one row per speaker across the release
data/<language>-<COUNTRY>/       the locale's recordings as parquet shards: 16 columns, the audio bytes in `audio`
```

Each row has 16 columns: `rank`, `series_id`, `intensity`, `recording_id`, `audio`, `speaker_id`, `locale`, `gender`, `age_band`, `steer`, `given_line`, `nonverbal_cues`, `situation`, `duration_s`, `nisqa_mos`, `nisqa_noise`; `audio` carries the recording as recorded (WAV, 16-bit PCM, 48 kHz, mono). Field meanings: [FIELDS.md](FIELDS.md).

### Dataset Statistics

| Measure | Value |
|---|---:|
| Hours | 525.17 |
| Recordings | 137,696 |
| Series | 54,575 |
| Speakers | 10,420 |
| Locales / languages / countries | 108 / 83 / 90 |
| Hours by declared gender | men 215.8 · women 308.1 · other 1.3 |

### Steers

Every reading of a series carries `steer`, the neutral reading included. Counts are series.

| Steer | Series |
|---|---:|
| affectionate | 1,150 |
| afraid | 1,171 |
| amused | 1,626 |
| angry | 1,588 |
| apologetic | 1,574 |
| assertive | 2,440 |
| bored | 928 |
| calm | 1,236 |
| confused | 1,119 |
| crying | 1,337 |
| curious | 1,422 |
| disappointed | 1,117 |
| disgusted | 1,192 |
| dramatic | 1,899 |
| embarrassed | 1,020 |
| encouraging | 2,272 |
| envious | 947 |
| excited | 1,420 |
| flirtatious | 927 |
| frustrated | 1,360 |
| grateful | 1,109 |
| guilty | 1,034 |
| happy | 1,842 |
| hesitant | 1,723 |
| laughing | 2,890 |
| mumbling | 1,604 |
| nostalgic | 1,141 |
| playful | 2,431 |
| proud | 1,306 |
| relieved | 1,074 |
| sad | 1,441 |
| sarcastic | 1,996 |
| screaming | 264 |
| shouting | 498 |
| singing | 1,751 |
| soothing | 1,584 |
| surprised | 1,376 |
| whispering | 1,766 |

### Non-verbal cues

Some lines ask the speaker to perform a non-verbal cue at some point in the line (e.g., sigh, scoff, tongue click, …). The cue is written inside `given_line` in square brackets, in the line's own language, exactly as the speaker saw it; `nonverbal_cues` lists the kinds of those cues in English, in order, and is empty when the line has none.

12,141 of 137,696 recordings (8.82%) have a non-verbal cue in the instructed script, across 13 cue kinds. As a reminder, `given_line` is what the voice actor was instructed to read, it is not a human transcription or ASR rendering.

| Scripted cue | Recordings |
|---|---:|
| laugh | 1,642 |
| sigh | 1,349 |
| scoff | 1,317 |
| tongue click | 1,070 |
| breathe | 1,061 |
| gasp | 918 |
| groan | 900 |
| sniffle | 875 |
| sob | 826 |
| clear throat | 826 |
| whimper | 766 |
| yawn | 537 |
| cough | 62 |

### Audio

WAV, 16-bit PCM, 48 kHz, exactly as recorded, no post-hoc denoising, enhancement, loudness normalization, resampling, etc.

### Audio quality

Every recording must pass minimum NISQA requirements (MOS and background-noise scores, each 1 to 5), with the exception of whisper and laughing deliveries, which instead have their own acoustic check. The minimums are 3.80 / 3.90 in every locale except kk-KZ and ko-KR (3.75 / 3.90), zh-TW (3.76 / 3.90) and hi-IN (3.80 / 3.85).

### Speakers

One line per speaker in `speakers.jsonl`: `speaker` (a stable anonymous id, consistent across the locales of this release), `gender`, `age_band`, `country`, `region`, the locales the speaker appears in, and the speaker's volume in the release (`recordings`, `series`, `seconds`).

### Transcripts

An important note is that `given_line` is the text the speaker was asked to read, not a transcription of the recording: a speaker may have departed from the line. Human-validated transcripts are not included in this release; they can be requested from data@withbasis.co.

## Dataset Creation

### Recording

Native speakers record steered reads on Basis's custom consumer applications and are paid for their contributions. The same speaker reads the same instructed line across intensity levels or a requested delivery style.

### Selection

All audio was rated by native speakers from its locale. Series were then chosen by a blend of those pairwise ratings and our internal models for steer following and microphone quality, balanced across steers and genders, with at most 35 minutes per speaker and ten series per line. `rank` is the order of that pick within the locale according to our blended quality scores.

### Consent and Privacy

Every participant agreed at signup to be recorded and to license their recordings for AI training, including resale to third parties and training of speech recognition, text-to-speech and voice-cloning systems, and waived their right of publicity for AI training. Every line is a scripted text, so no personal details are spoken. We additionally take extra effort to remove suspected minors from the release: speakers declare their age at signup, every speaker's voice is screened by an offline model that detects underage voices, and flagged speakers were reviewed by a person before shipping. Speaker identifiers are salted and stable; no names, account identifiers or contact data are in the release. Demographics are self-reported at signup and never inferred from audio.

**The license is deliberately permissive, for research and commercial use alike.** The Basis Data License grants a worldwide, royalty-free, perpetual license to download, store, process, annotate, modify and combine the data, and to pretrain, train, fine-tune, distill, evaluate and benchmark models on it, for research and commercial purposes. Models and results built on it are yours: you may publish, distribute, license and sell them, and operate commercial products, hosted inference services and APIs with them, with no royalties, no revenue sharing and no further permission from Basis, and no obligation to publish code, weights or methods. Two things are not allowed: reselling or redistributing the recordings themselves (or copies and derivatives that contain them), and identifying, locating or contacting speakers, impersonating a specific person, or reconstructing removed information. See [LICENSE](https://huggingface.co/datasets/basis-ai/basis-global-emotions/blob/main/LICENSE) for the full terms.

## Additional Information

### Verification

`CHECKSUMS.sha256` lists the SHA-256 of each root file; the repository's file listing shows each parquet shard's SHA-256.

### Licensing

The terms are in [LICENSE](https://huggingface.co/datasets/basis-ai/basis-global-emotions/blob/main/LICENSE). Custom licenses are available on request: [data@withbasis.co](mailto:data@withbasis.co).

### Citation

```bibtex
@misc{basis2026globalemotions,
  title     = {Basis Global Emotions},
  author    = {{Basis}},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/basis-ai/basis-global-emotions}
}
```
