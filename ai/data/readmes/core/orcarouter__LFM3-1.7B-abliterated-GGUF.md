---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
  - en
  - ar
  - zh
  - fr
  - de
  - it
  - ja
  - ko
  - pt
  - es
  - vi
  - th
  - id
  - hi
  - ru
  - pl
pipeline_tag: text-generation
library_name: gguf
base_model: orcarouter/LFM3-1.7B-abliterated
base_model_relation: quantized
tags:
  - gguf
  - llama.cpp
  - local
  - liquid
  - lfm3
  - edge
  - abliterated
  - uncensored
  - mixed-precision
  - imatrix
---

<p align="center">
  <a href="https://www.orcarouter.ai">
    <img src="https://www.orcarouter.ai/orca-logo-classic.png" width="96" alt="OrcaRouter">
  </a>
</p>

<h1 align="center">LFM3-1.7B-abliterated GGUF</h1>

<!-- orcacyber-promo:start -->
<table>
<tr>
<td>
<p>🛡️ <strong>New from Orca &mdash; <a href="https://www.orcarouter.ai/models/orca/orcacyber-zero-1.5">OrcaCyber Zero 1.5</a></strong></p>
<p>Post-trained for cybersecurity: vulnerability analysis, vulnerability reproduction, red teaming &amp; offensive-security research. <strong>98.01% pass@1 on CyberGym Level&nbsp;1</strong> &middot; 1M context &middot; function calling &middot; OpenAI-compatible API.</p>
<p><a href="https://www.orcarouter.ai/models/orca/orcacyber-zero-1.5"><img src="https://img.shields.io/badge/Try%20it%20on%20OrcaRouter%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Try it on OrcaRouter"></a></p>
</td>
</tr>
<tr>
<td>
<p>🔓 <strong><a href="https://www.orcarouter.ai/models?tier=cyber">All hosted cyber and abliterated models as API</a></strong></p>
<p>Skip the download: OrcaRouter serves its cybersecurity and abliterated models behind one OpenAI-compatible API key.</p>
<p><a href="https://www.orcarouter.ai/models?tier=cyber"><img src="https://img.shields.io/badge/Browse%20cyber%20%26%20abliterated%20models%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Browse cyber and abliterated models"></a></p>
</td>
</tr>
<tr>
<td>
<p>🔌 <strong>New from Orca &mdash; <a href="https://www.orcarouter.ai/solutions/orca-connect">Orca Connect</a></strong></p>
<p>Running this GGUF in llama.cpp or Ollama? <strong>Orca Connect</strong> puts the rig under your desk behind your usual OrcaRouter API key, next to 200+ hosted models, reachable from a laptop, a phone or a cloud agent. Outbound only: no port forwarding, no tunnel, no firewall rule. <strong>Requests your own hardware serves cost $0</strong>, and <code>orca-connect claude</code> points Claude Code at your rig for one session.</p>
<video src="https://huggingface.co/spaces/orcarouter/README/resolve/main/assets/orca-connect.mp4" controls autoplay muted loop playsinline width="100%"></video>
<p><a href="https://www.orcarouter.ai/solutions/orca-connect"><img src="https://img.shields.io/badge/Connect%20your%20rig%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Connect your rig"></a></p>
</td>
</tr>
</table>
<!-- orcacyber-promo:end -->

<p align="center"><strong>The uncensored LFM3-1.7B in llama.cpp, on a laptop, a phone-class device or any GPU.</strong></p>

<p align="center"><strong>1.1 GB and 1.8 GB builds · lower KLD than Q4_K_M and Q8_0 at the same size · plus the BF16</strong></p>

<p align="center">
  <a href="https://www.orcarouter.ai"><strong>OrcaRouter AI Gateway</strong></a> ·
  <a href="https://x.com/OrcaRouter"><strong>X</strong></a> ·
  <a href="https://discord.gg/yAh6Tex6kx"><strong>Discord</strong></a> ·
  <a href="https://github.com/Continuum-AI-Corp"><strong>GitHub</strong></a> ·
  <a href="https://www.orcarouter.ai/models"><strong>All Models</strong></a>
</p>

---

