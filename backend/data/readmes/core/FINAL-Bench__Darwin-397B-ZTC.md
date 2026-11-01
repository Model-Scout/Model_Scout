---
license: apache-2.0
language: [en, ko, zh, ja, multilingual]
library_name: transformers
pipeline_tag: text-generation
tags:
  - darwin
  - darwin-v9
  - darwin-jgos
  - vidraft
  - final-bench
  - qwen
  - qwen3.5
  - qwen3_5_moe
  - moe
  - mixture-of-experts
  - sparse-moe
  - 397b
  - a17b
  - hybrid-attention
  - linear-attention
  - long-context
  - 262k-context
  - reasoning
  - reasoning-model
  - thinking
  - chain-of-thought
  - cot
  - math
  - science
  - stem
  - code
  - agentic
  - tool-calling
  - function-calling
  - ztc
  - zero-token-confidence
  - confidence-estimation
  - uncertainty-quantification
  - hallucination-detection
  - calibration
  - self-verification
  - selective-prediction
  - pre-action-gating
  - agent-safety
  - llm-router
  - guardrails
  - gpqa
  - gpqa-diamond
  - mmlu-pro
  - benchmark
  - eval-results
  - greedy
  - korean
  - english
  - bilingual
  - multilingual-llm
  - vllm
  - sglang
  - openai-compatible
  - multi-gpu
  - h100
model-index:
  - name: Darwin-397B-ZTC
    results:
      - task: {type: text-generation, name: Graduate-Level Reasoning}
        dataset: {type: Idavidrein/gpqa, name: GPQA Diamond, config: gpqa_diamond, split: train}
        metrics:
          - {type: accuracy, value: 93.43, name: "Accuracy (greedy, single-sample)", verified: false}
---

# Darwin-397B-ZTC

### 397B Mixture-of-Experts built on Qwen 3.5 · **FP8** · GPQA Diamond **93.43 %** · **ZTC on board**

`reasoning` · `MoE` · `FP8` · `262K long context` · `Korean + English` · `hallucination detection` · `tool calling`

<p align="center">
<a href="https://vidraft.net"><img src="https://img.shields.io/badge/🌐_VIDRAFT-vidraft.net-111827?style=for-the-badge"></a>
<img src="https://img.shields.io/badge/GPQA_Diamond-93.43%25-gold?style=for-the-badge">
<img src="https://img.shields.io/badge/FP8-418GB-2563eb?style=for-the-badge">
<img src="https://img.shields.io/badge/ZTC-Zero--Token_Confidence-7c3aed?style=for-the-badge">
</p>

