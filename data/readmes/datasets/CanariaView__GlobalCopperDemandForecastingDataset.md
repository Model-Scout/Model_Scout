---
task_categories:
- time-series-forecasting
language:
- en
- ko
tags:
- mining
- LSTM
- TimeSeries
- CanariaView
---
# CanariaView Global Copper Demand Forecasting Dataset

## Description
This dataset encompasses economic and industrial indicators vital for constructing a copper demand forecasting model.

Coverage Period: Monthly data from January 1995 to March 2023, encompassing a total of 339 months.

Column Descriptions and Sources:
- `HSI_value (US Housing Starts Index)`: Y-Chart
- `CCI_value (Consumer Confidence Index)`: OECD
- `IPI_value (Industrial Production Total Index)`: FRED
- `GDPC_value (Real Gross Domestic Product)`: FRED
- `Copper price`: MacroTrends

Preprocessing Methodology and Data Collection Details:
- Comprehensive analysis of data structure followed by essential preprocessing.
- Appropriate handling of missing values.
- Daily and quarterly data uniformly expanded to a monthly timescale for consistency.
- Daily data (e.g., Copper price) and quarterly data (e.g., GDPC_value)
- Dependent variable data used in the model was available from 1995, guiding the collection of independent variables-this dataset- from that year.

## 한국어 설명
본 데이터셋은 구리 수요 예측 모델 구축을 위한 경제지표 및 산업지표로 구성되었습니다.

기간: 1995년 1월~2023년 3월(월별), 총 339개월.

컬럼 설명 및 출처
- `HSI_value (미국 주택착공지수)`: Y-Chart
- `CCI_value (미국 소비자신뢰지수)`: OECD
- `IPI_value (미국 산업생산자지수)`: FRED
- `GDPC_value (미국 실질 GDP)`: FRED
- `Copper price (구리 가격)`: MacroTrends

데이터 전처리 및 수집 방법:
- 데이터 구조 분석 및 전처리 과정 수행.
- 결측치 처리.
- 일별 및 분기별 자료는 월별 데이터로의 확장을 통해 일관된 시계열 데이터로 통합.
- 일별 자료 (구리 가격), 분기별 자료 (GDPC_value)
- 수요 모델에 사용된 종속변수 데이터가 1995년부터 확보되어 독립변수인 본 데이터셋도 1995년도부터 수집함.