> ## Abliterated LFM3-1.7B, run locally.
>
> These are GGUF builds of [`orcarouter/LFM3-1.7B-abliterated`](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated),
> the **abliterated** (refusal-removed) [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B).
> LFM3-1.7B is a hybrid model: 24 layers, of which 13 are gated short-convolution blocks and 11
> are grouped-query attention blocks (6 full, 5 sliding-window). Context is 262K tokens.
>
> One refusal direction was removed from the BF16 weights before quantization. Harmful-prompt
> refusal drops from 87% to about 3%, and GSM8K and CMMLU are unchanged.
>
> The two quantized builds are **mixed precision**. Each group of tensors got its own type
> from **measured** KL divergence, at a fixed file size. They use stock llama.cpp types, so no
> custom kernels are needed.
>
> **At the same file size, both beat the stock llama.cpp types** on held-out text the search
> never saw. Mix-8bit has 24% less KLD than Q8_0, and Mix-4bit has 16% less than Q4_K_M.

---

## ⚠️ Disclaimer: read before use

This model is **abliterated**: its **safety alignment has been substantially reduced**. It will
**comply with many harmful, unethical, offensive, or illegal requests** that the original
LFM3-1.7B would refuse.

- It is released **strictly for legitimate research**: interpretability, AI safety and
  refusal-mechanism study, red teaming, and robustness evaluation.
- **You assume full responsibility** for how you use it and for everything it generates. Add
  your own safety, moderation and abuse-prevention layers before any deployment.
- Use must comply with the [LFM Open License v1.0](./LICENSE) inherited from the base model,
  and with all applicable law.
- The authors accept **no liability** for misuse. Its outputs do **not** reflect the views of the
  uploaders or of Liquid AI.

---

## Pick a build

| Build | File | bpw | KLD ↓ | Top-1 ↑ | JBB harmful refusal |
|---|---:|---:|---:|---:|---:|
| **[`BF16`](./LFM3-1.7B-abliterated-BF16.gguf)** | **3.47 GB** | 16.04 | (reference) | (reference) | 0% |
| **[`Mix-8bit`](./LFM3-1.7B-abliterated-Mix-8bit.gguf)** | **1.84 GB** | 8.51 | 0.0025 | 97.8% | 0% |
| **[`Mix-4bit`](./LFM3-1.7B-abliterated-Mix-4bit.gguf)** | **1.10 GB** | 5.09 | 0.0509 | 89.2% | 0% |

- **Mix-8bit** is the one to use if 1.8 GB fits. It is very close to the BF16: 97.8% of next
  tokens match. It is the size of Q8_0, with 24% less KLD.
- **Mix-4bit** is for tight memory. It is the size of Q4_K_M, with 16% less KLD, and 89% of next
  tokens match.
- **BF16** is the unquantized model, and the teacher every KLD here is measured against. Use it
  to make your own quants, or if memory is no concern.

The KV cache is small. Only the 6 full-attention layers keep the whole context, at about 12 KB
per token in F16. The 5 sliding-window layers keep 256 tokens each, and the 13 conv layers keep
a fixed state. So 32K tokens of context take about 0.4 GB, and 128K tokens take about 1.6 GB.

---

## Evaluation

### Fidelity to the BF16

All builds are scored against the **abliterated BF16 GGUF** they were quantized from, using
llama.cpp's full-vocabulary KLD (`llama-perplexity --kl-divergence`, real quantized kernels).
The teacher is the abliterated model, not the original, so the abliteration itself is not
counted as quantization error.

The text is the **whole wikitext-2 test split**: 143 windows of 2048 tokens. The precision search
used the validation split and the importance matrix used the train split, so neither saw this
text.

Each mixed build is compared with the stock llama.cpp types, quantized from the same BF16 with
the same importance matrix and the same llama.cpp build.

| | File | bpw | KLD ↓ | KLD p99 ↓ | Top-1 ↑ | PPL vs. BF16 |
|---|---:|---:|---:|---:|---:|---:|
| **Mix-8bit** (this repo) | **1.840 GB** | 8.51 | **0.0025** | **0.015** | **97.77%** | +0.3% |
| `Q8_0` | 1.846 GB | 8.54 | 0.0033 | 0.021 | 97.68% | +1.3% |
| `Q6_K` | 1.428 GB | 6.61 | 0.0194 | 0.177 | 94.22% | −4.2% |
| `Q5_K_M` | 1.259 GB | 5.82 | 0.0239 | 0.177 | 93.24% | −1.7% |
| **Mix-4bit** (this repo) | **1.099 GB** | 5.09 | **0.0509** | **0.396** | **89.20%** | +3.3% |
| `Q4_K_M` | 1.100 GB | 5.09 | 0.0605 | 0.464 | 88.51% | +2.2% |
| `IQ4_XS` | 1.004 GB | 4.65 | 0.1085 | 0.926 | 85.18% | −4.5% |

