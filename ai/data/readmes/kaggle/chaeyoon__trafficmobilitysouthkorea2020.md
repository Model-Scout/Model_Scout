# Traffic|Mobility|SouthKorea|2020

Daily Regional Korea Expressway Corporation Traffic Control System matrix data

### Context
This is the national traffic data measured at every expressway gate operated and updated in public data portal by Korea Expressway Corporation (KEC). The aggregated data has been updated a matrix of daily regional Traffic Control System (TCS) by every month as of November 2020.

### Content
To respect originality, this kaggle dataset has consisted of Korean labels which encoding 'euc-kr' and you may want to apply 'unicode_escape' option for encoding, but eventually the matrix would be recommendable to convert Korean to English and add new columns for sum when your work need to merge with other data such as the edit version formatting as below sample table.
| date | region | arrival_Capital | arrival_Gangwon | arrival_DaejeonChungnam | arrival_GwangjuJeonnam | arrival_DaeguGyeongbuk  | arrival_BusanGyeongnam  | arrival_Jeonbuk  | arrival_Chungbuk  | sum_bydeparture | sum_byarrival |
| --- | --- |
| 20200101 | Capital | | | | | | | | | sum(c2:j2) | sum(c2:c9) |
| 20200101 | Gangwon | | | | | | | | | sum(c3:j3) | sum(d2:d9) |
| 20200101 | DaejeonChungnam | | | | | | | | | sum(c4:j4) | sum(e2:e9) |
| 20200101 | GwangjuJeonnam | | | | | | | | | sum(c5:j5) | sum(f2:f9) |
| 20200101 | DaeguGyeongbuk | | | | | | | | | sum(c6:j6) | sum(g2:g9) |
| 20200101 | BusanGyeongnam | | | | | | | | | sum(c7:j7) | sum(h2:h9) |
| 20200101 | Jeonbuk | | | | | | | | | sum(c8:j8) | sum(i2:i9) |
| 20200101 | Chungbuk | | | | | | | | | sum(c9:j9) | sum(j2:j9) |

You may refer to the translation table by author as follow:
| Korean | English |
| --- | --- |
| 집계일자 | date |
| 출발권역명 | region |
| 수도권 | Capital |
| 강원 | Gangwon |
| 대전충남 | DaejeonChungnam |
| 광주전남 | GwangjuJeonnam |
| 대구경북 | DaeguGyeongbuk |
| 부산경남 | BusanGyeongnam |
| 전북 | Jeonbuk |
| 충북 | Chungbuk |

### Acknowledgements
Public Data Portal (https://www.data.go.kr/) has linked to the KEC Portal (https://www.ex.co.kr/eng/)
[Online]. Available at: http://data.ex.co.kr/portal/fdwn/view?type=TCS&num=C5&requestfrom=dataset# [Accessed 6 January 2021]

### Inspiration
This study aimed at data exploration how the government policy had influenced on human movements and presents how traffic volume in transportation had changed at the South Korea county level.

출처: Kaggle (chaeyoon/trafficmobilitysouthkorea2020)
태그: government, data analytics, korea
라이선스: CC0: Public Domain
수정일: 2021-01-14T17:30:50.280Z
