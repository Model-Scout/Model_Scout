# Government Bonds

Prices and yields of government bonds

## General
The dataset contains government bond prices and yields of 30 countries from 6 world regions (Americas, Europe, Asia, Pacific, Middle East, Africa) in the range of 1970 to 2020.

The data was collected on **TradingView** and splitted in two files: ***prices.csv*** and ***yields.csv***

---

## Columns
There are **216** columns in both files sorted alphabetically. The difference is in units: for ***yields.csv*** each value represents a % yield for a particular bond and for ***prices.csv*** it is the cost of a bond in a particular country's currency.

| column   | description          | unit      |
|----------|------------------|--------|
| time        | UNIX timestamp | ms       |
| AU01  | Australian Government Bond 1Y term  | % or AUD   |
| AU02  | Australian Government Bond 2Y term  | % or AUD    |
| AU03  | Australian Government Bond 3Y term  | % or AUD    |
| AU05  | Australian Government Bond 5Y term  | % or AUD    |
...
| US07       | US Government Bond 5Y term  | % or USD    |
| US10       | US Government Bond 10Y term  | % or USD    |
| US20       | US Government Bond 20Y term | % or USD    |
| US30      | US Government Bond 30Y term  | % or USD    |

---

## Prefixes

| prefix  | country | 
|----------|--------|
| **AU** | Australia |
| **BE** | Belgium |
| **CA** | Canada |
| **CN** | China |
| **DK** | Denmark |
| **FR** | France |
| **DE** | Germany |
| **GR** | Greece |
| **HK** | Hong Kong |
| **IN** | India |
| **ID** | Indonesia |
| **IE** | Ireland |
| **IT** | Italy |
| **JP** | Japan |
| **KR** | Korea |
| **MY** | Malaysia |
| **NL** | Netherlands |
| **NZ** | New Zealand |
| **NO** | Norway |
| **PL** | Poland |
| **PT** | Portugal |
| **SG** | Singapore |
| **ZA** | South Africa |
| **ES** | Spain |
| **SE** | Sweden |
| **TW** | Taiwan |
| **TH** | Thailand |
| **TR** | Turkey |
| **GB** | UK |
| **US** | US |

---

## Acknowledgements

1. TradingView Inc., https://www.tradingview.com/
1. TradingView Inc., https://www.tradingview.com/
1. TradingView Inc., https://www.tradingview.com/

출처: Kaggle (everget/government-bonds)
태그: finance, government, exploratory data analysis, time series analysis, investing
라이선스: GNU Lesser General Public License 3.0
수정일: 2020-07-25T17:16:40.603Z