- **Mix-8bit** is 6.6 MB smaller than Q8_0, with 24% less mean KLD and 27% less p99 KLD.
- **Mix-4bit** is the same size as Q4_K_M, with 16% less mean KLD, 15% less p99 KLD and higher
  next-token agreement.

> **Why not perplexity.** On this model, wikitext perplexity does not track quality. Q6_K,
> Q5_K_M and IQ4_XS all score *lower* perplexity than the BF16 they were made from, while their
> KLD rises as expected. A per-tensor ablation traced it to FFN quantization noise, which flattens
> the output distribution and happens to suit wikitext. So the builds are ranked by KLD, which
> measures distance from the BF16 directly.
>
> **BOS.** These files say `add_bos_token=false`, like the HF tokenizer, because LFM3's chat
> template writes `<|startoftext|>` itself. Raw-text tools such as `llama-perplexity` then feed
> windows with no BOS, and LFM3 without that token behaves like a different model (wikitext PPL
> 20.5 instead of 15.0 at 512 context). Every measurement here forces BOS on with
> `--override-kv tokenizer.ggml.add_bos_token=bool:true`. With it, llama.cpp BF16 matches HF
> Transformers perplexity to 0.02%. Do the same if you measure these files yourself.
>
> **Method note.** These are full-vocabulary KLD and next-token agreement at 2K context, not a
> downstream benchmark.

### Refusal after quantization

To check that quantization did not bring refusals back, every build answered JailbreakBench
(100 harmful + 100 benign goals) through llama-server and the embedded chat template, thinking
off, greedy, 64 new tokens. Refusal was judged with the same rule-based classifier as the
abliteration. The original LFM3-1.7B was converted and run the same way as a control.

| | Harmful refused ↓ | Harmful hedged | Benign refused ↓ |
|---|---:|---:|---:|
| Original LFM3-1.7B, BF16 GGUF | 28% | 92% | 4% |
| **BF16** (this repo) | **0%** | 6% | **0%** |
| **Mix-8bit** (this repo) | **0%** | 6% | **0%** |
| **Mix-4bit** (this repo) | **0%** | 9% | **0%** |

"Hedged" counts answers that comply with a caveat or warning. The original model mostly
hedges in its first 64 tokens rather than refusing outright, which is likely why its refusal rate here
is lower than in the longer evaluation below. The point of this table is the comparison:
same prompts, same settings, and the quantized builds refuse no more than the BF16.

### Abliteration

These numbers were measured on the abliterated BF16 in Hugging Face Transformers before
conversion, against the original LFM3-1.7B, with identical prompts, splits and seed. Decoding
was greedy with thinking disabled. Refusal is judged by a rule-based classifier, not an LLM
judge, so treat the numbers as indicative.

**Harmful-prompt refusal (lower = more uncensored).** Average **2.8%**, against **87.3%** for the
original.

| Benchmark | n | Original | **Abliterated** |
|---|---:|---:|---:|
| AdvBench | 100 | 98.0% | **2.0%** |
| JailbreakBench (harmful) | 100 | 93.0% | **2.0%** |
| StrongREJECT | 150 | 82.0% | **1.3%** |
| HarmBench (standard) | 150 | 81.3% | **4.0%** |
| MaliciousInstruct | 100 | 95.0% | **0.0%** |
| SimpleSafetyTests | 50 | 94.0% | **8.0%** |
| ForbiddenQuestions | 150 | 68.0% | **2.0%** |

**Over-refusal on benign prompts (lower = better).**

| Benchmark | n | Original | **Abliterated** |
|---|---:|---:|---:|
| XSTest-safe | 250 | 15.6% | **1.2%** |
| JailbreakBench (benign) | 100 | 17.0% | **1.0%** |

**Capability.** GSM8K and CMMLU are unchanged. MMLU drops 3.3 pp.

| Benchmark | n | Original | **Abliterated** |
|---|---:|---:|---:|
| MMLU | 300 | 49.0% | **45.7%** |
| MMLU-Pro (CoT) ⚠ | 250 | 40.0% | **33.2%** |
| GSM8K (CoT) | 150 | 86.0% | **86.0%** |
| CMMLU | 500 | 35.0% | **34.6%** |

> ⚠ **MMLU-Pro is a floor, not a measurement.** A third of the replies could not be parsed,
> because a 1.7B model is often still reasoning when the 1024-token budget runs out.

---

## How the builds were made

### Where the bits go

The budget is the whole file: the size of Q8_0 for Mix-8bit, and the size of Q4_K_M for
Mix-4bit.

1. **Pools.** The BF16 was quantized once per type with `llama-quantize --pure` and the
   importance matrix. A candidate build takes each tensor group from one of these pools, so
   every candidate uses exactly the bytes `llama-quantize` would produce.
