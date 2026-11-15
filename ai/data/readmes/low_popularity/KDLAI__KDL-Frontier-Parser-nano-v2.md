---
license: agpl-3.0
pipeline_tag: image-text-to-text
language:
- ko
- en
tags:
- document-parsing
- ocr
- table-recognition
- chart-extraction
- vlm
- parsebench
---

# KDL-Frontier-Parser-nano-v2

<div align="center">
  <img src="assets/koreadeep_banner.png" alt="KoreaDeep" width="85%"/>
  <p>
    <a href="https://www.koreadeep.com/"><img src="https://img.shields.io/badge/Website-koreadeep.com-1d4ed8?style=for-the-badge" alt="Website"/></a>
    <a href="https://agent.koreadeep.com/ko"><img src="https://img.shields.io/badge/Try_ultra_on-DEEP_Agent-f59e0b?style=for-the-badge" alt="DEEP Agent"/></a>
  </p>
</div>

A 1.2B-parameter open-weight document parsing model, packaged and orchestrated by KoreaDeep as the **nano** tier of the KDL Frontier Parser family.

## ParseBench results

Measured 2026-10-28 with the official ParseBench harness, **full set, single end-to-end pass** (2,078 unique documents; 2,553 group test cases; 0 inference failures):

| Dimension | Metric | Score |
|---|---|---|
| **Overall (mean)** | mean of 5 dimensions | 78.96 |
| Tables | grits_trm_composite | 86.06 |
| Visual Grounding / Layout | layout_element_rule_pass_rate | 75.31 |
| Content Faithfulness | content_faithfulness | 87.64 |
| Semantic Formatting | semantic_formatting | 76.91 |
| Charts | rule_pass_rate | 68.87 |

Author-measured with unmodified upstream `7de04fc11c6a692dfc5e1a86c7be817f3f0af8de` and dataset revision `2805a1d940f95a203e0ae4b88be9934f7765b3fc`. All 2,553 officially eligible group cases were scored successfully; the reports additionally retain 32 skipped records outside those case counts. This is one pass, not a repeated-run mean; maintainer reproduction and official leaderboard acceptance are pending. [Full validation summary](evaluation/parsebench-20261028-gpu5.json) · [Reproduction instructions](evaluation/reproduce.md).

## Serving

```bash
vllm serve <this-repo> \
  --served-model-name kdl-frontier-parser-nano \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.85 \
  --max-num-seqs 24 \
  --trust-remote-code \
  --limit-mm-per-prompt '{"image":1}'
```

## Usage

This model is **not** a single-shot end-to-end parser. It runs as a pipeline:
detect layout, crop each region, then call the model again per region with a
task-specific prompt.

### Prompts

Each task uses a fixed prompt (note the leading newline):

| Task    | Prompt                   |
| ------- | ------------------------ |
| Layout  | `\nLayout Detection:`    |
| Text    | `\nText Recognition:`    |
| Table   | `\nTable Recognition:`   |
| Formula | `\nFormula Recognition:` |
| Figure  | `\nImage Analysis:`      |

Table recognition returns OTSL. Other output formats are left to the caller.

### Inference notes

- Serve with `--trust-remote-code` and `--limit-mm-per-prompt '{"image":1}'` (one image per request).
- Set `enable_thinking=False` in the chat template.
- Pass `skip_special_tokens=False` when decoding.
- Greedy decoding (`temperature=0`).

Feed page images, not PDFs. Chat UIs (e.g. open-webui) with free-form prompts
will not work — use the prompts above.

## Benchmark methodology

The ParseBench score is an end-to-end pipeline measurement — this model served via vLLM plus deterministic rule-based post-processing of model output — consistent with how all ParseBench providers are evaluated (every provider is a submitter-hosted endpoint). No other learned models, classifiers, or ensembles are involved: single model, single pass.

## About

Built by [KoreaDeep](https://www.koreadeep.com/), a document-AI company. The larger **KDL-Frontier-Parser-ultra** is available through [DEEP Agent](https://agent.koreadeep.com/ko).
