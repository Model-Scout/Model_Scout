---
license: other
license_name: mixed-open-licenses
language:
  - en
  - ko
task_categories:
  - text-generation
tags:
  - sft
  - instruction-tuning
  - chatml
  - korean
  - english
size_categories:
  - 1M<n<10M
pretty_name: Keural SFT (rebuilt, indentation-fixed)
---

# Keural SFT — Rebuilt (indentation-fixed)

Rebuild of the `keural-SFT` mixed EN/KO instruction dataset, reprocessed from the original
public sources with a **fixed cleaning stage**.

> ⚠️ **Why this rebuild exists**: the original `mkd-chanwoo/keural-SFT` was produced with a
> cleaner rule that collapsed consecutive spaces, which **flattened all code-block indentation
> to one space** — code samples were syntactically broken (root cause of a HumanEval
> regression). The corruption is not recoverable from the published data, so all sources were
> re-collected and reprocessed. **This dataset supersedes `mkd-chanwoo/keural-SFT` — do not
> train on the original if code ability matters.**

- **Total samples**: 1,077,050 (11 shards; per-shard counts and sha256 in `manifest.json`)
- **Languages**: English (~70%) and Korean (~30%)
- **Format**: JSONL, fully-rendered ChatML in `text` (same schema as the original)

## Row schema

```json
{
  "text": "<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n...<|im_end|>",
  "n_tokens": 342,
  "source_name": "magicoder",
  "license": "mit"
}
```

`<|im_start|>` / `<|im_end|>` must be registered as special tokens in your tokenizer
(`tokenizer.add_special_tokens({"additional_special_tokens": ["<|im_start|>", "<|im_end|>"]})`).

## Sources (11 of the original 14)

| source_name | Origin | Final rows | License | Task/Lang |
|---|---|---:|---|---|
| openorca | Open-Orca/OpenOrca (first 400K) | 264,713 | MIT | general/en |
| ultrachat | HuggingFaceH4/ultrachat_200k | 214,329 | MIT | general/en |
| orca_math_korean | kuotient/orca-math-word-problems-193k-korean | 185,541 | MIT | math/ko |
| mathinstruct | TIGER-Lab/MathInstruct | 159,819 | MIT | math/en |
| magicoder | ise-uiuc/Magicoder-OSS-Instruct-75K | 73,119 | MIT | code/en |
| alpaca | tatsu-lab/alpaca | 46,852 | CC-BY-4.0 | general/en |
| koinstruct_qa | GSON-backup/KoInstruct-QA | 45,253 | Apache-2.0 † | general/ko |
| koinstruct_base | GSON-backup/KoInstruct-Base | 42,191 | Apache-2.0 † | general/ko |
| koalpaca | beomi/KoAlpaca-v1.1a | 21,093 | CC-BY-SA-4.0 | general/ko |
| gsm8k | openai/gsm8k (main + socratic ‡) | 12,057 | MIT | math/en |
| competition_math | qwedsacf/competition_math | 12,083 | MIT | math/en |

† The upstream `GSON-backup/KoInstruct-*` repositories carry **no license tag** (checked
2026-07-10). The `apache-2.0` label here reflects MKD-internal confirmation of the original
KoInstruct license; it replaces the `license: unknown` tags in the original keural-SFT.

‡ The collector ingests all files in the repo snapshot, so gsm8k includes both the `main` and
`socratic` answer variants (same behavior as the original keural-SFT build).

**Omitted vs. the original 14 sources**: the three AI Hub datasets
(`aihub_multisession_sci` 71674, `aihub_multisession_social` 71675, `aihub_expert_qa` 71304,
~139K rows) — pending AI Hub credentials and commercial-use confirmation. Note that
AI Hub-tagged rows are excluded by the downstream training filter anyway.

## Processing

Same 10-stage pipeline as the original (structure → clean → quality ≥ 0.6 → safety → per-source
exact+MinHash dedup → ChatML → tokenize ≤ 8,192), with the cleaning stage fixed to **preserve
indentation** (only unicode-abnormal whitespace and control characters are normalized).
Verified post-build: 0 one-space-collapsed code blocks in sampled magicoder/openorca rows.

## Integrity

```bash
sha256sum *_shard_*.jsonl   # compare against manifest.json
```
