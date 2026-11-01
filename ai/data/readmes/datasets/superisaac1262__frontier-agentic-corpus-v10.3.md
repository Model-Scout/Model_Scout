---
language:
- en
- zh
- ko
license: other
license_name: multiple-upstream-licenses-and-source-specific-terms
tags:
- distillation
- frontier-models
- reasoning
- agentic
- chain-of-thought
- tool-use
- computer-use
- math
- science
- data-analysis
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- text-retrieval
pretty_name: Frontier Agentic Corpus v10.3
---

# Frontier Agentic Corpus v10.3

A multi-teacher knowledge-distillation corpus of genuine multi-step agentic
trajectories, coding, mathematical, scientific, and data-analysis reasoning,
built exclusively from **currently frontier-eligible teacher models** under a
strict, live-verified, two-leaderboard gate — released with row-level
provenance and a separate public/redistribution split.

| Metric | Value |
| :--- | :--- |
| **Total tokens** | **1,095,987,979** (chars/4 estimate) |
| **Total examples** | **430,532** |
| **Parquet shards** | **87** (corpus) · public release 44 (~47 MB each) · restricted 20 |
| **Teachers** | **15** (all live-verified) |
| **Max teacher share** | **31.15%** |
| **Serialized** | 2.32 GB (corpus) · 2.06 GB (public) · 0.26 GB (restricted) |
| **Realistic credentials** | **0** |
| **Duplicates** | **0** |
| **Parse rate** | **100%** (0 masking violations) |

## 1. Overview

Frontier Agentic Corpus is teacher-distilled/generated data for training language
models that behave agentically: when a task benefits from tools, iteration,
planning, verification, or external actions, the model should be capable of
multi-step work — while remaining useful for tasks that need only a direct
answer. The corpus therefore contains BOTH genuine agentic trajectories AND
high-quality direct-answer reasoning.

## 2. Motivation

Public distillation corpora aggregate everything available, so data from
superseded generations dominates by volume. This project treats teacher
eligibility as a first-class, time-dependent selection signal verified live at
build time. It also treats the capability mix as a measured outcome — not a
target — and documents where the strict gate leaves domains underrepresented.

## 3. Dataset composition (measured from the final shards)

| Dimension | Value |
| :--- | :--- |
| **Capability** | agentic-coding 48.36% · coding 25.80% · mathematical 16.33% · science-technical 7.81% · general-reasoning 1.31% · tool-assisted-coding 0.80% · planning-analysis 0.58% · agentic-general 0.06% |
| **Domain** | coding 69.20% · math 16.31% · science 7.80% · **data 5.00%** · general 1.03% · planning 0.58% · research 0.04% · knowledge 0.04% |
| **Agentic level** | none 49.0% · **deeply_iterative 45.6%** · multi_step 6.2% · assisted 3.2% |
| **Trajectory depth (tool turns)** | tool_free 49.0% · 8+ 45.7% · 4-7 2.5% · 1-2 1.1% |
| **Verification** | explicit 49.1% · implicit 31.1% · none 19.8% |
| **Error recovery** | present 81.3% · none 18.7% |

## 4. Teacher eligibility policy

**Exact frontier gate** (project-specific, time-dependent, live-verified):

```text
OPEN models:   total_parameters > 700B  AND  (AA rank <= 20 OR LMArena rank <= 10)
CLOSED models: AA rank <= 20  OR  LMArena rank <= 10
```

- The leaderboard condition is **OR**; the >700B condition applies ONLY to open
  models (total parameters — active MoE parameters do NOT satisfy it).
- Both leaderboards are fetched live at build time; a model qualifying on one
  leaderboard qualifies even if it fails the other.
- Rankings are NEVER inherited between model versions (opus-5 ≠ opus-5.5;
  grok-4.6 ≠ grok-4.7; GPT-5.6-Sol ≠ GPT-6-Sol).
- This criterion is a project-specific frontier threshold — it does NOT imply a
  teacher is universally "best", and it is time-dependent (ranks move).
