---
language:
  - en
  - ko
license: apache-2.0
tags:
  - gguf
  - moe
  - function-calling
  - tool-use
  - quantized
  - batiai
  - korean
base_model: trillionlabs/Gravity-30BA5B-RL
pipeline_tag: text-generation
library_name: llama.cpp
---

# Gravity 30B-A5B RL — GGUF by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-on--device%20AI-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://huggingface.co/trillionlabs/Gravity-30BA5B-RL"><img src="https://img.shields.io/badge/source-Trillion%20Labs-purple?style=for-the-badge" alt="Trillion Labs"></a>
  <img src="https://img.shields.io/badge/license-Apache%202.0-brightgreen?style=for-the-badge" alt="Apache 2.0">
</p>

> ### A tool-calling MoE that fits a laptop. 30B total, 5B active.
> First GGUF conversion of this model. Korean output and tool calling verified on every quant —
> and one conversion bug fixed so the files load with no extra flags.

---

## 📦 Sizes and measured speed

| Quant | Size | Generation (tg16) | Fits |
|-------|------|-------------------|------|
| `Q6_K` | 24.7 GiB (26.6 GB) | 20.03 tok/s | 48 GB+ |
| **`Q4_K_M`** ⭐ | 18.3 GiB (19.6 GB) | **24.98 tok/s** | 32 GB Mac |
| `IQ4_XS` | 15.0 GiB (16.1 GB) | **26.35 tok/s** | 24–32 GB Mac |
| **`IQ3_XXS`** | 12.2 GiB (13.1 GB) | **30.84 tok/s** | **16 GB Mac** |

<sub>`llama-bench -ngl 0 -n 16 -r 1` on 2× Intel Xeon Gold 6442Y (48 cores / 96 threads).
**CPU only, no GPU offload** — the floor, not a best case. Apple Silicon numbers go up
substantially; we publish those only once measured on the actual hardware.</sub>

Only ~5B of 30B parameters are active per token (64 experts, top-8, MLA attention), which is why
a 30B model generates at 25 tok/s on CPU alone — and why **the smaller file is the faster one** all
the way down. You are bandwidth-bound on the active slice, not compute-bound on dequantization.

**Which to pick.** We star `Q4_K_M` because K-quants at 4 bits are the best-understood quality
point and it still fits a 32 GB machine. If you have 16–24 GB, `IQ3_XXS` passed the same Korean and
tool-call checks and is 6.5 GiB smaller — we did not measure a quality gap between them, and we are
not going to claim one we did not measure.

## ✅ Verified

Every quant, including the lowest:

| Quant | Korean | Han / kana | Tool call |
|---|---|---|---|
| `Q6_K` | 70.7% Hangul | **0 / 0** | ✅ |
| `Q4_K_M` | 63.3% Hangul | **0 / 0** | ✅ |
| `IQ4_XS` | 70.5% Hangul | **0 / 0** | ✅ |
| **`IQ3_XXS`** | **71.4% Hangul** | **0 / 0** | ✅ |

All four parse tool calls as standard JSON and carry `general.author: BatiAI`.

<details><summary>Captured Korean output (IQ3_XXS — the lowest tier)</summary>

````
서울은 한국의 수도이자 문화·경제·정치 중심지로, 현대적인 고층 빌딩과 전통적인 사찰이
조화를 이루는 역동적인 도시입니다.
김치는 한국의 대표적인 발효 식품으로, 배추와 무 등을 양념에 버무려 오랜 기간 숙성시켜
풍부한 유산균과 독특한 맛을 자랑합니다.
비빔밥은 여러 가지 나물과 고기, 쌀밥을 한...
````

</details>

**`IQ3_XXS` is where we looked hardest.** It is the tier that fits a 16 GB Mac, and at 3 bits
Korean is where damage shows up before anything else. It came through clean — and it is also the
fastest of the four, because with ~5B active parameters you are bandwidth-bound, so the smaller
file wins.

**On Korean specifically.** The upstream card publishes BFCL numbers but says nothing about
Korean, so as far as we can tell these are the first public Korean measurements for this model.
Trillion Labs is a Seoul company and the model handled Korean cleanly at every tier we publish —
no Han characters, no kana, natural sentences, down to 3 bits. We think that is worth knowing.

## 🔧 Tool calling — simpler here than upstream

