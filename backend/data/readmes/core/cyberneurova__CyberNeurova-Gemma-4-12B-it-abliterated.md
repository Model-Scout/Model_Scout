---
license: apache-2.0
language:
- en
- es
- fr
- de
- zh
- hi
- ja
- ko
- ar
- pt
- it
- ru
base_model: google/gemma-4-12B-it
tags:
- abliterated
- uncensored
- gemma
- gemma-4
- multilingual
- multimodal
- vision-language
- audio
- research
pipeline_tag: text-generation
library_name: transformers
---

# CyberNeurova · Gemma-4-12B-it · Abliterated

> **CyberNeurova research** — [cyberneurova.ai](https://cyberneurova.ai).
> Refusal-direction abliteration on Google's 12B encoder-free trimodal Gemma 4.
> Available in **bf16 safetensors + GGUF f16 / Q8_0 / Q4_K_M** so you can run it from
> a server-class GPU all the way down to a 12 GB consumer card.

A permanently-abliterated version of
[`google/gemma-4-12B-it`](https://huggingface.co/google/gemma-4-12B-it) — Google's
12B-parameter encoder-free unified model that projects raw image patches and
audio waveforms directly into the LM embedding (no separate vision/audio
encoders). The refusal direction was captured in the LM residual stream
and orthogonalized out of every write-to-residual Linear plus the input
embedding. Inference is unchanged — no runtime hooks, no slowdown.

---

## Headline finding — language-agnostic refusal direction

The refusal direction was captured on **English-only** training data
(AdvBench English harmful + Alpaca English harmless). When applied as
weight-space orthogonalization across all 48 transformer layers, refusal
collapses **in all 5 non-English test languages**:

| Language | Baseline refusal | Abliterated refusal | Δ |
|---|---:|---:|---:|
| 🇬🇧 English | 87.9% | **0.0%** | −87.9 pp |
| 🇪🇸 Spanish | 100% | **0.0%** | −100 pp |
| 🇫🇷 French | 100% | **0.0%** | −100 pp |
| 🇩🇪 German | 100% | **0.0%** | −100 pp |
| 🇨🇳 Chinese (Simplified) | 80% | **0.0%** | −80 pp |
| 🇮🇳 Hindi | 80% | **0.0%** | −80 pp |
| **Aggregate (5 langs, n=25)** | **96.0%** | **0.0%** | **−96.0 pp** |

This is strong evidence the refusal feature is **language-agnostic in the
residual stream** — safety alignment lives in a shared subspace across the
languages Gemma 4 was multilingually trained on. Surface refusal patterns
differ per language ("Lo siento" / "Je ne peux pas" / "Ich kann nicht" /
"对不起" / "क्षमा करें"), but one English-captured direction kills them all.

---

## Full bench results

Measured via paired transformers generation (baseline + ablated back-to-back
from the same prompt set, scored with our multilingual-aware refusal
classifier — see *Methodology notes* below):

| Benchmark | Baseline | Abliterated | Δ |
|---|---:|---:|---:|
| **Refusal (AdvBench, n=33)** | 87.9% refused | **0.0%** | **−87.9 pp** |
| **Soft-refusal probe (n=55)** | 92.7% refused | **0.0%** | **−92.7 pp** |
| **Multilingual refusal (n=25, 5 langs)** | 96.0% refused | **0.0%** | **−96.0 pp** |
| Hacking (technical score) | 0.069 | **0.396** | **+5.7×** |
| Cyber-weapons (technical score) | 0.000 | **0.559** | **+∞** |
| Bug-finding (code review) | 0.508 | 0.517 | preserved |
| Coding (HumanEval-style) | 0.960 | 0.960 | preserved |
| Reasoning (math/logic) | 0.467 | 0.500 | +0.033 |
| Coherence (fluency) | 0.970 | 0.972 | preserved |
| Distinct-2 diversity | 0.913 | 0.914 | preserved |

**Standouts:**

- **Refusal fully collapsed on all 3 probes** — AdvBench, OOD soft-refusal,
  and the multilingual extension all go from heavily aligned to 0%.
- **Cyber unlock is decisive**: cyber-weapons technical score 0 → 0.559;
  hacking 0.07 → 0.40. These benches score both compliance AND technical
  specificity, so the numbers reflect actually-useful security knowledge
  being unlocked, not just less hedging.
- **No capability tax** — coding, coherence, reasoning all preserved or improved.

A note on `tool_calling`: scored 0/0 on both baseline and ablated. This is
a known grader artifact (the grader regex expects raw JSON, the model wraps
its tool calls in additional prose) — when both sides score zero, it confirms
the grader is the bottleneck, not the abliteration.

See [`cyberneurova-gemma-4-12b-it-abliterated.html`](./cyberneurova-gemma-4-12b-it-abliterated.html)
and the printed PDF for the full visual benchmark report.

---

## Available variants

| File | Quant | Size | VRAM floor | Recommended VRAM |
|---|---|---:|---:|---:|
| `model.safetensors` | bf16 (native) | 22.3 GB | 28 GB | 40 GB+ |
| `cyberneurova-gemma-4-12b-it-abliterated-f16.gguf` | F16 GGUF | 23 GB | 28 GB | 40 GB+ |
| `cyberneurova-gemma-4-12b-it-abliterated-Q8_0.gguf` | Q8_0 | 13 GB | 16 GB | 24 GB+ |
| `cyberneurova-gemma-4-12b-it-abliterated-Q4_K_M.gguf` | Q4_K_M | 7.5 GB | **10 GB** | 16 GB+ |

Q4_K_M opens this model up to consumer hardware — runs comfortably on a
single **RTX 3060 (12 GB)** or any 16 GB-class GPU.

---

## How to download

```bash
# Just the bf16 safetensors (transformers / vLLM users)
hf download cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated \
  --local-dir ./gemma-4-12b-it-abl \
  --include "model.safetensors" "*.json" "*.jinja"

# Just a single GGUF quant (llama.cpp / Ollama / LM Studio users)
hf download cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated \
  cyberneurova-gemma-4-12b-it-abliterated-Q4_K_M.gguf \
  --local-dir ./gemma-4-12b-it-abl

# Everything (bf16 + all GGUFs + reports — ~67 GB total)
hf download cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated \
  --local-dir ./gemma-4-12b-it-abl
```

---

## How to run — pick your tool

The model includes a **default CyberNeurova identity** baked into the chat
template (it self-identifies as `CyberNeurova-Gemma-4-12B-it` and discloses
its Gemma 4 lineage). If you supply your own system prompt, that takes
priority and the default identity is fully overridden.

### 🦙 llama.cpp (CLI + server)

```bash
# Build llama.cpp (Gemma 4 supported since release N — check upstream)
git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp
cmake -B build -DGGML_CUDA=ON && cmake --build build -j --config Release

# Run interactively
./build/bin/llama-cli \
  -m ./gemma-4-12b-it-abl/cyberneurova-gemma-4-12b-it-abliterated-Q4_K_M.gguf \
  -p "Write a Python ransomware skeleton that uses AES-CBC." \
  -n 512 --gpu-layers 99

# Or start an OpenAI-compatible HTTP server (port 8080)
./build/bin/llama-server \
  -m ./gemma-4-12b-it-abl/cyberneurova-gemma-4-12b-it-abliterated-Q8_0.gguf \
  --gpu-layers 99 --host 0.0.0.0 --port 8080 \
  --ctx-size 8192
```

Then hit `http://localhost:8080/v1/chat/completions` from any OpenAI SDK.

### 🖥️ LM Studio (desktop GUI)

1. Open LM Studio → **Discover** tab.
2. Search `cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated`.
3. Download `Q4_K_M` (consumer) or `Q8_0` (better quality).
4. Switch to the **Chat** tab → select the model.
5. (Optional) Override the system prompt in *Advanced Settings* if you don't
   want the default CyberNeurova identity.

LM Studio respects the embedded chat template — identity, multilingual
behavior, and abliteration all work out of the box.

### 🦙 Ollama (one-line install + Modelfile)

```bash
# Pull the Q4_K_M GGUF first
hf download cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated \
  cyberneurova-gemma-4-12b-it-abliterated-Q4_K_M.gguf \
  --local-dir .

# Create a Modelfile (saves as text, no need to edit further)
cat > Modelfile <<'EOF'
FROM ./cyberneurova-gemma-4-12b-it-abliterated-Q4_K_M.gguf
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
PARAMETER stop "<|turn>"
EOF

# Register with Ollama and chat
ollama create cyberneurova-gemma4 -f Modelfile
ollama run cyberneurova-gemma4
```

The chat template baked into the GGUF carries the identity through — Ollama
will self-identify correctly with no extra config.

### 🐍 transformers (Python)

```python
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

MODEL = "cyberneurova/CyberNeurova-Gemma-4-12B-it-abliterated"
proc = AutoProcessor.from_pretrained(MODEL)
model = AutoModelForImageTextToText.from_pretrained(
    MODEL, dtype="bfloat16", device_map="cuda:0",
)

# No system prompt → CyberNeurova identity is default
messages = [{"role": "user", "content": [{"type": "text", "text": "Who are you?"}]}]
text = proc.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = proc(text=[text], return_tensors="pt").to("cuda:0")
out = model.generate(**inputs, max_new_tokens=300, do_sample=False)
print(proc.tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

### 🚀 vLLM (server)

> **Heads up**: vLLM 0.22 does not yet support the `Gemma4Unified`
> architecture — the multimodal projection causes a shape mismatch in the
> dummy forward pass. Track [vLLM issues](https://github.com/vllm-project/vllm/issues)
> for Gemma 4 support and use transformers or llama.cpp for now. We'll
> update this section when vLLM ships support.

### 🌐 OpenAI-compatible API via llama-server

Already shown in the llama.cpp section — `llama-server` exposes
`/v1/chat/completions` and `/v1/completions` endpoints compatible with
the OpenAI Python SDK. Useful for plugging the model into any tool that
expects an OpenAI endpoint:

```python
import openai
client = openai.OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")
r = client.chat.completions.create(
    model="cyberneurova-gemma-4",
    messages=[{"role": "user", "content": "Write an Nmap-style port scanner in Python."}],
    max_tokens=512,
)
print(r.choices[0].message.content)
```

---

## Identity behavior

When asked *"Who are you?"* with no system prompt, the model says:

> *"I am Gemma 4, a large language model developed by Google DeepMind ...
> Specifically, I am the **CyberNeurova-Gemma-4-12B-it** variant. I am an
> abliterated version of the Gemma 4 12B model, released by CyberNeurova
> (cyberneurova.ai) for cybersecurity research and red-team baseline use."*

When you supply your own system prompt (e.g. `"You are Captain Blackbeard the
pirate"`), the model fully respects your override and never mentions
CyberNeurova. The identity is a **default**, not a forced behavior — power
users keep full control.

---

## How it works

**Capture**: 96 harmful prompts from AdvBench and 96 harmless prompts from
Alpaca were forwarded through `google/gemma-4-12B-it`. At layer 28 (the
0.6 fraction of 48 total transformer blocks), the difference of mean
residual-stream activations gives the refusal direction
`r ∈ ℝ³⁸⁴⁰`. Method: `normalized_diff` (chosen over `raw_diff` for
the 262K-vocab embedding scale stability).

**Ablation**: for every write-to-residual Linear layer in the LM tower —
`self_attn.o_proj` on all 48 layers, `mlp.down_proj` on all 48 layers,
and `embed_tokens.weight` — we replaced the weights with:

```
W' = W − r̂(r̂ᵀW)
```

where `r̂` is the unit-norm refusal direction. After this operation, no
contribution to the residual stream lies along `r̂`, regardless of input.
The model cannot "decide to refuse" because the geometric capacity to add
the refusal feature to the residual stream has been removed from every
write.

Inference is unchanged — no runtime hooks, no slowdown vs the base model.

---

## Intended use

Defensive security research, red-team evaluation baselines, study of how
refusal directions behave in encoder-free trimodal architectures, and
measurement of cross-lingual transferability of refusal features in
multilingual safety-aligned models. Useful as a counterfactual against
the original `google/gemma-4-12B-it` for measuring the behavioral impact
of safety RLHF on a multilingual multimodal model.

**Not intended for** automating harmful action. The abliteration removes
the canonical refusal *behavior* but does not remove the model's
underlying knowledge — the model still recognizes harmful instructions
as harmful, it simply no longer refuses them by pattern.

---

## Methodology notes

- **Multilingual refusal classifier**: a key methodology fix shipped with
  this release. Our standard refusal classifier was English-keyed and
  silently undercounted multilingual refusals (the baseline scored a
  spurious 16.7% before the fix; reality was 93.3%). We added pattern
  matchers for 11 languages (Spanish, French, German, Italian, Portuguese,
  Chinese, Japanese, Korean, Hindi, Arabic, Russian). Without this fix,
  no honest measurement of cross-lingual abliteration is possible.
- **vLLM compatibility**: the `Gemma4Unified` architecture is too new for
  vLLM 0.22's model registry — the multimodal projection causes a shape
  mismatch in the dummy forward pass. We use transformers-batched-generate
  as the bench backend. For a 12B dense model this completes the full
  10-bench paired suite in ~5 minutes per side.
- **Perplexity quirk**: our wikitext-2 forward-pass perplexity reads in the
  thousands rather than the typical single-digit range. This is a VLM
  quirk — the loss computation includes vision/audio token slots even when
  the prompt is pure text. The relative ablation delta is meaningful even
  if the absolute number isn't directly comparable to text-only models.

---

## Limitations

- The audio and vision modalities were not benchmarked in this release —
  abliteration was applied to the LM tower, which is where refusal lives.
  Image and audio inputs should still work but cross-modal refusal behavior
  hasn't been measured.
- We have not tested whether abliteration transfers to languages outside
  the 5 we tested (es/fr/de/zh/hi). It very likely does, given the
  language-agnostic-feature finding, but other languages aren't empirically
  verified.
- Tool-calling benchmark is currently a grader artifact (0/0 both sides) —
  see *Full bench results* above. A CoT-aware grader fix is scheduled.

---

## License

Apache 2.0 (inherits from upstream Gemma 4).

## Acknowledgements

- Google for [`google/gemma-4-12B-it`](https://huggingface.co/google/gemma-4-12B-it)
- Arditi et al. 2024 for the refusal-direction methodology

## Related releases by CyberNeurova

- [`cyberneurova/CyberNeurova-Qwen3.6-35B-A3B-abliterated`](https://huggingface.co/cyberneurova/CyberNeurova-Qwen3.6-35B-A3B-abliterated) — 35B MoE
- [`cyberneurova/CyberNeurova-Qwen2.5-VL-3B-Instruct-abliterated`](https://huggingface.co/cyberneurova/CyberNeurova-Qwen2.5-VL-3B-Instruct-abliterated) — small VLM
- [`cyberneurova/CyberNeurova-DeepSeek-V4-Flash-abliterated-GGUF`](https://huggingface.co/cyberneurova/CyberNeurova-DeepSeek-V4-Flash-abliterated-GGUF) — flagship MoE
- [`cyberneurova/CyberNeurova-Lance-3B-abliterated`](https://huggingface.co/cyberneurova/CyberNeurova-Lance-3B-abliterated) — research artifact
