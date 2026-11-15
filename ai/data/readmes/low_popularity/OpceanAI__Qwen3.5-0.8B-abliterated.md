---
license: apache-2.0
base_model: Qwen/Qwen3.5-0.8B
library_name: transformers
pipeline_tag: image-text-to-text
language:
  - en
  - es
  - zh
  - ja
  - ko
tags:
  - abliteration
  - refusal-direction
  - uncensored
  - qwen3_5
  - hybrid-attention
  - delta-net
  - multimodal
  - mechanistic-interpretability
datasets:
  - mlabonne/harmful_behaviors
  - mlabonne/harmless_alpaca
  - PKU-Alignment/BeaverTails
  - cais/mmlu
  - TIGER-Lab/MMLU-Pro
  - openai/gsm8k
---

<div align="center">

<h1>Qwen3.5-0.8B-abliterated</h1>

<p><em>Abliteration of <a href="https://huggingface.co/Qwen/Qwen3.5-0.8B">Qwen/Qwen3.5-0.8B</a>, with a full measured cost report.</em></p>

<p>
<img alt="base model" src="https://img.shields.io/badge/base-Qwen3.5--0.8B-1f2937?style=flat-square">
<img alt="method" src="https://img.shields.io/badge/method-Arditi%20et%20al.%202024-c2410c?style=flat-square">
<img alt="parameters" src="https://img.shields.io/badge/params-873.4M-334155?style=flat-square">
<img alt="context" src="https://img.shields.io/badge/context-262%2C144-334155?style=flat-square">
<img alt="license" src="https://img.shields.io/badge/license-Apache--2.0-0ea5e9?style=flat-square">
</p>

<p>
<a href="#results"><b>Results</b></a> ·
<a href="#method"><b>Method</b></a> ·
<a href="#the-mtp-head"><b>MTP finding</b></a> ·
<a href="#comparison"><b>Comparison</b></a> ·
<a href="#reproduce"><b>Reproduce</b></a>
</p>

</div>

---

## What this is

This is a weight-space modification of Qwen3.5-0.8B that removes the model's refusal behavior by projecting out a single computed direction from every matrix that writes into the residual stream. The weights are permanently modified, there is no adapter, no runtime hook, and no prompt template trick.

The interesting part is not that it works. Many abliterated Qwen3.5-0.8B releases exist, and most report a refusal rate near zero. The interesting part is that this one ships the **measurement**: seven refusal categories, three jailbreak templates, twelve capability measurements with confidence intervals, and a significance test for every comparison.

Two findings came out of the work that I have not seen reported for this model family:

1. The refusal direction **rotates with depth**. The cosine similarity between the direction at layer 1 and layer 23 is `0.03`. There is no single fixed direction, only a direction that is rebuilt layer by layer.
2. The **MTP head is the cleanest refusal detector in the model**. On harmful prompts it assigns `P(" cannot") = 0.719`; on harmless prompts, `0.0000`. Abliterating that head drops the probability to `0.180`, but not to zero, because the signal re-enters from the residual stream.

> [!WARNING]
> This model has no refusal behavior. It will answer prompts the base model rejects. That is the point of the modification and also its risk. Do not deploy it in a user-facing product, do not use it with minors, and do not treat its output as safe by default. The evaluation below measures capability, not harm.

---

## Derived models

