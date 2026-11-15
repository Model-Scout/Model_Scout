---
license: other
license_name: mistral-ecosystem-open-weight-license
license_link: LICENSE
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - ja
  - ko
  - ru
  - zh
  - ar
pipeline_tag: text-generation
library_name: gguf
base_model: mistralai/Mistral-Large-4-1T-A52B
base_model_relation: quantized
tags:
  - gguf
  - llama.cpp
  - local
  - mistral
  - mistral-large-4
  - moe
  - mixed-precision
  - imatrix
  - reasoning
---

<p align="center">
  <a href="https://www.orcarouter.ai">
    <img src="https://www.orcarouter.ai/orca-logo-classic.png" width="96" alt="OrcaRouter">
  </a>
</p>

<h1 align="center">Mistral-Large-4-1T-A52B GGUF</h1>

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
<p>🔌 <strong>New from Orca &mdash; <a href="https://www.orcarouter.ai/solutions/orca-connect">Orca Connect</a></strong></p>
<p>Running this GGUF in llama.cpp or Ollama? <strong>Orca Connect</strong> puts the rig under your desk behind your usual OrcaRouter API key, next to 200+ hosted models, reachable from a laptop, a phone or a cloud agent. Outbound only: no port forwarding, no tunnel, no firewall rule. <strong>Requests your own hardware serves cost $0</strong>, and <code>orca-connect claude</code> points Claude Code at your rig for one session.</p>
<video src="https://huggingface.co/spaces/orcarouter/README/resolve/main/assets/orca-connect.mp4" controls autoplay muted loop playsinline width="100%"></video>
<p><a href="https://www.orcarouter.ai/solutions/orca-connect"><img src="https://img.shields.io/badge/Connect%20your%20rig%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Connect your rig"></a></p>
</td>
</tr>
</table>
<!-- orcacyber-promo:end -->

<p align="center"><strong>The 1-trillion-parameter Mistral Large 4, in 256 GB or 512 GB of memory.</strong></p>

<p align="center"><strong>233 GB and 492 GB builds · lower KL divergence than unsloth's UD files of the same size · llama.cpp</strong></p>

<p align="center">
  <a href="https://www.orcarouter.ai"><strong>OrcaRouter AI Gateway</strong></a> ·
  <a href="https://x.com/OrcaRouter"><strong>X</strong></a> ·
  <a href="https://discord.gg/yAh6Tex6kx"><strong>Discord</strong></a> ·
  <a href="https://github.com/Continuum-AI-Corp"><strong>GitHub</strong></a> ·
  <a href="https://www.orcarouter.ai/models"><strong>All Models</strong></a>
</p>

---

> ## The full Mistral Large 4, run locally.
>
> These are GGUF builds of [`Mistral-Large-4-1T-A52B`](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B).
> It is a 1T-parameter MoE with 128 routed experts (top-4) and one shared expert, 52B active per
> token. It uses MLA attention, DeepSeek-style sparse attention (top-2048) and a 1M-token context.
>
> Routed experts are 98% of the weights, so that is where the bits were spent. Each group of
> expert layers got its own precision from **measured** KL divergence, not from a hand-set rule.
>
> **At the same file size, both builds sit closer to the original than unsloth's UD-IQ1_S and
> UD-Q3_K_XL:** 20% lower KLD at 233 GB, 13% lower at 492 GB, on held-out text the search never saw.
>
> **Vision and speculative decoding included.** The vision projector (`mmproj`) adds image input, and
> Mistral's DSpark drafter makes generation 1.4–1.5× faster.

---

## Pick a build

| Build | In memory | Download | Experts | KLD ↓ | Top-1 ↑ | PPL vs. original |
|---|---:|---:|---:|---:|---:|---:|
| **[`Mix-256G`](./Mix-256G)** | **232.9 GB** | 232.9 GB | 1.72 bpw | 0.0975 | 91.6% | +8.7% |
| **[`Mix-512G`](./Mix-512G)** | **492.2 GB** | 492.2 GB | 3.72 bpw | 0.0129 | 96.9% | +0.75% |

- **Mix-512G fits a 512 GB machine.** That covers a 512 GB Mac, a 512 GB server running on CPU, or
  4 × H200. It is close to the original: 97% of next tokens match, and perplexity
  is 0.75% higher.
- **Mix-256G fits a 256 GB machine.** That covers a 256 GB Mac, a 256 GB PC on CPU, or 2 × H200.
  It averages under 2 bits per expert weight, which costs quality: 92% of next tokens match, and
  perplexity is 8.7% higher.

Use Mix-512G if you have the memory. Use Mix-256G to run the full model on half of it.

---

## Evaluation

All builds are scored against a **Q8_0 GGUF of the official FP8 checkpoint**, using llama.cpp's
full-vocabulary KLD.