- Tests guard the gate (14 tests: open/closed, MoE total-vs-active,
  version-identity, OR-condition directions).

## 5. Teacher list (15, all live-verified)

| Teacher | Type | Share | Basis |
|---|---|---:|---|
| Claude-Fable-5 | closed | 31.15% | LMArena #3 |
| Claude-Fable-5.1 | closed | 24.94% | AA #2 / LMArena #5 |
| GLM-5.3 | open, 753B total | 20.35% | AA #9 |
| Qwen3.8-Max | closed | 6.26% | AA #8 |
| Claude-Opus-4.6 | closed | 6.09% | LMArena #2 |
| Claude-Opus-4.7 | closed | 4.86% | LMArena #4 |
| Kimi-K3 | open, 2.8T | 3.32% | AA #12 |
| Qwen3.8-2.4T-A95B | open, 2.4T | 2.01% | AA #16 |
| Claude-Opus-5.5 | closed | 1.45% | AA #1 |
| Claude-Sonnet-5 | closed | 0.79% | AA #19 |
| Muse-Spark-1.2 | closed | 0.20% | LMArena #7 |
| Gemini-3.8-Flash | closed | 0.11% | AA #15 / LMArena #10 |
| Claude-Opus-5 | closed | 0.01% | AA top-20 |
| Grok-4.6 | closed | 0.01% | AA #10 |
| GPT-6-Astra | closed | 0.00% | AA #3 |


## Source credits (all upstream sources in the public release)

The corpus aggregates 43 upstream sources. **Every source is credited here** —
this table is the full attribution record; `SOURCE_LICENSES.json` is the machine-readable
version with SPDX identifiers, license URLs, and per-source obligations.

