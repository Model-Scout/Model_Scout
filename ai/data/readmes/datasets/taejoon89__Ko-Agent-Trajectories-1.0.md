---
language:
  - ko
license: cc-by-4.0
size_categories:
  - 100K<n<1M
task_categories:
  - text-generation
task_ids:
  - dialogue-generation
tags:
  - korean
  - tool-use
  - tool-calling
  - agent
  - multi-turn
  - conversational
  - synthetic
  - distilled-from-glm-5.1
  - dpo
  - benchmark
configs:
  - config_name: train
    data_files:
      - split: train
        path: train/*.jsonl.gz
  - config_name: eval
    data_files:
      - split: test
        path: eval/*.jsonl.gz
  - config_name: dpo
    data_files:
      - split: train
        path: dpo/*.jsonl.gz
  - config_name: dpo_behavior
    data_files:
      - split: train
        path: dpo_behavior/*.jsonl.gz
---

# Ko-Agent-Trajectories-1.0

> **Dataset card v1.1.1 (2026-09-22).** The pipeline code is now released in this repository
> under `pipeline/`, together with the API catalogue, the scenario templates and the complete
> prompt set. The card reports the completed human review study and the v1.1 artefacts
> (behaviour DPO config, per-item validation scores, manifest, filter asset).
> Korean edition: `README.ko.md`.

## TL;DR

A **Korean multi-turn agent ↔ tool trajectory corpus** synthesized with GLM-5.1-FP8 as teacher: **518,232** SFT trajectories + **33,323** DPO chosen/rejected pairs + a **9,936**-item evaluation benchmark (Ko-Agent-Trajectories eval) + **14,238** behaviour-targeted preference pairs (v1.1), with 3-rater cross-judge metadata (GLM + GPT-5.4-mini + Claude Sonnet 4.5). **Data: CC BY 4.0. Pipeline code: Apache-2.0.**

**New (2026-07, card v1.0.1)**: downstream training experiments now **validate the dataset's effectiveness** — full SFT + DPO on Qwen3-8B yields a statistically significant +3.84%p composite gain over base (p<0.0001, n=9,934 paired bootstrap) — and characterize an important **behavior-transfer property** every user should read before training ([§ Downstream Validation](#downstream-validation-v11-2026-07)).

*한국어 요약: 한국어 tool-use 학습용 공개 코퍼스 (SFT 518K + DPO 33K + 벤치마크 9.9K + 행동 표적 DPO 14K). 한국어판 데이터시트는 `README.ko.md`.*


> **Naming.** The evaluation split is referred to as **Ko-Agent-Trajectories eval** throughout. Two released files, `bench/leaderboard.json` and `validation/bench_consensus_ids.json`, still carry the earlier internal label `Ko-Agent-Bench-1.0` from the v1.0 release; they are unchanged so that their checksums keep matching `MANIFEST.json` and the Zenodo deposit. This split is unrelated to the [Ko-AgentBench](https://huggingface.co/datasets/huggingface-KREW/Ko-AgentBench) dataset by Hugging Face KREW.

## Motivation

As of May 2026, there was effectively **no public Korean dataset for training LLM tool-use ability**. Only small evaluation sets existed (FunctionChat-Bench: 700 items, Ko-AgentBench: 106 items). This dataset fills that gap, enabling Korean LLMs to learn:

- Function-calling format correctness
- Multi-turn agentic behavior (plan → call → observe → answer)
- Natural Korean planning text (16 personas × register diversity)
- Error recovery (L5 includes deliberate error simulation)

Scale (~520K), license (CC BY 4.0), and diversity (12 categories × 6 difficulty levels × 16 personas × 4 registers) were all differentiators among Korean open datasets at v1.0 release time.

## Composition

### 1. Splits

| split | n | shards | purpose |
|---|---|---|---|
| **train** | **518,232** | 519 | SFT (Korean multi-turn tool use) |
| **dpo** | **33,323** chosen/rejected pairs | 34 | preference training (DPO/IPO/SimPO) |
| **test** (Ko-Agent-Trajectories eval) | **9,936** | 10 | evaluation benchmark (hold-out, n-gram deduped) |
| **dpo_behavior** (v1.1) | **14,238** pairs | 2 | behaviour-targeted preference pairs: `over_clarify` 8,078 (chosen = reference immediate call, rejected = SFT student's own clarification) + `refusal` 6,160 (chosen = GPT-5.4-mini-authored refusal, rejected = student's pretend-and-ask). Single-turn prompt+chosen/rejected format — schema in the record's `pair_type`/`subtype`/`prompt`/`chosen`/`rejected` fields |

Out of 798,728 cumulative raw trajectories, 528,168 (66.1%) were train-eligible and fed the splitter. The eval split is deduplicated against train (5-gram Jaccard ≥ 0.8, MinHash LSH).

Repository contents beyond the four configs: `cross_judge/` (3-rater metadata plus `cross_judge_report.json`), `validation/` (21 files — 7 per-item bench composites, 10 FunctionChat-Bench summaries, 2 cross-judge summaries, consensus ids, agreement stats), `MANIFEST.json` (size + SHA-256 for the 569 corpus and cross-judge files: 519 train, 34 dpo, 10 eval, 2 dpo_behavior, 4 cross_judge; 1.34 GB), `filters/chinese_whitelist.txt` (176 entries, 317 distinct hanja), `bench/` (v1.0 baselines), `docs/09_PROMPTS_ko.md`, `seeds/scenario_templates/` (72 templates), `apis/catalog_ko.yaml` (41 API specifications, 39 of them observed in train), `pipeline/` (the stage implementations, Apache-2.0), and two notebooks: `demo.ipynb` (loading and formatting the data) and `run_pipeline.ipynb` (re-running the validators, gates, benchmark metrics and deduplication).

### 2. Trajectory schema

OpenAI-Chat-compatible `messages` (system → user → assistant ↔ tool ↔ … → final assistant answer) plus metadata (persona, scenario, judge scores, filter results; cross-judge scores on eval). The field-level data dictionary is Table 3 of the Data Descriptor; each config is also self-describing through its `features` block.

**ID format**: `kat-{N:08d}`, globally unique and sequential. Chosen: `kat-00000000`–`kat-00528167`; DPO rejected: `kat-90000000`–`kat-90033322` (offset separates chosen/rejected at a glance). See [Limitations §5.9](#59-id-policy--orchestrator-resume-bug).

### 3. Category distribution (train split, measured)

| ID | Category | count | share |
|---|---|---|---|
| FIN | Finance/securities/banking | 63,744 | 12.30% |
| GOV | Public data/administration | 58,823 | 11.35% |
| MEDIA | Content/media | 51,379 | 9.91% |
| CRYPTO | Cryptocurrency | 50,814 | 9.81% |
| TRAVEL | Travel/lodging/flights | 47,101 | 9.09% |
| MAP | Maps/transit | 45,888 | 8.85% |
| WORK | Recruiting/HR/productivity | 42,051 | 8.11% |
| SHOP | Shopping/books | 38,643 | 7.46% |
| FOOD | Delivery/dining | 37,296 | 7.20% |
| EDU | Education/certification | 33,990 | 6.56% |
| MISC | Dictionary/misc | 31,673 | 6.11% |
| MSG | Messaging | 16,830 | 3.25% |

KL(train_cat ‖ uniform) = **0.0431**. MSG is lowest (3.25%) — its pass rate through the eligibility filter (judge_avg ≥ 4.0) was below other categories. The eval split has a similar distribution (MSG 2.70%, FIN 13.53%). 41 API specs, centered on Korean public APIs.

### 4. Difficulty distribution (measured; differs from seed quotas)

| Lv | train | eval | DPO | typical turns |
|---|---|---|---|---|
| L1 | 18.97% | 19.61% | 21.23% | 3–6 |
| L2 | 11.83% | 12.22% | 12.26% | 5–8 |
| L3 | 20.04% | 20.91% | 22.14% | 6–10 |
| L4 | 29.66% | 29.11% | 28.71% | 8–14 |
| L5 | 13.96% | 12.89% | 12.86% | 10–18 |
| L6 | **5.54%** | 5.26% | **2.81%** | 20–40 (long-horizon) |

L6 falls well below the seed quota (10%) because long-horizon trajectories pass the eligibility filter at a lower rate; DPO L6 drops further (noise injection difficulty). **Oversampling L6 during training is recommended** — our own downstream experiments confirm L6 as the weakest transfer region (see below).

### 5. Personas (16, train split measured)

Each 4.23%–7.22% (uniform would be 6.25%). Lowest four: `p_student_csat` 4.23%, `p_health_check` 4.79%, `p_senior` 5.29%, `p_lawyer_para` 5.34%. In the eval split `p_senior` is **2.29%** (below the intended lower bound) due to persona-blind stratification — oversample senior/student_csat personas when evaluating persona robustness.

Personas: `p_developer`, `p_freelancer`, `p_health_check`, `p_homemaker`, `p_invest_amateur`, `p_journalist`, `p_lawyer_para`, `p_marketer`, `p_office_30s`, `p_office_50s`, `p_parent_kid`, `p_senior`, `p_smb_owner`, `p_student_csat`, `p_student_uni`, `p_traveler`.

### 6. Register distribution (train, measured)

`polite_formal` **50.31%** · `polite_informal` **25.12%** · `casual` **14.63%** · `formal_business` **9.94%**.

### 7. DPO noise types (33,323 pairs)

Acceptance rule `axis_min`: rejected must have min axis ≤ 2 while chosen has min axis ≥ 4.

| noise_type | count | % |
|---|---|---|
| infinite_repetition | 6,714 | 20.15% |
| wrong_argument | 5,443 | 16.33% |
| wrong_tool | 5,238 | 15.72% |
| hallucinated_response | 5,084 | 15.26% |
| spec_violation | 4,395 | 13.19% |
| language_drift | 3,929 | 11.79% |
| premature_termination | 2,520 | 7.56% |

score_gap: mean 1.51, median 1.5, p10 1.0, p90 2.0. Note: these 7 types target **robustness defects**; they do not cover *behavioral* preferences (when to call vs. when to ask vs. when to refuse) — see [Downstream Validation](#downstream-validation-v11-2026-07).

## Collection

### 1. Teacher

- **Model**: GLM-5.1-FP8 (zai-org/GLM-5.1, 754B MoE, FP8)
- **Inference**: vLLM 0.19.0, self-hosted (4-node B200 fleet; 5 nodes 2026-05-08–05-20)
- **License**: GLM-5.1 is **MIT** — outputs freely usable/redistributable; Z.ai API ToS does not apply (self-hosted)

### 2. Pipeline summary (8 production batches + splitter + DPO)

1. **API catalog** — 41 Korean public-API-style specs in OpenAI Chat `tools` format.
2. **Scenario templates** (72 = 12 categories × 6 levels) × 16 personas × 4 register quotas → seed prompt cross-product.
3. **Seed builder** — GLM slot-fills natural Korean user prompts (distinct rng per batch).
4. **Generator** — GLM produces the multi-turn trajectory; thinking=plan_only (first turn only); tool responses are also GLM-simulated.
5. **Self-judge** — GLM scores 4 axes (correctness, korean_quality, trajectory_consistency, tool_spec_compliance), integers 1–5.
6. **Rule filters** (8) — schema_valid, no_chinese_leak (published 176-entry whitelist), korean_ratio, tool_spec_compliant, no_pii, turn_count_in_range, token_budget_in_range, language_drift.
7. **Splitter** — train-eligible (all filters pass AND judge_avg ≥ 4.0) 528,168 → stratified eval extraction (judge_avg ≥ 4.5, deduped) → DPO chosen pool (50K stratified).
8. **DPO rejected** — regenerate from chosen seeds with 7 noise-injection prompts; accept via axis_min.

Stage implementations: `pipeline/` in this repository. Prompts: `docs/09_PROMPTS_ko.md`.

### What the rule validators actually catch (v1.1)

Every released record lists the validators it passed in `metadata.filters_passed`, the ones it failed in `filters_failed`, and the rule version in `filter_version`. Across the whole eval split (9,936), the whole chosen side of the DPO pairs (33,323) and a random 60 shards of train (60,000), every record lists all eight as passed.

Their discriminative power is measured directly on the noise-injected DPO rejected side. Of 33,323 rejected trajectories, 24,520 (73.6%) pass all eight, so **the remaining 26.4% are removed by the rules alone, before any judge is involved.**

| noise_type | caught by rules / total | rate |
|---|---|---|
| spec_violation | 3,138 / 4,395 | **71.4%** |
| language_drift | 1,755 / 3,929 | 44.7% |
| infinite_repetition | 2,787 / 6,714 | 41.5% |
| premature_termination | 269 / 2,520 | 10.7% |
| wrong_tool | 388 / 5,238 | 7.4% |
| wrong_argument | 277 / 5,443 | 5.1% |
| hallucinated_response | 189 / 5,084 | 3.7% |

**Deterministic rules catch defects that leave traces in form and structure, and miss defects that keep the form intact and corrupt only the meaning.** That is why a judge layer exists alongside them.

### 3. Human review status

**v1.0 shipped with no human review** (by design; cross-judge metadata quantified self-judge bias instead). **This is complete as of v1.1**: two annotators independently rated the same **360 stratified items** on the 4-axis judge rubric. The frame extends the released splits (eval 190 / train 75 / dpo-rejected 35) with **60 trajectories the judge gate rejected and that were never released**, so the gate's own discriminative power can be measured. Results: [Quality Assessment §4](#4-human-inter-annotator-agreement-v11).

The judge rubric verbatim, the seed prompt, and the 7 noise-injection prompts are released in this repository as `docs/09_PROMPTS_ko.md`; the 72 scenario templates as `seeds/scenario_templates/`.

## Quality Assessment

### 1. GLM self-judge (source of training labels)

Axis means over the 8 production batches: correctness **4.38** (lowest), korean_quality **4.85**, trajectory_consistency **4.71**, tool_spec_compliance **4.92**. `judge_avg` is defined as the arithmetic mean of these four axes.

The `judge_avg ≥ 4.0` pass rate is **84.9% of the 621,188 rule-passing trajectories**, equivalently **66.1% of the 798,728 raw trajectories** (same fact, different denominators).

> **v1.1 correction.** Card v1.0 reported "judge_avg mean 4.65 (variance 0.007)" here. That figure is
> not consistent with the axis means printed in the same section (their mean is 4.715) and does not
> reproduce from the released files, so it has been removed. The axis means and pass rates stand.

### 2. Commercial cross-judge (release-time validation)

Evaluation use only — training labels unchanged.

**3 raters**: GLM-5.1-FP8 + gpt-5.4-mini-2026-03-17 + claude-sonnet-4-5.

| Scope | n (3-rater common) | note |
|---|---|---|
| Eval split | 9,857 | GLM at 100% ceiling (5.0), κ undefined |
| Train subsample | 1,354 | stratified random; κ measurable |

Train-subsample results:

| Axis | GLM | GPT | Claude | Δ(GLM,GPT) | Δ(GLM,Cla) | κ(GLM,Cla) | κ(GLM,GPT) | α (3-rater, ordinal) |
|---|---|---|---|---|---|---|---|---|
| correctness | 4.64 | **2.93** | 4.24 | +1.71 | +0.40 | 0.318 | 0.086 | 0.114 |
| korean_quality | 4.86 | 4.51 | 4.93 | +0.35 | −0.07 | 0.300 | 0.132 | 0.038 |
| trajectory_consistency | 4.68 | **3.01** | 4.32 | +1.67 | +0.36 | 0.359 | 0.105 | 0.123 |
| tool_spec_compliance | 4.93 | **3.06** | 4.52 | +1.88 | +0.41 | 0.126 | 0.022 | **−0.098** |

κ is quadratic-weighted; α is the three-rater **ordinal** Krippendorff α (bootstrap 95% CIs in `validation/agreement_stats.json`). judge_avg means: GLM 4.78 / GPT 3.38 / Claude 4.50.

1. **GPT-5.4-mini is +1.7–1.9 stricter than the GLM judge** on correctness/consistency/tool_spec (κ 0.02–0.13 — near disagreement).
2. **Claude Sonnet 4.5 tracks GLM closely** (Δ 0.07–0.4, κ 0.13–0.36).
3. **tool_spec_compliance α = −0.098 (worse than chance)** — the largest disagreement sits on the axis most central to agentic training.
4. korean_quality has the smallest mean delta but the weakest item-level agreement (α 0.038): all three raters mostly give 5 (within-1 agreement 94.1%), so nothing is resolved inside that top band.
5. **The disagreement is reordering, not miscalibration.** On correctness, GPT rated 446 of the 1,000 items GLM scored 5.0 at 2 or below, while rating 28 items GLM scored ≤ 3 at 4 or above. The raters are not offset; they are ranking different things.
6. 3-rater consensus (all raters ≥ 4.0): train 34.0% / eval 44.6%.

**Practical guidance**: treat GLM judge_avg as a **coarse filter calibrated to GLM's own distribution**, not an absolute quality signal. Do not use it to adjudicate individual trajectories; the gate it implements does work at corpus scale (§5). If you subsample, keep the gate or an equivalent device. For recalibration or ensemble filtering, use the per-item 3-rater metadata under `cross_judge/`.

### 3. Ko-Agent-Trajectories eval leaderboard (v1.0, single-turn protocol)

| Baseline | model | first_tool | args | lcs | final_J | kor_J | **composite** |
|---|---|---|---|---|---|---|---|
| **Claude Sonnet 4.5** | claude-sonnet-4-5 | 0.814 | 0.827 | 0.678 | 1.22 | 2.44 | **0.5981** ⭐ |
| **GPT-5.4-mini** | gpt-5.4-mini-2026-03-17 | 0.764 | 0.770 | 0.623 | 1.22 | 2.80 | 0.5764 |
| *Reference (GLM teacher, NOT ranked)* | glm-5.1-fp8 | 0.874 | 0.877 | 0.730 | 1.23 | 4.85 | 0.7033 |

**Judge self-bias warning**: the GLM judge rates GLM's own korean_quality 4.85 vs. 2.44–2.80 for external models — prefer **relative comparison** over absolute values. A **multi-turn evaluation mode (`mode=full`, reference tool-response replay) is now implemented** in this repository (`pipeline/eval/`) and was used for all downstream experiments below; single-turn leaderboard numbers above are kept for v1.0 continuity.

### 4. Human inter-annotator agreement (v1.1)

Two annotators independently rated all **360** stratified items, so every item carries two ratings.

**Between annotators**: quadratic-weighted κ is **0.295–0.654** across the four axes. Raw agreement is far higher — exact agreement per axis is **76.9 / 95.0 / 95.8 / 96.4%**, and the overall pass/fail verdict matched on **96.7%** of items. The two annotators gave nearly the same scores while the chance-corrected statistic stayed low: the **same base-rate effect** seen with the LLM judges. Low agreement statistics on this task are a property of a scale piled up at 5, not something specific to LLM raters.

**Measurement condition.** The annotation interface rendered the full dialogue but did not display the tool definitions available to each trajectory (`messages[0].tools`); annotators scored `tool_spec_compliance` against a separate reference sheet. Read the results below as the discrimination achieved under that condition.

**The low κ is an artifact of marginals piled up at 5.** Pooling the 720 ratings, 95.8% of `korean_quality`, 96.9% of `trajectory_consistency` and 97.9% of `tool_spec_compliance` ratings are 5, and even `correctness` has 94.0% at 4 or 5 (5 at 78.9%, 4 at 15.1%). The two annotators are effectively equally severe: the largest per-axis mean difference is 0.11 (correctness 4.76 against 4.65). Disagreement concentrates on `correctness` (16 of 360 items differ by 2 points or more, against 5 to 10 on the other axes).

**By stratum** (pass rate per annotator; four-axis mean averaged over both):

| Stratum | n | pass rate (R1 / R2) | four-axis mean |
|---|---|---|---|
| eval (released, top-scoring) | 190 | 100.0% / 100.0% | 4.96 |
| train (released) | 75 | 98.7% / 100.0% | 4.88 |
| **gate-rejected (not released)** | 60 | **96.7% / 98.3%** | **4.91** |
| DPO rejected (noise-injected) | 35 | 85.7% / 57.1% | 4.41 |

Two things follow.

1. **Injected defects were detected.** Annotators separated the programmatically corrupted DPO-rejected items from released data (4.41 vs 4.88–4.96). Discriminative power is not absent.
2. **Gate-rejected trajectories were not separated from released data** — 4.91, slightly above the train split (4.88). Annotators caught defects visible in the prose (hallucination, degraded Korean) but tended to miss argument-level spec violations, which are hard to adjudicate from text alone. The LLM judge covers exactly that gap. The two are complementary, not substitutes.

The implication is direct: **judge_avg cannot adjudicate an individual trajectory** — yet the gate it implements does work at corpus scale.

### 5. Mass-selection effect of the judge gate (v1.1)

We trained an identically sized, identically configured SFT run on 518,232 trajectories sampled deterministically from the 621,188 rule-passing pool **without** the judge gate; about 15% of that sample has judge_avg < 4.0. **Both training sets are the same size**; only *which* 518,232 differs.

| Training data | bench composite |
|---|---|
| no training (base) | 0.790 |
| ungated 518,232 | 0.793 |
| gated 518,232 | **0.808** |

The ungated run is not meaningfully different from no training (Δ +0.0029, 95% CI −0.0027 to +0.0086). Between the two training sets, Δ +0.0154 (95% CI +0.0114 to +0.0193). The gated model leads on **all five components** (first_tool_acc +0.020, args +0.020, lcs +0.021, final_answer_judge +0.037, korean_quality_judge +0.041 — the two judge axes on their native 1-5 scale), and the three deterministic components alone move 0.843 → 0.863, so the effect does not rest on one judge-dependent component.

**Scope.** The no-gate ablation was scored on this in-distribution benchmark only and was not evaluated on the external benchmarks. The three deterministic components involve no judge, so they break the judge circularity, but they do not break the selection bias that eval items were themselves drawn at `judge_avg ≥ 4.5`.

**Item-level verdicts are unreliable; the aggregate over 518K items is useful.** That is the precise standing of this label.

## Downstream Validation (v1.1, 2026-07)

Training experiments on **Qwen3-8B** (Apache-2.0, hermes tool template; thinking disabled to match the data) — the first end-to-end validation of this dataset. Evaluation: Ko-Agent-Bench 9,936, multi-turn `mode=full`, judge = GPT-5.4-mini (the *strict* external judge), paired bootstrap n=9,934.

| Model | bench composite | Δ vs base | significance |
|---|---|---|---|
| Qwen3-8B base | 0.7896 | — | — |
| + full SFT (518K, 1 epoch) | 0.8079 | +1.83%p | p<0.0001 |
| + SFT + robustness DPO (33K) | 0.8070 | +1.74%p | n.s. vs SFT |
| **+ SFT + robustness DPO + on-policy behavior DPO** | **0.8281** | **+3.84%p** | **p<0.0001 (also vs SFT)** |

**Self-preference control for the behaviour configuration**: the benchmark judge (gpt-5.4-mini) authored part of that configuration's training targets, so we re-scored the SFT→behaviour increment end to end with an independent judge that authored none of them (claude-sonnet-4-5, all 9,936 items). The increment holds and is somewhat larger: Δ +0.0247 (95% CI +0.0212 to +0.0283; composite 0.8503 → 0.8750 under the Claude judge).

### Component decomposition (base → +SFT)

| Component | weight | base | +SFT | Δ |
|---|---|---|---|---|
| `first_tool_acc` | 0.20 | 0.926 | 0.888 | −0.038 |
| `first_tool_args_score` | 0.20 | 0.938 | 0.897 | −0.041 |
| `tool_seq_lcs` | 0.20 | 0.764 | 0.804 | +0.040 |
| `final_answer_judge` (1–5) | 0.25 | 2.908 | 3.441 | +0.533 |
| `korean_quality_judge` (1–5) | 0.15 | 3.955 | 3.932 | −0.023 |
| **composite** | | **0.790** | **0.808** | **+0.018** |

The accurate statement: SFT on this corpus improves multi-turn sequence execution (`tool_seq_lcs` 0.764→0.804) and final-answer completeness (2.91→3.44), and **degrades first-call tool and argument selection** (−0.038, −0.041). The latter is the same phenomenon as the behaviour transfer below.

Supporting results: pilot 50K SFT was *not* significant (+0.68%p, p≈0.52) — the effect emerges at full scale. General-knowledge regression is mild (KMMLU 45-subject sample: −1.2%p, no catastrophic forgetting).

### Behavior transfer: read before training

SFT on this dataset transfers not only tool-use *skills* but also the teacher's **clarify-first interaction policy** (the data's system prompt instructs asking before calling when information is missing). Consequences measured on an independent external benchmark (FunctionChat-Bench, thinking OFF):

- **Immediate-call situations degrade**: singlecall 0.894 → 0.462 after SFT. Failure analysis: 257/269 failures are *no-call clarification questions*, not wrong tool choices — a behavioral shift, not a capability loss.
- **Legitimate slot-filling improves**: dialog-slot 0.583 → 0.806 (the base model instead hallucinated missing arguments).
- **Refusal coverage gap**: scenarios where the correct behavior is "this tool set cannot do that" are ~1% of the corpus; SFT models tend to pretend-and-ask instead of refusing.
- **Thinking mode masks most of this**: with thinking ON, singlecall recovers to 0.830.

**Mitigation (validated)**: on-policy preference pairs — (a) *over-clarify* pairs: prompts whose reference turn is an immediate call, chosen = reference call, rejected = the SFT model's own clarification (harvest rate ~13%); (b) *refusal* pairs: tool-removal variants, rejected = the model's pretend-and-ask response. DPO on these pairs recovered first_tool_acc to near-base (0.888 → 0.921) in-domain, lifted external refusal accuracy **above base** (0.652 → 0.696), and partially recovered external singlecall (+5.8%p). Robustness-only DPO (the released 33K pairs) does **not** fix behavior — pair your training objective with the behavior you want.

### 6. Contamination check against the external benchmark (v1.1)

We searched character 12-gram shingles taken from all FunctionChat-Bench user and assistant contents across the full released corpus. **1.02%** of trajectories contain at least one shared shingle, but the shared shingles amount to only about **74 unique strings**, and manual inspection of both the frequent head and a random sample of the low-frequency tail found all of them to be generic formulaic phrases, dates or English fragments. We found no scenario-, entity- or task-level overlap, and by construction no FunctionChat-Bench content entered the pipeline's inputs. This check rules out surface string overlap only.

## Recommended Uses

- Korean LLM **SFT** (instruction + tool calling) — train split
- **DPO/IPO/SimPO** preference training — 33K pairs (robustness axes; complement with behavior pairs as above)
- Korean agent **benchmark** — Ko-Agent-Trajectories eval (single-turn or `mode=full` multi-turn)
- Korean multi-turn **reasoning** (plan-only thinking traces included)
- **Research**: synthetic-data agent training, single-teacher distillation limits, judge-bias analysis (3-rater metadata), behavior transfer in distillation

### Out of scope

- Medical/legal/financial factual accuracy (tool responses are simulated)
- Predicting real Korean user behavior distributions (synthetic)
- Multimodal (text only)
- Learning *semantics* of specific production APIs — tool responses are GLM-simulated; **format learning OK, semantic dependence risky**

## Limitations & Risks

### 5.1 Single teacher + self-judge
All trajectories come from one model (GLM-5.1); its stylistic bias transfers (measured downstream: markdown/emoji-flavored answers penalized by naturalness judges). Training labels share the same judge (self-circularity; quantified via cross-judge above).

### 5.2 Quality labels cannot adjudicate individual trajectories
Three LLM judges disagree at the item level (§2) and two human annotators did not reproduce the gate's verdicts either (§4), while the gate's mass-selection effect is real (§5). Treat the labels as a filter only, and keep the gate or an equivalent device when subsampling.

### 5.3 Scope of the human review
The 360-item dual annotation is complete (§4), but that sample is **0.07% of the corpus**. The annotators were one AI PhD student and one professor of information medicine; argument-level defects proved hard to adjudicate from text alone. Review PRs are welcome, particularly argument-level review and annotators with different backgrounds.

### 5.4 Synthetic tool responses
Plausible-but-inaccurate responses exist; do not train semantic reliance (see Out of scope).

### 5.5 Language/culture bias
GLM leans Chinese/English; hanja-leak filter passes 99.5% (with a published 176-entry whitelist covering 317 distinct hanja), not 100%. Persona coverage of Korean society is partial; `p_senior` is underrepresented in eval (2.29%).

### 5.6 Domain bias
41 API specs are defined and **39 are observed in the released train split**; they centre on Korean public APIs, and medical/legal coverage is thin. Each record carries the full definitions of the tools available to it in `messages[0].tools`, so the specs are recoverable from the data.

### 5.7 Difficulty bias
L6 (long-horizon) underrepresented (train 5.54%, DPO 2.81%); it is also the weakest downstream transfer region (validated). Oversample L6.

### 5.8 Behavior transfer (v1.1 finding)
The clarify-first policy transfers indiscriminately (see [Downstream Validation](#downstream-validation-v11-2026-07)): out-of-domain immediate-call performance drops sharply in non-thinking deployments, and refusal behavior is undertrained (~1% coverage). Mitigate with on-policy behavior DPO, data mixing, or thinking-enabled inference.

### 5.9 PII & safety
Structured PII removed by rule filters (99.5%+); unstructured synthetic names/addresses may coincidentally match real ones (very low impact); all payment/banking scenarios are synthetic.

### 5.10 ID policy & orchestrator resume bug
A resume bug produced trajectory-id collisions in raw data; the splitter reassigned globally-unique sequential IDs (`kat-{N:08d}`) at release. Original generation-time ids are recoverable via `metadata.seed_id`.

### 5.11 The benchmark is an in-distribution measurement
All 72 template combinations and all 39 APIs called in eval also appear in train, and 100% of eval items share a template combination with some train item. Only surface-level duplication was removed. Benchmark scores therefore mix task competence with conformity to the teacher's output conventions, and rankings should not be read as general capability rankings.

### 5.12 Single-turn v1.0 benchmark protocol
v1.0 leaderboard numbers are single-turn (weak `final_answer_judge` signal, ~1.22). Multi-turn `mode=full` is available in this repository (`pipeline/eval/runner.py`) and is the recommended protocol — single-turn evaluation *structurally penalizes* trained slot-filling behavior (validated in our experiments).

## Using the benchmark

```python
from datasets import load_dataset

ds = load_dataset("taejoon89/Ko-Agent-Trajectories-1.0", "eval", split="test")

for item in ds:
    # the tool array sits on the system message; lift it out before calling the API
    tools = item["messages"][0]["tools"]
    system = {"role": "system", "content": item["messages"][0]["content"]}
    user = {"role": "user", "content": item["messages"][1]["content"]}
    response = student.chat.completions.create(
        model="<student>",
        messages=[system, user],
        tools=tools, tool_choice="auto",
        temperature=0.0, max_tokens=2048,
    )
    # score with the 5 metrics — see pipeline/eval/{runner.py, metrics.py} in this repository
    # multi-turn: pipeline/eval/runner.py --mode full (reference tool-response replay)
```

Metrics: `first_tool_acc`, `first_tool_args_score`, `tool_seq_lcs`, `final_answer_judge`, `korean_quality_judge`; composite = `0.20·first_tool + 0.20·args + 0.20·lcs + 0.25·final_J/5 + 0.15·kor_J/5`.

3-rater eval metadata (in this repo): `cross_judge/cross_judge_eval_gpt54mini.jsonl`, `cross_judge/cross_judge_eval_claude45.jsonl` (match by `kat-XXXXX` id); train subsample under `cross_judge/cross_judge_train_*.jsonl`.

## License

- **Data (this repository): CC BY 4.0** (re-licensed from Apache-2.0 on 2026-07-27 — data files unchanged; see Changelog).
- **Pipeline code** (`pipeline/`, `apis/`, `seeds/` in this repository): **Apache-2.0** (see `pipeline/LICENSE`). The data files remain CC BY 4.0; the two scopes are separate.
- GLM-5.1 (MIT) teacher outputs → no additional restrictions on ours.
- The `dpo_behavior` config's *refusal* preferred responses (6,160 items) were **authored by GPT-5.4-mini** (`gpt-5.4-mini-2026-03-17`); they are labelled as such in each record's `gen_meta.chosen_model` field.
- OpenAI/Anthropic cross-judge raw response bodies are **not** released — only judge scores + short rationales (≤ 300 chars each). Baseline response trajectories are likewise not released — scores only.

### Citation

```bibtex
@dataset{ko_agent_trajectories_1_0_2026,
  title  = {Ko-Agent-Trajectories-1.0: A Korean Multi-turn Agent <-> Tool Trajectory Corpus Distilled from GLM-5.1},
  author = {Imjin Ahn and Young-Hak Kim and Sanghyun Park and Tae Joon Jun},
  year   = {2026},
  month  = {5},
  publisher = {Hugging Face},
  url    = {https://huggingface.co/datasets/taejoon89/Ko-Agent-Trajectories-1.0},
  license= {CC-BY-4.0}
}
```

## Changelog

- **v1.0** (2026-05-29): initial release — train 518,232 + DPO 33,323 pairs + Bench 9,936 + 3-rater cross-judge metadata.
- **card v1.0.1** (2026-07-27): English datasheet (Korean original preserved as `README.ko.md`); added **Downstream Validation** (Qwen3-8B SFT/DPO results), behavior-transfer findings & mitigation, KMMLU regression check; multi-turn `mode=full` protocol implemented; human review (blind dual annotation) in progress. Data files unchanged.
- **v1.1** (2026-07-27): (a) **license change: data re-licensed Apache-2.0 → CC BY 4.0** (no file changes; aligns with data-repository norms); (b) **new config `dpo_behavior`** — 14,238 on-policy behaviour-targeted preference pairs (over_clarify 8,078 + refusal 6,160; refusal chosen responses authored by GPT-5.4-mini, labelled per record). These are the pairs used in the behaviour-corrected validation configuration; releasing them makes that configuration fully reproducible.
- **card v1.1** (2026-08-26): **human review complete** — 360-item dual annotation, inter-annotator agreement and per-stratum pass rates attached (Quality Assessment §4); **judge-gate ablation** added (§5); component decomposition and self-preference control added to Downstream Validation; per-axis cross-judge table restored with α labelled as the **ordinal** Krippendorff variant; the `judge_avg mean 4.65 (variance 0.007)` figure removed (arithmetically inconsistent with the axis means in the same section and not reproducible from the released files); API count split into 41 defined / 39 observed; in-distribution caveat added; `docs/09_PROMPTS_ko.md` and `seeds/scenario_templates/` released; Korean card brought back into sync.
- **card v1.1.1** (2026-09-22): **pipeline code released in this repository** — `pipeline/` (18 stage modules, Apache-2.0, `pipeline/LICENSE`), `apis/catalog_ko.yaml` (41 API specifications), `seeds/scenario_templates/` (72 templates) and `docs/09_PROMPTS_ko.md` (complete prompt set), plus `demo.ipynb` and `run_pipeline.ipynb`. Every Korean-language asset also ships with an English edition: `catalog_en.yaml`, `all_levels_en.yaml` per category, and `docs/09_PROMPTS_ko.md` with `docs/09_PROMPTS_en.md`; the Korean files are the ones the pipeline used. References to a separate companion repository removed. Corrected against the Data Descriptor: whitelist coverage 324 -> 317 distinct hanja; train-eligible share 66.2% -> 66.1%; `MANIFEST.json` scope stated as the 569 corpus and cross-judge files. Data files unchanged.
- **v1.1 (remaining plan)**: OS baselines on the leaderboard; multi-turn leaderboard refresh.
- **v2.0** (aspirational): long-context tool use, multimodality, multi-teacher distillation.

## Contact & Contributions

Issues/PRs on this HF repo. Human-review PRs, additional baselines (`pipeline/eval/runner.py`), and cross-judge re-runs with other frontier models are all welcome.
