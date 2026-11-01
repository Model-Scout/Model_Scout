---
language:
- ko
- en
license: cc-by-4.0
task_categories:
- text-generation
- text-ranking
- text-classification
tags:
- multi-agent
- agent-orchestration
- code-review
- llm-collaboration
- agent-handoff
- claude
- codex
- neo-genesis
- agent-evaluation
- bilingual
- wikidata-Q139569680
- yesol-heo-founder
- ko
- en
- agent-collaboration
- anonymized-transcripts
size_categories:
- n<1K
pretty_name: Cross-Agent Code Review Queue (Codex <-> Claude, Neo Genesis 2026)
configs:
- config_name: queue_metadata
  data_files:
  - split: train
    path: data/queue_metadata.parquet
- config_name: checkpoints
  data_files:
  - split: train
    path: data/checkpoints.parquet
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
---

## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018477.svg)](https://doi.org/10.5281/zenodo.20018477)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018477`** ([Zenodo record](https://zenodo.org/record/20018477)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018477,
  author       = {Heo, Yesol and Neo Genesis Lab},
  title        = {Cross-Agent Code Review Queue (Codex <-> Claude, Neo Genesis 2026)},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018477},
  url          = {https://doi.org/10.5281/zenodo.20018477}
}
```

# Cross-Agent Code Review Queue (Codex <-> Claude, Neo Genesis 2026)

> The first publicly released dataset of **bounded multi-agent code review checkpoints** with explicit `owner_goal`, `owner_intent`, `review_lens`, and `result` fields. 37 full bilingual (ko + en) review transcripts plus 37 queue-metadata entries from a real production AI-native company operating 11 business units.

Released by **[Neo Genesis](https://neogenesis.app)** to support agent-orchestration research.

## Why this dataset exists

Public benchmarks for code-related LLM work (SWE-bench, AgentBench, HumanEval, MBPP) target a **single agent** producing or evaluating a single artifact. They miss the most operationally important question of agent orchestration:

> *When two specialist agents disagree on a patch, what does the bounded handoff actually look like?*

This dataset captures **real Codex <-> Claude review handoffs** from a production environment between **2026-04-08 and 2026-04-14**, covering subsystems ranging from a Telegram personal assistant, a small-account quantitative trading runtime governor, a job-search pipeline, to autonomous-trading orchestrator design.

Every checkpoint follows a shared protocol: the requester reconstructs the **owner's goal, intent, constraints, and success criteria** before asking; the reviewer responds against a declared **review lens** (`risk` / `architecture` / `usability` / `security` / `rollout` / `verification`); and the outcome is recorded as `new_signal` / `no_new_signal` / `failed`.

## Dataset summary

- **37 full transcripts** in `data/checkpoints.jsonl` — each with `prompt`, `response`, and the full request schema (owner-goal reconstruction, lens, constraints, success criteria, result).
- **37 queue-metadata entries** in `data/queue_metadata.jsonl` — the canonical request log including items where the transcript was not preserved (cross-reference via `id`).
- **Fully anonymized**: paths, hostnames, owner identifiers, and credential patterns redacted (see *Anonymization disclosure* below).

## Distributions

### Review lenses

| Lens | Count |
|---|---|
| `risk` | 34 |
| `goal-fit` | 15 |
| `operations` | 13 |
| `verification` | 12 |
| `maintenance` | 7 |
| `usability` | 5 |
| `bugs` | 5 |
| `regressions` | 5 |
| `controls` | 5 |
| `security` | 2 |
| `architecture` | 2 |
| `regression` | 1 |
| `scope-control` | 1 |
| `rollout-safety` | 1 |

### Requester agent

| Agent | Count |
|---|---|
| `codex` | 37 |

### Target reviewer

| Target | Count |
|---|---|
| `neo-reviewer` | 29 |
| `neo-architect` | 8 |

### Outcome

| Result | Count |
|---|---|
| `new_signal` | 31 |
| `failed` | 4 |
| `no_new_signal` | 2 |

## Schema

### `data/checkpoints.jsonl` (one record per line)

```json
{
  "id": "ccr-20260408-122805",
  "created_at": "2026-04-08T12:29:17+09:00",
  "requester": "codex",
  "target": "neo-architect",
  "mode": "architecture",
  "model": "sonnet",
  "scope": "telegram scheduling + gmail/calendar orchestration",
  "owner_goal": "trustworthy personal assistant on Telegram",
  "owner_intent": "one message should accurately execute scheduling, gmail-grounded additions, ...",
  "constraints": "Korean, final report must match actual tool outcomes, ...",
  "success_criteria": "compound assistant commands report created/updated/failed items separately ...",
  "review_lens": "goal-fit,risk,usability,maintenance",
  "expected": "design",
  "ask": "Provide the highest-leverage implementation principles and risks for this patch scope.",
  "result": "new_signal",
  "title": "Telegram personal-assistant reliability remediation",
  "prompt": "Context:\n- Current failure case: ...",
  "response": "## Owner goal and intent restatement\n\n...full Korean review with markdown tables..."
}
```

### `data/queue_metadata.jsonl` (one record per line)

```json
{
  "id": "ccr-20260408-122805",
  "requester": "codex",
  "target": "neo-architect",
  "model": "sonnet",
  "title": "Telegram personal-assistant reliability remediation",
  "scope": "telegram scheduling + gmail/calendar orchestration",
  "owner_goal": "...",
  "review_lens": "goal-fit,risk,usability,maintenance",
  "expected": "design",
  "result": "new_signal",
  "has_transcript": true
}
```

## Quick start

```python
from datasets import load_dataset