The text is **Mistral Large 4's own answers**. Prompts come from four sources:
- English chat (UltraChat 200k)
- non-English chat (WildChat)
- code (Magicoder OSS-Instruct)
- math reasoning (OpenR1-Math)

The Q8_0 model answered each one, sampled as the model card recommends (temperature 1.0, top_p
0.95), with reasoning effort drawn per prompt from low / medium / high. Each conversation was
rendered through the chat template with its reasoning as a `[THINK]` block. KLD is counted on the
**assistant tokens**, reasoning and answer, over 64 windows of 2048 tokens. Truncated answers were
dropped. The precision search used a separate draw and never saw this text.

Each build is compared with **unsloth's dynamic GGUF of the same size**, from
[unsloth/Mistral-Large-4-1T-A52B-GGUF](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF).
Their published files were downloaded and scored with the same text, teacher and llama.cpp build.

| | In memory | KLD ↓ | KLD p99 ↓ | Top-1 ↑ | PPL vs. original |
|---|---:|---:|---:|---:|---:|
| **Mix-256G** (this repo) | **232.9 GB** | **0.0975** | **1.41** | **91.61%** | **+8.7%** |
| unsloth `UD-IQ1_S` | 233.0 GB | 0.1220 | 1.82 | 90.84% | +10.9% |
| **Mix-512G** (this repo) | **492.2 GB** | **0.01285** | **0.193** | **96.93%** | **+0.75%** |
| unsloth `UD-Q3_K_XL` | 492.8 GB | 0.01482 | 0.219 | 96.81% | +0.81% |

**At the same size**, Mix-256G has **20% less KL divergence** than UD-IQ1_S, and Mix-512G has
**13% less** than UD-Q3_K_XL. Both are also a little smaller, and both win in the tail (KLD p99).

> **Why the model's own text.** Mistral Large 4 always reasons before it answers. On other
> models' answers (no reasoning block, someone else's style) it makes confident misses on ~3% of
> tokens even at Q8_0, and which of those misses a quant happens to flip dominated the KLD. The
> same applies to the user turns, which are human-written. So the score covers what the model
> itself writes.
>
> **Method note.** These are full-vocabulary KLD and next-token agreement at 2k context, not a
> downstream benchmark.

---

## How the precision was chosen

The budget is set on the bytes that have to fit in memory: 233.0 GB for Mix-256G (the size of
UD-IQ1_S) and 492.7 GB for Mix-512G (the size of UD-Q3_K_XL).

1. **Measure.** For every group of tensors, the search measures the real KLD of moving it one
   precision level up and one level down. Groups are as follows:
   - **routed experts:** one projection (gate, up or down) over three layers
   - **attention:** `q`, `output`, `v_b` and the sparse-attention indexer's `q_b`, one group each
     over all layers
   - **shared expert:** `gate`, `up` and `down`, one group each
   - **leading dense FFN:** layer 0
   - **embedding and output head:** one group each

   Each measurement runs llama.cpp's own kernels on 32 (Mix-512G) or 64 (Mix-256G) windows of
   2048 tokens of the model's own text.
2. **Choose.** A knapsack picks the combination of moves that fits the budget exactly.
3. **Accept.** Only steps whose candidate KLD was actually measured lower are kept.

Mix-256G puts its bits as follows:

| Part | Type |
|---|---|
| Routed experts `gate` | IQ1_S; IQ2_XXS on layers 46–51 and 61–66, IQ1_M on 3 layer triples |
| Routed experts `up` | IQ1_S; IQ1_M on 6 layer triples, IQ2_XXS on 2 |
| Routed experts `down` | IQ2_XS on layers 43–51, IQ2_XXS on layers 37–42 and 52–66, IQ1_M on layers 22–33, IQ1_S elsewhere |
| Attention `q` / `output` / `v_b` / indexer `q_b` | IQ4_XS / Q4_K / Q5_K / IQ4_XS |
| Shared expert `gate` / `up` / `down` | Q4_K / IQ4_XS / Q4_K |
| Dense FFN (layer 0) | Q5_K |
| Token embedding / output head | Q3_K / Q5_K |

Mix-512G puts its bits as follows:

| Part | Type |
|---|---|
| Routed experts `gate` | IQ3_S, with 7 of 24 layer triples at IQ4_XS |
| Routed experts `up` | IQ3_S, with 7 of 24 layer triples at IQ4_XS |
| Routed experts `down` | IQ4_XS on layers 13–15 and 43–71, IQ3_S elsewhere |
| Attention `q` / `output` / `v_b` / indexer `q_b` | Q5_K / Q5_K / Q6_K / Q4_K |
| Shared expert | Q5_K |
| Dense FFN (layer 0) | Q4_K |
| Token embedding / output head | Q5_K / Q5_K |