| # | Upstream source | License | Public tokens |
|---:|---|---|---:|
| 1 | MoreThought/Fable-5.1-Max-Reasoning-Filtered-10000x | Apache-2.0 | 207,069,524 |
| 2 | Crownelius/Complete-FABLE.5-traces-2M | MIT | 201,076,227 |
| 3 | open-athena/GLM-5.3-RLVR1-Training-Rollouts-2026.09.25 | Apache-2.0 | 176,077,881 |
| 4 | Nexlab/fable5-agentic-coding-sft | MIT | 92,372,626 |
| 5 | saidutta69/fable-5.1-premium | Apache-2.0 | 60,851,098 |
| 6 | open-athena/recursive-task-synthesis-glm-5.3-rollouts | CC-BY-4.0 | 48,249,257 |
| 7 | saidutta69/fable-5-premium-v2 | MIT | 29,600,121 |
| 8 | angrygiraffe/claude-opus-4.6-4.7-reasoning-8.7k | Apache-2.0 | 28,427,997 |
| 9 | YL95/hrm-text-opus46-math-coding | Apache-2.0 | 20,989,113 |
| 10 | Gryphe/Opus-4.6-Reasoning-24k | Apache-2.0 | 19,073,959 |
| 11 | shanjiaz/Qwen3.8-2.4T-A95B-responses-original10k | Apache-2.0 | 17,656,186 |
| 12 | nisten/opus5-5-doctor-patient-conversations-all-human-diseases | Apache-2.0 | 12,706,395 |
| 13 | greghavens/kimi-k3-coding-and-debugging-traces | CC-BY-4.0 | 11,042,135 |
| 14 | SJCaldwell/proofjudge-eval-traces | MIT | 6,902,117 |
| 15 | saidutta69/fable-5-premium | MIT | 6,523,571 |
| 16 | Swarm-AI-Research/fable5-traces-sft | AGPL-3.0 | 6,507,908 |
| 17 | jiajiale9/kimi-k3-coding-and-debugging-traces | CC-BY-4.0 | 4,154,347 |
| 18 | TeichAI/lordx64-claude-opus-4.7-max-cleaned | Apache-2.0 | 4,077,069 |
| 19 | Jongsim/claude-opus-4.6-reasoning-12k-ko-filtered-v2 | Apache-2.0 | 3,923,083 |
| 20 | Infatoshi/kimi-k3-open-swe-distillation | CC-BY-4.0 | 3,238,318 |
| 21 | Jackrong/Claude-opus-4.7-TraceInversion-5000x | Apache-2.0 | 2,952,494 |
| 22 | 11-47/Fable-5.1-Max-Reasoning-5K | Apache-2.0 | 2,617,993 |
| 23 | p-research/kimi-k3-cyber-reasoning-distill | WTFPL | 2,575,144 |
| 24 | MoreThought/Fable-5.1-Max-Reasoning-Filtered-1000x | Apache-2.0 | 2,260,849 |
| 25 | siddharth0713/fable-5-coding-and-debugging-traces | CC-BY-4.0 | 2,242,879 |
| 26 | cfahlgren1/Fable-5-traces | AGPL-3.0 | 1,912,710 |
| 27 | muse12-24000-seed campaign (Meta contributor) | MIT | 1,758,748 |
| 28 | internlm/WildClawBench-Trajectories | MIT | 1,605,720 |
| 29 | Jongsim/claude-opus-4.6-reasoning-12k-en-filtered-v2 | Apache-2.0 | 1,506,465 |
| 30 | TeichAI/Fable-5-Cursor-Traces | Apache-2.0 | 1,248,440 |
| 31 | bevangelista/AIME_2000_2026_Kimi_K3 | MIT | 1,159,512 |
| 32 | moehamid/kimi-k3-coding-and-debugging-traces | CC-BY-4.0 | 936,360 |
| 33 | Nettoov/Claude-Opus-4.6-Reasoning-887x | Apache-2.0 | 403,308 |
| 34 | bevangelista/AIME_1983_2026_Kimi_K3 | MIT | 186,862 |
| 35 | AgentNativeResearchLab/tbs-claude-opus5-high-trajectories | Apache-2.0 | 110,805 |
| 36 | INONONO/tarkov-customs-trajectory | MIT | 89,959 |
| 37 | kelexine/fable-5-sft-traces | AGPL-3.0 | 62,584 |
| 38 | AgentNativeResearchLab/fm-open-problems-kimi-k3-trajectories | CC-BY-4.0 | 61,255 |
| 39 | AgentNativeResearchLab/tbs-grok4.6-trajectories | Apache-2.0 | 54,661 |
| 40 | INONONO/fable-5.1-mario-trajectory | MIT | 53,445 |
| 41 | paulbatum/pareto-rail-rollouts | MIT | 26,678 |
| 42 | Crownelius/Opus-4.6-Reasoning-3300x | Apache-2.0 | 6,159 |
| 43 | Nettoov/claude-opus-4.6-10000x | MIT | 333 |
| | **Total** | | **984,352,295** |

For the full 70+-source base-corpus provenance (including the V9-era upstream
repositories and their attribution evidence), see `SOURCE_LICENSES.json` and the
audit artifacts in the companion repository.
## 6. Source provenance