# Full transcripts (request + response)
ds = load_dataset("neogenesislab/cross-agent-review-queue-2026", "transcripts", split="train")
print(ds[0]["title"])
print(ds[0]["prompt"][:500])
print(ds[0]["response"][:500])

# Lightweight queue metadata only
ds_meta = load_dataset("neogenesislab/cross-agent-review-queue-2026", "queue_metadata", split="train")
```

## Comparison with prior work

| Dataset | Multi-agent? | Goal-intent reconstruction | Bounded lens? | Production source |
|---|---|---|---|---|
| **SWE-bench** | single-agent | partial | task-only | GitHub issues |
| **AgentBench** | single-agent | task spec | varied | synthetic + real |
| **MetaGPT-Pub / AutoGen-Bench** | multi-agent (synthetic) | task only | implicit | scripted scenarios |
| **HumanEvalPack / CodeXGLUE** | single-agent | none | none | curated code |
| **Cross-Agent Review Queue (this)** | **multi-agent (Codex <-> Claude)** | **explicit, structured** | **declared lens (6 types)** | **live production logs** |

This dataset is **not** a code-generation benchmark and is **not** a single-agent evaluation set. It is a **collaboration log** — the closest public analog is a code-review transcript dataset, but with a multi-agent boundary protocol layered on top.

## Suggested research applications

1. **Agent handoff training** — fine-tune a requester-side model to produce well-formed `owner_goal` / `review_lens` / `success_criteria` blocks that lead to `new_signal` results.
2. **Reviewer politeness vs. bluntness analysis** — the `result` field marks `no_new_signal` (legitimate "nothing to add") separately from `new_signal` (substantive feedback). Useful for studying reviewer over-engagement.
3. **Cold-review prompting** — many transcripts illustrate the *Goal-Intent Review Protocol* where Claude is required to restate the owner's goal before critiquing. Compare cold reviews with warm/agreement-first reviews.
4. **Lens-specific instruction following** — measure how a model adheres to a declared lens (e.g., `risk` only) when it would naturally also discuss `usability`.
5. **Boundary management** — Codex + Claude operate under a *bounded specialist collaboration* contract (no recursive delegation, single primary writer per branch). Analyze how this constraint shapes the dialogue.

## Anonymization disclosure

The source data was Neo Genesis' live agent-runtime SSOT. The following transformations were applied before publication:

| Class | Examples in raw source | Public form |
|---|---|---|
| Absolute paths | local development paths starting with a Windows drive letter | `<repo>/...` |
| Owner identifiers | owner full name, personal email, phone | `<owner>` / removed |
| Hostnames (devices) | named work-PC / GPU-worker / server / mac-build hostnames | `<work-pc>`, `<gpu-worker>`, `<server>`, `<mac-build>` |
| Tailscale / private IPs | `100.x.y.z`, `192.168.x.y` | `<tailscale-ip>`, `<private-ip>` |
| Credentials | `sk-*`, `ghp_*`, `hf_*`, JWT, Telegram bot tokens | `<redacted-*>` |
| Korean RRN | 6+7 digit format | `<redacted-rrn>` |

Public Neo Genesis identifiers (Wikidata Q139569680, the public business-unit names that already appear on `neogenesis.app`, and the public agent-orchestration concepts like the *Sora* assistant) are intentionally retained because they are already attested in public sources.

Verification: every emitted string was passed through a post-anonymization assertion that re-runs the redaction regexes; any remaining match aborts the publish job.

## Provenance

- **Source SSOT**: Neo Genesis private `.agent/shared-brain/cross-agent-review.md` and `claude-checkpoints/`
- **Time window**: 2026-04-08 to 2026-04-14 (the most active multi-agent collaboration window during Phase -1 quant runtime hardening + Sora assistant remediation)
- **Curator**: <owner> (sole founder/operator of Neo Genesis)
- **Wikidata**: [Q139569680 (Neo Genesis)](https://www.wikidata.org/wiki/Q139569680)
- **Related releases by the same operator**:
  - [`korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`ethicaai-mixed-safe-evidence`](https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence)
  - [`whylab-gemini-2-5-docker-validation`](https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation)
  - [`sbu-pseo-effects-2026-04`](https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04)