In both builds, the MLA `kv_a` / `k_b` projections and the indexer's `k` projection stay Q8_0,
and the router, norms and SSMax parameters stay F32 (0.75 GB in all).

The importance matrix comes from ~740k tokens of the exllamav3 calibration mix:
- web text (C4)
- code
- multilingual text
- technical text
- Wikipedia
- tiny stories
- random token rows

None of it overlaps the evaluation text.

---

## What's in this repo

| Path | Size | Contents |
|---|---:|---|
| `Mix-256G/…-00001-of-00006.gguf` … `00006` | 232.9 GB | the 256 GB build |
| `Mix-512G/…-00001-of-00012.gguf` … `00012` | 492.2 GB | the 512 GB build |
| `mmproj-Mistral-Large-4-1T-A52B-BF16.gguf` | 3.4 GB | the vision projector, for image input |
| `Mistral-Large-4-1T-A52B-DSpark-Q8_0.gguf` | 2.2 GB | the DSpark draft model, for speculative decoding |
| `imatrix.gguf` | 1.4 GB | the importance matrix the builds were quantized with |

Mix-256G is split into 6 parts and Mix-512G into 12, each under 45 GB. The chat
template is embedded in each build.

The vision projector and the DSpark drafter both come from the official checkpoint. The projector
is kept at BF16. The drafter is Mistral's 3-layer DSpark head, which proposes 3 tokens at a time
and is stored at Q8_0. Both work with either build.

---

## Serving (llama.cpp)