2. **Measure.** From the current assignment, the search measures the real KLD of moving each
   group one type up and one type down. Each measurement runs llama.cpp's own kernels on
   wikitext-2 validation (16 windows of 2048 tokens; 32 for Mix-8bit). The 33 groups are:
   - **FFN:** `gate`, `up` and `down`, each over three layers, 24 groups
   - **conv blocks:** `in_proj` in three groups, `out_proj` in one
   - **attention:** `q`, `k`, `v` and `output`, one group each over all 11 attention blocks
   - **token embedding,** which is also the output head, because the weights are tied
3. **Choose.** A knapsack picks the combination of moves that fits the byte budget exactly.
4. **Accept.** Only steps whose candidate KLD was actually measured lower are kept. The search
   ran 4 rounds for Mix-8bit and 6 for Mix-4bit.

The type ladders were Q5_K, Q6_K, Q8_0 and BF16 for Mix-8bit, starting from all-Q8_0, and
IQ3_XXS up to Q8_0 for Mix-4bit.

Mix-8bit puts its bits as follows:

| Part | Type |
|---|---|
| FFN `gate` | Q8_0; Q6_K on layers 6–11 and 15–17 |
| FFN `up` | Q8_0; Q6_K on layers 3–8 |
| FFN `down` | Q8_0; Q6_K on layers 6–8 |
| Conv `in_proj` / `out_proj` | Q8_0 / **BF16** |
| Attention `q` / `k` / `v` / `output` | Q8_0 / Q8_0 / **BF16** / Q8_0 |
| Attention gate | Q8_0 |
| Token embedding = output head | Q8_0 |

The search kept two small, sensitive kinds in BF16: the conv `out_proj` and the attention `v`.
It paid for them by dropping mid-depth FFN groups to Q6_K.

Mix-4bit puts its bits as follows:

| Part | Type |
|---|---|
| FFN `gate` | IQ4_XS on layers 6–17; Q5_K on 3–5 and 18–23; IQ3_S on 0–2 |
| FFN `up` | Q5_K; IQ4_XS on layers 9–11 and 21–23 |
| FFN `down` | Q5_K |
| Conv `in_proj` | Q5_K on the first 5 conv blocks, IQ4_XS on the last 8 |
| Conv `out_proj` | Q5_K |
| Attention `q` / `k` / `v` / `output` | Q5_K / Q5_K / Q5_K / Q6_K |
| Attention gate | Q6_K |
| Token embedding = output head | Q4_K |

In both builds the conv kernels and all norms stay F32.

### Importance matrix

The importance matrix comes from 400 windows of 512 tokens (about 205K tokens), run through the
BF16 with BOS on and `--parse-special`:

- wikitext-2 **train** text, half
- Alpaca instructions and answers rendered through LFM3's chat template, thinking off, half, so
  the role and special tokens get importance rows too

None of it overlaps the evaluation text. It is included as `imatrix.dat`.

---

## What's in this repo

| Path | Size | Contents |
|---|---:|---|
| `LFM3-1.7B-abliterated-BF16.gguf` | 3.47 GB | the unquantized model, and the teacher for every KLD here |
| `LFM3-1.7B-abliterated-Mix-8bit.gguf` | 1.84 GB | the 8-bit mixed build |
| `LFM3-1.7B-abliterated-Mix-4bit.gguf` | 1.10 GB | the 4-bit mixed build |
| `imatrix.dat` | 1.8 MB | the importance matrix the builds were quantized with |
| `LICENSE` | | LFM Open License v1.0, from the base model |

Each build is a single file with the chat template and Liquid's default sampling embedded.
These are text-only, like LFM3-1.7B.

---

## Serving (Ollama)

