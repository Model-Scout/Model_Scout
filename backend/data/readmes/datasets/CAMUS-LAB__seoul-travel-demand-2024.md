---
language:
  - ko
license: other
license_name: source-attribution
license_link: https://sgis.kostat.go.kr/
pretty_name: Seoul Travel Demand Foundation Dataset (2024)
tags:
  - urban-mobility
  - travel-demand
  - transportation
  - gis
  - seoul
  - korea
  - origin-destination
  - trip-generation
  - census
  - living-population
configs: []
---

# Seoul Travel Demand Foundation Dataset (2024)

서울특별시 **통행수요 모델링** 을 위한 공간·인구·도로·토지이용 통합 raw 데이터셋.
2024년 인구주택총조사(SGIS) + 2024-12 서울 생활인구(LOCAL_PEOPLE) + 도로명주소·LSMD 용도지역 필지 + SGIS 집계구 경계(2016·2025) 를 한 곳에 모았습니다.

대상: **교통공학 대학원생·연구자**. Trip Generation, OD Estimation, Land-Use Mix, Activity Pattern 분석의 기반 데이터로 사용 가능.

---

## 빠른 시작

```bash
# 1) 다운로드 (7z 단일 파일, 약 ~2 GB)
huggingface-cli download CAMUS-LAB/seoul-travel-demand-2024 \
    seoul_taz_raw.7z --repo-type dataset --local-dir .

# 2) 압축 해제 (7-Zip 필요)
7z x seoul_taz_raw.7z   # → ./data/raw/ 생성

# 3) 강좌 노트북 (별도 lecture_note 동봉 시)
jupyter lab lecture_note/notebooks/01_spatial_data.ipynb
```

압축 해제 후 디렉터리 = `data/raw/` 1개.

---

## 데이터셋 구성 (7z 안)

```
data/raw/
├─ sgis_oa/                 2025 SGIS 집계구 경계 (19,097 폴리곤, 권위 키 TOT_OA_CD 14자리)
├─ sgis_oa_2016/            2016 SGIS 집계구 경계 (19,153 폴리곤, LOCAL_PEOPLE 매핑 기반)
├─ sgis_census/             2024 SGIS 인구·가구·주택 통계 10종 (long format CSV, cp949)
├─ seoul_living_pop/        서울 생활인구 2024-12 (KT 시그널링 기반, 시간대 × OA × 성연령)
│                            ⚠ zip 그대로 보존 (3.7 GB compressed). zipfile 모듈로 스트리밍 권장.
├─ roads/
│  ├─ centerline/           국토지리정보원 도로중심선 (414,791 LineString)
│  ├─ segment/              도로명주소 도로구간 (66,698 LineString, ROA_CLS_SE 등급)
│  └─ _reference/           인접 프로젝트 알고리즘 참고 코드
├─ lsmd_zoning/             국토부 LSMD 용도지역지구도 (89.9만 필지, A7=용도지역 코드)
└─ lsmd_zoning_uq111/       LSMD 일반주거 1종 별도 추출
```

각 디렉터리의 자세한 컬럼 명세는 동봉된 `data/README.md` (md 파일 47KB, 전 컬럼·인코딩·CRS 명세) 참조.

---

## 키 데이터 요약

| 데이터 | 행/객체 수 | 시점 | 핵심 키 | 비고 |
|---|---:|---|---|---|
| SGIS 집계구 (2025) | 19,097 폴리곤 | 2025-06-30 | `TOT_OA_CD` (14) | EPSG:5179. 605.3 km² |
| SGIS 집계구 (2016) | 19,153 폴리곤 | 2016 | `TOT_REG_CD` (13) | LOCAL_PEOPLE 호환 |
| SGIS 인구·가구·주택 통계 | 10 CSV | 2024 | `TOT_OA_CD` × `var_code` | `value='N/A'` 통계 보호 |
| 서울 생활인구 | 31일 × 24h × 19,152 OA | 2024-12 | `집계구코드` (13, 2016 SGIS) | KT LTE 시그널링 |
| 도로 중심선 | 414,791 라인 | 2025-08 | `UFID` | RDDV 등급 코드 |
| 도로구간 (도로명주소) | 66,698 라인 | 2026-01 | `RDS_MAN_NO` | **ROA_CLS_SE 가 권위 등급** |
| LSMD 필지 + 용도지역 | 899,432 필지 | 2026-04-12 | `pnu` (19) | 11 zone class 매핑 가능 |

---

## 좌표계

| EPSG | 단위 | 사용 데이터 |
|---:|---|---|
| **5179** | m | SGIS, 도로, 분석 표준 |
| 5186 | m | LSMD raw (분석 시 5179 변환) |
| 5174 | m | KTDB raw (현재 부재) |
| 4326 | degree | 웹 뷰어 |

---

## 통합 작업의 핵심 사실

1. **LOCAL_PEOPLE 의 13자리 `집계구코드` = 2016 SGIS `TOT_REG_CD`** (100% 일치 검증).
2. 2016 → 2025 SGIS 는 폴리곤 50개 재구획. 공간 교차 면적가중 매핑 필요 (코드 동봉).
3. 행안부 행정동 8자리 ≠ SGIS 행정동 8자리 (시군구 prefix 부터 다름). 직접 join 금지.
4. 면적·거리 계산은 EPSG:5179 (m 단위) 에서만 의미 있음.
5. SGIS `value='N/A'` 와 LP 미수집 OA 는 NaN 보존 — 0 imputation 금지.

자세한 매핑 chain·검증 결과는 동봉 `data/README.md` 참조.

---

## 출처·라이선스

각 raw 데이터는 출처별 라이선스를 따릅니다. **재배포 시 반드시 출처 표기**:

| 데이터 | 출처 | 라이선스 |
|---|---|---|
| SGIS 집계구·통계 | 통계청 SGIS (`sgis.kostat.go.kr`) | 통계청 공공누리 |
| 서울 생활인구 | 서울 열린데이터 광장 (`data.seoul.go.kr/dataList/OA-14979/F/1/datasetView.do`) | 공공누리 1유형 |
| 도로중심선 | 국토지리정보원 (NGII) | NGII 약관 |
| 도로명주소 도로구간 | 행정안전부 도로명주소 전자지도 | 공공누리 |
| LSMD 용도지역지구도 | 국토교통부 공간정보 | 공공누리 |

본 데이터셋은 **연구·교육 목적의 학술 활용** 을 전제로 큐레이션·재배포되었습니다.
원천 데이터의 갱신·정정은 출처 사이트 기준이 우선합니다.

---

## 분석 단위 — Superblock (제안)

본 데이터셋과 함께 공개된 **superblock 분석 단위 정의** (코드 별도 공개) :
- 도로 등급 1~3 (간선) 으로 polygonize → 1,647 cell → 산/강 OA 제외 → **907 도시 superblock**
- median 264,000 m² (≈ 510 × 510 m). 도시 통행 단위에 가까움.

---

## 인용

```bibtex
@dataset{seoul_travel_demand_2024,
  author       = {CAMUS Lab},
  title        = {Seoul Travel Demand Foundation Dataset (2024)},
  year         = {2026},
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/CAMUS-LAB/seoul-travel-demand-2024},
}
```

원천 데이터는 별도로 각 출처를 인용하십시오.

---

## 문의

CAMUS Lab — `https://huggingface.co/CAMUS-LAB`