> 🏆 **New:** the successor **[Darwin-180B-RSI](https://huggingface.co/FINAL-Bench/Darwin-180B-RSI)** is now **#1 on the GPQA Diamond leaderboard (94.44 %)** — Darwin holds #1 and #3.

**Half the footprint, GPQA Diamond 93.43 %.
And this model stops itself before it acts on an answer it is about to get wrong.**

---

## 🧬 The Darwin Family

<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-180B-RSI"><img src="https://img.shields.io/badge/Darwin--180B--RSI-GPQA_94.44_%231-gold"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF"><img src="https://img.shields.io/badge/POCKET--35B-824K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-26B-GGUF"><img src="https://img.shields.io/badge/POCKET--26B-365K_↓-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/Darwin--35B--A3B--Opus-♥98-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-36B-Opus"><img src="https://img.shields.io/badge/Darwin--36B--Opus-♥97-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/Darwin--4B--Genesis-♥63-e11d48"></a>
</p>
<p align="center">
<a href="https://huggingface.co/FINAL-Bench/Darwin-9B-NEG"><img src="https://img.shields.io/badge/Darwin--9B--NEG-♥57-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/Darwin-28B-REASON"><img src="https://img.shields.io/badge/Darwin--28B--REASON-GPQA_89.39-16a34a"></a>
<a href="https://huggingface.co/FINAL-Bench/Ourbox-35B-JGOS-GGUF"><img src="https://img.shields.io/badge/Ourbox--35B--JGOS-♥30-e11d48"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF"><img src="https://img.shields.io/badge/POCKET--EN-♥43-1f6feb"></a>
<a href="https://huggingface.co/FINAL-Bench/POCKET-KR-GGUF"><img src="https://img.shields.io/badge/POCKET--KR-♥36-1f6feb"></a>
</p>

**Darwin** is [VIDRAFT](https://vidraft.net)'s measurement-driven reasoning model family —
roughly **20 official models**, **400+ community derivatives**, and a standing place among the
top open models on GPQA.

---

## 🧬 Darwin — transplanting the experts that work

A large MoE model is made of hundreds of **experts**.
**Darwin V9** selects the experts that perform best across several high-performing models,
transplants them onto a base backbone, and fuses them with trust-weighted evolutionary merging.

**Nothing is trained from scratch — proven capability is grafted on.**
That is why the same method holds across every model size.

| Model | Scale | GPQA Diamond |
|:---|:---|:---:|
| Darwin-9B-NEG | 9B | 84.3 |
| Darwin-27B-Opus | 27B dense | 86.9 |
| Darwin-36B-Opus | 36B MoE | 88.4 |
| Darwin-28B-Opus | 28B | 88.89 |
| Darwin-28B-REASON | 28B + DELPHI | 89.39 |
| Darwin-398B-JGOS | 397B MoE (bf16) | 90.9 |
| **Darwin-397B-ZTC** | **397B MoE (FP8)** | **93.43** |

### Lineage

| Role | | |
|:---|:---|:---|
| **Base** | `Qwen/Qwen3.5-397B-A17B` | 397B MoE backbone, ~17B active — Apache-2.0 |
| **Darwin V9** | expert transplant + trust-weighted evolutionary merging | this is where the model becomes Darwin |
| **Precision** | compressed-tensors W8A8 FP8 | 418.7 GB |
| **ZTC** | zero-token confidence readout | ships in `ztc/` |

- **Darwin V9** — evolutionary FFN/expert transplant and trust-weighted merging onto large MoE backbones
- **FINAL Bench** — VIDRAFT's evaluation framework
- **Four-layer Pre-AGI roadmap** — Darwin → AETHER → PROMETHEUS → HEPHAESTUS

---

## 🏛️ ZTC — it knows **before it answers**

Until now there were two ways to find out whether a model is about to be wrong.
Both of them only work **after the answer already exists**.

| Existing approach | Limitation |
|:---|:---|
| **Ask the model in words** | Costs extra tokens, adds latency, and models are badly overconfident |
| **Attach an external judge model** | **Two models to operate** · re-reads the entire answer · **degrades on long outputs** · 🔴 **arrives too late — the answer is already produced** |

**ZTC is a third path. It reads the model's own internal state once, before generation begins.**

| | External judge model | **ZTC** |
|:---|:---|:---|
| When | **After** the answer | **Before it starts** |
| Extra model | Required (two to operate) | **None (one)** |
| Extra generated tokens | Re-processes prompt + answer | **0** |
| Added latency | A second inference pass | **0.52 ms** — 0.003 % of generation cost |
| Long answers, long trajectories | **Degrades as length grows** | **Length-independent** |

---

### 📊 Measured — on this model

**① It judges its own answers** (PubMedQA, 539 items, 146 incorrect)

| | AUROC |
|:---|:---:|
| Self-reported confidence (asked in words) | 0.7646 |
| **ZTC (internal-state readout)** | **0.8801** |
| **Gain** | **+0.1155** |

Permutation null control: **z = 13.31** — shuffle the labels and the signal disappears.

**② It judges other models' answers** (Korean KMMLU, 400 items — law, math, biology, history)

| Judge | AUROC |
|:---|:---:|
| **Darwin-397B-ZTC** | **0.8228** (z = 9.66) |
| Qwen3.5-27B | 0.8171 |
| Qwen3.5-9B | 0.7297 |
| Qwen3.5-4B | 0.7284 |
| Open-source 4B judge model | 0.6844 |

*Single domain, random folds. The ladder under the harder leaderboard protocol reads
0.7272 / 0.7289 / 0.6506 / 0.6360 — see the section below.*

**Same 400 items, same conditions: +0.138 over the open-source judge model.**

---

### 📊 Independent leaderboard — 2,018 items, leave-one-domain-out

The **Typed Decision Leaderboard** scores answer verifiers from several vendors on one identical
item set with identical labels: <https://huggingface.co/spaces/mayafree/typed-decision-leaderboard>

| System | AUC |
|:---|:---:|
| **Darwin-397B-ZTC** | **0.7272** |
| JEV (TypeSafe AI) | 0.7350 |
| ZTC-Judge-27B | 0.7289 |
| GPT-5.2 asked directly | 0.7148 |
| open-jev 4B | 0.6844 |
| *Answer length and formatting only* | *0.6223* |

> **Revised 2026-09-21.** Earlier revisions of this card reported **0.7364** for Darwin-397B-ZTC
> and **0.7282** for ZTC-Judge-27B. Those figures were produced by a run whose standardisation
> statistics were computed over all five domains, including the held-out one, which leaks a small
> amount of the evaluation domain into every figure. Re-run with the statistics fitted inside the
> training domains only, the figures are **0.7272** and **0.7289**. Cite the current values.

| Patronus Lynx 8B | 0.5179 |
| *The answering model's own stated confidence* | *0.5000* |

**First place — and the gap to second is 0.0014, with a 95% interval of −0.019 to +0.032.**
Under the board's own rule an interval containing zero yields no rank, so this model and JEV are
**not statistically separable**. That is stated here for the same reason it is stated there.

**Per domain, against the surface baseline in the same domain:**

| Domain | Baseline | **Darwin-397B-ZTC** | ZTC-Judge-27B |
|:---|:---:|:---:|:---:|
| Professional exams (law · math · biology) | 0.7138 | **0.8660** | 0.8462 |
| Biology & medicine | 0.5908 | **0.7433** | 0.7154 |
| Disaster & safety procedures | 0.5949 | **0.7319** | 0.6961 |
| Scientific reasoning | 0.7272 | 0.6287 | **0.7410** |
| General multi-step reasoning | 0.5420 | 0.6072 | **0.6172** |
| **Size-weighted mean** | **0.6223** | **0.7272** | 0.7289 |

🔴 **On scientific reasoning the 27B model beats this one by 0.11.** A model fourteen times smaller
wins that column. It is printed rather than dropped, because the ladder only means something if the
places it inverts are visible.

**Self-readout.** Given only the question, this model answers on its own and the same forward pass
tells whether it was right: **0.7572** (3 domains, 1,595 items). Verifiers that see only text from
outside a model cannot do this at all.

**Protocol.** Every figure comes from a domain the probe never saw; hyper-parameters are selected
inside the training domains only; scores are computed per domain and then size-weighted. Pooling all
items into a single AUC inflates the result, because score scales differ between domains.

---

### Known limitation — the answering-model mixture matters

- **Sensitive to which model wrote the answer.** The probe is fitted on answers from four models.
  Adding 1,772 answers from a single additional model shifted the mixture and **lowered** the
  size-weighted score from 0.7278 to 0.7177 — professional exams rose to 0.8575 while every other
  domain fell. Treat "works on any model's output" as a design goal, not a measured guarantee: if
  your generator differs sharply from the training mixture, measure before relying on the number.

### 🔎 Two measurements, two protocols — do not mix them

| | Section above (PubMedQA / KMMLU) | Leaderboard |
|:---|:---|:---|
| Items | 539 self-judged · 400 other-judged | 2,018, five domains |
| Split | random folds | **held-out domain** |
| Result | 0.8801 · 0.8228 | **0.7272** |

Leave-one-domain-out is far harsher than random folds, which is why the numbers differ. **Quote
0.7272 when comparing against other systems**; the higher figures describe an easier protocol.

---

### 📦 The probe ships with this model

| File | |
|:---|:---|
| `ztc/ztc_probe_darwin397b.npz` | **45 KB** — the confidence readout for this model |
| `ztc/usage.py` | minimal, runnable example |

```python
z = np.load("ztc/ztc_probe_darwin397b.npz")
s = ((h - z["mu"]) / z["sd"]) @ z["w"]        # h = last-token hidden state, 4096-dim
p = 1 / (1 + np.exp(-(z["cal_A"] * (s - z["s_mean"]) / z["s_std"] + z["cal_B"])))
```

One matrix product. No second model, no extra tokens, no network call.
The probe is specific to this model's hidden space (4096-dim) and does not transfer to others.

---

### 🤖 Why this is decisive for agents — **after-the-fact report vs. pre-action stop**

In an agent loop the expensive thing is not tokens. It is **actions**.
Files get edited, APIs get called, payments go through, mail leaves the building.

```
External judge :  [generate] → [tool runs] → [cost, time, side effects] → [judge] → "that was wrong"
ZTC            :  [read state, 0.52 ms] → stop here if risky → the action never happens
```

**In front of an irreversible action, an after-the-fact verdict is an incident report.**

### Patterns

| Pattern | Behaviour |
|:---|:---|
| **Tool-call gating** | Low confidence → do not call the tool, ask a human instead |
| **Model routing** | Send only the low-confidence queries to a larger model or external API |
| **Retry budgeting** | Spend multi-sample decoding only on the steps that wobble |
| **Long-trajectory monitoring** | Agent trajectories run to tens of thousands of tokens — **length-independent, so it can stay on at every step** |
| **Selective prediction** | Withhold a risky answer and return "I don't know" |

### Gate deployment, measured

| Metric | Before | After |
|:---|:---:|:---:|
| Gate accuracy | 71.3 % | **93.3 %** |
| Incorrect answers blocked | 40.7 % | **74.1 %** |
| Expensive-path calls | 42 % | **17 %** |

At effectively zero cost it can stay on for **every** request.

**Use cases** — hallucination detection · uncertainty quantification · confidence calibration ·
selective prediction · routing risky queries upstream · **pre-action gating for agents**

---

## 🏆 GPQA Diamond 93.43 %

| Model | GPQA Diamond |
|:---|:---:|
| **Darwin-397B-ZTC** | **93.43** |
| GPT5.2 | 92.4 |
| Gemini-3 Pro | 91.9 |
| Qwen3.5-397B-A17B | 88.4 |
| Claude 4.5 Opus | 87.0 |

```
GPQA Diamond, all 198 items · greedy · single sample · no test-time engine
```
*Comparison figures: Qwen3.5-397B-A17B official model card.*

---

## API — drop-in for an existing JEV integration

The endpoint takes the same request shape and returns the same response shape, so switching an
existing integration is a URL change.

```bash
POST /v1/evaluate
Authorization: Bearer <token>

{"model": "vidraft/ztc",
 "state": {"question": "...", "answer": "..."},
 "questions": {"correct": {"type": "boolean",
                           "instructions": "Is the ANSWER factually correct?"}}}
```

```json
{"model": "vidraft/ztc-judge-397b",
 "answers": {"correct": {
    "probability": 0.1043,
    "verdict": "review",
    "score": -0.72,
    "position": 0.268,

    "band": "low",
    "action": "hold_or_escalate",
    "measured": {
      "band_accuracy": 0.485,
      "base_accuracy": 0.748,
      "if_lowest_20pct_dropped": 0.814,
      "escalate_gain_at_20pct_budget": 0.0134,
      "do_not": "resample_same_model",
      "why_not": "measured: fixes 6.7% of wrong answers, breaks 13.1% of right ones"}}},
 "usage": {"generated_tokens": 0}}
```

`type` accepts `boolean` and `noul`. Existing clients read `answers.<key>.probability` and ignore
the rest; the additional fields are there for clients that want to act on the score rather than
merely record it. **0.19 s per call, zero generated tokens.**

### What `probability` means

The raw score is unbounded. The shipped calibration maps it to P(answer is correct), fitted
**leave-one-domain-out** — the mapping never sees the domain it is applied to.

| | Expected calibration error |
|---|---|
| **ZTC-Judge-27B (after calibration)** | **0.0245** |
| JEV, as shipped | 0.0381 |
| JEV, after the same calibration | 0.0261 |
| Laya-Multilingual, as shipped | 0.4985 |
| Laya-Typed-Decisions, as shipped | 0.2641 |

Measured on the same 2,018 items. **ZTC and JEV are effectively tied on calibration; the difference
of 0.0016 is not meaningful.** Figures published elsewhere for these systems were measured on other
test sets and do not reproduce here.

🔴 Calibration is uneven across domains: 0.0225 on biology & medicine, but 0.2941 on scientific
reasoning and 0.2381 on general reasoning. Treat the probability as reliable in the first case and
as a ranking signal only in the other two.

## What to do when the score is low

The score alone is not actionable, so the response carries the measured consequence of each choice.

| Band | Share | **Actual accuracy of answers in this band** | Recommended |
|---|---|---|---|
| `low` | 20% | **48.5%** | hold, or escalate to a stronger model |
| `mid` | 40% | 73.2% | escalate if budget allows |
| `high` | 40% | **89.6%** | accept |

**Three things that work, measured on 2,018 items:**

| Action | Effect |
|---|---|
| **Drop the lowest-scoring 20%** | accuracy of what remains: **74.8% → 81.4%** |
| **Escalate the lowest 20% to a stronger model** | **+1.34 pp** end-to-end |
| **Send the lowest 20% to human review** | catches **47.2%** of all errors — 2.4× random |

### Generate several candidates and let the verifier pick

When the score is low, the most effective next step is not to escalate — it is to **produce more
candidate answers and select between them**. Measured on 346 questions with five candidates each
(1,730 candidates), all scored through this endpoint:

| Policy | Accuracy | Output tokens | vs. one attempt |
|---|---|---|---|
| One attempt | 49.13% | 72 | — |
| Majority vote over 3 | 46.82% | 212 | **−2.31 pp** |
| Majority vote over 5 | 46.53% | 353 | **−2.60 pp** |
| **Pick best of 5 with this model** | **51.45%** | 353 | **+2.31 pp** |
| Pick best of 5 with JEV | 53.47% | 353 | +4.34 pp |
| Pick one of 5 at random | 46.82% | 353 | −2.31 pp |
| *Oracle — any correct candidate counts* | *63.87%* | *353* | *+14.74 pp* |

**The same five candidates swing by 5 points depending on how one is chosen.** Majority voting is
worse than not resampling at all: when a model prefers a wrong answer, more samples make that wrong
consensus more certain. A verifier that ranks the candidates is what turns extra samples into
accuracy.

**Spend the budget only where it is needed.** Generating extra candidates only for low-scoring
first attempts captures most of the gain at a fraction of the cost:

| Triggered on | Accuracy | Output tokens | vs. one attempt |
|---|---|---|---|
| 10% of items | 49.71% | 80 | +0.58 pp |
| **30% of items** | **50.87%** | **132** | **+1.73 pp** |
| 100% of items | 51.45% | 353 | +2.31 pp |

**At a 30% trigger rate you get three quarters of the benefit for 1.8× the tokens**, where always
generating costs 4.9× for 1.3× the benefit.

*Scope: one generator (GPT-4o-mini), one item set, five candidates. The oracle row shows the
headroom that remains — a correct candidate is present far more often than any policy recovers it.*

**One thing that does not work:**

🔴 **Do not take a majority vote over resamples.** Measured: five resamples with majority voting score **46.53%** where a single attempt scores **49.13%**. More candidates make a wrong consensus more certain unless something picks between them — see the table above.



*Escalation pays for itself through precision, not recall. Re-answering repairs about 38% of wrong
answers and damages about 30% of right ones, so a gate is only worth its budget if it mostly calls
answers that are actually wrong.*

---

## ⚙️ Specifications

| Item | Value |
|:---|:---|
| Architecture | `Qwen3_5MoeForConditionalGeneration` |
| Parameters | **397 B total / 17 B active** (512 experts, 10 routed + 1 shared per token) |
| Layers · hidden | 60 · 4096 |
| Attention | Hybrid (45 linear + 15 full attention layers) |
| **Precision** | **FP8** (compressed-tensors W8A8) |
| Size on disk | **418.7 GB** |
| Context | **262,144 tokens** |
| License | apache-2.0 |

---

## 🚀 Quickstart

### Serving with vLLM (4 × H100 80GB)

```bash
vllm serve FINAL-Bench/Darwin-397B-ZTC \
  --served-model-name darwin-397b \
  --tensor-parallel-size 1 --pipeline-parallel-size 4 \
  --gpu-memory-utilization 0.92 --max-model-len 262144 \
  --cpu-offload-gb 20 --enforce-eager --trust-remote-code \
  --reasoning-parser qwen3 --enable-auto-tool-choice \
  --port 8000
```

### SGLang

```bash
python -m sglang.launch_server --model-path FINAL-Bench/Darwin-397B-ZTC \
  --port 8000 --tp-size 8 --context-length 262144
```

### Chat Completions (OpenAI-compatible)

```python
from openai import OpenAI
c = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

r = c.chat.completions.create(
    model="darwin-397b",
    messages=[{"role": "user", "content": "Why is the Riemann hypothesis hard?"}],
    temperature=0.0, max_tokens=8192,
)
m = r.choices[0].message
print(m.reasoning_content)   # thinking trace
print(m.content)             # final answer
```

### 🛠️ Tool calling

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {"type": "object",
                       "properties": {"city": {"type": "string"}},
                       "required": ["city"]},
    },
}]