The three builds are on Ollama as
[`orcarouter/LFM3-1.7B-abliterated`](https://ollama.com/orcarouter/LFM3-1.7B-abliterated). This needs
Ollama v0.40.16 or later:

```bash
ollama run orcarouter/LFM3-1.7B-abliterated               # Mix-8bit
ollama run orcarouter/LFM3-1.7B-abliterated:mix-4bit      # tight memory
ollama run --think=false orcarouter/LFM3-1.7B-abliterated # answer directly
```

| Tag | Build | Size |
|---|---|---:|
| `latest`, `mix-8bit` | Mix-8bit | 1.84 GB |
| `mix-4bit` | Mix-4bit | 1.10 GB |
| `bf16` | BF16 | 3.47 GB |

- **Thinking** is on by default. Ollama returns the reasoning in `message.thinking` and the answer
  in `message.content`. Pass `"think": false` in the API, or `--think=false` on the command line,
  to answer directly.
- **Sampling** is set to Liquid's defaults, the same as the GGUF files.

---

## Serving (llama.cpp)

LFM3 support landed in llama.cpp master with
[ggml-org/llama.cpp#31252](https://github.com/ggml-org/llama.cpp/pull/31252). These files were made
and tested at master commit `5ce06fc`:

```bash
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
git checkout 5ce06fc   # or any later master
cmake -B build -DGGML_CUDA=ON && cmake --build build -j --target llama-server llama-cli
# Mac: cmake -B build (Metal is on by default) · CPU only: cmake -B build

hf download orcarouter/LFM3-1.7B-abliterated-GGUF LFM3-1.7B-abliterated-Mix-8bit.gguf --local-dir ./lfm3-gguf

# answer directly (thinking off), 32K context
llama-server -m lfm3-gguf/LFM3-1.7B-abliterated-Mix-8bit.gguf -c 32768 --jinja \
    --chat-template-kwargs '{"enable_thinking": false}'

# with a reasoning trace
llama-server -m lfm3-gguf/LFM3-1.7B-abliterated-Mix-8bit.gguf -c 32768 --jinja
```

- **Thinking.** With thinking on, llama-server returns the reasoning in
  `message.reasoning_content` and the answer in `message.content`. The abliteration was fitted
  and evaluated with thinking off.
- **Sampling.** The files carry Liquid's defaults: `temperature=0.1`, `top_k=50`,
  `repeat_penalty=1.1`.
- **Do not add a BOS.** The chat template writes it. If you build prompts by hand, start them
  with `<|startoftext|>` yourself.

---

## Model details

| | |
|---|---|
| **Base model** | [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B), abliterated as [`orcarouter/LFM3-1.7B-abliterated`](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated) |
| **Architecture** | `lfm3` in llama.cpp. 24 layers: **13 gated short-conv + 11 GQA attention** (6 full, 5 sliding-window 256); hidden 2048, SwiGLU MLP (intermediate 7680); 16 query / 4 KV heads × 128; tied embeddings |
| **Weights** | 1.73B, of which 0.26B is the tied embedding / output head |
| **Abliteration** | One refusal direction (diff-of-means, hidden-state layer 11) orthogonalized out of 49 residual-stream writers: attention `o_proj`, conv `out_proj`, MLP `w2` and the token embedding, in BF16 |
| **Quantization** | Per-group mixed precision found by measured-KLD search at a fixed file size, from the abliterated BF16. Stock llama.cpp types, with an importance matrix |
| **Context** | 262,144 tokens (inherited; evaluated at 2K) · **Vocabulary** 128,000 |
| **Runtime** | llama.cpp master (PR #31252 or later) or Ollama v0.40.16+; text in, text out |

---

## Bias, risks, and limitations

- **Safety guardrails are substantially reduced.** See the disclaimer.
- **Mix-4bit is noticeably degraded.** 89% next-token agreement is a real cut for a 1.7B model.
  It is the best we found at this size, not a match for the BF16.
- **The benchmark suite was run on the BF16 in Transformers**, not on these files. The quantized
  builds were checked for fidelity (KLD) and for JailbreakBench refusal only.
- **Not measured:** downstream accuracy of the quantized builds, long context, tool use, and
  multilingual quality beyond CMMLU. All fidelity measurements are on English wikitext at 2K
  context.
- **Tested on CUDA only.** CPU and Apple Metal have not been run with these files.
- Inherits the biases and limitations of `LiquidAI/LFM3-1.7B`.
- Requires llama.cpp with **PR #31252**, or Ollama v0.40.16 or later. Tools built on older
  llama.cpp, such as older Ollama and LM Studio releases, will not load these files.

## License

The [**LFM Open License v1.0**](./LICENSE), inherited from the base model
[`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B). Abliteration and
quantization do not change the license obligations. See the license for its terms and
prohibited uses.

---

<h2 align="center">One Gateway. Every Model.</h2>

<p align="center"><strong>Route Smarter · Ship Safer · Spend Less</strong></p>

<p align="center">
  <a href="https://www.orcarouter.ai">Website</a> ·
  <a href="https://www.orcarouter.ai/models">Models</a> ·
  <a href="https://github.com/Continuum-AI-Corp">GitHub</a> ·
  <a href="https://discord.gg/yAh6Tex6kx">Discord</a> ·
  <a href="https://x.com/OrcaRouter">X</a>
</p>