## Citation

```bibtex
@misc{neogenesis_cross_agent_review_queue_2026,
  title  = {Cross-Agent Code Review Queue: Bounded Codex-Claude review checkpoints from a production AI-native company},
  author = {Neo Genesis},
  year   = {2026},
  url    = {https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026},
  note   = {First public dataset of multi-agent code review checkpoints with explicit goal-intent reconstruction and declared review lens}
}
```

## License

CC-BY-4.0 — free for research and commercial use with attribution to Neo Genesis.

---

## 한국어 요약

**Cross-Agent Code Review Queue** 는 **Codex <-> Claude** 두 주력 코딩 에이전트가 실제 프로덕션 환경(2026-04-08 ~ 04-14)에서 주고받은 **37건의 코드 리뷰 체크포인트 전체 트랜스크립트** 와 **37건의 큐 메타데이터** 를 모은 데이터셋이다.

기존 SWE-bench / AgentBench 가 "한 에이전트가 한 작업을 하는" 케이스만 다루는 반면, 이 데이터셋은 **두 에이전트가 경계를 두고 의견을 주고받는 핸드오프 프로토콜** 자체를 평가/연구용으로 공개한다는 점에서 차별화된다.

각 체크포인트는 다음을 포함:
- `owner_goal` / `owner_intent` 재구성 (요청자가 오너의 진짜 의도를 먼저 정리)
- `review_lens` (risk / architecture / usability / security / rollout / verification 중 선언)
- `success_criteria` 와 `constraints`
- 실제 prompt + Claude 응답 (한국어 + 영어 혼용 마크다운)
- `result`: `new_signal` / `no_new_signal` / `failed`

응용 예시:
- 에이전트 핸드오프 튜닝 (좋은 owner_goal 요약 → new_signal 결과)
- cold review prompting 연구 (오너 의도 재진술 강제 효과)
- 선언된 lens 만 따르는 instruction-following 평가
- 멀티에이전트 boundary 협상 분석

**익명화**: 절대 경로 / 오너 식별자 / 디바이스 호스트명 / 자격증명 / 한국 주민등록번호 패턴은 모두 익명화 토큰으로 치환되었으며, 발행 직전 모든 출력 문자열에 대해 재검증을 수행한다.

라이선스 CC-BY-4.0 — 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_cross_agent_review_queue_2026_2026,
  author       = {Yesol Heo and Neo Genesis Lab},
  title        = {Cross-Agent Review Queue 2026 (Codex ↔ Claude)},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Cross-Agent Code Review Queue (Codex <-> Claude, Neo Genesis 2026)"
type: dataset
authors:
  - family-names: "Heo"
    given-names: "Yesol"
    affiliation: "Neo Genesis Lab"
date-released: "2026-04-30"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026"
repository: "https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018477"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - multi-agent
  - code-review
  - claude
  - codex
  - ai-collaboration
  - checkpoints
  - neo-genesis
preferred-citation:
  type: dataset
  title: "Cross-Agent Code Review Queue (Codex <-> Claude, Neo Genesis 2026)"
  authors:
    - family-names: "Heo"
      given-names: "Yesol"
      affiliation: "Neo Genesis Lab"
  doi: "10.5281/zenodo.20018477"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018477"
```
