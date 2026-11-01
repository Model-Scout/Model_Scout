---
language:
- ko
- en
license: cc-by-4.0
task_categories:
- text-generation
- text-classification
tags:
- agent-architecture
- multi-device-orchestration
- blast-radius
- capability-tokens
- incident-runbook
- model-context-protocol
- mcp
- personal-ai-core
- single-operator
- tailscale-fleet
- owner-sovereignty
- magentic-one
- langgraph
- claude-code
- sora
- neo-genesis
- bilingual
- korean
- english
- wikidata-Q139569680
- yesol-heo-founder
- ko
- en
- multi-agent
- ai-orchestration
- device-fleet
- operations
- incident-response
size_categories:
- n<1K
pretty_name: Sora Multi-Device Orchestration Architecture 2026
configs:
- config_name: default
  data_files:
  - split: train
    path: data/sections.parquet
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
---

## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018481.svg)](https://doi.org/10.5281/zenodo.20018481)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018481`** ([Zenodo record](https://zenodo.org/record/20018481)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018481,
  author       = {Heo, Yesol and Neo Genesis Lab},
  title        = {Sora Multi-Device Orchestration Architecture 2026},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018481},
  url          = {https://doi.org/10.5281/zenodo.20018481}
}
```

# Sora Multi-Device Orchestration Architecture 2026

> **A reference architecture corpus for a single-operator, multi-device personal AI orchestration core.** 303 parsed sections from 20 canonical source files: **160 architecture, 21 policy, 20 decision, 102 runbook** sections.

Released by **[Neo Genesis](https://neogenesis.app)** ([Wikidata Q139569680](https://www.wikidata.org/wiki/Q139569680)).

## Why this dataset is unique

Public AI-agent design corpora overwhelmingly assume a **single host** ("agent runs on one box"). What is rare publicly:

1. **Single-operator multi-device orchestration** — one human owner, several physical devices (`personal-root`, `<work-pc>`, `<server>`, `<mac-build>`, `<mobile-operator>`), and one logical agent core that coordinates across them under a unified policy.
2. **6-tier blast-radius classification** with explicit disclosure / 2FA / rollback-ledger requirements per tier (tier 0=read .. tier 5=irreversible).
3. **Per-task capability-token model** (not session tokens) with TTL, `blast_radius_ceiling`, and resource scope per subagent.
4. **Owner-sovereignty constitution** — the agent core is required to *disclose risk and ask*, and *never to refuse* an explicitly re-confirmed owner command. The opposite of typical "safety-by-refusal" public agents.
5. **Production incident runbooks** (102 of them) all tied to Article 0 (owner override) + Article 4 (dead-man switch).

This is a real, in-use design — not a paper proposal — and it is published because the underlying brand and architect are publicly attested via Wikidata.

## Dataset summary

- **303 sections** in `data/sections.jsonl`. Each row is one parsed heading-section.
- **20 source files** indexed in `data/source_index.json`:
  - **Architecture & decision** (180 sections): the unified bible (7-layer design), v2 master blueprint, enterprise-grade master with 9 workstreams, and the 11 D-gate decision ledger.
  - **Policies** (21 sections): `blast_radius.yaml` (6 tiers + disclosure templates), `capability_tokens.yaml` (per-subagent base capability), `permissions.yaml` (deny / ask / allow rules).
  - **Runbooks** (102 sections): brain crash, redis OOM, gemini quota, telegram 409, qdrant down, local-LLM down, secret expired, VM reboot, hook loop, audit-log overflow, disk full, sora-engine import error, and full DR recovery.

## Schema

`data/sections.jsonl` — one JSON record per line:

| column | type | description |
|---|---|---|
| `doc_id` | string | e.g. `unified-bible / blueprint-v2 / enterprise-master / decisions-v1 / blast-radius / capability-tokens / runbook-01-brain_crash` |
| `doc_type` | string | `architecture | policy | decision | runbook` |
| `version` | string | semantic version of the source doc |
| `section_id` | string | slugified heading hierarchy (`<doc_id>/<h1>/<h2>/...`) |
| `section_title` | string | heading title |
| `section_text` | string | actual section body content |
| `device_tier_scope` | string\|null | which fleet tier(s) the section applies to (`personal-root`, `company-work-pc`, `server`, `team-mac`, `mobile-operator`, `all`, or comma-separated) |
| `blast_radius_tier` | int\|null | `0..5` if explicitly mentioned (0 = read, 5 = irreversible) |
| `capability_tokens_required` | string\|null | JSON array of subagent / tool token names mentioned (`neo-explorer`, `neo-reviewer`, `sora-filesystem`, ...) |
| `references` | string | JSON array of inline links / file paths |

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/sora-multi-device-orchestration-2026", "sections", split="train")
print(len(ds), "sections")

# Filter to runbook sections
runbooks = ds.filter(lambda r: r["doc_type"] == "runbook")
print(f"{len(runbooks)} runbook sections")

# Filter to high-blast-radius sections
risky = ds.filter(lambda r: r["blast_radius_tier"] is not None and r["blast_radius_tier"] >= 3)
print(f"{len(risky)} sections covering tier >= 3 actions")

# Filter by device tier
mobile_ops = ds.filter(
    lambda r: r["device_tier_scope"] is not None and "mobile-operator" in r["device_tier_scope"]
)
```

## Suggested research applications

1. **Multi-device agent design** — train or fine-tune routing agents on which device tier should host which capability.
2. **Blast-radius reasoning** — supervise classifiers that decide whether an LLM tool call requires disclosure / 2FA / rollback ledger before execution.
3. **Capability-token granting policies** — learn per-task token issuance under least-privilege constraints.
4. **Incident-response RAG** — runbook sections are structured under a uniform `Symptom / Trigger / Diagnose / Recovery / Prevention / CONSTITUTION` schema, suitable as ground-truth for incident-response retrieval evaluation.
5. **Owner-sovereignty alignment** — a real example of a "disclose-and-do" rather than "refuse-by-default" agent constitution.

