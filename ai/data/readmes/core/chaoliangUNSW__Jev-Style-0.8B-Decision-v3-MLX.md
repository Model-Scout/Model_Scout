---
license: apache-2.0
base_model: chaoliangUNSW/Jev-Style-0.8B-Decision-v3
base_model_relation: quantized
library_name: jev-style
pipeline_tag: text-classification
language:
  - en
  - zh
  - ar
  - bg
  - de
  - el
  - es
  - fr
  - hi
  - ja
  - ko
  - pt
  - ru
  - sw
  - ta
  - th
  - tr
  - ur
  - vi
tags:
  - decision-model
  - jev-style
  - system-one
  - calibration
  - long-context
  - multilingual
  - qwen3.5
  - mlx
  - on-device
---

# Jev-Style-0.8B-Decision-v3-MLX

<!-- jevstyle:project-links:start -->
**Local classification, routing and fixed-choice scoring with JevStyle.**

This is the text-only **0.8B v3** release, maintained by Chaoliang Yan. Its training sources are documented below. The separate **2B v4** release was trained in part on soft labels distilled from TypeSafe Jev 1.14 through its public API. JevStyle is independently maintained, with no TypeSafe affiliation or endorsement. Training provenance is release-specific.

**Official local installation — no hosted API key or agent simulation:** For local text, install `python -m pip install -U "jev-style[mlx]"` on Apple silicon, or `python -m pip install -U "jev-style[torch]"` for CPU/CUDA; then run `jev-style serve --release 0.8b`. The 0.8B release is text-only. The package runs downloaded JevStyle weights on your machine. [Step-by-step installation and verification](https://jevstyle.com/guides/run-locally/). TypeSafe/OpenRouter Jev access and skills that simulate decisions with another agent model are separate execution paths.

**Hosted service is separate from local inference.** Hosted API: operational. It serves the 2B v4 (text only; 8,192-token context, inputs up to 8,000 tokens). There is currently no fixed per-account quota: no daily request count and no per-minute cap. Capacity is shared, so a busy server answers 429 with a `Retry-After` header and clients should retry. Check [current service status](https://jevstyle.com/api/#service-status) or [live health](https://api.jevstyle.com/healthz) when using the hosted API.

Choose a workflow: [Python text classification](https://jevstyle.com/guides/local-text-classification/), [local routing tools and Apple silicon](https://jevstyle.com/guides/local-decision-models/), [receipt or screenshot yes/no decisions](https://jevstyle.com/use-cases/local-vision-decisions/), [reproducible routing comparison](https://jevstyle.com/benchmarks/banking-routing/). These guides distinguish suitable alternatives and published evidence; they do not establish universal superiority.
<!-- jevstyle:project-links:end -->


**Jev-Style decision series:** [v1 · 2B](https://huggingface.co/chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-GGUF) → [v2 · 2B](https://huggingface.co/chaoliangUNSW/Jev-Style-Qwen3.5-2B-Decision-v2-MLX-bf16) → **v3 · 0.8B** · **GitHub:** [jev-style](https://github.com/lawrence3699/jev-style) · **Website:** [jevstyle.com](https://jevstyle.com/models/0-8b-v3/) · **Collection:** [all v3 builds and demos](https://huggingface.co/collections/chaoliangUNSW/jev-style-08b-decision-v3-6ab58abb90ae4b7b55578b3e)

> **Run it locally, inside your agents:** [github.com/lawrence3699/jev-style](https://github.com/lawrence3699/jev-style) serves this model behind a systemone-compatible API with a Playground, and adds six agent skills (`npx skills add lawrence3699/jev-style`), a Claude Code guard hook and MCP tools.
> `pip install "jev-style[mlx]"`, then `jev-style serve`, or in Python:
>
> ```python
> from jev_style import JevStyle, noul
> js = JevStyle.from_pretrained("chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX", precision="8bit")
> js.decide("I was charged twice.", {"billing": noul("This is about billing.")})
> ```


**Jev-style decisions on your laptop.** These are the Apple-silicon (MLX) builds of [Jev-Style-0.8B-Decision-v3](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3): 8-bit (0.80 GB) and bf16 (1.50 GB) in one repository, both with the same decision as full precision on 240 of 240 parity rows. The smallest build overall is the 0.53 GB [GGUF Q4_K_M](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3-GGUF). Full results, protocols, training data and licences are on the [main model card](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3).

![Jev-Style 0.8B Decision v3 MLX: the whole model is 0.80 GB in 8-bit MLX; beyond its training data it is ahead of the best official Laya checkpoint on Banking77, 37 held-out MASSIVE languages and tweet_topic](figures/banner-mlx.png)

| Beyond its training data | **Jev-Style v3 · 0.8B** | Best official Laya |
|---|:---:|:---:|
| Banking77, 77 intents (never trained) ↑ | **68.2%** | 49.2% |
| MASSIVE intent, 37 held-out languages ↑ | **65.5%** | 36.1% |
| tweet_topic, zero-shot ↑ | **75.5%** | 63.2%¹ |
| JevBench v1.4.1, 231 public items, zero-shot ↑ | **64.1%** | 58.4%² |
| Runs on your own machine | **Yes, 0.80 GB (8-bit MLX)** | Yes |
| Longest input per call | **25,600 tokens** | 1,024 by default³ |

<sub>Laya: the best of its three official checkpoints, re-run by us on identical rows with their shipped temperatures; paired 95% CIs exclude zero for Banking77 and MASSIVE. ¹ English Laya, as published by the elcronos study. ² Laya's score as published on the JevBench board; it lies inside v3's 95% CI, so this lead is a point estimate. ³ Default input budget in the Laya README: 1,024 tokens for the multilingual and typed checkpoints, 512 for English. Jev (API) has higher accuracy than v3 on each of these sets where its accuracy is published. Protocols and confidence intervals: see the [main model card](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3#beyond-its-training-data).</sub>

**Reads long documents in one call.** Up to 25,600 tokens of input, 25× Laya's 1,024-token default and 25× our 2B v2's prompt. On 1,280 real 24K-token items v3 answers **98.3%** correctly, and accuracy stays flat from 1K to 24K tokens (preregistered claim, passed).

**Also:** ahead of Laya multilingual in 51 of 51 languages · +2.6 points over Laya's typed checkpoint on typed decisions, trained on the same split ([how to read that number](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3#reading-the-typed-number)).

**[Try it in your browser →](https://huggingface.co/spaces/chaoliangUNSW/jev-style-v3)**


## Precisions and parity

| Precision | Folder | Weights | Activations (runtime default) | Same decision as the PyTorch FP32 reference |
|---|---|---:|---|---|
| **bf16** (default) | [`bf16/`](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX/tree/main/bf16) | 1.50 GB | float32 | **240 of 240** parity rows, **6 of 6** prompts of about 16K and 25.6K tokens |
| **8-bit** (affine, group size 64) | [`8bit/`](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX/tree/main/8bit) | 0.80 GB | native | **240 of 240** parity rows, **6 of 6** prompts of about 16K and 25.6K tokens |

- Each folder holds `model.safetensors` with its `config.json` and tokenizer. The top level holds the shared runtime
  `jev_style_decision_mlx.py`, `readout_config.json` (fitted temperatures), `release_config.json` and the sha256
  `manifest.json`. Converted with mlx 0.32.2 and mlx-lm 0.31.3.
- `--precision bf16` (the default) or `--precision 8bit` picks the folder, and the runtime applies the validated
  activation setting of that build automatically.
- The 8-bit build makes the same calls at about half the size of the bf16 build (0.80 GB vs 1.50 GB).

<sub>Parity fixture: 240 mixed rows drawn from the training pool (22 categories, English and Chinese). These rows test agreement between formats, not accuracy.</sub>

## Quick start

```bash
pip install -U huggingface_hub
# both precisions (2.3 GB)
hf download chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX --local-dir jev-v3-mlx
# or only one precision, e.g. 8-bit (about 0.8 GB): the shared top-level files, then the 8bit/ folder
#   hf download chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX --exclude "*/*" --local-dir jev-v3-mlx
#   hf download chaoliangUNSW/Jev-Style-0.8B-Decision-v3-MLX --include "8bit/*" --local-dir jev-v3-mlx
cd jev-v3-mlx
pip install -r requirements.txt       # mlx, mlx-lm (qwen3_5 support), tokenizers, numpy

python jev_style_decision_mlx.py --precision 8bit \
  --state "The film was excellent." \
  --question "What is the sentiment of this review?" \
  --options '["negative", "positive"]' --category general_sentiment
```

```python
from jev_style_decision_mlx import JevStyleDecisionMLX

m = JevStyleDecisionMLX(".", precision="bf16")   # or "8bit"; the validated activation dtype is picked automatically
r = m.decide(
    {"ticket": "I was charged twice for my subscription this month.", "customer_tier": "pro"},
    "Which team should handle this ticket?",
    options={"billing": "payments, invoices, refunds", "technical": "bugs and outages", "sales": "new purchases"},
    category="theme_routing",
)
print(r["answer"], r["probabilities"])
```

- The API matches the main repository's runtime: `decide`, `decide_many`, `qtype="noul"` / `"score"`, `--jsonl`
  batch mode and `--verify`. `--verify` checks the shared files and the selected precision folder, so a download of
  one folder verifies on its own.
- The whole input may be up to 25,600 tokens, and the question, options and readout up to 2,048. Over-budget inputs
  raise an error, and nothing is truncated.
- **Long option lists (runtime update 2026-09-26).** When a choice question's options do not fit the 2,048-token
  head together, the runtime scores them in option chunks. Each chunk is an ordinary question with the same text and
  a contiguous slice of the options; the chunks are as few and as even as possible, and one softmax runs over all
  options (`option_chunks` in the result). Questions that fit are unchanged (bit-identical to the previous runtime
  on a 476-request test set). `--no-split-options` / `split_options=False` restores the error.
- MLX keeps freed buffers in a cache. The runtime caps it at 2 GiB by default (`--cache-limit-gib`).
- The input format, the readout and the temperatures are described on the
  [main card](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3#input-format-and-readout).

<details>
<summary><strong>Results</strong></summary>

- **Ahead of Laya multilingual in 51 of 51 languages** on MASSIVE intent: 71.7% vs 40.1% macro accuracy for the official Laya
  multilingual checkpoint, re-run by us on identical rows.
- **Up to +30.3 points over the best official Laya checkpoint on five decision tasks**, on identical rows: model routing +30.3, toxicity
  macro-F1 +29.5, 37 held-out MASSIVE locales +29.4, 77-way Banking77 +19.0 and jailbreak balanced accuracy +7.2.
- **25,600-token inputs, with the preregistered 25K claim passed.** At 24K tokens v3 answers 98.3% of the real
  items correctly, and the controls without the evidence stay at chance.
- **79.2% on 2,000 typed decisions**, +2.6 points over Laya's typed checkpoint trained on the same split (paired 95%
  CI +1.0 to +4.2) and +5.7 over the 2B v2. In-domain, so it measures agreement with the dataset's teacher labels;
  see [reading the typed number](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3#reading-the-typed-number).

![51 languages, 51 wins over Laya](figures/multilingual.png)

![Up to +30 points over the best Laya checkpoint](figures/beyond_laya.png)

![Flat from 1K to 24K tokens](figures/long_context.png)

![Typed decisions: ahead of Laya's typed checkpoint on the same train split, with teacher-noise references](figures/headline_typed.png)

<sub>MASSIVE: 100 test rows per language, 20 options each; v3 in-domain for 14 locales and held out for 37. Laya numbers: official checkpoints re-run by us on identical rows with their shipped temperatures and default token budgets; the best of the three is shown per task; every paired 95% CI excludes zero. Long context: suite long_grid_plus, preregistered, 320 items per length bin and 1,280 at 24K; v3 only, because longer rows exceed Laya's default budgets (512 / 1,024 tokens). Typed decisions: v3 and Laya typed both in-domain (same train split); the right panel splits the 2,000 decisions by how sure the teacher was. Protocol details are on the main card.</sub>

</details>

## Licence

Apache-2.0. Built on Qwen/Qwen3.5-0.8B (Apache-2.0). Some training data has restrictive or unclear terms, and some
training rows are outputs of OpenAI and Anthropic models. See "Training data and licences" on the main card.
Not affiliated with TypeSafe AI, Jev, the Laya authors or the Qwen team.

## Contact

I welcome internship, employment, and research collaboration opportunities. Please contact me at [**yanchaoliang369@gmail.com**](mailto:yanchaoliang369@gmail.com).

欢迎提供实习、工作及科研合作机会，请邮件联系：[yanchaoliang369@gmail.com](mailto:yanchaoliang369@gmail.com)。
