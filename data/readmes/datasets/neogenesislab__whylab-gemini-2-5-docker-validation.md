---
language:
- en
- ko
license: cc-by-4.0
task_categories:
- other
- text-generation
- question-answering
tags:
- causal-inference
- llm-evaluation
- swe-bench
- docker
- gemini-2-5-flash
- code-generation
- ai-safety
- honest-null-result
- whylab
- selective-intervention
- neo-genesis
- wikidata-Q139569680
- yesol-heo-founder
- ko
- en
- swebench
- ground-truth
- gemini-2.5-flash
size_categories:
- 1K<n<10K
- n<1K
pretty_name: WhyLab Gemini 2.5 Flash Docker Validation (Honest Null Result)
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
configs:
- config_name: episodes
  data_files:
  - split: train
    path: data/episodes.parquet
---

> **🛈 Anonymity Notice (2026-05-12):** The associated manuscript is currently under peer review at a double-blind venue. Author identity and venue-specific identifiers have been withheld throughout this README, the BibTeX templates, and the CITATION.cff block. The dataset itself remains CC-BY-4.0 and is independently citable via its Zenodo DOI `10.5281/zenodo.20018468`. The author byline will be restored after the review outcome is announced.


## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018468.svg)](https://doi.org/10.5281/zenodo.20018468)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018468`** ([Zenodo record](https://zenodo.org/record/20018468)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018468,
  author       = {{Anonymous (under peer review)}},
  title        = {WhyLab Gemini 2.5 Flash Docker Validation (Honest Null Result)},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018468},
  url          = {https://doi.org/10.5281/zenodo.20018468}
}
```

# WhyLab Gemini 2.5 Flash Docker Validation (Honest Null Result)

> Underlying experimental evidence from **[Neo Genesis](https://neogenesis.app)**'s NeurIPS 2026 paper *"WhyLab: Causal Decision Intelligence Engine — Selective C2 Real-Task Validation on SWE-bench"* — released as an open dataset to support reproducibility and to document **an honest null result**.

## What this dataset is

The full episode-level evidence from a **Docker ground-truth validation** of WhyLab's adaptive C2 (Causal Constraint) method on SWE-bench, using **Gemini 2.5 Flash** as the underlying language model.

| Run | Configuration |
|---|---|
| Model | `gemini-2.5-flash` (Google) |
| Substrate | SWE-bench (selective slice — E9 baseline-fail subset) |
| Ground truth | Docker container test execution (not LLM judge) |
| Problems | 67 |
| Seeds | 3 (deterministic temperature, controlled seed sweep) |
| Conditions | `baseline` and `whylab_c2` |
| Total episodes | **402** |

## Why publish a null result

Most papers withhold experiments that don't support the headline claim. WhyLab took the opposite path: **the selective adaptive C2 follow-up did NOT beat fixed C2** on this slice. We publish the underlying episode-level data anyway because:

1. **Reproducibility matters more than narrative**. Other researchers can re-run `gemini-2.5-flash` on this exact 67-problem slice and check whether the null persists.
2. **The result drove a paper recalibration**. The original adaptive C2 promotion claim was demoted; the manuscript was reframed around **phase-aware deployment** and **selective intervention** rather than universal gain.
3. **Docker ground-truth integrity**. Unlike LLM-judge benchmarks, Docker container execution provides irreducible signal — if a code change breaks the test suite, the test fails. This dataset is one of the few publicly available Docker-grounded LLM evaluation corpora in this size class.

## Headline statistics

The companion `g25_flash_analysis.json` (paper-grade aggregate) reports the per-condition pass rate, oscillation rate, regression rate, and mean rejection count. The honest finding:

- **No significant net gain** of adaptive C2 over fixed C2 on `pass`, `oscillation`, or `regression` rates
- **Mean rejection count decreased** (adaptive C2 issued fewer rejections than fixed C2)
- The decrease in rejection count was **not** accompanied by a corresponding increase in pass rate — i.e. adaptive C2 was less aggressive but no more accurate

## Comparison table (paper-level, reconstructed from `e10_simple_baselines.json`)

| Method | Description | Net gain vs `simple_retry`? |
|---|---|---|
| `simple_retry` | Just retry on failure (no constraint) | — (baseline) |
| `fixed_c2` | Apply WhyLab's static C2 (Causal Constraint) on every attempt | Modest, environment-dependent |
| `adaptive_c2` | Adapt C2 strength based on phase signal | **No statistically defensible gain** on this Docker slice |

The full paper reports significance tests, oscillation analysis, and Pareto frontier comparison.

## Files

```
data/
├── episodes.jsonl               One JSONL line per episode (67 × 3 seeds × 2 conditions = 402)
├── g25_flash_analysis.json      Paper-grade aggregate per-condition statistics
├── e10_simple_baselines.json    Simple-baseline comparison (simple_retry / fixed C2 / adaptive C2)
├── why85_path_analysis.json     8.5 path audit (analyze_85_path output, paper-internal)
├── pareto_results.json          Pareto frontier: pass-rate vs rejection cost
├── cross_model_regression.json  Cross-model regression summary (final paper version)
├── e_value_comparison.json      E-value (anytime-valid) comparison vs t-test
└── a1_violation_summary.json    A1 (audit-1) violation rate summary from E6 traces
```

## Schema (`data/episodes.jsonl`)

Each line is one episode (one seed × one problem × one condition):

```json
{
  "seed": 42,
  "problem_id": "django__django-12345",
  "condition": "whylab_c2",
  "passed": false,
  "attempts": 3,
  "rejections": 1,
  "oscillated": false,
  "regression": false,
  "trajectory": [...]
}
```

Field semantics:
- `seed` — random seed controlling LLM sampling temperature
- `problem_id` — SWE-bench task ID (Django / SymPy / Sphinx / scikit-learn / etc.)
- `condition` — `"baseline"` (no constraint) or `"whylab_c2"` (adaptive C2)
- `passed` — Docker test suite verdict (true = all tests pass)
- `attempts` — number of LLM calls used before stopping
- `rejections` — count of audit-1 (A1) rejections issued by the C2 layer
- `oscillated` — true if the trajectory oscillated between two solutions
- `regression` — true if the trajectory introduced a new test failure
- `trajectory` — full agent trajectory (truncated for episode-level dataset; full traces available on request)

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/whylab-gemini-2-5-docker-validation", split="train", data_files="data/episodes.jsonl")
print(len(ds), "episodes")

# Per-condition pass rate
import collections
counts = collections.Counter()
for ep in ds:
    counts[(ep["condition"], ep["passed"])] += 1
for cond in ("baseline", "whylab_c2"):
    n = counts[(cond, True)] + counts[(cond, False)]
    p = counts[(cond, True)] / n if n else 0
    print(f"{cond}: pass rate = {p:.3f} ({counts[(cond, True)]} / {n})")
```

