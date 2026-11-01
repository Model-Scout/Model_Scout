---
language:
- ko
license: other
task_categories:
- text-generation
tags:
- construction-safety
- risk-assessment
- korean
- sft
- sharegpt
- instruction-tuning
pretty_name: RAGCON Construction Safety SFT
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files: sft_train.json
---

# RAGCON 건설현장 안전 분석 SFT 데이터셋 / Construction Safety Analysis SFT Dataset

건설현장의 **현장 조건(시설물·공종·작업·공정률·작업자수·기상 등)** 을 입력하면
**예상 사고유형, 심각도 등급, 위험 시나리오, 사고원인, 예방 조치**를 생성하도록 LLM을
지도학습 미세조정(SFT)하기 위한 한국어 instruction 데이터셋입니다.

A Korean instruction-tuning dataset for supervised fine-tuning (SFT) of LLMs to perform
**construction-site risk analysis**: given site conditions (facility, work type, task, progress
rate, worker count, weather), the model predicts the **expected accident type, severity grade,
risk scenario, root cause, and preventive measures**.

> 본 데이터셋은 RAGCON 프로젝트에서 사용 가능 데이터로 선별된 `risk`(위험성평가) 계열 데이터를
> 기반으로, 사고사례(accident) 정보와 결합·라벨 정규화·입력 패러프레이즈 증강을 거쳐 구축되었습니다.
> (변동성이 높은 `accident`·`law` 데이터는 학습에서 제외하고 RAG 검색 전용으로 사용)

---

## 데이터 구성 / Dataset Summary

| 항목 | 값 |
|---|---|
| 총 샘플 수 (samples) | **28,646** |
| 형식 (format) | ShareGPT 대화형 (`conversations`: system → human → gpt) |
| 파일 (file) | `sft_train.json` (단일 JSON 배열, 약 36.8 MB) |
| 언어 (language) | 한국어 (ko) |
| 턴 구조 | 전 샘플 3-turn (system/human/gpt) 일관 |
| 시스템 프롬프트 | 단일 고정 프롬프트 |

### 스키마 / Schema

각 레코드는 ShareGPT 형식을 따릅니다:

```json
{
  "conversations": [
    { "from": "system", "value": "당신은 건설현장 안전 분석 전문가입니다. ..." },
    { "from": "human",  "value": "다음 건설현장의 위험을 분석해 주세요.\n\n시설물: ...\n공종: ...\n작업: ...\n공정률: ...\n작업자수: ...\n기상: ..." },
    { "from": "gpt",    "value": "사고유형(인적): ...\n사고유형(물적): ...\n심각도: ...\n위험 시나리오: ...\n사고원인: ...\n구체적 원인: ...\n예방 조치:\n- ...\n- ...\n- ..." }
  ]
}
```

**입력(human) 필드**: `시설물`, `공종`, `작업`, `공정률`, `작업자수`, `기상`, (일부) `시간대`
**출력(gpt) 필드**: `사고유형(인적)`, `사고유형(물적)`, `심각도`, `위험 시나리오`, `사고원인`, `구체적 원인`, `예방 조치`(항상 3개 항목)

---

## 입력 템플릿 변형 / Input Template Variants

모델의 표현 강건성(robustness)을 위해 동일 의미의 입력을 3가지 형태로 증강했습니다.

| 템플릿 | 샘플 수 | 비율 | 예시 |
|---|---:|---:|---|
| 구조화 키-값 | 19,744 | 68.9% | `시설물: 토목 - 도로 - 도로\n공종: ...` |
| 구조화 + 시간대 | 3,314 | 11.6% | 위 형태 + `시간대: ...` |
| 자연어 패러프레이즈 | 5,588 | 19.5% | `토목 - 항만 - 방파제 / ... — 위험 분석 요청` 또는 완전 서술형 문장 |

출력(gpt) 스키마는 모든 변형에서 동일합니다.

---

## 라벨 분포 / Label Distributions

### 심각도 (Severity)

| 등급 | 건수 | 비율 |
|---|---:|---:|
| 경상위험 | 24,896 | 86.9% |
| 사망위험 | 3,312 | 11.6% |
| 저위험 | 258 | 0.9% |
| 중상위험 | 180 | 0.6% |

