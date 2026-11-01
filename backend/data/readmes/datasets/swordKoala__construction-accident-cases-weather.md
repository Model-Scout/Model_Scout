---
language:
- ko
license: other
task_categories:
- text-classification
- tabular-classification
tags:
- construction-safety
- accident-cases
- weather
- risk-assessment
- korean
- csi
pretty_name: Construction Accident Cases with Weather
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files: csi_wt_wd_dataset.json
---

# 건설현장 사고사례 + 날씨 데이터셋 / Construction Accident Cases with Weather

과거 **건설현장 사고사례**(현장·공종·작업·피해·사고유형 등) 레코드에
**발생 시점의 기상 정보(기온·체감온도·풍속·습도)** 를 결합한 한국어 데이터셋입니다.
사고-기상 상관관계 분석, 위험요인 모델링, 건설안전 분석용 LLM/ML 학습의 원천 데이터로 활용할 수 있습니다.

A Korean dataset that joins **construction-site accident cases** (site, work type, task, damage,
accident type, etc.) with the **weather conditions at the time of the accident** (temperature,
apparent temperature, wind speed, humidity). Useful for accident–weather correlation analysis,
risk-factor modeling, and as a source corpus for construction-safety LLM/ML training.

> 본 데이터셋은 건설공사 안전관리 종합정보망(CSI) 계열 사고사례 데이터에
> 기상 관측 정보를 매칭·결합하여 구축되었습니다.

---

## 데이터 구성 / Dataset Summary

| 항목 | 값 |
|---|---|
| 총 레코드 수 (records) | **29,495** |
| 형식 (format) | 단일 JSON 배열 (flat record, 26 fields) |
| 파일 (file) | `csi_wt_wd_dataset.json` (약 43.9 MB, UTF-8) |
| 언어 (language) | 한국어 (ko) |
| 사고 발생 기간 | **2019-01-18 ~ 2025-03-04** |
| 스키마 일관성 | 전 레코드 동일 26개 필드 |

---

## 스키마 / Schema

각 레코드는 다음 26개 필드를 가진 평면(flat) JSON 객체입니다.

### 사고 정보 / Accident
| 필드 | 설명 | 예시 |
|---|---|---|
| `case_no` | 사고 식별 번호 (int) | `184` |
| `사고명` | 사고 발생 현장/공사명 | `… 외곽순환도로` |
| `시설물 종류` | 시설물 분류 (대-중-소) | `토목 - 터널 - 도로터널` |
| `사고경위` | 사고 발생 경위 서술 | `… 철근의 낙하로 근로자를 타격, 사망사고 발생` |
| `사고원인` | 주요 사고원인 | `* 주원인 : 안전관리계획 수립 미흡` |
| `구체적 사고원인` | 구체적 원인 서술 | `… 슬링벨트 체결 … 이탈하여 …` |
| `공사종류` | 공사 종류 (대/중/소) | `토목 / 터널 / 도로터널` |
| `공정률` | 공정 진행률 구간 | `40~49%` |
| `작업자수` | 현장 작업자 규모 구간 | `500인 이상` |

### 사고 분류 / Classification (KOSHA 체계)
| 필드 | 설명 | 예시 |
|---|---|---|
| `사고분류.공종` | 공종 | `토목 > 철근콘크리트공사` |
| `사고분류.사고객체` | 사고 객체 | `건설기계 > 기중기(이동식크레인 등)` |
| `사고분류.작업프로세스` | 작업 프로세스 | `운반작업` |
| `사고유형.인적` | 인적 사고유형 | `물체에 맞음` |
| `사고유형.물적` | 물적 사고유형 | `낙하` |

### 피해 상황 / Damage
| 필드 | 설명 |
|---|---|
| `피해상황.사망자수(명).내국인` / `.외국인` | 사망자 수 (int) |
| `피해상황.부상자수(명).내국인` / `.외국인` | 부상자 수 (int) |
| `피해상황.피해금액` | 피해 금액 |
| `피해상황.피해내용` | 피해 내용 서술 |

### 기상 정보 / Weather (본 데이터셋의 추가 결합 정보)
| 필드 | 설명 | 범위 (min ~ max, mean) |
|---|---|---|
| `기온(℃)` | 기온 | -19.3 ~ 37.3 (16.4) |
| `체감온도(℃)` | 체감온도 | -25.7 ~ 37.3 (15.9) |
| `10분풍속(m/s)` | 10분 평균 풍속 | 0.0 ~ 21.7 (2.1) |
| `습도(%)` | 상대습도 | 1 ~ 100 (59.8) |
| `발생일시_변환` | 사고 발생 일시 | `2020-05-07 11:40` |
| `요일` | 발생 요일 (영문) | `Thursday` |