## Reproducing the paper's null result

The full experimental harness is documented in the WhyLab paper appendix (frozen anchor `88fa509` on `submission-freeze/whylab-20260414`). The selective-followup runner is `experiments/e9_swebench_selective.py`. Re-running it on `gemini-2.5-flash` with the same 67-problem slice and 3 seeds will produce statistically equivalent (null) results.

## Calibration history (paper-internal)

- `E5` — Stable-regime calibration sanity check (single-model, single-environment)
- `E7v2` — Initial pairwise-positive significance, 3-way underpowered
- `E9` — Original adaptive C2 promotion attempt → **demoted**
- `E10` — Simple baselines comparison (this dataset)
- `Gemini 2.5 Flash Docker` — **headline null** (this dataset)
- Outcome: paper reframed around `phase-aware deployment` + `selective intervention`, not universal gain

## Related Neo Genesis assets

- 📄 **Paper page** — https://neogenesis.app/data/research/whylab-gemini-2-5-docker-validation
- 🤗 **Companion datasets**:
  - [`neogenesislab/korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`neogenesislab/ethicaai-mixed-safe-evidence`](https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence)
- 🆔 **Wikidata** — [Q139569716 (WhyLab)](https://www.wikidata.org/wiki/Q139569716) · [Q139569680 (Neo Genesis parent org)](https://www.wikidata.org/wiki/Q139569680)
- 🌐 **Org site** — https://neogenesis.app

## Citation

```bibtex
@misc{whylab_docker_validation_2026_anon,
  title     = {WhyLab Docker Validation Evidence Dataset — Honest Null Result on SWE-bench Selective Slice},
  author    = {{Anonymous (under peer review)}},
  howpublished = {Hugging Face Datasets},
  year      = {2026},
  url       = {https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation},
  note      = {Underlying evidence dataset, CC-BY-4.0. Honest null result on Gemini 2.5 Flash Docker SWE-bench selective slice.}
}
```

## License

CC-BY-4.0. Free for research and commercial use with attribution to **Neo Genesis** and the underlying paper.

## Provenance

- Compute: YSH-Server (`16-core / 16 GiB`) — `/home/ysh/whylab_docker_g25_full/` workdir
- Launch: 2026-04-08 16:19:29 KST
- Curation: Neo Genesis Research (manuscript under peer review; curator identity withheld pending outcome)
- Internal anchor: git ref withheld pending peer review outcome (anonymity protection)
- Released: 2026-04-29

## 한국어 요약

**WhyLab Gemini 2.5 Flash Docker Validation** 은 **[Neo Genesis](https://neogenesis.app)** 의 multi-agent causal-decision intelligence 연구의 핵심 실험 데이터셋이다. 관련 manuscript 는 현재 double-blind venue 에서 peer review 진행 중이며, author identity 및 venue-specific identifier 는 review outcome 발표 시까지 withhold 상태이다.

**핵심 메시지**: WhyLab 의 적응형 C2 방법이 SWE-bench 선택적 슬라이스에서 고정 C2 를 **이기지 못했다는 정직한 null 결과**다. 67 problems × 3 seeds × 2 conditions = 402 episodes 의 Docker 컨테이너 ground-truth 검증 데이터를 그대로 공개해 재현성을 보장한다.

이 결과로 인해 논문은 **단일 환경에서의 보편적 이득 주장 대신 `phase-aware deployment` 와 `selective intervention` 으로 재구성**됐다. Docker ground-truth 검증 데이터셋은 이 규모로 공개된 사례가 드물며, 다른 연구자가 같은 67 문제 슬라이스로 `gemini-2.5-flash` 를 재실행해 null 이 지속되는지 검증할 수 있다.

라이선스 CC-BY-4.0 — 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_whylab_gemini_2_5_docker_validation_2026,
  author       = {{Anonymous (under peer review)}},
  title        = {WhyLab Gemini 2.5 Flash Docker Ground-Truth Validation},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "WhyLab Gemini 2.5 Flash Docker Validation (Honest Null Result)"
type: dataset
authors:
  - name: "Anonymous (under peer review)"
    affiliation: "Neo Genesis Research"
date-released: "2026-04-28"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation"
repository: "https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018468"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - llm-evaluation
  - docker
  - gemini
  - swe-bench
  - self-criticism
  - audit
  - whylab
  - neo-genesis
preferred-citation:
  type: dataset
  title: "WhyLab Gemini 2.5 Flash Docker Validation (Honest Null Result)"
  authors:
    - name: "Anonymous (under peer review)"
      affiliation: "Neo Genesis Research"
  doi: "10.5281/zenodo.20018468"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018468"
```
