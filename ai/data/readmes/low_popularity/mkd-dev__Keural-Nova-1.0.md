---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
language:
  - ko
  - en
library_name: transformers
pipeline_tag: text-generation
tags:
  - korean
  - moe
  - lora
  - instruction-tuning
  - keural
---

# Keural Nova 1.0

**Keural Nova** is a Korean-focused instruction-tuned model built by MKD on top of
[Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) (Apache 2.0), a
35B-parameter Mixture-of-Experts model with ~3B active parameters per token. Full credit for
the base architecture and pretraining goes to the Qwen team at Alibaba Cloud — this release
is a supervised fine-tune (LoRA, merged into the base weights) targeting Korean
conversational quality, with an English/general replay mix to limit capability regression.

**Version note:** v1.0 is the end-of-epoch-1 checkpoint (7,500 optimizer steps), selected as
the best held-out eval-loss point of the training run. A sibling release,
**Keural Nova v1.1**, is the full 2-epoch checkpoint (15,846 steps) — see the comparison
table below; the two make slightly different trade-offs and we publish both transparently.

![benchmark comparison](assets/benchmarks.png)

![animated comparison](assets/benchmarks.gif)

## Evaluation

All numbers measured by us with lm-evaluation-harness 0.4.12 (vLLM backend, bf16, seed 42,
default few-shot settings), same harness and settings for base and fine-tuned models.

| Benchmark | Suite | Base model | **v1.0 (this model)** | v1.1 | Δ v1.0 vs base |
|---|---|---:|---:|---:|---|
| KoBEST | Korean | 62.88 | **68.82** | 67.29 | **+5.94** |
| HAE-RAE | Korean | 75.53 | 73.42 | 74.52 | −2.11 |
| KMMLU | Korean | 64.46 | 62.52 | 62.38 | −1.94 |
| MMLU | General | 83.83 | 82.07 | 82.37 | −1.76 |
| GSM8K (strict-match) | Math | 32.15* | **87.11** | 86.88 | +54.96* |
| HumanEval (pass@1) | Code | 62.20 | 20.73 | 11.59 | **−41.47** |

\* The base model's GSM8K score is heavily depressed by answer-format mismatch under
strict-match extraction; the post-SFT jump is largely format compliance (flexible-extract
scores the fine-tune at 87.49). Treat the delta as a formatting improvement, not a ~55-point
reasoning gain.

**Honest summary:** the fine-tune substantially improves Korean conversational/comprehension
performance (KoBEST) and answer formatting, at the cost of small regressions on
knowledge-recall benchmarks (KMMLU, HAE-RAE, MMLU) and a large regression on code
generation — see Limitations. If your workload is Korean dialogue/comprehension, this model
is the point of this release; if it is knowledge QA or coding, use the base model.

## Intended use & limitations

- **Intended:** Korean conversational AI, Korean text comprehension and generation,
  bilingual (ko/en) assistant use, RAG-style grounded answering in Korean.
- **NOT suitable for code generation.** HumanEval drops from 62.2 → 20.7 pass@1. Root cause
  (identified, not speculative): a large fraction of code examples in one upstream training
  source had whitespace/indentation corrupted during that dataset's original export, and the
  model learned the corrupted formatting. A future release will address this with repaired
  data.
- Knowledge-heavy benchmarks (KMMLU/HAE-RAE/MMLU) regress by ~1–2 points vs base.
- **Context length:** SFT sequences were up to 8,192 tokens; the base architecture supports
  262,144 tokens natively and **up to 1,000,000 tokens via YaRN** rope scaling. Extended-context
  **serving up to 1M tokens has been run in production** through MKD's OpenAI-compatible gateway
  (YaRN factor 4.0) and works. Note: long-context *answer accuracy* has not been measured with a
  dedicated benchmark (e.g., needle-in-a-haystack / RULER), so validate for your specific
  long-document workload.
- The model inherits the base model's multimodal architecture (vision tower is present and
  untouched), but this fine-tune neither trained nor evaluated vision — treat it as a text
  model.

## Training details

| | |
|---|---|
| Base model | Qwen/Qwen3.6-35B-A3B @ `995ad96e` |
| Method | LoRA (rank 32, α 64, dropout 0.0), merged into base weights |
| Adapted modules | attention (`q/k/v/o_proj`), Gated-DeltaNet linear attention (`in_proj_qkv/z/b/a`, `out_proj`), shared experts, **and all 256 routed experts per layer** (fused `gate_up_proj`/`down_proj` tensors via PEFT `target_parameters`) |
| Deliberately frozen | MoE router (`mlp.gate`), `shared_expert_gate`, embeddings, LM head, vision tower |
| Data | 253,528 examples (~85% Korean / 15% English replay), 13 sources, ChatML, empty-`<think>` (non-thinking) format |
| Schedule | effective batch 32, LR 1e-4 cosine, warmup 5%, bf16, DeepSpeed ZeRO-2, 2× H200 |
| This checkpoint | step 7,500 (~1 epoch) — best held-out eval loss (0.857) of the run |
| Loss masking | assistant tokens only; empty think-block scaffold excluded from loss |

Router-integrity and expert-targeting were verified programmatically before and after
training (the router and gates are bit-identical to the base model in this release; the
routed-expert weights are where most of the adaptation lives).

## Training data & licensing

Sources (per-row license tags preserved from upstream): Korean conversation/RAG/QA and
instruction data from the `mkd-chanwoo` keural datasets (CC BY 4.0 / MIT / Apache-2.0 /
CC BY-SA 4.0 subsets only), plus eight sources from `Mkd-Yonas/keural-SFT-chatml-ko-v1`
(MIT / Apache-2.0 / CC BY 4.0), plus English replay data (ultrachat, openorca, alpaca,
magicoder, mathinstruct, gsm8k — MIT/CC BY 4.0).

License mix of the final training set: CC BY 4.0 (105k rows), MIT (87k), Apache-2.0 (46k),
CC BY-SA 4.0 (3.5k), unlabeled (13.7k — two Korean instruction subsets whose upstream rows
carry `license: unknown`; upstream documentation states Apache-2.0, verification pending).

**Excluded by policy:** all AI Hub-derived subsets (non-commercial research terms) were
filtered out of training data.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mkd-ai/Keural-Nova-1.0"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="bfloat16", device_map="auto")

messages = [{"role": "user", "content": "한국의 전통 발효 음식에 대해 설명해 주세요."}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True,
                                 enable_thinking=False, return_tensors="pt").to(model.device)
out = model.generate(inputs, max_new_tokens=512, temperature=0.7, top_p=0.95)
print(tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

vLLM serving (this is a fully merged model — no adapter loading needed):

```bash
vllm serve mkd-ai/Keural-Nova-1.0 --tensor-parallel-size 2 --dtype bfloat16
```

The model is trained in the base model's **non-thinking** chat format
(`enable_thinking=False`); thinking-mode behavior is inherited from the base model untouched.

## Acknowledgements

Built on **Qwen3.6-35B-A3B** by the Qwen team (Alibaba Cloud), released under Apache 2.0.
Korean datasets curated by the MKD data team. Fine-tuning, evaluation, and release
engineering by MKD.
