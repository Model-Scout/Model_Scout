---
base_model:
- ermund/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
- Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B
base_model_relation: quantized
license: apache-2.0
license_link: https://huggingface.co/ermund/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic/blob/main/README.md
language:
- en
- zh
- ko
- ja
- es
- ru
pipeline_tag: image-text-to-text
library_name: llama.cpp
quantized_by: hUh63
tags:
- gguf
- q4_k_m
- imatrix
- mtp
- multi-token-prediction
- nextn
- speculative-decoding
- self-speculative-decoding
- qwen3_5
- qwen3.5
- text-generation
- image-text-to-text
- conversational
- reasoning
- distillation
- deepseek
- math
- stem
- heretic
- uncensored
- decensored
- abliterated
- unsloth
---

# DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic — Q4_K_M GGUF with built-in MTP draft head

A **Q4_K_M** GGUF quantization of
[ermund/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/ermund/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)
that keeps the model's **own multi-token prediction (MTP / NextN) head** inside the weights, so
[llama.cpp](https://github.com/ggml-org/llama.cpp) can run **speculative decoding without loading a
separate draft model**. Quantized with an importance-matrix (imatrix) calibration pass.

> This repo only performs format conversion, restoration of the built-in prediction head, and
> quantization. The decensoring and all training work belong to the upstream authors (see
> [Attribution](#attribution--license)).

## Highlights

- **No extra draft model.** The prediction head is part of this single GGUF file (the 33rd /
  NextN block, `blk.32.nextn.*`). Speculative decoding reuses the model itself as the drafter —
  there is no second model file to download or keep in memory.
- **Lossless speculation.** The head only *proposes* candidate tokens; every token is still
  verified by the main trunk before it is emitted. Enabling speculation therefore does **not**
  change the output distribution relative to running the same quantized weights without it.
- **Q4_K_M + imatrix.** ~5.38 GiB text GGUF, importance-matrix calibrated to preserve quality
  under 4-bit quantization.
- **Multimodal.** The source is `Qwen3_5ForConditionalGeneration`, so a separate f16 `mmproj`
  projector is provided for image / video input.

## Files

| File | Quant | Size | Description |
| :--- | :---- | :--- | :---------- |
| `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-MTP-Q4_K_M.gguf` | Q4_K_M | 5.38 GiB (5,780,092,352 B) | Text trunk **+ built-in MTP draft head**, imatrix-calibrated |
| `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic.mmproj-f16.gguf` | f16 | 876 MiB (918,166,240 B) | Vision projector; load it together with the text GGUF for image / video |
| `calibration.txt` | — | 527 KiB | The exact multilingual / math-STEM / code corpus used for the imatrix pass |

`general.file_type = 15` (MOSTLY_Q4_K_M), `qwen35.block_count = 33`,
`qwen35.nextn_predict_layers = 1`. The NextN block is **not** a separate file — it is 15 tensors
embedded in the text GGUF (`blk.32.nextn.{eh_proj,enorm,hnorm,shared_head_norm}` plus
`blk.32.attn_*` / `blk.32.ffn_*`).

## How to run

### llama.cpp — speculative decoding with the built-in head (recommended)

```bash
llama-cli \
  -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-MTP-Q4_K_M.gguf \
  --mmproj DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic.mmproj-f16.gguf \
  --spec-type draft-mtp \
  -c 4096 -fa on
```

`--spec-type draft-mtp` tells llama.cpp to use the **embedded** NextN block as the draft head
(`graph_mtp`). No `-md` / draft-model argument and no second file is needed.

```bash
llama-server \
  -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-MTP-Q4_K_M.gguf \
  --mmproj DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic.mmproj-f16.gguf \
  --spec-type draft-mtp -c 8192 --host 0.0.0.0 --port 8080
```

### llama.cpp — without speculation

```bash
llama-cli -m DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-MTP-Q4_K_M.gguf -c 4096 -fa on
```

Ollama / LM Studio / any llama.cpp-based runtime can load the GGUF directly. The NextN block is
simply inert without `--spec-type draft-mtp`, so the model still works normally. Check whether your
build exposes that flag; it is available in recent 0.9.x-dev builds.

### Builds that do not expose `--spec-type`

You can still use the plain (non-speculative) command above; the file is a standard Q4_K_M GGUF.
Only the optional speed-up is unavailable.

## Why there is no separate draft model

Classic speculative decoding pairs a large *target* model with a small *draft* model and verifies
the draft's guesses. MTP takes a different route: during training, the model learns extra
**prediction heads (NextN layers)** that read its own hidden states and predict several future
tokens at once. At inference time these heads live **inside the same checkpoint**, so the drafter
and the verifier are literally the same weights.

Practical consequences:

- No independent draft model file, no second set of weights in memory, no vocabulary/tokenizer
  mismatch between drafter and verifier.
- The head proposes multiple tokens per step; the trunk verifies them in one pass and keeps the
  longest accepted prefix. Rejected guesses are discarded, so the sampled distribution is
  identical to ordinary autoregressive decoding (lossless).
- Measured on 8 CPU cores with Q4_K_M: **9.6 tok/s** with `--spec-type draft-mtp` vs **7.3 tok/s**
  without (~**+30 %**), draft acceptance **57.6 %** (19 / 33), mean accepted run **2.73** tokens.
  Gains are larger on GPU, where the trunk is not the bottleneck. Acceptance varies with prompt
  style — code and structured math draft better than free prose.

### Why the head had to be restored

The upstream [Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B)
checkpoint ships 775 tensors, 15 of which are the MTP block (`mtp.fc`,
`mtp.pre_fc_norm_hidden`, `mtp.pre_fc_norm_embedding`, `mtp.norm`, and the 11 tensors of
`mtp.layers.0.*`). The decensored ermund checkpoint has 760 — exactly those 15 MTP tensors are
missing — even though its `config.json` still declares `mtp_num_hidden_layers: 1`.

The MTP block is a **draft-only** head: it never runs in the main forward pass, so the decensoring
ablation (which touched only trunk layers 9–24) never modified it. The upstream MTP weights are
therefore still numerically valid for this trunk and were transplanted as-is, after a one-to-one
shape/dtype check. No retraining was involved.

| MTP tensor (HF) | Shape | GGUF destination |
| :--- | :---- | :--------------- |
| `mtp.fc.weight` | 4096 × 8192 | `blk.32.nextn.eh_proj.weight` |
| `mtp.pre_fc_norm_hidden.weight` | 4096 | `blk.32.nextn.hnorm.weight` |
| `mtp.pre_fc_norm_embedding.weight` | 4096 | `blk.32.nextn.enorm.weight` |
| `mtp.norm.weight` | 4096 | `blk.32.nextn.shared_head_norm.weight` |
| `mtp.layers.0.self_attn.{q,k,v,o}_proj.weight` | 8192×4096 / 1024×4096 / 1024×4096 / 4096×4096 | `blk.32.attn_{q,k,v,output}.weight` |
| `mtp.layers.0.self_attn.{q,k}_norm.weight` | 256 | `blk.32.attn_{q,k}_norm.weight` |
| `mtp.layers.0.input_layernorm.weight` | 4096 | `blk.32.attn_norm.weight` |
| `mtp.layers.0.post_attention_layernorm.weight` | 4096 | `blk.32.post_attention_norm.weight` |
| `mtp.layers.0.mlp.{gate,up,down}_proj.weight` | 12288×4096 / 12288×4096 / 4096×12288 | `blk.32.ffn_{gate,up,down}.weight` |

## Quantization recipe

Built with [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) master (`b1-281e7da`,
0.9.0-dev), CPU-only, 8 cores / 16 GiB RAM, no GPU. Steps are reproducible:

```bash
# 0) toolchain (Debian 12). The checkpoint needs transformers 5.20.2 for Qwen3_5Tokenizer,
#    while llama.cpp pins 4.57.6 — keep 5.20.2 isolated on PYTHONPATH.
apt-get install -y build-essential cmake ninja-build
pip install 'torch==2.11.0' 'numpy~=2.2.6' 'gguf>=0.1.0' 'sentencepiece' 'protobuf<5' \
  --extra-index-url https://download.pytorch.org/whl/cpu
pip install --target /tmp/tf5 'transformers==5.20.2'

git clone --depth 1 https://github.com/ggml-org/llama.cpp.git && cd llama.cpp
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=OFF -DGGML_VULKAN=OFF \
      -DGGML_HIP=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_CURL=OFF -DGGML_NATIVE=ON
cmake --build build -j 8 --target llama-quantize llama-imatrix llama-cli llama-mtmd-cli

# 1) HF checkpoint that contains the 15 mtp.* tensors (restored from the upstream checkpoint),
#    with model.safetensors.index.json patched accordingly.

# 2) BF16 text GGUF — do NOT pass --no-mtp / --no-nextn
PYTHONPATH=/tmp/tf5 python3 convert_hf_to_gguf.py model_mtp \
  --outfile out/model-BF16.gguf --outtype bf16

# 3) vision projector
PYTHONPATH=/tmp/tf5 python3 convert_hf_to_gguf.py model_mtp --mmproj \
  --outfile out/model.mmproj-f16.gguf --outtype f16

# 4) importance matrix (multilingual + math/STEM + code corpus, 16 chunks)
llama-imatrix -m out/model-BF16.gguf -f calibration.txt -o out/imatrix.gguf \
  -c 512 -b 512 --chunks 16 --output-frequency 4 --no-ppl -t 8

# 5) Q4_K_M
llama-quantize --imatrix out/imatrix.gguf out/model-BF16.gguf \
  out/model-MTP-Q4_K_M.gguf Q4_K_M 8
```

Notes:

- **`--spec-type draft-mtp` is the switch that activates the built-in head.** Without it llama.cpp
  builds the trunk graph only and the NextN block is loaded but never executed.
- **Do not override `block_count = 33` down to 32.** `qwen35.attention.recurrent_layers` has
  length 33 to match; changing one without the other fails the loader.
- **The BF16 intermediate (18.4 GiB) is not uploaded** — only the two final GGUF files are here.
- `quantize.imatrix.chunks_count = 16`, `quantize.imatrix.entries_count = 248`.

## Attribution & license

Format conversion, restoration of the built-in prediction head, and quantization only. All weights
and training contributions belong to the original chain:

1. **Qwen / Alibaba Qwen team** — [Qwen3.5-9B](https://huggingface.co/Qwen) base family.
2. **Jackrong** — [DeepSeek-V4-Pro-Qwen3.5-9B](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B):
   reasoning fine-tune distilled from **DeepSeek-V4-Pro (Max Effect)** on ~250 K math / STEM
   samples (SFT + light GSPO RL), built with [Unsloth](https://unsloth.ai). **The MTP head in this
   repo comes from this checkpoint.**
3. **ermund** — decensored / abliterated variant via [Heretic](https://heretic-project.org)
   v2.0.0.dev0, Arbitrary-Rank Ablation on layers 9–24. Direct source of the trunk and vision
   weights.
4. **hUh63** — MTP restoration, GGUF conversion, Q4_K_M quantization and this repo.

Acknowledgements carried over from the upstream cards: **Kyle Hessling** (hardware / training /
evaluation), **DeepSeek** (teacher model), **Unsloth** (fine-tuning tooling), and the open-source
**vLLM** / **llama.cpp** communities.

**License:** `apache-2.0`, inherited from the source models.

## Caveats

> ⚠️ The source is an **uncensored / decensored / abliterated** community experiment. Its safety
> alignment was deliberately weakened. Quantization and MTP restoration do not change that. Use
> responsibly, verify high-stakes outputs, and follow local rules.

- "Lossless" above refers specifically to **speculative decoding**: enabling `--spec-type draft-mtp`
  does not change the output distribution of *these quantized weights*. Q4_K_M quantization itself
  is lossy relative to the BF16 / FP16 source — that is a separate, unavoidable trade-off.
- The MTP head was trained on the *censored* parent model. It still drafts effectively for this
  trunk (57.6 % acceptance measured), and because the trunk verifies every token, decensoring
  behaviour is unchanged.
- Acceptance numbers were measured on CPU with short generations; results vary with prompt style,
  context length and sampler settings.
- Benchmark numbers on the upstream cards were measured on the **original high-precision models**,
  not on this Q4_K_M build.