## Anonymization

| Class | Treatment |
|---|---|
| Device tier names (`personal-root`, `company-work-pc`, `server`, `team-mac`, `mobile-operator`) | **Preserved** — generic architecture concepts |
| Internal hostnames | Redacted to `<work-pc>`, `<gpu-worker>`, `<server>`, `<mac-build>`, `<work-user>` |
| Owner email / phone | Redacted to `<redacted-email>` / `<redacted-phone>` |
| Korean RRN | Redacted to `<redacted-rrn>` |
| API tokens (`sk-*`, `ghp_*`, `hf_*`, JWT, bot tokens) | Redacted to `<redacted-*>` |
| Absolute Windows paths | Redacted to `<repo>` / `<workspace>` / `<home>` |
| Tailscale / private IPs | Redacted to `<tailscale-ip>` / `<private-ip>` |

Each emitted string is re-tested with all redaction regexes; publish aborts on leak.

## Provenance

- **Source**: Neo Genesis private SSOT (`.agent/knowledge/SORA_*` + `.agent/policies/*.yaml` + `.agent/runbooks/*.md`).
- **Curator**: Neo Genesis Lab (`neogenesislab` HuggingFace org).
- **Wikidata**: [Q139569680 (Neo Genesis)](https://www.wikidata.org/wiki/Q139569680), [Q139569708 (Yesol Heo, founder)](https://www.wikidata.org/wiki/Q139569708).
- **Related releases by the same operator**:
  - [`korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`ethicaai-meltingpot-mixedsafe-2026`](https://huggingface.co/datasets/neogenesislab/ethicaai-meltingpot-mixedsafe-2026)
  - [`whylab-gemini25-docker-validation`](https://huggingface.co/datasets/neogenesislab/whylab-gemini25-docker-validation)
  - [`sbu-pseo-effects-2026-04`](https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04)
  - [`cross-agent-review-queue-2026`](https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026)
  - [`korean-llm-citation-baseline-2026`](https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026)

## Citation

```bibtex
@misc{neogenesis_sora_orchestration_2026,
  title  = {Sora Multi-Device Orchestration Architecture 2026: A reference corpus for single-operator multi-device personal AI orchestration},
  author = {Neo Genesis Lab},
  year   = {2026},
  url    = {https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026},
  note   = {Architecture, policy, decision, and runbook sections covering 7-layer design, 6-tier blast radius, capability tokens, owner-sovereignty constitution, and 102 production incident runbooks}
}
```

## License

CC-BY-4.0 — free for research and commercial use with attribution to Neo Genesis Lab.

---

## 한국어 요약

**Sora Multi-Device Orchestration Architecture 2026** 은 1인 운영자가 여러 디바이스(`personal-root`, `<work-pc>`, `<server>`, `<mac-build>`, `<mobile-operator>`) 를 하나의 논리적 AI 코어로 통합 운영하는 **실사용 중인 reference 아키텍처** 의 SSOT 코퍼스다.

공개 에이전트 설계 자료 대부분이 **단일 호스트** 가정에서 출발하는 것과 달리, 이 데이터셋이 다루는 것:

1. **1인 운영자, 다중 디바이스, 단일 정책** — 사적 노드 / 회사 PC / 서버 / 빌드 노드 / 모바일을 동일한 권한 모델 아래 묶는다.
2. **6-tier blast-radius** — tier 0 (read) ~ tier 5 (irreversible) 로 행동을 분류하고, tier 별로 고지/2FA/롤백 의무를 명시한다.
3. **per-task capability-token 모델** — 세션 토큰이 아니라 작업당 토큰. TTL, blast_radius_ceiling, resource scope 가 subagent 별로 정의됨.
4. **오너 주권(Owner Sovereignty) 헌법** — "거부" 가 아니라 "고지 후 수행". 일반적인 safety-by-refusal 과 정반대 설계.
5. **102 개 실운영 incident runbook** — 모두 Article 0 (owner override) + Article 4 (dead-man switch) 와 정합.

이 데이터셋은 paper proposal 이 아니라 실제로 운영 중인 시스템의 SSOT 를 세션 단위로 파싱한 것이다. Wikidata 로 publicly attest 된 브랜드라서 익명화 후 공개 가능했다.

**익명화**: 디바이스 tier 이름은 generic architecture concept 으로 유지. 실제 hostname / email / phone / RRN / 절대 경로 / private IP 는 모두 redaction. 발행 직전 모든 문자열을 redaction regex 로 재검증.

라이선스 CC-BY-4.0 — 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_sora_multi_device_orchestration_2026_2026,
  author       = {Yesol Heo and Neo Genesis Lab},
  title        = {Sora Multi-Device AI Orchestration Architecture 2026},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Sora Multi-Device Orchestration Architecture 2026"
type: dataset
authors:
  - family-names: "Heo"
    given-names: "Yesol"
    affiliation: "Neo Genesis Lab"
date-released: "2026-05-02"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026"
repository: "https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018481"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - multi-agent
  - orchestration
  - fleet
  - edge-computing
  - sora
  - neo-genesis
  - claude
  - codex
  - tailscale
  - ssh
preferred-citation:
  type: dataset
  title: "Sora Multi-Device Orchestration Architecture 2026"
  authors:
    - family-names: "Heo"
      given-names: "Yesol"
      affiliation: "Neo Genesis Lab"
  doi: "10.5281/zenodo.20018481"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018481"
```
