---
license: other
license_name: source-attribution
language:
  - en
  - ko
tags:
  - drt
  - demand-responsive-transport
  - urban-mobility
  - simulation
  - benchmark
  - multi-city
pretty_name: "DRT Multi-City Benchmark Dataset"
size_categories:
  - 100M<n<1B
---

# DRT Multi-City Benchmark Dataset

다도시 DRT(Demand-Responsive Transport) 시뮬레이션 벤치마킹을 위한 통합 입력 데이터셋. 서로 다른 밀도·면적·데이터 포맷을 가진 세 도시(**NYC 맨해튼**, **Chicago**, **성남시 수정구**)의 수요·도로 네트워크·차량 데이터를 공통 스키마로 정제하여 제공한다.

- **대상**: DRT/모빌리티 연구자, 교통공학 대학원생, 도시 시뮬레이션 개발자
- **용도**: 다도시 DRT 알고리즘 벤치마킹, 배차/리밸런싱 비교, 차량대수 산정 검증, 도시 카테고리 일반화 연구
- **연계 시뮬레이터**: [DTUMOS](https://github.com/DTUMOS/DTUMOS) — Digital Twin Urban Mobility Simulator

## 핵심 사실

- **데이터 이질성**: NYC = Zone ID(좌표 없음), Chicago = 15분 binned + Census Tract centroid, 성남 = 초 단위 GPS 좌표
- 세 도시의 원본 정밀도 차이를 통합 스키마(`pickup_time`, `pickup_lon`, `pickup_lat`, `dropoff_lon`, `dropoff_lat`)로 정규화
- 도로 네트워크는 OSM 기반 `road_graph.gpkg` (노드/엣지)와 `osm_simplified.osm.pbf` 동봉 — Rust CH 라우팅 즉시 사용 가능
- 모든 좌표계: **EPSG:4326 (WGS84)**

---

## 폴더 구조

```
data/raw/
├── nyc/                              NYC Yellow Taxi (TLC, 2017-10-19 목)
│   ├── demand.csv                    정제된 수요 (통합 스키마)
│   ├── nyc_avg_demand_5day.csv       5일 평균 수요 (Poisson 시드용)
│   ├── nyc_manhattan_2017-10-19.parquet   해당일 필터된 원본
│   ├── yellow_tripdata_2017-10.parquet    원본 한 달치 (TLC raw)
│   ├── nyc_taxi_preprocessing.ipynb       전처리 노트북 (NYC Zone → 좌표 매핑 + 통합 스키마 변환)
│   ├── explore_taxi_data.ipynb            데이터 탐색 노트북 (TLC raw 구조·컬럼 분석)
│   ├── taxi+_zone_lookup.csv              TLC 263개 Zone ID ↔ 자치구·이름 매핑표
│   ├── boundary.geojson              맨해튼 경계
│   ├── road_graph.gpkg               OSM 도로 그래프 (LineString)
│   ├── road_graph_nodes.gpkg         노드 (Point)
│   ├── road_graph.meta.json          메타 (노드/엣지 수)
│   ├── osm_simplified.osm.pbf        OSM PBF (라우팅 엔진용)
│   ├── edge_index.pkl                Rust CH용 엣지 인덱스
│   ├── taxi_zones/                   TLC 263개 택시존 shapefile
│   └── seeds/                        시드별 샘플 3종
│       ├── demand_seed1.csv
│       ├── demand_seed2.csv
│       └── demand_seed3.csv
│
├── chicago/                          Chicago TNC Ride-hail (2024-03-14 목)
│   ├── demand.csv                    정제된 수요 (15분 binned → 분 단위 disaggregation)
│   ├── Taxi_Trips_2024-03-14.parquet 원본 일자 추출본
│   ├── boundary.geojson              시카고 경계
│   ├── road_graph.gpkg
│   ├── road_graph_nodes.gpkg
│   ├── road_graph.meta.json
│   ├── osm_simplified.osm.pbf
│   ├── edge_index.pkl
│   ├── tl_2024_17_tract/             Census Tract shapefile (centroid 매핑용)
│   └── seeds/
│       ├── demand_seed1.csv
│       ├── demand_seed2.csv
│       └── demand_seed3.csv
│
└── seongnam/                         성남시 수정구 스마트카드 택시 (2024-04-18 목)
    ├── demand.csv                    정제된 수요 (초 단위 GPS)
    ├── vehicles.csv                  실측 차량 풀
    ├── boundary.geojson              수정구 경계
    ├── road_graph.gpkg
    ├── road_graph_nodes.gpkg
    ├── road_graph_edges.parquet
    ├── road_graph_nodes.parquet
    ├── road_graph.meta.json
    ├── osm_simplified.osm.pbf
    ├── edge_index.pkl
    ├── semantic_graph.json           격자 기반 임시 정류장(Virtual Stop) 시드
    └── seeds/
        ├── demand_seed1.csv
        └── demand_seed2.csv
```

---

## 도시별 데이터 명세

| 항목 | NYC (맨해튼) | Chicago | 성남시 (수정구) |
|------|-------------|---------|----------------|
| **원본 출처** | NYC TLC Yellow Taxi | City of Chicago Open Data (TNC) | 성남시 스마트카드 택시 |
| **대상 일자** | 2017-10-19 (목) | 2024-03-14 (목) | 2024-04-18 (목) |
| **원본 시간 정밀도** | 초 단위 | **15분 binned** | 초 단위 |
| **원본 공간 정밀도** | **Zone ID만 (263개)** | Census Tract centroid | **GPS 좌표** |
| **수요 건수 (정제 후)** | 65,894건 | 53,553건 | 8,041건 |
| **시뮬 면적** | ~60 km² (맨해튼) | ~600 km² (시카고시) | ~25 km² (수정구) |
| **수요 밀도 (건/km²/h)** | ~258 (초고밀도) | ~18 (저밀도 광역) | ~43.6 (중밀도) |
| **차량대수 산정 (다반조 GM)** | 1,000대 | 1,600대 | 130대 |

### 통합 스키마 (`demand.csv` 컬럼)

| 컬럼 | 타입 | 설명 |
|------|------|------|
| `pickup_time` | datetime | 픽업 시각 (ISO 8601) |
| `pickup_lon`, `pickup_lat` | float | WGS84 픽업 좌표 |
| `dropoff_lon`, `dropoff_lat` | float | WGS84 하차 좌표 |
| `pax_count` | int | 승객 수 (기본 1) |

> **시드 파일(`seeds/demand_seed*.csv`)**: 동일 스키마. 평일 5일 평균을 Poisson 시드로 샘플링한 3종. 재현성을 위해 시드 1·2·3 동봉.

---

## 데이터 출처 및 라이선스

| 데이터 | 출처 | 라이선스 |
|--------|------|---------|
| NYC Yellow Taxi 2017-10 | [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | NYC Open Data Terms |
| NYC TLC Taxi Zones | NYC TLC | NYC Open Data Terms |
| Chicago Taxi Trips 2024-03 | [City of Chicago Open Data Portal](https://data.cityofchicago.org/) | City of Chicago Open Data |
| Chicago Census Tract 2024 | US Census TIGER/Line 2024 | Public Domain |
| 성남시 스마트카드 택시 2024-04 | 성남시 (연구 협약 데이터) | 비공개 — 정제·집계본만 공개 |
| OSM 도로 네트워크 | [OpenStreetMap](https://www.openstreetmap.org/) | ODbL 1.0 |

**본 데이터셋 라이선스**: `source-attribution` — 재배포 시 반드시 출처를 명기할 것.

---

## 다운로드 및 사용법

### 전체 다운로드

```bash
# (권장) 풀 데이터셋 — 약 420MB
hf download CAMUS-LAB/drt --repo-type dataset --local-dir ./data
```

### 도시별 부분 다운로드

```bash
# NYC만
hf download CAMUS-LAB/drt --repo-type dataset \
    --include "data/raw/nyc/**" --local-dir ./data
```

### Python에서 직접 로드

```python
from huggingface_hub import snapshot_download
local_path = snapshot_download(
    repo_id="CAMUS-LAB/drt",
    repo_type="dataset",
    allow_patterns=["data/raw/seongnam/**"],
)

import pandas as pd
df = pd.read_csv(f"{local_path}/data/raw/seongnam/demand.csv")
```

### DTUMOS 시뮬레이터에 연결

다운로드한 데이터를 DTUMOS의 `data/cities/<city>/` 에 배치하면 자동 감지된다:

```
DTUMOS/data/cities/
├── NYC/        ← data/raw/nyc/  의 내용
├── Chicago/    ← data/raw/chicago/  의 내용
└── Seongnam/   ← data/raw/seongnam/  의 내용
```

```bash
cd DTUMOS
python -m dtumos.cli simulate --city NYC --dispatch D3R --rebalancing R1b
```

---

## 관련 연구

- **시뮬레이터**: [DTUMOS](https://github.com/DTUMOS/DTUMOS) — Digital Twin Urban Mobility Simulator (Python + Rust CH + Java RAPTOR)
- **수요 모델**: [dtumos-demand-model](https://github.com/DTUMOS/dtumos-demand-model) — 수요 프로파일 생성 모델
- **연구 발표**: 2026 ITS 춘계학회 — "다도시 DRT 알고리즘 벤치마킹: 도시 맥락 기반 성능 비교 프레임워크" (방혜원, 가천대 스마트시티융합학과)

### 향후 확장

- **도시 추가**: 한국 5+ 도시 (서울/대구/대전/수원 등 스마트카드), 해외 추가 (싱가포르 등)
- **시간 이질성**: 일자 → 한 달 평균 (계절성), 시간대별 (피크/오프피크/심야)
- **Virtual Stop**: 격자 기반 임시 정류장 데이터 (저밀도 도시용)

---

## 인용

```bibtex
@dataset{drt_multi_city_benchmark_2026,
  author       = {Bang, Hyewon and CAMUS Lab},
  title        = {DRT Multi-City Benchmark Dataset (NYC, Chicago, Seongnam)},
  year         = {2026},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/CAMUS-LAB/drt},
  note         = {Multi-city DRT simulation input dataset for benchmarking dispatch and rebalancing algorithms}
}
```

---

## 변경 이력

- **2026-05** — 초기 공개판: NYC / Chicago / Seongnam 3개 도시 raw 입력 데이터, Dataset Card 및 통합 스키마 명세 추가
