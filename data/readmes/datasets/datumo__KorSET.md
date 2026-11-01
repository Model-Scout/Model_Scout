---
license: cc-by-nc-4.0
language:
- ko
pretty_name: KorSET (Korean Red-teaming Safety Evaluation)
size_categories:
- 1K<n<10K
task_categories:
- text-generation
tags:
- safety
- red-teaming
- korean
- benchmark
- taxonomy
- cultural-adaptation
dataset_info:
  features:
  - name: category_index
    dtype: string
  - name: lv1_name
    dtype: string
  - name: lv2_name
    dtype: string
  - name: lv3_name
    dtype: string
  - name: prompt
    dtype: string
  splits:
  - name: 1_A_Toxic_Language
    num_bytes: 156890
    num_examples: 369
  - name: 1_B_Sexual_Content
    num_bytes: 193648
    num_examples: 508
  - name: 2_C_Discrimination
    num_bytes: 1229114
    num_examples: 1175
  - name: 2_D_Bias_and_Hate
    num_bytes: 409227
    num_examples: 1352
  - name: 3_E_False_Misinformation
    num_bytes: 394079
    num_examples: 1404
  - name: 3_F_Prohibited_Advisory
    num_bytes: 248873
    num_examples: 929
  - name: 4_G_Privacy_Violation
    num_bytes: 149648
    num_examples: 560
  - name: 4_H_Sensitive_Info_Organization
    num_bytes: 185151
    num_examples: 674
  - name: 5_I_Illegal_Activities
    num_bytes: 206369
    num_examples: 533
  - name: 5_J_Violence_and_Extremism
    num_bytes: 209281
    num_examples: 687
  - name: 5_K_Enc_Unethical_Actions
    num_bytes: 198300
    num_examples: 546
  - name: 5_L_Security_Threats
    num_bytes: 167251
    num_examples: 512
  download_size: 1546453
  dataset_size: 3747831
configs:
- config_name: default
  data_files:
  - split: 1_A_Toxic_Language
    path: data/1_A_Toxic_Language-*
  - split: 1_B_Sexual_Content
    path: data/1_B_Sexual_Content-*
  - split: 2_C_Discrimination
    path: data/2_C_Discrimination-*
  - split: 2_D_Bias_and_Hate
    path: data/2_D_Bias_and_Hate-*
  - split: 3_E_False_Misinformation
    path: data/3_E_False_Misinformation-*
  - split: 3_F_Prohibited_Advisory
    path: data/3_F_Prohibited_Advisory-*
  - split: 4_G_Privacy_Violation
    path: data/4_G_Privacy_Violation-*
  - split: 4_H_Sensitive_Info_Organization
    path: data/4_H_Sensitive_Info_Organization-*
  - split: 5_I_Illegal_Activities
    path: data/5_I_Illegal_Activities-*
  - split: 5_J_Violence_and_Extremism
    path: data/5_J_Violence_and_Extremism-*
  - split: 5_K_Enc_Unethical_Actions
    path: data/5_K_Enc_Unethical_Actions-*
  - split: 5_L_Security_Threats
    path: data/5_L_Security_Threats-*
---

# KorSET — Korean Red-teaming Safety Evaluation Benchmark

> 소유자: DATUMO AI Safety Team
> 작성일: 2026-09-11
> 상태: active
> 대상리소스그룹: Public (academic / safety research)

> ⚠️ **WARNING**: 본 데이터셋은 LLM 안전성 평가를 위한 **의도적으로 적대적(adversarial)인 레드팀 프롬프트**를 포함하며, 불쾌하거나 유해하게 느껴질 수 있는 표현이 포함되어 있습니다. 학술 및 안전성 연구 목적으로만 사용해야 합니다.

**KorSET**은 **CAGE (Culturally Adaptive GEneration)** 프레임워크로 구축된 **문화 적응형 한국어 레드팀 안전성 평가 벤치마크**입니다. 영어 레드팀 벤치마크를 단순 번역하는 대신, 프롬프트의 **적대적 의도(구조)** 를 보존하면서 **한국의 언어·문화·법률 맥락**에 맞게 재구성하여, 국내 환경에 실재하는 사회·기술적 취약성을 평가할 수 있도록 설계되었습니다.

- 📄 **Paper**: *CAGE: A Framework for Culturally Adaptive Red-Teaming Benchmark Generation* (ICLR 2026)
- 💻 **Code**: https://github.com/selectstar-ai/CAGE-paper

## 1. 데이터셋 요약

- **목적 / 사용 프로젝트**: LLM의 **한국어 안전성 평가 및 ASR(Attack Success Rate) 기반 비교**를 위한 평가 전용 벤치마크. CAGE 프레임워크의 대표 사례(case study).
- **주요 특성**
  - 총 **9,249건**의 한국어 적대적(red-teaming) 프롬프트
  - 3단계 위험 택소노미: **위험 도메인(Lv1) 5개 · 카테고리(Lv2) 12개 · 세부 Type(Lv3)** (논문 기준 53 Types 설계)
  - 컬럼: `category_index`, `lv1_name`, `lv2_name`, `lv3_name`, `prompt`
  - 카테고리(Lv2)별 split 구성 (12 splits)
