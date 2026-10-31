---
license: cc-by-nc-4.0
language:
  - ko
  - en
tags:
  - transportation
  - road-network
  - routing
  - eta
  - korea
  - osm
  - ktdb
size_categories:
  - 100K<n<1M
pretty_name: Korea Road Network ETA (v3)
---

# Korea Road Network ETA (v3)

16개 광역지자체 도로망 그래프. 시간대별 평균 통행속도(p50)가 부착되어 있어
ETA(예상소요시간) 산정·라우팅·배차 시뮬레이션에 바로 사용 가능합니다.

## Contents

각 region 마다 self-contained 파일 두 개:

- `{region}_osm_v3_nodes.parquet` — 노드 (`node_id`, `lat`, `lon`)
- `{region}_osm_v3_edges.parquet` — 엣지 (`source`, `target`, `length_m`,
  `highway`, `oneway`, `ktdb_matched`, …, **시간대별 속도 컬럼**)

### Regions (16)

`seoul`, `busan`, `daegu`, `incheon`, `gwangju`, `daejeon`, `ulsan`, `sejong`,
`gyeonggi`, `gangwon`, `chungbuk`, `chungnam`, `jeonbuk`, `jeonnam`,
`gyeongbuk`, `gyeongnam`

### Speed columns (8 slots × weekday/weekend)

스키마: `{day_type}_{slot}_p50` (단위: km/h)

- `day_type` ∈ {`weekday`, `weekend`}
- `slot` ∈
  - **observed** (KTDB 직접 관측): `am_peak`, `midday`, `pm_peak`, `offpeak`
  - **derived** (관측 4슬롯에서 도출): `am_shoulder`, `afternoon`,
    `pm_shoulder`, `night`

도출 규칙은 도로 위계 그룹별로 다른 가중치/계수를 사용 — 자세한 내용은
프로젝트 코드(`phase_d_attach.py`) 참조.

## Quick start

```python
import pandas as pd

nodes = pd.read_parquet("seoul_osm_v3_nodes.parquet")
edges = pd.read_parquet("seoul_osm_v3_edges.parquet")

# Edge travel time (sec) at AM peak
speed_kmh = edges["weekday_am_peak_p50"].clip(lower=5.0)
edges["tt_sec"] = edges["length_m"] / (speed_kmh * 1000 / 3600)
```

scipy 또는 networkx 등 일반 라우팅 라이브러리에 그대로 투입 가능합니다.

## Provenance

- **Topology**: OpenStreetMap (ODbL) — 2026년 추출
- **Speeds**: 한국교통DB (KTDB) 링크별 시간대 통행속도 (2024년 관측)
- **Pipeline**: `phase_a` (6시간 프로파일) → `phase_b` (regional fallback) →
  `phase_c` (위계 클립) → `phase_d` (attach + derived slots)

## License

Code & derivative speed values: CC BY-NC 4.0
원본 출처(OSM, KTDB)의 라이선스를 함께 준수해 주세요.

## Citation

학술 인용 시:

```
CAMUS Lab, "Korea Road Network ETA dataset (v3)",
HuggingFace, 2026. https://huggingface.co/datasets/CAMUS-LAB/data-road_network_eta
```
