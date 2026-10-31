---
language:
- ko
pretty_name: KoPolNLI-pre-v0.9
task_categories:
- text-classification
tags:
- natural-language-inference
- korean
- politics
- social-issues
- provisional-labels
size_categories:
- 10K<n<100K
license: cc-by-nc-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: KoPolNLI-pre-v0.9-train.parquet
  - split: validation
    path: KoPolNLI-pre-v0.9-validation.parquet
  - split: test
    path: KoPolNLI-pre-v0.9-test.parquet
---

\* This research was supported by the Graduate Student Mini Grant from the Department of Political Science and International Relations at Korea University.

\* 이 연구는 고려대학교 정치외교학과로부터 대학원생 Mini Grant를 지원받아 수행되었습니다.

# KoPolNLI-pre-v0.9

**Provisional release — not a human-verified NLI benchmark.** The `entailment` values in all three splits are the pair generators' **intended labels**, not independently adjudicated or human-gold labels. In particular, the test labels are being released ahead of planned human review. Do not use this test split for training, checkpoint selection, prompt tuning, or claims of final benchmark performance.

**이 버전의 train·validation·test 레이블은 생성형 모델에 의해 판정된 레이블이며 독립 판정이나 인간 검수로 확정된 정답이 아닙니다.
검수에 앞서 선공개된 버전이므로 최종 벤치마크 성능의 근거로 사용하지 마세요.**

KoPolNLI-pre-v0.9 is a Korean political and social-issues premise–hypothesis dataset. It is a **standalone generated dataset**; `1 = entailment`, `0 = non-entailment`.

## Size and splits

| Split | Pairs | Intended entailment (1) | Intended non-entailment (0) | Intended use |
| --- | ---: | ---: | ---: | --- |
| train | 71,216 | 35,608 | 35,608 | Provisional training |
| validation | 8,904 | 4,452 | 4,452 | Provisional model selection; not gold |
| test | 8,904 | 4,452 | 4,452 | Early-release evaluation only; human review pending |
| **Total** | **89,024** | **44,512** | **44,512** | |

Each public row has `premise_ko`, `hypothesis_ko`, `entailment`, and `task`. The `task` values are `stance detection`, `event extraction`, and `topic classification`. Source documents, source IDs, blind pair IDs, and private generation/annotation provenance are not distributed in these public Parquet files. The label origin for every row is `generator-intended-assumed-target`.

## Short premise Example pairs

The following are examples from the train split, using a short premise and a positive/negative hypothesis for each task. The `entailment` values are **generator-intended provisional labels**, not independently verified answers. These examples are not drawn from the test split.

### Stance detection

`premise_ko`: 중앙일보는 정치인들이 지역구 사업에 국가 재정을 끌어쓰는 관행을 비판했다. 이런 지역이기주의와 포퓰리즘이 계속되면 국민 세금과 국가 재정이 위험해진다고 평가했다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 중앙일보는 지역구 사업에 국가 재정을 낭비하는 정치인의 행태를 비판한다. | 1 |
| 중앙일보는 지역구 사업에 국가 재정을 끌어쓰는 정치인의 행태를 긍정적으로 평가한다. | 0 |

### Event extraction

`premise_ko`: 크라우드펀딩은 창업·벤처기업의 온라인 자금조달을 지원하기 위해 2016년 도입됐다. 김상훈 의원은 침체된 크라우드펀딩 활성화를 위한 자본시장법 개정안을 발의했다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 김상훈 의원은 크라우드펀딩 활성화를 위한 자본시장법 개정안을 발의했다. | 1 |
| 김상훈 의원은 크라우드펀딩 폐지를 위한 자본시장법 개정안을 발의했다. | 0 |

### Topic classification

`premise_ko`: 국회 수소경제포럼은 수소산업 발전을 위한 규제개선 정책과제 발굴 세미나를 열었다. 포럼은 수소 생산·저장·운송·활용 생태계와 관련 제도 개선이 필요하다고 밝혔다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 이 글은 수소경제와 수소산업 육성에 관한 내용이다. | 1 |
| 이 글은 전력산업과 전기요금 정책에 관한 내용이다. | 0

## Longer premise examples

These additional **verbatim train examples** use five-sentence premises. The labels are still generator-intended and provisional.

**Stance detection — longer premise (`premise_ko`)**: 대법원은 임금피크제 도입 전과 같은 일을 하면서 임금만 삭감된 A씨 사건에서 원고 일부 승소 판결을 확정했다. 재판부는 합리적 이유 없이 연령만으로 임금을 줄이는 제도가 고령자고용법에 위반된다고 판단했다. 임금 삭감에는 정년 연장이나 업무량 저감 같은 반대급부가 필요하다는 기준도 제시했다. 사설은 기존 임금피크제가 인건비 축소와 고령 노동자 구조조정에 악용되고 청년 고용 효과도 미미했다고 지적했다. 노사는 판결 취지에 맞게 차별을 없애고 경영계는 절감 재원을 신규 고용에 활용해야 한다고 주장했다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 사설은 임금피크제 적용에서 고령 노동자 차별을 없애야 한다고 주장한다. | 1 |
| 사설은 보상 없이 고령 노동자의 임금만 삭감하는 임금피크제를 지지한다. | 0 |