~70 upstream repositories (V9 base) + 5 acquired sources (V10/V10.1/V10.2):
glm53_rlvr1 (open-athena — 176.1M tokens of GLM-5.3 agentic rollouts, ROW_LEVEL:
the source's own manifest names `cyankiwi/GLM-5.3-AWQ-INT4`), opus55_doctor
(nisten — 2,194 Claude Opus 5.5 clinical encounters, DOCUMENTED_GENERATION),
tbs_opus5 / tbs_grok46 (AgentNativeResearchLab — verifier-successful
scientific-agent ATIF trajectories, ROW_LEVEL), fm_open_kimi (FrontierMath OPEN
PROBLEMS — unsolved research mathematics, ROW_LEVEL). Per-row provenance fields:
candidate_id, source_id, teacher, license, license_conf, eligibility_status;
the row-level model attribution evidence is preserved in the audit artifacts.

## 7. Licensing and redistribution

**Repository umbrella license: OTHER / MULTIPLE UPSTREAM LICENSES** — no single
standard license accurately describes the complete public release (the formal
rights-intersection decision is in `LICENSE_INTERSECTION_REPORT.md`:

- a permissive umbrella (MIT/Apache) would over-grant — it omits the CC-BY-4.0
  attribution requirement and the AGPL-3.0 share-alike/source-disclosure
  obligations;
- a restrictive umbrella (CC-BY-SA/AGPL) would over-impose — it applies
  obligations the MIT/Apache/WTFPL rows' upstreams do not impose, and CC-BY-SA
  does not satisfy AGPL's own §13 requirement;
- therefore the umbrella is the explicit multi-license notice, and the
  authoritative source→license mapping is `SOURCE_LICENSES.{md,json}`).

**This dataset is a derived/distilled dataset: it does not represent a
relicensing of third-party source material.** Each upstream source retains its
applicable licensing obligations; the public release contains only rows cleared
for redistribution; row/source metadata (`source_id`, `license`, `license_conf`)
identifies the applicable upstream license per row. Downstream users must
independently verify the applicable upstream terms before redistribution or
commercial use. Restricted training-only material is NOT included in this
repository. The release is explicitly split:

- **Public release** (`public/`): 309,981 rows / 984,352,295 tokens — only rows
  with a defensible redistribution basis (Apache-2.0 ~40%, MIT ~38%, CC-BY-4.0
  ~8% [attribution REQUIRED], AGPL-3.0 ~2% [**derived works must carry AGPL**],
  WTFPL ~0.3%).
- **Restricted training release** (`restricted/`): 120,551 rows / 111,635,684
  tokens — training-only rows (unknown-license, declared noncommercial-
  research-only, declared-unspecified, provider-terms, request-access). **NOT
  published.**

See `LICENSE_MATRIX.md` for the full matrix. Provider terms for teacher model
outputs are a separate layer that cannot be verified from repository data.

## 8. Data processing pipeline

1. Row-level teacher attribution (model/teacher_model/generation_model/
   agent.model_name fields outrank repo titles; mixed repositories split per row)
2. Format normalization (content blocks, reasoning channels, tool calls/results,
   raw chat-template boundaries where they parse unambiguously; quarantined otherwise)
3. Security filtering (full-text secret-pattern detection; realistic credentials
   remove the row — 291 rows removed during acquisition; documented placeholders
   and security-training fixtures retained)
4. Contamination classification per source (benchmark-derived work documented;
   active-benchmark eval runs excluded; failed trials recorded, not ingested)
5. Exact deduplication (SQLite-backed SHA-256 on normalized text)
6. Taxonomy characterization (orthogonal dimensions per row)
7. Selection (taxonomy-aware marginal utility, multi-pass, per-decision reasons;
   every candidate has exactly one terminal state)

## 9. Selector methodology

Multi-pass constrained selection: validate (hard constraints) → quality floor →
statistics → seed (per teacher × capability) → greedy marginal-utility fill
(quality + capability/domain coverage + teacher diversity + source novelty +
agentic value + length/depth diversity + verification/error-recovery value −
redundancy penalty) → capability/domain coverage correction → redundancy cleanup
→ backfill. Hard constraints may exclude (reason recorded); soft objectives
influence ranking without deleting. Deferred candidates remain traceable.

## 10. Known capability gaps (NOT fabricated balance)

| Gap | Observed | Reason |
|---|---:|---|
| Agentic research (deep research, multi-hop, literature analysis) | 0.04% | **source-universe-caused**: every large public research-trajectory corpus is generated by sub-700B open models that fail the strict gate; three exhaustive search passes confirmed NOT FOUND |
| Computer-use | 0% | **source-universe-caused**: verified sources fail the gate (gemini-3-flash LMArena #40), lack trajectory content (OSWorld metadata-only), or are empty |
| Agentic planning | 0.58% | **source-universe-caused**: no eligible-teacher planning corpus found |
| Agentic general | 0.06% | no meaningful corpus found |

The strict frontier-teacher constraint is responsible for these gaps. This
dataset does NOT claim to be a balanced sample of all possible agent behavior.

## 11. Limitations

- Token counts use a chars/4 estimate (consistent across all builds; a real
  tokenizer gives different absolute counts).
- ~10.2% of the corpus (111.6M tokens) is training-only (restricted) and NOT in
  the public release.
- Provider terms for teacher model outputs cannot be verified from repository
  data.
- Teacher eligibility reflects the 2026-09-25/26 leaderboard snapshot.
- 95 rows (0.009%) retain raw chat-template markers that are genuinely part of
  taught content (template/code definitions inside the task text).
- The corpus is coding-heavy (69.2% of tokens) because the available eligible
  signal is coding-dominated.

## 12. Intended use

- Pre-training or fine-tuning language models on long-form reasoning and
  genuine multi-step agentic behavior.
- Training models that plan, use tools, verify their work, and recover from
  errors — across coding, math, science, and data-analysis domains.
- Research on distillation methodology, data composition, and trace quality.

## 13. Out-of-scope use

- Training models to imitate a specific commercial provider's persona.
- Uses violating any upstream source license — filter with the `license` column;
  the public release already excludes restricted rows.
- Uses of AGPL-3.0 slices in ways that violate AGPL's copyleft terms.

## 14. Training recommendations

- The corpus is model-size agnostic: the schema/loader support models
  substantially larger than the 12B-class; assistant-only loss masking is
  verified (0 violations; system/user/tool turns masked).
- **Long-context requirement**: only 33.5% of tokens fit a 4K context; 43.4% at
  8K; 54.5% at 16K; **83.2% at 32K**. The high-value deeply-iterative
  trajectories are long — use ≥16K context to retain over half the corpus; 32K
  to retain 83%. Do not truncate high-value trajectories.
- Packing: the loader supports example-level batching; sequence packing is a
  loader-side transform (variable-length agentic trajectories benefit from
  packing — measure utilization on your stack).
- The loader (`frontier_v10/training_loader.py`) is streaming, deterministic,
  low-RAM, shard-aware, and distributed-safe (rank-safe shard subsets).

## 15. Dataset statistics

See the composition table (§3), `FINAL_SCHEMA.md`, and the dashboard in
`RELEASE_READINESS_REPORT.md`.

## 16. Reproducibility

```bash
git clone <this-repository> && cd frontier-agentic-corpus
pip install -e ".[dev]"
export FRONTIER_DOWNLOADS=/path/to/sources
python -m frontier_agentic_corpus all          # pipeline stages
python frontier_v10/build_v10.py acquire     # acquisitions
python frontier_v10/build_corpus.py all      # final corpus + release split
python scripts/validate_release.py           # final audit (exit nonzero on failure)
```

See `REPRODUCIBILITY.md` for the full package (seeds, versions, hashes).

## 17. Citation

```bibtex
@dataset{frontier_agentic_corpus_v10_3,
  title  = {Frontier Agentic Corpus v10.3: A Multi-Teacher Frontier Agentic Corpus},
  year   = {2026},
  note   = {1.096B tokens, 430,532 examples, 15 live-verified frontier teachers}
}
```

## 18. Version history

- **v10.3** — final training + public-release readiness: the 1.096B corpus
  materialized (87 shards), public/restricted split, final audits (0 credentials,
  100% parse, 0 masking violations), license matrix, schema frozen.
- **v10.2** — exhaustive frontier-teacher hunt: the GLM-5.3 RLVR1 rollouts
  (176.1M tokens) + FrontierMath open-problems; dr-tulu/DataMind teacher
  investigations (UNKNOWN, definitively).
- **v10.1** — the OR-condition gate correction (Claude Opus 5); the Opus 5.5
  clinical data + Opus 5 scientific-agent trial.
- **v10.0** — the acquisition infrastructure + the Grok-4.6 source.
- **v9** — the taxonomy-aware selector + the honest recomposition (879.5M).
- **v8.6** — the remediation pass (0 credentials, 0 metadata, 100% parse).
- **v8.5** — the audited 1.019B corpus.