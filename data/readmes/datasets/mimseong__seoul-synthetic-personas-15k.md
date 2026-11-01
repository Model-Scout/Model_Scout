---
license: cc-by-4.0
language:
- ko
pretty_name: Seoul Synthetic Personas 15K
size_categories:
- 10K<n<100K
task_categories:
- text-generation
tags:
- synthetic
- persona
- agent-based-simulation
- seoul
- korean
configs:
- config_name: default
  data_files:
  - split: train
    path: data/personas-*.jsonl.gz
---

Seoul Synthetic Personas 15K
=========================================================================

# 데이터셋 개요 (Overview)
Seoul Synthetic Personas 15K는 서울시 거주자 15,000명을 가정해 합성한 페르소나 데이터셋입니다. 서울 행정동 단위의 소비·이동 특성과 [Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)의 생활 서사를 한 인물 안에 결합한 것이 특징입니다.

소비·이동 관련 수치는 [서울특별시 빅데이터캠퍼스](https://bigdata.seoul.go.kr) 데이터를 참조하여 반출 기준에 맞추어 합성하였고, 직업·취미·가족 등 서사 정보는 Nemotron-Personas-Korea의 서울 거주 페르소나에서 가져왔습니다. 서울 지역 정책이나 상권 변화에 대한 에이전트 기반 시뮬레이션(agent-based simulation)의 초기 인구로 쓰기 위해 제작되었습니다.

–

Seoul Synthetic Personas 15K is a dataset of 15,000 synthetic personas representing residents of Seoul. Each record combines dong-level consumption and mobility attributes with a narrative persona from [Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea).

Consumption and mobility attributes were synthesized with reference to data from the [Seoul BigData Campus](https://bigdata.seoul.go.kr), in line with its data export standards. Occupation, hobbies, family and other narrative attributes come from Seoul-resident personas in Nemotron-Personas-Korea. The dataset was built as an initial population for agent-based simulations of policy and local-commerce changes in Seoul.

## 데이터셋에 포함되지 않은 항목 (What is NOT in the dataset)
직장 위치, 좌표, 상세 주소는 포함하지 않으며, 거주지는 행정동 단위까지만 제공합니다. 개인 단위의 원천 데이터는 포함되어 있지 않습니다.

모든 데이터는 인공적으로 합성되었습니다. 이름이나 페르소나 설명이 실존 인물과 유사한 경우 이는 우연에 의한 것입니다.

–

Workplace, coordinates and street addresses are not included; residence is given at the administrative-dong level only. No individual-level source records are included.

All data is artificially generated. Any similarity in names or persona descriptions to actual persons is purely coincidental.

# 공개일 (Release Date)
2026-10-21

# 라이센스/이용 약관 (License/Terms of Use)
이 데이터셋은 [크리에이티브 커먼즈 저작자표시 4.0 국제 라이선스](https://creativecommons.org/licenses/by/4.0/deed.ko) (CC BY 4.0)에 따라 제공됩니다. Nemotron-Personas-Korea(CC BY 4.0)에서 가져온 필드를 포함하므로, 이용 시 해당 데이터셋의 출처도 함께 표기해 주시기 바랍니다.

–

This dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode) (CC BY 4.0). It contains fields derived from Nemotron-Personas-Korea (CC BY 4.0); please attribute that dataset as well.

# 의도된 사용 용도 (Intended Use)
* 서울 지역 정책·상권 시뮬레이션의 에이전트 초기화
* 지역·연령·소비 수준 조건을 건 페르소나 기반 텍스트 생성
* 소비 성향이 다른 가상 시민을 대상으로 한 인터뷰·설문 시뮬레이션

–

* Initializing agents for policy and local-commerce simulations in Seoul
* Persona-conditioned text generation by district, age and spending level
* Simulated interviews and surveys across citizens with different spending profiles

# 데이터셋 세부사항 (Dataset Details)

본 데이터셋은 다음을 포함합니다:
* 15,000건의 레코드 (1인 1레코드)
* 서울 25개 자치구, 421개 행정동
* 20대부터 70대 이상까지 6개 연령대, 성별 여성 7,706명 · 남성 7,294명
* 소비 수준, 업종별 소비 비율, 이동거리, 재택 시간 등 정량 속성
* Nemotron-Personas-Korea의 7가지 서사(요약, 직업, 스포츠, 예술, 여행, 음식, 가족)와 문화적 배경, 기술, 경력 목표, 취미
* 정량 속성과 서사를 바탕으로 작성한 5줄 생활 요약

–

The dataset contains:
* 15,000 records (one person per record)
* 25 districts (자치구) and 421 administrative dongs (행정동) of Seoul
* Six age groups from 20s to 70+, with 7,706 women and 7,294 men
* Quantitative attributes: spending level, spending share by category, travel distance, hours at home, etc.
* Seven narrative personas from Nemotron-Personas-Korea (concise, professional, sports, arts, travel, culinary, family) plus cultural background, skills, career goals and hobbies
* A five-line lifestyle summary written from the quantitative attributes and narratives

## 기반 데이터 (Seed Data)
* [서울특별시 빅데이터캠퍼스](https://bigdata.seoul.go.kr) 데이터 (반출 기준에 맞추어 합성한 행정동 × 성별 × 연령대 수준의 소비·이동 특성)
* 행정동 × 성별 × 연령대별 통신 기반 생활 지표 (외부 공개 데이터, 이동거리 · 배달 이용)
* [Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)의 서울 거주 페르소나 185,228명

–

* Data from the [Seoul BigData Campus](https://bigdata.seoul.go.kr) (consumption and mobility attributes at the dong × sex × age level, synthesized in line with export standards)
* Telecom-based living indicators by dong × sex × age (publicly available; travel distance and delivery use)
* 185,228 Seoul-resident personas from [Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea)

## 생성 방법 (Generation Process)
1. 서울을 행정동 × 성별 × 연령대 셀로 나누고, 인구 규모에 비례하여 15,000명을 배정했습니다.
2. 각 셀의 소비·이동 수준을 부여했습니다. 하루 소비액은 셀의 소비 분위 구간 안에서 추출했습니다.
3. 같은 자치구 · 성별 · 연령대 안에서 인물의 소비 순위와 Nemotron 페르소나의 사회경제 점수(학력 · 직업 · 주거) 순위를 맞추는 방식(rank coupling)으로 서사를 연결했습니다. 하나의 Nemotron 페르소나는 한 인물에만 연결됩니다.
4. 정량 속성과 서사를 LLM에 입력해 5줄 생활 요약을 작성했습니다.

–

1. Seoul was divided into dong × sex × age cells, and 15,000 people were allocated in proportion to population.
2. Each cell was assigned consumption and mobility levels; daily spending was sampled within the cell's spending-decile range.
3. Narratives were attached by rank coupling within the same district × sex × age group: a person's spending rank was matched to the socioeconomic score rank (education, occupation, housing) of Nemotron personas. Each Nemotron persona is used once.
4. A five-line lifestyle summary was written by an LLM from the quantitative attributes and narratives.

## 데이터 필드 (Data Fields)

| 필드 (Field) | 타입 (Type) | 설명 (Description) |
|---|---|---|
| `agent_id` | string | `AGT_{행정동코드}_{성별}_{연령대}_{번호}` |
| `residence.dong_code` / `dong` / `gu` | string | 거주 행정동 코드 · 행정동 · 자치구 |
| `personal.age_group` | string | 연령대 (20대 ~ 70대이상) |
| `personal.gender` | string | `F` / `M` |
| `personal.job` | string | 직업 (Nemotron `occupation`) |
| `personal.life_stage` | string | 생애 단계 (사회초년생, 독립, 기혼, 자녀양육, 은퇴, 학생) |
| `personal.income_proxy` | string | 소비 수준에서 매핑한 5단계 (상 ~ 하). 실제 소득이 아님 |
| `spending.weekday_spending_level` / `weekend_spending_level` | int | 1인 1일 소비 수준 10분위 (1 = 낮음) |
| `spending.daily_spending_weekday` / `daily_spending_weekend` | int | 하루 소비액 (원) |
| `spending.weekend_weekday_spending_ratio` | float | 주말 ÷ 평일 소비 비율 |
| `spending.top_categories` | dict | 업종 대분류별 소비 비율 (식사, 마트, 편의점, 건강, 쇼핑 등) |
| `behavior.delivery_days` | float | 월 배달 이용일 |
| `behavior.weekday_move_km` / `weekend_move_km` | float | 하루 이동거리 (km) |
| `behavior.home_hours_weekday` / `home_hours_weekend` | float | 집에 머무는 시간 (추정) |
| `behavior.mobility_level` | int | 이동성 10분위 |
| `personality.spending_tendency` | string | 절약형 / 보통 / 소비형 |
| `personality.lifestyle` | string | 5줄 생활 요약 (LLM 생성) |
| `nemotron_persona.*` | string, list | 요약, 취미, 문화적 배경, 혼인 상태, 주거 형태, 가구 형태, 학력 |
| `nemotron_extra.*` | string | 직업 · 스포츠 · 예술 · 여행 · 음식 · 가족 페르소나, 기술, 경력 목표, 전공, 병역, `uuid` |
| `match.*` | string, float | 매칭 방식, 매칭 단위, 소비 백분위, Nemotron 사회경제 점수, Nemotron `uuid` |

# 데이터셋 사용 방법 (How to use it)
본 데이터셋은 다음의 코드처럼 로드할 수 있습니다.

–

You can load the dataset with the following lines of code.

```python
from datasets import load_dataset

ds = load_dataset("mimseong/seoul-synthetic-personas-15k", split="train")
```

```python
>>> ds[1]["residence"], ds[1]["personal"]
({'dong_code': '11110560', 'dong': '평창동', 'gu': '종로구'},
 {'age_group': '20대', 'gender': 'F', 'job': '온라인 쇼핑 판매원', 'life_stage': '사회초년생', 'income_proxy': '하'})
>>> ds[1]["spending"]["daily_spending_weekday"], ds[1]["spending"]["daily_spending_weekend"]
(30144, 17499)
>>> ds[1]["nemotron_persona"]["summary"]
'안원희 씨는 교육학적 전문성을 온라인 커머스에 접목해 성장 중인 23세의 예비 창업가로, ...'
```

# 데이터셋 특징 (Dataset Characterization)

## 데이터 수집 방법 (Data Collection Method)
* 합성 데이터 (Synthetic)

## 데이터셋 포맷 (Dataset Format)
* JSON Lines, gzip 압축 5개 파일 (3,000 레코드씩)

## 데이터셋 크기 (Dataset Quantification)
* 레코드 개수 : 15,000 (15,000 records)
* 저장 용량 : 압축 22.6 MB, 해제 시 약 89 MB (22.6 MB compressed, ~89 MB uncompressed)

# 제한 사항 (Limitations)
* 같은 셀(행정동 × 성별 × 연령대)에 속한 인물은 소비 분위, 업종 비율, 이동거리 등 셀 단위 값을 공유합니다. 개인 간 차이는 주로 셀 내 추출과 서사에서 비롯됩니다.
* `personal.job`은 Nemotron-Personas-Korea의 분포를 따르며, 약 34%가 무직(학생, 전업주부, 은퇴자 포함)입니다.
* `personality.lifestyle` 중 약 1%는 "한 줄 요약:"과 같은 머리말이 포함되는 등 형식이 고르지 않습니다.
* 저자들의 시뮬레이션에서는 같은 방식으로 생성한 다른 버전의 정량 속성을 사용했으므로, 이 데이터셋만으로 해당 시뮬레이션 결과를 그대로 재현할 수는 없습니다.

–

* People in the same cell (dong × sex × age) share cell-level values such as spending decile, category shares and travel distance; individual variation comes mainly from within-cell sampling and the narratives.
* `personal.job` follows the Nemotron-Personas-Korea distribution; about 34% are unemployed (including students, homemakers and retirees).
* About 1% of `personality.lifestyle` entries are irregularly formatted (e.g., a leading "한 줄 요약:").
* The authors' simulations used a different generation of the quantitative attributes produced by the same method, so simulation results cannot be reproduced exactly from this dataset alone.

# 인용 (Citation)
본 데이터셋을 사용하실 경우 아래와 같이 인용해 주시기 바랍니다. Nemotron-Personas-Korea도 함께 인용해 주세요.

–

If you use this dataset, please cite it together with Nemotron-Personas-Korea.

```
@misc{seoul_synthetic_personas_15k,
  title = {Seoul Synthetic Personas 15K},
  year = {2026},
  url = {https://huggingface.co/datasets/mimseong/seoul-synthetic-personas-15k}
}

@software{nvidia/Nemotron-Personas-Korea,
  author = {Kim, Hyunwoo and Ryu, Jihyeon and Lee, Jinho and Ryu, Hyungon and Praveen, Kiran and Prayaga, Shyamala and Thadaka, Kirit and Jennings, Will and Sadeghi, Bardiya and Sharabiani, Ashton and Choi, Yejin and Meyer, Yev},
  title = {Nemotron-Personas-Korea: Synthetic Personas Aligned to Real-World Distributions for Korea},
  month = {April},
  year = {2026},
  url = {https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea}
}
```