### 사고유형(인적) — 상위 항목 (Human accident type, top)

KOSHA 표준 재해유형 체계에 정렬: `물체에 맞음`(4,045), `끼임`(2,970), `넘어짐(미끄러짐)`(2,544),
`넘어짐(기타)`(2,232), `부딪힘`(2,190), `떨어짐(2미터 미만)`(2,057), `절단·베임`(1,903),
`넘어짐(물체에 걸림)`(1,732), `깔림`(912) 등. `떨어짐`은 높이 구간별로 세분화.

### 사고원인 — 상위 항목 (Root cause, top)

`작업자 부주의`(15,133 · 52.8%), `작업자의 불안전한 행동`(2,320), `작업자 통제 미흡`(878),
`위험정보 미제공`(834), `작업순서 미준수`(811), `시공품질 미확보`(542) 등.

### 시설물 대분류 / 공종 / 작업 (Facility / Work type / Task)

- **시설물 대분류**(구조화 샘플 기준): 건축 17,387 · 토목 4,642 · 산업환경설비 846 · 조경 183
- **고유 공종 수**: 50개 (예: `건축 > 철근콘크리트공사`, `건축 > 가설공사`, `기계설비 > 기계설비공사`, `토목 > 토공사`, `건축 > 철골공사` …)
- **고유 작업유형 수**: 57개 (예: `설치작업`, `이동`, `해체작업`, `운반작업`, `정리작업`, `조립작업`, `타설작업` …)

---

## 사용 예시 / Usage

```python
from datasets import load_dataset

ds = load_dataset("swordKoala/ragcon-construction-safety-sft", split="train")
print(ds[0]["conversations"])
```

ShareGPT 형식이므로 **LLaMA-Factory, Axolotl, Unsloth** 등에서 `conversations`(roles: `system`/`human`/`gpt`)
스키마로 바로 사용할 수 있습니다.

```yaml
# 예: LLaMA-Factory dataset_info.json
"ragcon_safety": {
  "hf_hub_url": "swordKoala/ragcon-construction-safety-sft",
  "formatting": "sharegpt",
  "columns": { "messages": "conversations" },
  "tags": { "role_tag": "from", "content_tag": "value",
            "user_tag": "human", "assistant_tag": "gpt", "system_tag": "system" }
}
```

---

## 구축 과정 / Provenance

- **원천(source)**: RAGCON 프로젝트의 `risk`(건설작업 위험성평가) 계열 데이터 (원본 약 2,426건, 11개 JSONL).
  주요 구성: `syn_risk_data`(Gemini 합성, 약 67%), `kras_risk_chunks`(KRAS 실데이터), 공종별 위험성평가 파일.
- **가공(processing)**: 원천 데이터의 품질 이슈(재해유형 동의어 중복, 구분자 불일치, 비표준 등급 등)를 정리하고,
  사고사례 정보(기상·심각도·구체 시나리오)와 결합하여 **사고유형/심각도/원인/예방조치** 스키마로 재구성.
  입력은 3가지 템플릿으로 패러프레이즈 증강.
- **참고 문서**: 「건설안전 데이터셋 LLM 활용방안 분석」, 「Risk 데이터 품질 분석」.

### 한계 / Limitations

- 합성(Gemini) 데이터 비중이 높아 일부 공종은 합성 분포에 의존합니다 — 실제 현장 분포와 차이가 있을 수 있습니다.
- 라벨 불균형: `심각도`는 `경상위험`(86.9%)에, `사고원인`은 `작업자 부주의`(52.8%)에 크게 치우쳐 있습니다.
- **완전 중복(human+gpt 동일) 583건(약 2%)이 의도적으로 보존**되어 있습니다 (원본 유지). 필요 시 사용자가 제거하십시오.
- 의료·법적 판단이나 실제 안전 의사결정의 단독 근거로 사용하지 마십시오. 연구/보조 용도로 활용하십시오.

---

## 인용 / Citation

```bibtex
@misc{ragcon_construction_safety_sft,
  title  = {RAGCON Construction Safety Analysis SFT Dataset},
  author = {swordKoala},
  year   = {2026},
  howpublished = {Hugging Face Hub},
  url    = {https://huggingface.co/datasets/swordKoala/ragcon-construction-safety-sft}
}
```
