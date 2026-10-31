---
pretty_name: Agentic Quant Panel v1
language:
  - en
  - zh
  - cs
  - de
  - es
  - fr
  - id
  - it
  - ja
  - ko
  - nl
  - pl
  - pt
  - ru
  - sv
  - th
  - uk
  - vi
license: other
license_name: mixed-upstream-licenses
license_link: https://huggingface.co/datasets/wrldsuksgo2mars/agentic-quant-panel-v1/blob/main/README.md#licensing-and-attribution
task_categories:
  - text-generation
size_categories:
  - 1K<n<10K
tags:
  - calibration
  - quantization
  - post-training-quantization
  - mixture-of-experts
  - agentic
  - code
  - math
  - function-calling
  - multilingual
  - reproducible
  - arxiv:2505.03804
  - arxiv:2506.13329
  - arxiv:2510.13999
  - arxiv:2406.18518
  - arxiv:2306.16636
configs:
  - config_name: default
    data_files:
      - split: calibration
        path: data/calibration.parquet
      - split: heldout
        path: data/heldout.parquet
      - split: screening
        path: data/screening.parquet
---

# Agentic Quant Panel v1

A compact, reproducible calibration panel for post-training quantization of language models, with particular attention to the workload of an MoE model used for coding, reasoning, and tool use.

The panel combines real source code, multilingual reference text, worked mathematics, and function-call schemas and examples. Its budget is measured in **tokens**, so a few long examples cannot silently dominate a category. Each prompt has a stable source identity, a source group, a recorded token count, and content hashes.

