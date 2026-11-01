---
license: cc-by-nc-4.0
language:
- ko
pretty_name: KOSPI Stocks Daily Data with Technical & Macro Features
size_categories:
- 1M<n<10M
task_categories:
- time-series-forecasting
- tabular-regression
tags:
- finance
- stocks
- korea
- kospi
- time-series
- technical-indicators
- quant
configs:
- config_name: default
  data_files: kospi_data_v1.parquet
---

# KOSPI Stocks Daily Data with Technical & Macro Features

🇰🇷 한국어 / 🇺🇸 English

2021년부터 2026년까지 KOSPI 948개 종목의 일별 시세에 기술적 지표·거시지표·투자자 수급을 결합한 머신러닝 학습용 한국 주식 데이터셋입니다.

A machine-learning–ready Korean stock dataset combining daily prices of 948 KOSPI stocks with technical indicators, macro variables, and investor flows, covering 2021 to 2026.

---

## 📊 Contents

- **1,214,339 rows / 121만 행** (948 stocks / 948개 종목)
- **Period / 기간: 2021-01-04 ~ 2026-05-29** (약 5.4년)
- **60 columns / 60개 컬럼**

| Group / 구분 | Columns / 컬럼 |
|---|---|
| **Identifier (식별자)** | Date, Code, Name |
| **Price (시세)** | Open, High, Low, Close, Volume, Change, LogReturn |
| **Technical indicators (기술적 지표)** | MA5/20/60/120, Disp5/20/60/120, Vol20, RSI14, MACD, MACD_signal, MACD_hist, BB_pctB, VolumeMA20, VolumeRatio |
| **Macro (거시지표)** | KOSPI_lvl/ret, USDKRW_lvl/ret, SP500_lvl/ret, NASDAQ_lvl/ret, VIX_lvl/ret, US10Y_lvl/ret |
| **Calendar (캘린더)** | DayOfWeek, Month, IsMonthEnd, IsQuarterEnd, DoW_sin/cos, Month_sin/cos |
| **Investor flows (투자자 수급)** | Foreign_net, Inst_net, Indiv_net, EtcCorp_net, Foreign_ratio, Inst_ratio, Indiv_ratio, Foreign_net_ma5, Inst_net_ma5, Indiv_net_ma5 |
| **Market cap (시가총액)** | Marcap, Shares, LogMarcap |

> 📖 각 컬럼의 상세 설명·단위는 [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) 를 참고하세요.
> See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) for column-by-column descriptions and units.

---

## 🚀 Quick Start / 빠른 시작

```python
from datasets import load_dataset

ds = load_dataset("podongchip/kospi-daily-stock-features-2021-2026", split="train")
print(ds[0])
```

```python
# pandas 로 바로 쓰기 / load directly with pandas
import pandas as pd

df = pd.read_parquet(
    "hf://datasets/podongchip/kospi-daily-stock-features-2021-2026/kospi_data_v1.parquet"
)

# 종목별 시계열 / per-stock time series
samsung = df[df["Code"] == "005930"].sort_values("Date")
print(samsung[["Date", "Close", "RSI14", "Foreign_net"]].tail())
```

> ⚠️ **`Code` 는 반드시 문자열로 다루세요 / Always treat `Code` as a string.**
> 종목코드는 앞자리 0이 있고(`000020`), 우선주는 끝에 알파벳이 붙습니다(예: `00088K`).
> 숫자로 변환하면 앞자리 0이 사라지거나 우선주 코드가 깨집니다.
> Stock codes are zero-padded (`000020`) and preferred shares carry a letter suffix
> (e.g. `00088K`). Casting to int drops the leading zeros and breaks preferred-share codes.
> 본 데이터는 Parquet 포맷이라 `Code` 가 문자열로 저장되어 있어 그대로 안전합니다.
> This dataset ships as Parquet, so `Code` is stored as a string and stays safe by default.

---

## 💡 Use Cases

- Stock price / return prediction modeling / 주가·수익률 예측 모델링
- Quant strategy & factor research / 퀀트 전략·팩터 리서치
- Time-series & financial ML education / 시계열·금융 ML 학습
- Investor flow and macro impact analysis / 수급·거시지표 영향 분석

---

## 📝 Notes / 참고

- **종목코드(`Code`) / Stock code:** 6자리 문자열이며, 우선주 등은 끝에 알파벳(K·L·M 등)이 붙습니다. 정수로 변환하지 마세요.
  6-digit string; preferred and special shares carry a trailing letter (K, L, M, …). Do not cast to integer.
- **결측치 / Missing values:** 기술적 지표(MA, RSI, MACD 등)는 룩백 기간이 필요하므로 각 종목의 초기 행에 결측치(빈 값)가 존재합니다.
  Technical indicators require a lookback window, so early rows per stock contain missing values.
- **거시지표 / Macro:** 영업일 기준으로 정렬되어 있으며, 일부 휴장일 차이로 인한 결측이 있을 수 있습니다.
  Aligned to trading days; some gaps may exist due to holiday mismatches.
- **정렬 / Ordering:** `Code` → `Date` 순으로 종목별 시계열이 이어집니다.
  Rows are ordered by `Code` then `Date`, forming per-stock time series.
- **Look-ahead 주의 / No look-ahead:** 모든 지표는 해당 일자까지의 정보로만 계산됩니다(미래 정보 미포함).
  All features use information up to that date only.

---

## 🗂️ Data Sources / 데이터 출처

- **KOSPI 시세·투자자 수급 (Price & investor flows):** 한국거래소(KRX) 공개 시장 데이터 기반으로 가공.
  Derived from Korea Exchange (KRX) public market data.
- **거시지표 (Macro indicators):** 환율·해외 지수·변동성·금리 등 공개적으로 공표되는 시장 지표.
  Publicly published market indicators (FX rates, global indices, volatility, yields).

본 데이터셋은 위 공개 시장 데이터를 기술적 지표·파생 변수로 **가공한 2차 저작물**입니다.
This dataset is a derived work that processes the above public market data into technical and engineered features.

---

## ⚖️ License & Disclaimer / 라이선스·면책

- 본 데이터셋은 **CC BY-NC 4.0** 라이선스로 제공됩니다(비영리·출처표시).
  Released under **CC BY-NC 4.0** (non-commercial, attribution required).
- 데이터셋의 **가공·구성·파생 변수 및 편집에 대한 권리는 제작자에게 있습니다.**
  Rights to the **processing, structure, engineered features, and compilation** of this dataset belong to its creator.
- 원천이 되는 시세·거시지표 값은 공개 시장 데이터에 기반하며, 각 원천 데이터의 권리는 해당 제공처에 있습니다.
  The underlying price and macro values are based on public market data; rights to the source data remain with their respective providers.
- 본 데이터셋은 **연구 및 교육 목적**으로 제공됩니다. 데이터의 정확성·완전성을 보증하지 않으며, 투자 판단의 근거로 사용해 발생하는 책임은 사용자에게 있습니다.
  Provided for **research and educational purposes**. No warranty is given regarding accuracy or completeness; any investment decisions made using this data are solely the user's responsibility.
