---
language:
- ko
- en
pretty_name: MINDCAST Monthly Time Series Benchmark Results
tags:
- time-series
- forecasting
- benchmark-results
- graph-learning
configs:
- config_name: metrics
  data_files:
  - split: results
    path: metrics_by_target.csv
- config_name: leaderboard
  data_files:
  - split: results
    path: leaderboard.csv
- config_name: dml
  data_files:
  - split: results
    path: dml_estimates.csv
---

# MINDCAST 예측 결과 — 1·2·3·6개월

2026-10-14 업데이트. **4,932개 예측 실험, 예측값 133,164행, 미해결 오류 0건**. 2개월 추가 실행은 2026-10-13 17:53 KST경 완료했습니다. 원인별 9개 대상과 전체·남·여 3개 대상을 평가했습니다.

## 그래프 네트워크에 관심이 있다면

먼저 **[그래프 결과 및 구현 설명](docs/GRAPH_RESULTS.md)**을 보세요. PCMCI·NOTEARS·DYNOTEARS 탐색과 그래프 부모 선택+Ridge 예측을 수행했습니다. **메시지 전달 GNN(GCN/GAT 등)은 이번에 학습하지 않았습니다.** 이 구분과 성능 비교, 그림, 한계를 따로 정리했습니다.

![탐색적 DYNOTEARS 그래프](h2/dag_exploratory.png)

그림은 전체 표본 탐색 결과이며 실제 인과관계의 증명이 아닙니다. 예측 모델은 별도로 각 기준월의 과거에서 그래프를 다시 학습합니다.

## Markdown 문서

- [그래프 결과](docs/GRAPH_RESULTS.md)
- [전체 모델 결과 및 1·2·3·6개월 비교](docs/RESULTS.md)
- [데이터·평가·모델 설정](docs/METHODS.md)
- [결과 데이터 사전](docs/DATA_DICTIONARY.md)
- [최종 검증](docs/VALIDATION.md)
- [재현 방법](docs/REPRODUCE.md)
- [2개월 추가 전 최초 보고서(과거 기록)](docs/archive/RESULTS_20261008.md)
- [원본 데이터 README](docs/source/README_2013_2024.md), [원본 raw README](docs/source/README_raw.md)

모든 Markdown을 개별 파일로 올렸으므로 ZIP을 받지 않고 읽을 수 있습니다.

## 주요 파일

| 파일 | 내용 |
|---|---|
| [metrics_by_target.csv](metrics_by_target.csv) | 전체 대상·모델·예측거리의 시드 평균 점수 |
| [h2/metrics_h2.csv](h2/metrics_h2.csv) | 2개월 예측 전체 점수 |
| [h2/graph_forecast_h2.csv](h2/graph_forecast_h2.csv) | 그래프 기반 2개월 예측 24개, 부모 선택 빈도 |
| [results/predictions.csv](results/predictions.csv) | 예측값 133,164행 |
| [results/metrics_by_target_seed.csv](results/metrics_by_target_seed.csv) | 개별 시드 점수 |
| [dml_estimates.csv](dml_estimates.csv) | 기존 DML 144개 명세 |
| [최신 전체 ZIP](mindcast_benchmark_20261014.zip) | 결과·코드·완료 job·문서·메타데이터 |
| [SHA256SUMS.txt](SHA256SUMS.txt) | 이번 업로드 파일별 해시 |

20261007 ZIP은 이전 버전입니다. 최신 결과는 **20261014 ZIP**을 사용하세요. 원인별 자료는 2013–2020년, 전체·성별은 2013–2024년이며 분모와 평가 기간을 혼합하지 않습니다. 신경망은 소형 구조·fit당 80 updates의 초기 비교이므로 충분한 수렴이나 최적 성능을 보장하지 않습니다.

## 월별 실패·validation 그림·계절성 추가 비교

[월별 오차 그림과 계절성 비교 보고서](docs/VALIDATION_PLOTS_AND_SEASONALITY.md): A·B·A+B·전체의 validation/test 선그래프, 월별 오차 히트맵, 최악 월, 달력 변수 4종 비교. 기존 테스트 및 validation 튜닝점과 추가 진단을 구분했습니다.


## 데이터·모델군·월별 validation·그래프 해석 (2026-10-14)

[통합 보고서](reports/model_groups_20261014/README.md): 데이터와 입력·타깃·기간, 모델군별 월별 validation 그림 48개, 평균·최악 월 표, 그래프 해석표 및 DML 효과 탐색을 구분했습니다. [그래프 해석](reports/model_groups_20261014/04_GRAPH_INTERPRETATION.md) · [전체 보고서 ZIP](reports/model_groups_20261014/model_groups_report.zip).

추가 월별 validation은 2개월 뒤 예측·A/B/A+B/전체·seed42의 176개 조합입니다. DYNOTEARS의 주요 4타깃 Test 예측에서는 이용 가능한 거시 부모가 모두 비어 있었으며, GCN/GAT 등 GNN은 아직 실행하지 않았습니다.
