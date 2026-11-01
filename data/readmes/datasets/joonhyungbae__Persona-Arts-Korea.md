---
license: cc-by-4.0
language:
- ko
size_categories:
- 10K<n<100K
task_categories:
- text-generation
pretty_name: Persona Arts Korea
tags:
- synthetic
- personas
- Korean
- cultural-arts
- public-statistics-grounded
- iterative-proportional-fitting
configs:
- config_name: default
  data_files:
  - split: train
    path: personas.parquet
---

# Persona Arts Korea (PAK)

30,000 synthetic Korean cultural arts personas grounded in the
[2024 Survey of Korean Artists](https://www.mcst.go.kr/site/s_policy/dept/deptView.jsp?pSeq=2002&pDataCD=0417000000&pType=)
(Ministry of Culture, Sports and Tourism). Each persona carries 16
quantitative variables and 17 narrative fields in Korean.

## Quick facts

| | |
|---|---|
| Personas | 30,000 |
| Language | Korean |
| Art fields | 14 |
| Variables per persona | 16 quantitative + 17 narrative |
| Source | 2024 Survey of Korean Artists (population 334,036; respondents 5,059) |
| Source licence | KOGL Type 1 |
| Release licence | CC-BY-4.0 |

## How to load

```python
from datasets import load_dataset

ds = load_dataset("joonhyungbae/Persona-Arts-Korea")
print(ds["train"][0])
```

Or read the Parquet directly:

```python
import pandas as pd
df = pd.read_parquet("hf://datasets/joonhyungbae/Persona-Arts-Korea/personas.parquet")
```

## Schema

### Quantitative variables

| Variable | Type | Values |
|---|---|---|
| `pak_uuid` | string | unique identifier |
| `art_field_primary` | categorical(14) | 문학, 미술, 공예, 사진, 건축, 음악, 국악, 대중음악, 방송연예, 무용, 연극, 영화, 만화, 기타 |
| `sex` | categorical(2) | 남자, 여자 |
| `age` | int | 13–90 |
| `age_band` | categorical(7) | 10대, 20대, 30대, 40대, 50대, 60대, 70대 이상 |
| `province` | categorical(18) | 17 administrative provinces plus 기타 |
| `education_level` | string | 4-level free-text education label |
| `education_level_pak` | categorical(3) | 고졸 이하, 대졸 이하, 대학원 이상 |
| `career_years` | int | 0–50 |
| `career_band` | categorical(5) | 10년 미만, 10–20년 미만, 20–30년 미만, 30–40년 미만, 40년 이상 |
| `employment_type` | categorical(2) | 전업, 겸업 |
| `is_freelance` | bool | freelance status |
| `has_secondary_job` | bool | derived from employment / freelance |
| `individual_art_income_bracket` | categorical(9) | 없음, 5백만원 미만, …, 6천만원 이상 (creative income) |
| `household_income_bracket` | categorical(9) | household total income |
| `has_contract_experience` | bool | contract activity in past year |
| `uses_standard_contract` | categorical(3) | True, False, None (None when no contract experience) |
| `has_copyright` | bool | holds copyright or neighbouring rights |
| `had_career_break` | bool | one or more career-interruption episodes |
| `has_overseas_experience` | bool | overseas artistic activity in past year |
| `occupation` | string | free-text occupation aligned with art field |
| `country` | string | constant "대한민국" |

### Narrative fields (all Korean)

| Field | Description |
|---|---|
| `persona` | One-sentence third-person summary |
| `professional_persona` | Professional life and work rhythm |
| `creative_world_persona` | Creative philosophy and craft worldview |
| `network_persona` | Professional network and collaboration patterns |
| `living_persona` | Living environment and daily logistics |
| `support_persona` | Attitude toward public arts funding and grants |
| `family_persona` | Family life and time allocation |
| `sports_persona` | Physical activity and body management |
| `arts_persona` | Arts consumption outside the persona's own field |
| `travel_persona` | Leisure travel patterns |
| `culinary_persona` | Eating habits and food culture |
| `cultural_background` | Family origin and entry point into the art form |
| `skills_and_expertise` | Skills and tools (paragraph) |
| `skills_and_expertise_list` | Normalised skill items (string-encoded list) |
| `hobbies_and_interests` | Hobbies and side interests (paragraph) |
| `hobbies_and_interests_list` | Normalised hobby items (string-encoded list) |
| `career_goals_and_ambitions` | Medium-term career goals |

## Source

The dataset is derived from the 2024 Survey of Korean Artists
(「2024년 예술인 실태조사 통계보고서」), released by the Korea Culture and
Tourism Institute under [Korea Open Government Licence Type 1](https://www.kogl.or.kr/info/license.do).
KOGL Type 1 permits redistribution and derivative works with
attribution.

Each quantitative distribution in this dataset traces to a publicly
verifiable cell in the source report. The release bundles the 15
grounding tables (T1–T15) under `grounding/` for transparency.

## Distribution quality

### Field marginal (vs source population)

All 14 art fields lie within 0.25 percentage points of the population
share.

| Field | Synthetic % | Report % | Diff |
|---|---:|---:|---:|
| 미술 (fine art) | 24.42 | 24.27 | +0.15 |
| 대중음악 (popular music) | 17.28 | 17.50 | -0.22 |
| 음악 (classical music) | 11.34 | 11.14 | +0.20 |
| 방송연예 (broadcasting and entertainment) | 9.28 | 9.40 | -0.12 |
| 문학 (literature) | 9.15 | 9.10 | +0.05 |
| 연극 (theatre) | 8.01 | 8.05 | -0.04 |
| 사진 (photography) | 4.41 | 4.66 | -0.25 |
| 국악 (traditional Korean music) | 3.64 | 3.65 | -0.01 |
| 영화 (film) | 2.87 | 2.74 | +0.13 |
| 무용 (dance) | 2.43 | 2.36 | +0.07 |
| 기타 (other) | 2.38 | 2.33 | +0.05 |
| 공예 (craft) | 1.95 | 1.87 | +0.08 |
| 건축 (architecture) | 1.61 | 1.69 | -0.08 |
| 만화 (comics) | 1.24 | 1.25 | -0.01 |

### Survey-rate fact checks

All five within 1 percentage point of the published rate.

| Variable | Source report | Synthetic | Diff |
|---|---:|---:|---:|
| Full-time rate | 52.50% | 52.25% | -0.25 |
| Contract experience | 57.30% | 57.72% | +0.42 |
| Copyright holding | 29.10% | 28.76% | -0.34 |
| Career break experience | 23.00% | 23.06% | +0.06 |
| Overseas activity | 16.50% | 16.72% | +0.22 |

### Age-by-variable cross-tab cells

Across 104 cells covering eight (age group × variable) cross-tabs,
**every cell** lies within 5 percentage points of the source statistics.
Maximum absolute deviation is 4.67 percentage points; mean absolute
deviation is 1.15 percentage points.

### Narrative validation

| Validator | Flagged rows |
|---|---:|
| Cultural-background timeline | 0.90% |
| Late-debut tone | 0.15% |
| Schema pass rate | 100% |
| Live cliché count | 0 |

## Intended uses

- Supervised fine-tuning of Korean language models for persona
  conditioning in the cultural arts domain
- Few-shot exemplar pools for prompt engineering involving Korean
  artist personas
- Controllable evaluation sets where downstream tasks condition on
  quantitative anchors with a known joint distribution

## Out-of-scope uses

- Substituting surveys of real Korean artists. The personas are
  synthetic and do not represent individual respondents.
- Distributional reference for Korean culture beyond the registered
  artist population.
- Privacy-respecting transformation of any individual respondent. No
  individual records were used in generation.
- Inferring health, political, or other variables not covered by the
  source survey.

## Limitations

The quantitative distributions are grounded in the source statistics,
but the narrative fields are generated by a language model conditioned
on those quantitative anchors and are not derived from observational
data. A persona's lived experience as written is not the experience of
any real artist.

The narrative generator is qwen3:30b-a3b at temperature 0.45 with a JSON
output schema. Narrative voice and length reflect this choice.

Validation is fully automated. The released table contains only the
quantitative and narrative fields listed in the Schema section. No
human-rater labels, review statuses, memos, or annotation columns are
shipped with the dataset. Quality is evidenced by the cell-level
distribution metrics above (field marginal, survey-rate fact checks,
age-by-variable cross-tabs) and by the automated narrative validators.

## Citation

```bibtex
@misc{pak2026,
  author = "Bae, Joonhyung",
  title  = "PAK: A Publicly Grounded Synthetic Persona Dataset of Korean Cultural Arts Workers",
  year   = "2026"
}
```

Please also cite the upstream source:

```bibtex
@techreport{kctistudy2024,
  author      = "{Korea Culture and Tourism Institute}",
  title       = "{2024 Survey of Korean Artists}",
  institution = "Ministry of Culture, Sports and Tourism",
  year        = "2024",
  note        = "Korea Open Government Licence Type 1"
}
```

## Acknowledgements

The author thanks the Korea Culture and Tourism Institute for
releasing the 2024 Survey of Korean Artists under Korea Open Government
Licence Type 1, which made this work possible.