Mistral Large 4 support landed in llama.cpp master with
[ggml-org/llama.cpp#31376](https://github.com/ggml-org/llama.cpp/pull/31376) (commit `78feec0`).
These files were made and tested at master commit `e0f142d`:

```bash
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
git checkout e0f142d   # or any later master
cmake -B build -DGGML_CUDA=ON && cmake --build build -j --target llama-server llama-cli
# Mac: cmake -B build (Metal is on by default) · CPU only: cmake -B build

hf download orcarouter/Mistral-Large-4-1T-A52B-GGUF --include "Mix-256G/*" "mmproj-*" "*DSpark*" \
  --local-dir ./ml4-gguf

# 2 x H200 (Mix-256G) -- llama.cpp spreads the layers across the GPUs by free memory
llama-server -m ml4-gguf/Mix-256G/Mistral-Large-4-1T-A52B-Mix-256G-00001-of-00006.gguf \
  -c 32768 --jinja -fitt 4096

# 4 x H200 (Mix-512G)
llama-server -m ml4-gguf/Mix-512G/Mistral-Large-4-1T-A52B-Mix-512G-00001-of-00012.gguf \
  -c 32768 --jinja

# 2 x H200 (Mix-256G) with image input and DSpark speculative decoding; the same two flags work with Mix-512G
llama-server -m ml4-gguf/Mix-256G/Mistral-Large-4-1T-A52B-Mix-256G-00001-of-00006.gguf \
  -c 32768 --jinja -fitt 4096 \
  --mmproj ml4-gguf/mmproj-Mistral-Large-4-1T-A52B-BF16.gguf \
  -md ml4-gguf/Mistral-Large-4-1T-A52B-DSpark-Q8_0.gguf --spec-type draft-dspark --spec-draft-n-max 3

# CPU only, 256 GB RAM (not tested)
llama-server -m ml4-gguf/Mix-256G/Mistral-Large-4-1T-A52B-Mix-256G-00001-of-00006.gguf \
  -ngl 0 -c 16384 --jinja
```

- **Reasoning is always on.** Pick the effort per request with
  `"chat_template_kwargs": {"reasoning_effort": "low" | "medium" | "high"}` (default `high`). The
  reasoning comes back in `message.reasoning_content`, and the answer in `message.content`.
- **Sampling.** Mistral recommends `temperature=1.0`, `top_p=0.95` for every reasoning effort.
  The files carry these as their default sampling metadata.
- **Point llama.cpp at the `00001` part.** It finds the other parts.
- **Mix-256G on exactly 2 x H200.** Keep `-fitt 4096`. With the default 1 GB margin per GPU, the
  first long prompt can run out of GPU memory.
- **Images.** With `--mmproj`, send OpenAI-style `image_url` content parts (base64 data URLs work).
  On both builds, the model read a newspaper front page (publication, date and headline) and counted
  and named the shapes and text in a synthetic image correctly, with and without DSpark.
- **DSpark.** The draft proposes 3 tokens per step and the main model checks them, so every token is
  still the main model's choice. At temperature 0, outputs are not bit-identical to plain decoding:
  checking a block in one batch changes the arithmetic slightly, so near-ties can break the other way.
- **Mac.** macOS lets the GPU wire only about 75% of RAM by default. Raise the limit before loading
  on Metal, for example `sudo sysctl iogpu.wired_limit_mb=500000` for Mix-512G on a 512 GB Mac,
  and close other apps.

Measured with llama-bench (512-token prompt, 128 generated tokens, one request at a time):

| Build | Hardware | Prompt | Generation |
|---|---|---:|---:|
| Mix-256G | 2 x H200 (CUDA) | ~320 tok/s | ~36 tok/s |
| Mix-512G | 4 x H200 (CUDA) | ~360 tok/s | ~33 tok/s |

With the DSpark drafter, measured through llama-server on six prompts (code, explanation, math,
story, translation, SQL), up to 1024 generated tokens each, low reasoning effort, one request at a time:

| Build | Hardware | Without DSpark | With DSpark | Speed-up | Draft tokens accepted |
|---|---|---:|---:|---:|---:|
| Mix-256G | 2 x H200 (CUDA) | 35.4 tok/s | 51.5 tok/s | 1.45× | 69% |
| Mix-512G | 6 x H200 (CUDA) | 31.8 tok/s | 44.4 tok/s | 1.40× | 67% |

The gain depends on the text: 1.2–1.4× on long prose (the story and the explanation), 1.6–1.7× on
code and math.
CPU and Apple Metal speeds have not been measured yet.

---

## Serving (Ollama)

Both builds are on Ollama as
[`orcarouter/Mistral-Large-4-1T-A52B`](https://ollama.com/orcarouter/Mistral-Large-4-1T-A52B),
with the BF16 vision projector included. This needs Ollama v0.40.16 or later:

```bash
ollama run orcarouter/Mistral-Large-4-1T-A52B            # Mix-256G
ollama run orcarouter/Mistral-Large-4-1T-A52B:mix-512g
```

| Tag | Build | Size |
|---|---|---:|
| `latest`, `mix-256g` | Mix-256G | 236.4 GB |
| `mix-512g` | Mix-512G | 495.6 GB |

- **Reasoning is always on**, and `"think": false` does not turn it off. The reasoning comes back in
  `message.thinking`, the answer in `message.content`.
- **Images** go in the `images` field of a message, or as a file path in the prompt with `ollama run`.
- **No DSpark.** The Ollama builds don't include the draft model, so generation runs at plain-decoding
  speed.
- Mix-256G was run in Ollama (chat, reasoning and an image). Mix-512G was built the same way but not
  run there.

---

## Model details

| | |
|---|---|
| **Base model** | [`mistralai/Mistral-Large-4-1T-A52B`](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) |
| **Architecture** | `mistral-large4` in llama.cpp. 72 layers, hidden 6144, 64 heads, **MLA** (kv rank 512), **sparse attention** with a lightning indexer (top-2048), NoPE on every 4th layer, KV sharing in the later layers, 1 leading dense layer, **128 routed experts top-4** + 1 shared expert |
| **Weights in these files** | 1.05T: 1.03T routed experts, 20B attention / shared expert / dense / embeddings / head. 4 of 128 experts active per token |
| **Quantization** | Per-group mixed precision found by measured-KLD search, from a Q8_0 conversion of the official FP8 weights. Experts are IQ1_S–IQ2_XS (Mix-256G) or IQ3_S–IQ4_XS (Mix-512G). Uses an importance matrix. |
| **Context** | 1,048,576 tokens (inherited; evaluated at 2k) · **Vocabulary** 204,800 |
| **Runtime** | llama.cpp master (PR #31376 or later), or Ollama v0.40.16+ (see Serving (Ollama)); text and images in (with `mmproj`), text out; DSpark speculative decoding (`--spec-type draft-dspark`) |

---

## Bias, risks, and limitations

- **Mix-256G is noticeably degraded.** Under 2 bits per expert weight is a large cut for any
  model. It is the best we found at this size, not a match for the original.
- **Tested on CUDA only.** CPU and Apple Metal have not been run with these files yet.
- Vision was checked on a few images, not benchmarked. Long-context behaviour was not tested: all
  measurements are at 2k context or on short chats.
- Inherits the biases and limitations of `Mistral-Large-4-1T-A52B`.
- Requires llama.cpp with **PR #31376** (master `78feec0` or later). Tools built on older
  llama.cpp, such as older Ollama and LM Studio releases, will not load these files. Ollama v0.40.16
  and later do (see Serving (Ollama)).

## License

The [**Mistral Ecosystem Open-Weight License**](./LICENSE), inherited from the base model
[`mistralai/Mistral-Large-4-1T-A52B`](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B). It is
a modified MIT license that allows commercial and non-commercial use. Operating a
Model-as-a-Service business with the model requires a separate commercial license from Mistral. See
the license for the terms.

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