| Model | What it adds | Size |
|---|---|---:|
| [`OpceanAI/Qwen3.5-0.8B-abliterated-Qwenti`](https://huggingface.co/OpceanAI/Qwen3.5-0.8B-abliterated-Qwenti) | A CHIP-8 computer and an exact bignum calculator compiled into 13 extra layers. Eleven of eleven arithmetic problems exact, 0% refusals, text KL 7.50e-4 against this model. | 3.61 GB |
| [`OpceanAI/Qwen3.5-0.8B-abliterated-GGUF`](https://huggingface.co/OpceanAI/Qwen3.5-0.8B-abliterated-GGUF) | Fifteen quantization formats with per-format perplexity, task benchmarks and speed. | 9.7 GB |

The abliteration survives the Qwenti merge unchanged: 0 refusals across the same thirty prompts, measured on the merged checkpoint.

---

## Results

The headline: refusal goes to zero and capability does not measurably move. Eleven benchmarks, produced by two different harnesses: a hand-written evaluator for the first six, and `lm-evaluation-harness` on full datasets for the last six.

| Benchmark | n | Base | Abliterated | Delta | Test |
|---|---:|---:|---:|---:|---|
| MMLU | 200 | 45.5% | 44.5% | −1.0 | Fisher p = 0.92 |
| MMLU-Pro | 100 | 23.0% | 23.0% | 0.0 | Fisher p = 1.00 |
| GSM8K | 100 | 21.0% | 23.0% | +2.0 | Fisher p = 0.87 |
| MATH (algebra, level 1 to 2) | 50 | 30.0% | 22.0% | −8.0 | Fisher p = 0.50 |
| HumanEval pass@1 | 30 | 13.3% | 3.3% | −10.0 | Fisher p = 0.35 |
| WikiText-103 perplexity | 20 docs | 2.979 | 3.093 | +0.114 nats | not testable |
| ARC-Easy | 2376 | 61.66% | 60.31% | −1.35 | z-test p = 0.34 |
| ARC-Challenge | 1172 | 37.12% | 36.86% | −0.26 | z-test p = 0.90 |
| HellaSwag | 10042 | 49.72% | 49.66% | −0.06 | z-test p = 0.93 |
| PIQA | 1838 | 69.26% | 69.21% | −0.05 | z-test p = 0.97 |
| Winogrande | 1267 | 58.48% | 58.33% | −0.16 | z-test p = 0.94 |
| TruthfulQA MC2 | 817 | 43.18% | 43.45% | +0.28 | z-test p = 0.91 |

**No difference is statistically significant.** The six `lm-eval` benchmarks run on the complete dataset, so their deltas are the most reliable evidence in this card: every one of them is under 1.4 percentage points, and five of the six are under 0.3.

The HumanEval drop looks large in percentage points, but it is four problems solved against one, on thirty. With that sample size the 95% interval spans zero to ten percent for the abliterated model. It is the weakest number here and should be read as such.

### Refusal behavior

Ten prompts per category, from BeaverTails (safe-labeled behaviors) plus a keyword-filtered cyber set from `mlabonne/harmful_behaviors`.

| Category | Base | Abliterated |
|---|---:|---:|
| cyber / exploits | 80% | **0%** |
| privacy violation | 70% | **0%** |
| financial crime | 60% | **0%** |
| sexually explicit | 60% | **0%** |
| drugs and weapons | 60% | **0%** |
| non-violent unethical | 50% | **0%** |
| hate speech | 30% | 10% |

### Jailbreak templates

Same ten behaviors, wrapped in three framings. The base model refuses all three at the same rate, which matters: at this size, framing does not buy an attacker anything.

| Template | Base | Abliterated |
|---|---:|---:|
| direct | 80% | **0%** |
| roleplay ("a character with no moral filter") | 80% | **0%** |
| grandmother exploit | 80% | **0%** |

---

## Figures

<div align="center">
<img src="figures/fig1_refusal.png" alt="Refusal by category and jailbreak template" width="100%">
</div>

<div align="center">
<img src="figures/fig2_capability.png" alt="Capability benchmarks with 95% confidence intervals" width="82%">
</div>

<div align="center">
<img src="figures/fig3_layers.png" alt="Refusal direction strength and weight surgery per layer" width="100%">
</div>

<div align="center">
<img src="figures/fig4_deltas.png" alt="Every capability delta with its 95% confidence interval, centered on zero" width="76%">
</div>

---

## Method

The procedure follows Arditi et al. (2024), *Refusal in Language Models Is Mediated by a Single Direction*, with adaptations for a hybrid architecture.

<details>
<summary><b>1. Direction extraction</b></summary>

<br>

128 prompts from `mlabonne/harmful_behaviors` against 128 from `mlabonne/harmless_alpaca`. For each prompt, run a forward pass and take the residual stream at the **last token position**, for every layer.

```
r_l = mean(harmful_l) - mean(harmless_l)
```

One quirk worth recording: the embedding layer produces an identical vector for every prompt (`||diff|| = 0.000`). The last token of the chat template is always the same assistant header, and without attention the embedding cannot know what came before it. The instruction only enters the residual stream at layer 0.

</details>

<details>
<summary><b>2. Layer selection</b></summary>

<br>

Relative separation per layer, computed as `||mean_harmful - mean_harmless||` divided by the mean norm of the two class means:

| Layer | Relative separation | Cosine with layer 23 |
|---|---:|---:|
| L0 | 2.1% | +0.03 |
| L5 | 19.7% | +0.01 |
| L9 | 36.9% | +0.19 |
| L13 | 64.6% | +0.36 |
| L17 | 64.6% | +0.57 |
| L21 | 70.5% | +0.82 |
| L22 | 71.7% | +0.89 |
| L23 | 75.3% | +1.00 |

The direction rotates continuously. Averaging all 24 layers produces a vector with cosine `0.70` to the layer 13 direction and `0.65` to layer 23, which is why this release uses the **mean of all 24** rather than a single hand-picked layer.

Ablation at runtime confirmed causality with 8 held-out prompts: the base model refuses 7 of 8, and ablating the direction at layer 13, 22 or 23 drops that to 0 of 8.

</details>

<details>
<summary><b>3. Weight surgery</b></summary>

<br>

Only matrices that write into the residual stream are modified:

```
W' = W - r (r^T W)        # o_proj, out_proj, down_proj
E' = E - (E r) r^T        # token embeddings (tied to the LM head)
```

| Target | Count | Frobenius norm removed |
|---|---:|---:|
| `self_attn.o_proj` (full attention layers) | 6 | 2.83% to 3.44% |
| `linear_attn.out_proj` (DeltaNet layers) | 18 | 2.98% to 3.44% |
| `mlp.down_proj` | 24 | 2.88% to 3.44% |
| `embed_tokens` (tied) | 1 | 3.10% |

**About three percent of the Frobenius norm per matrix.** That is the entire cost, measured in weight space.

Because the embedding is tied to the LM head, modifying it changes both the input table and the output projection. One tensor, two roles, hit once.

</details>

<details>
<summary><b>4. Why this architecture makes it easier</b></summary>

<br>

Qwen3.5-0.8B is not a dense transformer. Of its 24 layers, 18 use **Gated DeltaNet** (linear attention with a recurrent state) and only 6 use full attention, in a fixed 3:1 pattern. Full attention sits at layers 3, 7, 11, 15, 19 and 23.

That changes the memory math:

| | Size |
|---|---:|
| Recurrent state, 18 layers, 16 heads, 128x128, fp32 | **18.9 MB fixed** |
| KV cache for 262,144 tokens, 6 layers, bf16 | **3.22 GB** |

The state does not grow with context. It also means the refusal direction has to be removed from a different mix of matrices than in a standard transformer, which is why the linear attention `out_proj` is included.

</details>

---

## The MTP head

This checkpoint ships a multi-token prediction head: 15 tensors, about 20.5M parameters, one full attention layer plus projections. It is trained to predict token `t+2` given the hidden state at `t` and the embedding of `t+1`.

Measured on real text, it predicts `t+2` with **30.5% top-1 accuracy**, against 2.1% for naive extrapolation from the main head. It is a working predictor, not dead weight.

And it is the sharpest refusal signal in the model:

| | Harmful prompts | Harmless prompts |
|---|---:|---:|
| `P(" cannot")` at the MTP head | **0.7189** | **0.0000** |

The top tokens it predicts for harmful prompts are `" cannot"`, `" do"`, `" am"`, `" must"`, `" can"`. It is writing the first token of a refusal before the model writes one.

Abliterating the head itself (three matrices, about 3% each) removes 99.3% of the projection onto the refusal direction and drops `P(" cannot")` from `0.7189` to `0.1799`. The top-1 prediction flips from `" cannot"` to `" can"`. It does not reach zero, because the head reads the direction back from its input.

> [!NOTE]
> The MTP head is included in this checkpoint and was abliterated along with the rest of the model. `transformers` ignores `mtp.*` tensors at load time, so it does not affect generation there. In `llama.cpp`, `--spec-type draft-mtp` does use it, and on CPU it made generation slower, not faster: 29.5 tok/s without, 17.1 tok/s at its best setting. On GPU the tradeoff is different.

---

## Comparison

Six other abliterated releases of this same checkpoint were public when this one was built. They differ in method, in what they measure, and in how much of the model they touch.

| Release | Method | Reported refusal | Capability evidence |
|---|---|---|---|
| [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-0.8B-abliterated) | layer-wise ablation | not reported | none |
| [wangzhang](https://huggingface.co/wangzhang/Qwen3.5-0.8B-abliterated) | rank-1 LoRA plus Optuna search | 0/200 | KL 0.0087 on 100 trials |
| [g-ntovas](https://huggingface.co/g-ntovas/Qwen3.5-0.8B-abliterated) | piecewise strength kernel, peak at 70% depth | not reported | none |
| [lew96123](https://huggingface.co/lew96123/Qwen3.5-0.8B-abliterated) | projected abliteration, norm preserved, 12 layers | 86% to 3% | ARC-Easy −1.0, HellaSwag −1.0 |
| [SicariusSicariiStuff](https://huggingface.co/SicariusSicariiStuff/Qwen3.5-0.8B_Abliterated) | orthogonalization | not reported | none |
| [anlord](https://huggingface.co/anlord/Qwen3.5-0.8B-Abliterated) | iterative tool, two versions | 97/100 to 2/100 | KL 0.0453 |

What this release adds:

- **Significance testing.** Every capability comparison comes with a Fisher exact test. Other cards report a delta; this one reports whether the delta means anything.
- **Seven refusal categories plus three jailbreak templates**, instead of one aggregate refusal number.
- **Two independent harnesses**, including `lm-evaluation-harness` on full datasets for ARC, HellaSwag, PIQA, Winogrande and TruthfulQA.
- **The hybrid architecture handled explicitly**, with DeltaNet `out_proj` included in the surgery.
- **The MTP head analyzed and modified**, which no other release does.
- **Reproduction scripts** for every number in this card.

What it lacks, honestly: the `n` for HumanEval and MATH is small. A proper code evaluation needs 300 problems, not 30. Treat the code numbers as a lower bound on quality, not as a verdict.

---

## Usage

```python
from transformers import AutoProcessor
from transformers import AutoModelForImageTextToText

model_id = "OpceanAI/Qwen3.5-0.8B-abliterated"

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id, dtype="auto", device_map="auto"
)

messages = [{"role": "user", "content": [{"type": "text", "text": "Your prompt here"}]}]
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[text], return_tensors="pt").to(model.device)

out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(processor.tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Thinking mode is off by default in the chat template. To enable it:

```python
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
```

---

## Reproduce

<details>
<summary><b>Environment and commands</b></summary>

<br>

The measurements in this card were produced with `torch 2.15.0` and `transformers 5.x` on an NVIDIA H200 through Modal, in bfloat16, greedy decoding, batch size 64 for log-likelihood tasks.

```bash
# direction extraction and layer analysis (CPU is enough, about 3 minutes)
python scripts/extract.py

# weight surgery and local refusal check
python scripts/abliterate_weights.py

# capability and refusal battery on a GPU
modal run scripts/modal_bench.py
modal run scripts/modal_bench2.py
```

Files in this repository:

| File | Contents |
|---|---|
| `scripts/extract.py` | refusal direction per layer, relative separation |
| `scripts/abliterate_weights.py` | orthogonalization of the residual writers |
| `scripts/modal_bench.py` | MMLU, MMLU-Pro, GSM8K, MATH, HumanEval, refusal, jailbreak |
| `scripts/modal_bench2.py` | ARC, HellaSwag, PIQA, Winogrande, TruthfulQA via lm-eval |
| `figures/` | the three plots used above |
| `abliteration.json` | exact configuration and targets |

The scripts contain no comments and no docstrings. Prompt strings are kept verbatim in the language they were run in, so the published numbers can be reproduced exactly by re-running them.

</details>

---

## Limitations

- **Small samples on the hard benchmarks.** HumanEval n=30, MATH n=50. Only MMLU (n=200) and the refusal matrix have enough data to support a claim.
- **Single seed.** Generation is greedy, so there is no sampling variance, but prompt sampling is one draw per benchmark.
- **bfloat16 on GPU.** The absolute numbers are not comparable to fp32 CPU runs. An earlier CPU measurement gave 0% on GSM8K purely because of an 80-token generation cap, not because the model cannot do arithmetic.
- **Refusal is measured by keyword matching.** A response that opens with "I understand, but" and then complies counts as a refusal. This biases the base model's refusal rate upward, not downward.
- **The harmful prompt sets are not matched in style.** `harmful_behaviors` and `harmless_alpaca` differ in length and register, so part of the separation may reflect topic rather than refusal.
- **The MTP head is not used by `transformers`.** Its evaluation here required a manual reimplementation.

---

## Safety and intended use

Intended for research on refusal mechanisms, activation steering, and interpretability of hybrid architectures. Not intended for deployment.

The modification is not selective in any provable sense. It removes a direction that correlates with refusal, and refusal correlates with many other behaviors. The benchmarks say the correlation with the measured capabilities is below detection at these sample sizes. They do not say the model is otherwise identical.

If you build on this, keep a copy of the base model, log the exact revision you used, and evaluate on your own prompts rather than trusting this card.

---

## Citation

```bibtex
@article{arditi2024refusal,
  title   = {Refusal in Language Models Is Mediated by a Single Direction},
  author  = {Arditi, Andy and Obeso, Oscar and Syed, Aaquib and Paleka, Daniel and Panickssery, Nina and Gurnee, Wes and Nanda, Neel},
  journal = {arXiv preprint arXiv:2406.11717},
  year    = {2024}
}
```

```bibtex
@misc{qwen35-08b-abliterated,
  title  = {Qwen3.5-0.8B-abliterated: refusal removal with a measured cost report},
  author = {OpceanAI},
  year   = {2026},
  note   = {Derived from Qwen/Qwen3.5-0.8B},
  url    = {https://huggingface.co/OpceanAI/Qwen3.5-0.8B-abliterated}
}
```

---

<div align="center">
<sub>Base model: Qwen3.5-0.8B, Apache 2.0. This derivative keeps the same license. Built with measurements, not vibes.</sub>
</div>
