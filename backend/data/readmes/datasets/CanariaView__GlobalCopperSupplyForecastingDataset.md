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
# CanariaView Global Copper Supply Forecasting Dataset

## Description

This dataset encompasses economic and industrial indicators vital for constructing a copper supply forecasting model.

Coverage Period: Monthly data from January 2000 to March 2023, encompassing a total of 279 months.

Column Descriptions and Sources:
- `Copper price`: MacroTrends
- `Cash Costs (Antofagasta's Pure Mining Costs)`: Antofagasta Annual Report
- `Transport (Antofagasta's Transportation Cost)`: Antofagasta Annual Report
- `Stock (LME Copper Stock)`: MacroMicro
- `Oil Price`: Source - EIA
- `M_GDP (Chile Copper Mining GDP)`: Banco Central de Chile

Preprocessing Methodology and Data Collection Details:
- Comprehensive analysis of data structure followed by essential preprocessing.
- Appropriate handling of missing values.
- Daily (e.g., Copper price, Oil Price) and quarterly data (e.g., Cash Costs, Transport, M_GDP) uniformly expanded to a monthly timescale for consistency.
- The Antofagasta annual report was available from the year 2000, hence the data collection started from 2000.

## 한국어 설명

본 데이터셋은 구리 공급 예측 모델 구축을 위한 경제지표 및 산업지표로 구성되었습니다.

기간: 2000년 1월~2023년 3월(월별), 총 279개월.

컬럼 설명 및 출처:
- `Copper price (구리 가격)`: MacroTrends
- `Cash Costs (Antofagasta 순수채굴비용)`: Antofagasta Annual Report
- `Transport (Antofagasta 운송비)`: Antofagasta Annual Report
- `Stock (런던금속거래소 구리 재고량)`: MacroMicro
- `Oil Price (원유 가격)`: EIA
- `M_GDP (칠레 구리 채굴 GDP)`: Banco Central de Chile

데이터 전처리 및 수집 방법:
- 데이터 구조 분석 및 전처리 과정 수행.
- 결측치 처리.
- 일별 자료 (구리 가격, 원유 가격), 분기별 자료 (Cash Costs, Transport, M_GDP)는 월별 데이터로의 확장을 통해 일관된 시계열 데이터로 통합.
- 안토파가스타 관련 데이터가 2000년부터 확보가 가능하여 2000년 부터 수집함.