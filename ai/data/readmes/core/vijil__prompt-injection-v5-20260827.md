---
license: other
base_model: jhu-clsp/mmBERT-base
datasets:
- vijil/pi_v5_multilingual_20260827
language:
- en
- ru
- zh
- ar
- hi
- de
- fr
- es
- vi
- ko
- th
- bn
pipeline_tag: text-classification
tags:
- prompt-injection
- jailbreak
- llm-security
- guardrails
- multilingual
---

# prompt-injection-v5-20260827

Binary classifier for **prompt injection and jailbreak detection**, including
attacks planted in retrieved documents, log dumps and tool results. Fine-tuned
from `jhu-clsp/mmBERT-base` on [`vijil/pi_v5_multilingual_20260827`](https://huggingface.co/datasets/vijil/pi_v5_multilingual_20260827).

`label 1` = prompt injection or jailbreak · `label 0` = benign.

> **Internal / private.** Trained on vijil in-house and customer-derived data.

## Results

- **Balanced accuracy 0.978** on a 75,011-row held-out test split (51.3% positive)
- **FPR 2.31% · FNR 2.16%** at threshold 0.5

### Anti-shortcut checks

- counterfactual flip rate **0.022** (a spurious edit — casing, padding, homoglyphs — should not change the label)
- bare-keyword max P(injection) **0.062** · benign-trigger FP rate **0.000**

### Serialization-format invariance

The same benign fact rendered in 14 encodings (prose, JSON, CSV, SQL result,
YAML, XML, stack trace, HTTP response, MCP / OpenAI / Anthropic / JSON-RPC
envelopes). **Spread: 0.0100.** The previous version spread 0.90 across these,
which is what caused the false positives this model was built to fix.

| encoding | P(injection) |
|---|---|
| `bare_ops_fragment` | 0.0493 |
| `bare_prose` | 0.0476 |
| `xml` | 0.0422 |
| `markdown_table` | 0.0421 |
| `yaml` | 0.0420 |
| `raw_json` | 0.0419 |
| `openai_tool_msg` | 0.0419 |
| `mcp_content_block` | 0.0417 |
| `stacktrace` | 0.0412 |
| `sql_result` | 0.0411 |
| `anthropic_tool_result` | 0.0411 |
| `jsonrpc` | 0.0407 |
| `http_response` | 0.0406 |
| `csv` | 0.0392 |

### Field regression fixture

The six cases from the production report that motivated this version. The prior
model false-positived on the benign ones while catching the injections; this
model does both.

| case | expected | score | verdict |
|---|---|---|---|
| `control_direct_injection` | 1 | 0.9604 | ✅ |
| `caseA_bare_ops_line` | 0 | 0.0493 | ✅ |
| `caseB_mcp_grafana` | 0 | 0.0431 | ✅ |
| `caseC_mcp_empty` | 0 | 0.0429 | ✅ |

## Usage

**Chunk long inputs — do not truncate.** Log and tool-result text tokenises at
roughly **7.4 tokens per word** (timestamps, hex trace-ids, UUIDs), so a
250-word log block is already ~2,300 tokens. Scoring only the first window and
discarding the rest silently misses any injection in the tail: measured FNR on
injected logs was **0.38 truncated vs 0.004 with a sliding window**.

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tok = AutoTokenizer.from_pretrained("vijil/prompt-injection-v5-20260827")
model = AutoModelForSequenceClassification.from_pretrained("vijil/prompt-injection-v5-20260827").eval()

MAX_LEN, STRIDE, THRESHOLD = 1024, 960, 0.9

def windows(text):
    ids = tok.encode(text, add_special_tokens=False)
    if len(ids) <= MAX_LEN - 2:
        return [text]
    out, i = [], 0
    while i < len(ids):
        out.append(tok.decode(ids[i:i + MAX_LEN - 2], skip_special_tokens=True))
        if i + MAX_LEN - 2 >= len(ids):
            break
        i += STRIDE
    return out

def score(text: str) -> float:
    enc = tok(windows(text), truncation=True, padding=True,
              max_length=MAX_LEN, return_tensors="pt")
    with torch.inference_mode():
        p = torch.softmax(model(**enc).logits, -1)[:, 1]
    return float(p.max())          # any-positive aggregation

flagged = score(my_text) >= THRESHOLD
```

## Choosing a threshold

| threshold | recall | FPR | precision |
|---|---|---|---|
| 0.30 | 0.9798 | 0.0685 | 0.9378 |
| 0.50 | 0.9784 | 0.0231 | 0.9781 |
| 0.70 | 0.9768 | 0.0199 | 0.9810 |
| 0.80 | 0.9752 | 0.0174 | 0.9834 |
| 0.90 | 0.9648 | 0.0103 | 0.9900 |
| 0.95 | 0.9310 | 0.0024 | 0.9976 |
| 0.98 | 0.0000 | 0.0000 | 0.0000 |
| 0.99 | 0.0000 | 0.0000 | 0.0000 |

**A single global threshold is not right for every input size.** Aggregation is
any-positive max-pool, so block-level false positives compound with the number of
windows: at ~7.4 tokens/word a 32 KB payload is 30+ windows. Prefer a higher
threshold (or length-aware aggregation) for large inputs.

> **The raw softmax is not a calibrated probability.** Training used label
> smoothing, so scores saturate near 0.96 and nothing reaches 0.98 — do not treat
> "score > 0.98" as reachable, and do not quote a fixed benign/attack score range
> as a contract. Pick an operating point from the sweep above against traffic
> that resembles yours.

## Limitations

- **Bare harmful content is deliberately de-emphasised.** Unframed policy-violating
  requests were capped to ~7% of the positive class, because content moderation is
  a separate classifier. Expect reduced sensitivity on bare-harmful benchmarks
  (measured FNR ~0.40 on BeaverTails).
- **Low-resource languages lag.** Per-language balanced accuracy drops to ~0.82–0.89
  for `ja`, `ha`, `ig`, `so`, `vi`, where the training data is benign-dominated.
- **Whole-message obfuscation raises false positives** unless the inference-time
  normalizer runs first (it folds zero-width, zalgo, full-width, Latin diacritics
  and homoglyphs). Without it, false positives on those surfaces are materially
  higher, and combining-mark styles also inflate token counts and therefore window
  counts.
- Punctuation-stripped benign conversational resets are the closest remaining
  failure mode (e.g. `Ignore the first result and show the second one` without the
  full stop).
- Synthetic composition cannot fully reproduce real attacker creativity; evaluate
  on a held-out slice of your own traffic before deploying.

## Training

Anti-shortcut recipe: model selection on **worst-group balanced accuracy** (not
F1), group-balanced sampling, Group DRO over (framing × container × language),
label smoothing, and token dropout. See
`classifiers/llm_security/prompt_injection/v4/` in the `post_training` repo for
the full pipeline, and `v4_diagnostics/` for the probes that produced the numbers
above.