**Event extraction — longer premise (`premise_ko`)**: 동시다발 산불로 인명과 생활 터전, 문화유산까지 큰 피해를 입자 권영세 국민의힘 비상대책위원장은 28일 현장을 방문했다. 한덕수 대통령 권한대행을 포함한 당정 관계자들은 피해 상황과 진화 작업의 한계를 점검하고 복구·지원 대책을 논의했다. 정부는 전날 특별재난지역을 대폭 확대했다. 당정은 긴급 생활지원금을 빠르게 지급하고 지역경제 회복을 위한 맞춤 지원책을 마련하기로 했다. 또한 진화 자원과 장비를 보강하고 의료·복지 대책, 지방정부·지역사회 협력체계를 강화해 주민의 일상 복귀를 돕겠다고 밝혔다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 권영세 비상대책위원장과 정부 관계자들은 28일 산불 피해 현장을 점검했다. | 1 |
| 권영세 비상대책위원장은 산불 피해 현장점검을 취소하고 지원대책 논의를 중단했다. | 0 |

**Topic classification — longer premise (`premise_ko`)**: 김문수 의원이 분석한 자료에 따르면 전남대학교병원 응급실을 찾은 전남 환자의 사망률은 광주 환자보다 높았다. 전남에는 의과대학과 상급종합병원이 없어 의료 접근성이 취약한 점이 주요 원인으로 지적된다. 순천이나 목포에서 전남대학교병원까지 약 한 시간이 걸려 응급상황의 골든타임을 확보하기 어렵다. 순천에서 피습된 10대 여성이 병원을 거쳐 이송된 뒤 사망한 사례도 제시됐다. 김 의원은 사는 곳에 따라 생존 가능성이 달라지는 문제를 해결하려면 순천과 목포가 상생할 의대 설립 방안이 필요하다고 주장했다.

| `hypothesis_ko` | `entailment` |
| --- | ---: |
| 이 글은 전남 지역의 응급의료 격차와 지역 의과대학 설립 필요성에 관한 내용이다. | 1 |
| 이 글은 의사 파업에 따른 의료대란에 관한 내용이다. | 0

## Source material and construction

The source frame was assembled from Korean newspaper editorials, National Assembly member press releases, and political-party press releases published in **2014–2026**. The selected 30,000-document frame spans **2014-01-02 through 2026-08-28**, with 10,000 documents from each source family. The present release draws on 22,500 source documents from that frame: 22,256 yielded candidate pairs and 244 were excluded. Thus this release does **not** represent all 30,000 selected documents.

The project describes its upstream topic modeling as SBERT-based. The release-side selection records confirm 571 raw BERT/BERTopic-style topics and HDBSCAN, c-TF-IDF, and embedding-based assignment methods. The exact sentence-embedding/SBERT checkpoint is **not identified in this release's auditable artifacts**; no specific encoder is claimed here. Topic balancing was used to select generation inputs, not to estimate the real-world prevalence of issues or views.

Agents received topic references, example premise–hypothesis pairs, and the PolNLI-style task/label schema. They summarized source documents into premises and authored paired positive and controlled negative hypotheses. The requested generation families were Claude Sonnet 5 (29,344 pairs), GPT-5.6 Terra (59,080 pairs), and GPT-5.6 Sol for the two boundary waves (600 pairs).

## Split construction

The 89,024 pairs were assigned with seed 42 at the connected source-document/contrast-set group level, approximately 80% train, 10% validation, and 10% test. All four pairs from a source document stay in one split. Source IDs and exact premise–hypothesis pairs are disjoint across splits in the release audit. This protects against direct source reuse, but does not rule out near-duplicate texts, shared events, generator style, hypothesis-only cues, or overlap with external model pretraining. A high validation score against these intended labels is therefore not evidence of human-level NLI accuracy.

## Planned verification and limitations

- The **test** split is scheduled for human review. Its currently released labels are provisional and visible to anyone with access to the dataset; later use as a strictly blind benchmark would require a new held-out set.
- The **train and validation** splits are scheduled for independent labeling by GPT-6.1 Sol and Claude Sonnet 5.5, followed by agreement-based review. Those independent labels are **not included in this version**.
- Generated summaries and hypotheses can contain factual, semantic, stance, or polarity errors. Positive and negative examples may have stylistic artifacts. The dataset is topic-balanced and source-selected, not representative of Korean public opinion or the frequency of political issues.
- Political content may contain disputed claims, partisan framing, and identifiable public figures. A generated hypothesis is a model-produced statement, not an endorsement by a source publisher or the dataset creators.
- Original full-text articles and press releases are not distributed here. No license or permission for downstream redistribution of source-derived text is asserted by this card. Prospective public release and downstream uses should be assessed against the relevant source rights and terms.

## Loading

```python
from datasets import load_dataset

ds = load_dataset("jongrock17/KoPolNLI-pre-v0.9")
print(ds["train"][0])
```

## Version note

`pre-v0.9` deliberately denotes a pre-verification snapshot. Do not silently replace these intended labels with future adjudicated labels under the same version; publish a clearly versioned successor and document its changes.