The upstream card serves this model through vLLM with three extra pieces:

```
--tool-call-parser cyan_glm --tool-parser-plugin <kit>/serve/glm_tool_parser.py
--reasoning-parser glm45
```

and warns that *"without the reasoning parser the model's `<think>` block lands in `content` and
answers stop parsing."*

**None of that is needed with llama.cpp.** Pass `--jinja` and the model emits standard JSON tool
calls that `/v1/chat/completions` parses directly — we got a clean `tool_calls` entry on the first
try, with reasoning landing in `reasoning_content` where it belongs. Reasoning was also short
(150 characters for a simple tool question), so you do not need a large `max_tokens` budget the
way some reasoning models require.

Upstream's own BFCL v3 results, for reference (their measurement, not ours — three runs per
checkpoint, mean ± sd):

| | Live Acc (n=1351) | multi-turn (n=800) |
|---|---|---|
| SFT base | 69.97 ± 0.99 | 27.05 ± 0.29 |
| **this model** | **73.11 ± 0.34** | **30.25 ± 0.50** |

## 🐛 The conversion bug — and why these files just work

If you tried to quantize this model yourself, you probably hit this:

```
key not found in model: deepseek2.attention.q_lora_rank
```

The model sets `q_lora_rank: null` in its config — meaning it skips the Q-side LoRA and projects
straight through `q_proj`. But `conversion/deepseek.py` only writes that key when it is *not* null:

```python
if "q_lora_rank" in hparams and hparams["q_lora_rank"] is not None:
    self.gguf_writer.add_q_lora_rank(hparams["q_lora_rank"])
```

while `src/models/deepseek2.cpp` reads it as a **required** key. So the converter succeeds, and
then nothing can load the result — not `llama-imatrix`, not `llama-quantize`, not `llama-server`.

The right value is `0`, which llama.cpp already understands to mean "no Q LoRA" — its tensor
creation branches on exactly that and builds `wq` instead of `wq_a`/`wq_b`. We confirmed the
tensors match (52× `blk.N.attn_q.weight`, zero `attn_q_a`), and that the one place asserting
`n_lora_q > 0` is the MTP graph, which this model does not have.

**We baked that key into the files at quantization time**, so you need no `--override-kv`, no
patched build, no flags. Download and run.

## 🧪 imatrix

All quants are imatrix-quantized. Corpus composition, measured:

| | |
|---|---|
| Total | 4.90 M characters |
| **Hangul** | **20.06%** |
| Han | 0.17% |

Korean OCR labels, Korean technical prose, source code, and English wikitext. `--chunks 200`.

## 🚀 Usage

```bash
hf download batiai/Gravity-30BA5B-RL-GGUF \
  --include "Gravity-30BA5B-RL-Q4_K_M.gguf" --local-dir ./gravity

./llama-server -m ./gravity/Gravity-30BA5B-RL-Q4_K_M.gguf \
  --jinja -c 32768 --port 8080
```

**Context.** The model supports 131,072 tokens and upstream notes that BFCL's long-context problems
need the full window — score drops to zero if you truncate. Size `-c` to your RAM; the KV cache at
131k is substantial.

## ⚖️ License

**Apache 2.0**, no additional conditions. Commercial use is fine.

## 📋 What is not here

- **Apple Silicon speeds** — we publish only what we measured, and we measured on x86 CPU.
- **Korean benchmark scores** — our check is a publish gate, not a benchmark. It tells you the
  model writes clean Korean down to 3 bits; it does not tell you how it ranks.

## ✨ What BatiAI did differently

| | |
|---|---|
| 🇰🇷 **Korean verified per quant** | With character counts, not a claim. |
| 🔧 **Loads with no flags** | We fixed the `q_lora_rank` gap at quantization time instead of documenting a workaround. |
| 📐 **Numbers, not adjectives** | Sizes, speeds and corpus composition all measured. |
| 🔏 **From the source** | Quantized from Trillion Labs' official weights, never a re-quant. Signed `general.author: BatiAI`. |

---

**Who we are.** [BatiAI](https://bati.ai) builds **on-device Korean AI**.
[BatiFlow](https://flow.bati.ai) runs chat, speech-to-text, document OCR and speaker diarization
entirely on a Mac. Full line: **[huggingface.co/batiai](https://huggingface.co/batiai)**