**Thanks to Brandon for the initial calibration dataset inspiration.** The subsequent five-axis blend, source selection, and publication were developed by [wrldsuksgo2mars](https://huggingface.co/wrldsuksgo2mars).

## Quick start

```bash
pip install datasets
```

```python
from datasets import load_dataset

panel = load_dataset("wrldsuksgo2mars/agentic-quant-panel-v1")
calibration = panel["calibration"]
screening = panel["screening"]  # small subset for fast experiments
heldout = panel["heldout"]      # source-disjoint diagnostic inputs

prompts = calibration["prompt"]
code = calibration.filter(lambda row: row["axis"] == "code_agentic")
print(calibration[0]["messages"])  # one user message, ready for your template
```

Apply the **target model's** chat template once, then tokenize with its tokenizer. For example, with a tokenizer whose template supports a generation prompt:

```python
token_batches = [
    tokenizer.apply_chat_template(
        row["messages"], tokenize=True, add_generation_prompt=True
    )
    for row in calibration
]
```

Use your model's documented thinking-mode settings where applicable. `prompt` and `text` are identical **unwrapped** strings; `messages` contains that same string in one user message. The recorded token counts include the historical selection wrapper and will differ with another tokenizer or template.

For tools that accept JSONL, download [`calibration.jsonl`](calibration.jsonl), [`heldout.jsonl`](heldout.jsonl), or [`screening.jsonl`](screening.jsonl). These are the original files, byte for byte, with the simple schema `{"id": ..., "prompt": ..., "max_tokens": 8}`. The original [`manifest.json`](manifest.json) accompanies them.

## What is in the release?

This release packages the original **`flash-corpus-next-v1`** selection, which was developed for DeepSeek-V4-Flash-0731 quantization. The selection recipe was subsequently adapted in GLMRT and other model projects. This release preserves the original panel; it does not claim to be a tokenizer-identical copy of those later model-specific selections.

| Split | Prompts | Recorded prompt tokens | Purpose |
| --- | ---: | ---: | --- |
| `calibration` | 1,426 | 1,081,027 | Full calibration stream |
| `screening` | 144 | 110,116 | Axis-stratified subset of calibration |
| `heldout` | 88 | 67,437 | Separate source groups for diagnostics |

There are **1,514 distinct selected source identities** across calibration and heldout. Screening reuses calibration identities with different split-local IDs; it does not add independent examples.

Records target 768 rendered tokens and stay within 512–1,024 tokens under the recorded tokenizer. Whole records are selected, so realized budgets can slightly exceed their targets. The legacy `max_tokens: 8` field is a generation cap for the original diagnostic harness; it is **not** the calibration context length or a limit on how much of each prompt to calibrate.

## Why this design?

Quantization uses the activations induced by its calibration inputs. The panel therefore exposes the model to several kinds of text it is expected to process in deployment: code syntax and editing instructions, factual prose in multiple scripts, worked reasoning, and structured tool-call output.

The design revision kept the approximately 1.08 million token budget, increased the code allocation, added worked math and structured function calling, and removed the earlier dedicated legal-topic allocation. These are deliberate workload assumptions, not an experimentally established optimum for every model.

| Axis | Target tokens | Actual calibration tokens | Actual share | Material |
| --- | ---: | ---: | ---: | --- |
| `code_agentic` | 360,000 | 360,274 | 33.3% | Code review, rewriting, and masked-function implementation |
| `general` | 260,000 | 259,969 | 24.0% | Reference-grounded tasks over multilingual Wikipedia excerpts |
| `math_reasoning` | 220,000 | 220,421 | 20.4% | NuminaMath worked solutions and a Chinese CMATH slice |
| `reasoning_termination` | 130,000 | 130,328 | 12.1% | Multiple-choice and relationship tasks over reasoning-related Wikipedia topics |
| `structured_output` | 110,000 | 110,035 | 10.2% | Packed xLAM tool schemas, user queries, and expected calls |

**Code with source context.** Code prompts retain task instructions and a bounded window of real source code. The blend covers application and systems languages as well as CUDA, LLVM, TVM, and related kernel/compiler material. Python, C++, CUDA, C, and Rust are priority languages in the selector. The code examples are single-turn tasks; this release does not contain multi-turn agent trajectories.

**Multilingual breadth.** Each Wikipedia axis targets a token ratio of 40% English, 35% Chinese, and 25% other languages. The realized mix depends on the eligible source groups and record boundaries. The math selector targets up to 20% Chinese tokens within its axis, using all eligible CMATH records when their supply is insufficient and filling the remainder with NuminaMath. Those ratios describe the individual selectors, not the entire dataset. Per-language counts and tokens are in [`statistics.json`](statistics.json).

**Reasoning and structure appear as input tokens.** NuminaMath problems include worked solutions; CMATH prompts include question/answer pairs; xLAM prompts include expected function calls. Although the historical manifest says `answers_included: false`, that means there is no separate generated completion or label field. It does **not** mean the prompt text is answer-free. Calibration sees these solution and output tokens during its forward pass.

**The `reasoning_termination` name is historical.** Its inputs concern mathematics, physics, chemistry, computer science, philosophy, and AI. It has no labeled stopping decisions or generated reasoning traces. It is an input category for diagnostics, not an independently validated termination benchmark.

**Data diversity and expert coverage are separate concerns.** The panel can help sample a deployment distribution, but cannot guarantee adequate routed activations for every expert. Measure coverage and quantization error on the target model. This selection does not implement MoEQuant's expert-balanced self-sampling or EAQuant's optimization algorithm.

## Split construction

The original builder uses seed **`20260806`** and a deterministic SHA-256 group assignment into four buckets. One bucket supplies heldout candidates; three supply calibration candidates. It then selects records to each split's token budget. This is a 25% holdout of **candidate source groups**, not a 25% holdout of the released records.

Grouping follows the underlying source:

| Source | Group boundary |
| --- | --- |
| Wikipedia | Article path |
| Code | Entire upstream repository |
| Math | Bank `problem_id` |
| Structured output | Bank `sample_id` |

Calibration and heldout share no recorded source groups or exact prompt hashes. Packed CMATH and xLAM records are grouped by their bank identifiers; the original manifests do not enumerate every member inside each pack. The split guarantee is at the recorded group level, not a semantic deduplication guarantee across all upstream datasets.

Screening selects approximately 10% of each calibration axis by tokens, using deterministic source-identity ordering. It is useful for early routing or numerical diagnostics. **Do not use screening as independent held-out evidence**, and do not concatenate it with calibration when counting unique examples.

The heldout split contains calibration-style inputs and embedded example answers, rather than scored labels. Use separate, uncontaminated benchmarks to measure downstream task accuracy.

## Schema and provenance

The Parquet files preserve the original row order and add convenient columns from the manifest.

| Columns | Meaning |
| --- | --- |
| `id`, `prompt`, `max_tokens` | Original JSONL fields |
| `text`, `messages` | Plain-text alias and one-user-message chat representation |
| `axis`, `domain`, `family`, `language`, `topic` | Filtering and analysis metadata; `language` includes programming-language labels for code |
| `prompt_tokens` | Rendered input length under the original tokenizer |
| `group`, `source_identity` | Source grouping and identity used by the selector |
| `prompt_sha256`, `token_ids_sha256` | Prompt bytes and rendered token-ID hashes |
| `repo`, `file`, `article_path` | Code or Wikipedia provenance, where applicable |
| `source`, `subset`, `problem_id`, `sample_id`, `schema_id` | Math and structured-source metadata, where applicable |
| `source_url`, `source_revision`, `source_license` | Attribution and source information added for this release |
| `provenance_json` | Exact original per-record manifest entry, serialized as JSON |

Unused source fields are null. Identifier columns in the Parquet export are strings, including `sample_id`. For code, `source_revision` is the upstream Git commit; for Wikipedia it is the dump date; for math and structured data it is the committed **local bank revision**, not an upstream Hugging Face revision. Original upstream collection details remain distinct from these bank identities.

[`provenance/code_sources.json`](provenance/code_sources.json) records the selected repositories, exact source commits, and bundled license/notice paths. Wikipedia URLs identify the original articles and their contributor histories; the excerpts were extracted and bounded from the **2026-07-01** dumps. Prompts and packed examples are adaptations of their upstream sources.

## Reproducibility

The raw split files and manifest are unchanged. [`SHA256SUMS`](SHA256SUMS) covers every published payload, document, and reproduction file. The historical manifest records:

- Training-data snapshot: `792a5d5cc047e50d53780b5b38affb98a0a27a64`.
- DS4RT builder revision: `0ce4686b1b6cf02629190620ae21feac1bdb5eb7`.
- Builder SHA-256: `99b916c3587caae82d75845681f2c8a9058ae90f8397823cadf838be72fd0e55`.
- Selection tokenizer: `deepseek-ai/DeepSeek-V4-Flash-0731`.
- Tokenizer SHA-256: `8f9f37ca37fdc4f5fd36d5cf4d3b0e8392edb4e894fd10cc0d70b4957c8633cf`.

The original one-user-message wrapper is:

```text
<｜begin▁of▁sentence｜><｜User｜>{prompt}<｜Assistant｜></think>
```

Tokens were encoded with `add_special_tokens=False`; the wrapper supplies its own markers. Token-ID hashes use the UTF-8 encoding of `json.dumps(ids, separators=(",", ":"))`.

The exact historical builder and its renderer dependency are in [`reproduction/`](reproduction). Rebuilding from source requires the recorded source banks and processed articles, plus the exact tokenizer bytes. Those full source collections and tokenizer assets are not bundled here; the published JSONL is sufficient to reuse the panel without rebuilding it.

```bash
pip install tokenizers
python reproduction/build_ds4_flash_calibration_corpus.py \
  --training-data /path/to/training-data-at-recorded-revision \
  --tokenizer /path/to/exact/tokenizer.json \
  --output /path/to/new-empty-corpus
```

`manifest.json` retains historical local paths as provenance, not runtime requirements. [`publication.json`](publication.json) records release validation: original split hashes, every prompt and token hash, Parquet round trips, heldout separation, and screening subset membership.

## Research that informed the planning

The original [NEXT design notes](https://github.com/tpurtell/ds4rt/blob/0ce4686b1b6cf02629190620ae21feac1bdb5eb7/CALIBRATION_CORPUS_NEXT.md) referenced the following work. They motivate the attention to workload diversity and sparse expert calibration; their reported gains are results from their own experiments, not claims about this panel.

- [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://proceedings.mlr.press/v267/chen25aa.html), ICML 2025 ([arXiv](https://arxiv.org/abs/2505.03804)). Studies imbalance in expert calibration and proposes expert-balanced sampling and affinity guidance.
- [EAQuant: Enhancing Post-Training Quantization for MoE Models via Expert-Aware Optimization](https://arxiv.org/abs/2506.13329). Addresses sparse expert calibration, outliers, and routing consistency.
- [REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression](https://arxiv.org/abs/2510.13999) and its [released calibration mixture](https://github.com/CerebrasResearch/reap#huggingface-checkpoints). The planning notes used REAP's mix of code, reasoning, and function calling as a workload reference. This panel is a different mixture and does not contain REAP's agent trajectories.
- [LLM Compressor: Choosing a dataset](https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/choosing-dataset/). Practical guidance on domain alignment and calibration size.

Related papers for the included sources:

- [APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets](https://arxiv.org/abs/2406.18518): the work behind xLAM function-calling-60k.
- [CMATH: Can Your Language Model Pass Chinese Elementary School Math Test?](https://arxiv.org/abs/2306.16636): the Chinese mathematics source.
- [NuminaMath-CoT dataset card and citation](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT): the worked mathematics source.

## Licensing and attribution

This is a **mixed-source compilation**. Each component retains its upstream terms; the release does not apply one permissive license to all prompt contents.

| Component | Attribution and terms |
| --- | --- |
| Wikipedia excerpts | Wikipedia contributors; [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Per-row article links identify the contributors and original pages. Excerpts were extracted and shortened. |
| NuminaMath-CoT | [Project Numina / AI-MO and contributors](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT); [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Problem and worked-solution text was sampled and bounded by the source banks/selector. |
| CMATH | [Tianwen Wei, Jian Luan, Wei Liu, Shuang Dong, and Bin Wang](https://arxiv.org/abs/2306.16636); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Question/answer examples were packed into calibration inputs. |
| xLAM function-calling-60k | [Salesforce AI Research / APIGen authors](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Schemas, queries, and expected calls were packed. |
| Open-source code | Upstream authors and contributors, under the applicable repository and file-specific licenses. Exact source links and commits appear per row and in the code source registry; retained license and notice files are under [`licenses/code/`](licenses/code). Code windows may be shortened or have a function body removed for an implementation task. |

The xLAM bank was collected from [`NobodyExistsOnTheInternet/xlam-function-calling-60k`](https://huggingface.co/datasets/NobodyExistsOnTheInternet/xlam-function-calling-60k), a mirror recorded in the collection notes. Salesforce and APIGen remain the upstream attribution.

CMATH material includes upstream validation/test examples. NuminaMath also aggregates established math problem collections. Once used for calibration, overlapping upstream benchmark scores cannot serve as uncontaminated evaluation. The panel's source-disjoint heldout split does not establish freedom from a model's pretraining data.

## Citation and acknowledgments

```bibtex
@misc{agentic_quant_panel_v1,
  author = {wrldsuksgo2mars},
  title = {Agentic Quant Panel v1},
  year = {2026},
  howpublished = {Hugging Face dataset},
  url = {https://huggingface.co/datasets/wrldsuksgo2mars/agentic-quant-panel-v1}
}
```

Please also credit the underlying sources when redistributing their material, and cite APIGen and CMATH when using their components. Thanks to **Brandon** for the initial calibration dataset inspiration, and to the source authors, Wikipedia contributors, and open-source maintainers whose work makes the panel possible.