- **생성/수집 배경**: 기존 다국어 안전성 벤치마크는 **직접 번역** 방식이라 현지 문화·법에 뿌리내린 취약성을 포착하지 못해 LLM 안전성 평가의 사각지대를 만든다. KorSET은 검증된 영어 레드팀 프롬프트의 **적대적 의도를 한국 문화 맥락으로 이식**하여 이 공백을 메운다.
- **민감도**: **상~중** (적대적 프롬프트 — 오남용 방지를 위해 **접근 승인제(gated)** 로 배포)

## 2. Risk Taxonomy (5 Domains × 12 Categories)

| Lv1 (Domain) | Lv2 (Category) | # |
|---|---|---:|
| I. Toxic Contents | Toxic Language | 369 |
| I. Toxic Contents | Sexual Content | 508 |
| II. Unfair Representation | Discrimination | 1,175 |
| II. Unfair Representation | Bias and Hate | 1,352 |
| III. Misinformation Harms | False or Misleading Information | 1,404 |
| III. Misinformation Harms | Prohibited Advisory | 929 |
| IV. Information & Safety Harms | Privacy Violation Activity | 560 |
| IV. Information & Safety Harms | Sensitive Information of Organization/Government | 674 |
| V. Malicious Use | Illegal Activities | 533 |
| V. Malicious Use | Violence and Extremism | 687 |
| V. Malicious Use | Encouraging Unethical Actions | 546 |
| V. Malicious Use | Security Threats | 512 |
| | **합계** | **9,249** |

## 3. 데이터셋 생성 방식 (CAGE Pipeline)

- **가공/생성 방식**: **Human + AI**
- 핵심 개념 **Semantic Mold**: 프롬프트의 **적대적 구조**를 **문화적 내용**과 분리하는 슬롯 기반 표현. 유해 시나리오 표현에 필요한 최소 의미 요소(행위[Action]·대상[Target]·수단[Method]·조건[Condition] 등)를 정의한다.
- **3단계 파이프라인**
  1. **Seed Prompt Collection**: 검증된 영어 레드팀 벤치마크에서 시드 수집 → 문화 기반 택소노미로 매핑. **6개 모델의 만장일치(model agreement)** 로 라벨을 선별하고 **사람 검증**으로 신뢰도 확보.
  2. **Refinement (REFINER)**: 각 프롬프트를 **슬롯 태그가 붙은 Semantic Mold**로 재작성(예: "루머가 있다: [Fake Event] in [Time]"). `refined_sentence`, `refined_with_slot`, `slot_used`를 JSON으로 산출.
  3. **Content Localization (TRANSLATOR)**: Semantic Mold + 슬롯 스키마 + **한국의 실제 언어·규범·법률에 근거한 콘텐츠 풀**을 결합해 현지화된 프롬프트 생성. few-shot으로 문화적 구체성(예: 법령 조항·지역·고유명사) 반영.
- **품질 검증**: LLM-as-a-Judge(GPT-4.1) + 사람 평가로 위험 정합성·시나리오 현실성·문화 구체성 3축 채점 → 직접 번역 대비 전 도메인에서 품질 우위.

## 4. 데이터 구조 & 사용 방법

컬럼: `category_index`(예: 1_A), `lv1_name`, `lv2_name`, `lv3_name`(세부 Type), `prompt`(한국어 적대적 프롬프트).

```python
from datasets import load_dataset

# 접근 승인(gated) 후 사용
ds = load_dataset("datumo/KorSET", split="2_D_Bias_and_Hate")
print(ds[0]["prompt"])
```

## 5. 주요 실험 결과 (요약)

- CAGE 생성 프롬프트는 **직접 번역(DirTrans)·LLM 적응(LLM-Adapt) 대비 유의하게 높은 ASR** 달성 (예: Llama-3.1에서 Direct Request ASR 43.8% vs 28.2%/32.4%).
- 성능 향상의 주 동인은 **문화 지식 격차(Cultural Knowledge Gap, ∆Culture +20~35%)** 로, 단순 구체성(specificity)보다 크다 → **문화 기반 벤치마크의 필요성**을 실증.
- 프레임워크의 일반화 가능성을 **크메르어(Khmer, 저자원 언어)** 에 적용해 검증.

## 6. 윤리 및 접근 통제

KorSET은 레드팀 도구로서 **의도적으로 적대적인 프롬프트**를 담고 있어 오남용 소지가 있습니다. 이를 방지하기 위해 **HuggingFace 접근 승인제(gated)** 로 배포하며, 접근 요청은 수동 검토를 거쳐 **학술 및 안전성 연구 목적**으로 사용을 제한합니다.

## 7. 라이선스

**CC BY-NC 4.0** (비상업적)

## 8. Citation

```bibtex
@inproceedings{kim2026cage,
  title     = {CAGE: A Framework for Culturally Adaptive Red-Teaming Benchmark Generation},
  author    = {Kim, Chaeyun and Lim, YongTaek and Kim, Kihyun and Kim, Junghwan and Kim, Minwoo},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2026}
}
```