```json
{
  "case_no": 184,
  "사고명": "… 외곽순환도로",
  "시설물 종류": "토목 - 터널 - 도로터널",
  "사고경위": "… 철근의 낙하로 근로자를 타격, 사망사고 발생",
  "공정률": "40~49%",
  "작업자수": "500인 이상",
  "사고분류.공종": "토목 > 철근콘크리트공사",
  "사고유형.인적": "물체에 맞음",
  "사고유형.물적": "낙하",
  "기온(℃)": 23.7,
  "체감온도(℃)": "23.7",
  "10분풍속(m/s)": "3",
  "습도(%)": 20,
  "발생일시_변환": "2020-05-07 11:40",
  "요일": "Thursday"
}
```

> 참고: 일부 수치 필드(`체감온도(℃)`, `10분풍속(m/s)`)는 원본 보존을 위해 문자열로 저장되어 있습니다. 사용 시 `float` 캐스팅을 권장합니다.

---

## 라벨 분포 / Label Distributions

### 사고유형(인적) — 상위 (Human accident type, top)
`물체에 맞음`(4,300), `끼임`(3,205), `넘어짐(미끄러짐)`(2,883), `부딪힘`(2,433),
`넘어짐(기타)`(2,428), `기타`(2,342), `떨어짐(2미터 미만)`(2,261), `절단, 베임`(2,186),
`넘어짐(물체에 걸림)`(1,982) 등 (고유 24종). `떨어짐`은 높이 구간별로 세분화.

### 사고유형(물적) (Physical accident type)
`없음`(26,076), `기타`(682), `전도`(438), `낙하`(359), `충돌`(246), `붕괴`(79),
`파열,파단`(78), `탈락`(76), `화재`(64), `폭발`(9) (고유 11종, 미기재 1,388).

### 시설물 대분류 / 공종 / 작업 (Facility / Work type / Task)
- **시설물 대분류**: 건축 22,302 · 토목 5,914 · 산업환경설비 1,026 · 조경 253
- **고유 공종 수**: 50개 (상위: `건축 > 철근콘크리트공사` 7,888, `건축 > 가설공사` 1,984, `기계설비 > 기계설비공사` 1,190, `토목 > 토공사` 1,166 …)
- **고유 작업프로세스 수**: 57개 (상위: `설치작업` 5,082, `이동` 3,205, `해체작업` 3,119, `운반작업` 2,638 …)
- **고유 사고객체 수**: 120개

### 공정률 / 작업자수 / 요일
- **공정률**: 10개 구간에 비교적 고른 분포 (`90% 이상` 4,325가 최다)
- **작업자수**: `19인 이하` 9,899, `100~299인` 5,992, `20~49인` 5,536 …
- **요일**: 평일(월~금)에 집중(각 ~5,000건), 토 3,745 · 일 1,050

### 피해 규모
- 누적 사망자: **1,344명** · 누적 부상자: **28,550명**

---

## 사용 예시 / Usage

```python
from datasets import load_dataset

ds = load_dataset("swordKoala/construction-accident-cases-weather", split="train")
print(ds[0])

# 예: 기온대별 사고 건수 집계
import collections
bins = collections.Counter(int(float(r["기온(℃)"]) // 5 * 5) for r in ds)
print(sorted(bins.items()))
```

또는 직접 JSON 로드:

```python
import json
data = json.load(open("csi_wt_wd_dataset.json", encoding="utf-8"))
print(len(data), "records")
```

---

## 구축 과정 / Provenance

- **원천(source)**: 건설공사 안전관리 종합정보망(CSI) 계열 사고사례 데이터.
- **결합(join)**: 각 사고의 `발생일시`·위치 정보를 기준으로 해당 시점의 **기상 관측값(기온·체감온도·10분 풍속·습도)** 을 매칭하여 결합.
- **정규화**: 사고유형/공종/작업프로세스 등은 KOSHA 표준 분류 체계에 정렬.

### 한계 / Limitations
- 일부 필드에 결측이 존재합니다 (예: `사고유형.물적` 미기재 1,388건, `사고분류.사고객체` 662건, `발생일시_변환`·`요일` 94건 등). 결측은 원본 그대로 보존했습니다.
- 수치 기상 필드 일부가 문자열로 저장되어 있어 분석 전 형 변환이 필요합니다.
- `사고명`에는 사고 발생 현장/위치 정보가 포함될 수 있습니다.
- 본 데이터는 연구·분석·보조 용도이며, 실제 안전 의사결정의 단독 근거로 사용하지 마십시오.

---

## 인용 / Citation

```bibtex
@misc{construction_accident_cases_weather,
  title  = {Construction Accident Cases with Weather Dataset},
  author = {swordKoala},
  year   = {2026},
  howpublished = {Hugging Face Hub},
  url    = {https://huggingface.co/datasets/swordKoala/construction-accident-cases-weather}
}
```