r = c.chat.completions.create(
    model="darwin-397b", tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
)
print(r.choices[0].message.tool_calls)
```

### 🤖 Agents and coding CLIs

The endpoint is OpenAI-compatible, so **existing tooling connects unchanged.**

opencode — `~/.config/opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "darwin": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Darwin (local)",
      "options": { "baseURL": "http://localhost:8000/v1", "apiKey": "EMPTY" },
      "models": { "darwin-397b": { "name": "Darwin-397B-ZTC" } }
    }
  }
}
```

Any OpenAI-compatible client (Cline, Continue, Aider, …)

```bash
export OPENAI_BASE_URL=http://localhost:8000/v1
export OPENAI_API_KEY=EMPTY
export OPENAI_MODEL=darwin-397b
```

---

## 🎯 Intended use
- Graduate-level STEM reasoning (GPQA, science qualifying exams)
- Mathematics and long multi-step chains of thought
- Code generation and debugging
- 🤖 **Agent workflows** — ZTC blocks irreversible tool calls **before** they run
- **Bilingual Korean + English reasoning** (Chinese and Japanese supported)
- **Work where a wrong answer is expensive** — ZTC filters risky answers before they ship

## 🔗 Links
- 🌐 **[vidraft.net](https://vidraft.net)** — VIDRAFT
- 🤗 **[FINAL-Bench](https://huggingface.co/FINAL-Bench)** — all models
- 📱 **[POCKET](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6)** — on-device line that runs on phones and GPU-less PCs

## 📚 Citation
```bibtex
@misc{darwin397b_ztc_2026,
  title = {Darwin-397B-ZTC: FP8 Mixture-of-Experts with Zero-Token Confidence},
  year  = {2026},
  url   = {https://vidraft.net},
  note  = {Base: Qwen/Qwen3.5-397B-A17B}
}
```
