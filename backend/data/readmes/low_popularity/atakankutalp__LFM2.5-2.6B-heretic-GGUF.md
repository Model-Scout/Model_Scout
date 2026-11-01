---
library_name: gguf
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
base_model: atakankutalp/LFM2.5-2.6B-heretic
quantized_by: atakankutalp
tags:
- liquid
- lfm2.5
- gguf
- llama.cpp
- heretic
- uncensored
- decensored
- abliterated
- reproducible
---

# This is a decensored version of [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B), made using [Heretic](https://heretic-project.org) v1.4.0

GGUF quantizations of the abliterated checkpoint
[`atakankutalp/LFM2.5-2.6B-heretic`](https://huggingface.co/atakankutalp/LFM2.5-2.6B-heretic).

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0232 | 0 *(by definition)* |
| **Refusals** | 6/100 | 94/100 |

## Quantizations

| File | Type | BPW | Size | Use case |
| :--- | :---: | :---: | ---: | :--- |
| [`LFM2.5-2.6B-heretic-F16.gguf`](LFM2.5-2.6B-heretic-F16.gguf) | `F16` | 16.00 | 5,403.2 MB | Tam hassasiyet. Referans; kalite kaybı yok. |
| [`LFM2.5-2.6B-heretic-Q8_0.gguf`](LFM2.5-2.6B-heretic-Q8_0.gguf) | `Q8_0` | 8.50 | 2,874.8 MB | Kayıp neredeyse yok. VRAM bol olanlar için. |
| [`LFM2.5-2.6B-heretic-Q6_K.gguf`](LFM2.5-2.6B-heretic-Q6_K.gguf) | `Q6_K` | 6.56 | 2,221.6 MB | Yüksek kalite / iyi boyut dengesi. |
| [`LFM2.5-2.6B-heretic-Q5_K_M.gguf`](LFM2.5-2.6B-heretic-Q5_K_M.gguf) | `Q5_K_M` | 5.73 | 1,939.7 MB | Dengeli. 4 GB sınıfı cihazlara uygun. |
| [`LFM2.5-2.6B-heretic-Q4_K_M.gguf`](LFM2.5-2.6B-heretic-Q4_K_M.gguf) | `Q4_K_M` | 4.94 | 1,674.5 MB | Önerilen varsayılan. En yaygın kullanım. |
| [`LFM2.5-2.6B-heretic-Q4_0.gguf`](LFM2.5-2.6B-heretic-Q4_0.gguf) | `Q4_0` | 4.70 | 1,593.9 MB | Küçük + hızlı. Uyumlu donanımlar için. |

## SHA-256

- `LFM2.5-2.6B-heretic-F16.gguf` → `aa3f5f4fc2b89f72dcb945eda13ae568153be0a138cbe3d4c28dd4fdfe9cd94e`
- `LFM2.5-2.6B-heretic-Q8_0.gguf` → `199e1cc2780b51dfec35a30939aad712f722f123ea544b23fe4646ae67c7540d`
- `LFM2.5-2.6B-heretic-Q6_K.gguf` → `64ce6cce9f184a98e182afc1360f5099664c6c98453b34eb34a15b1fe6f710c5`
- `LFM2.5-2.6B-heretic-Q5_K_M.gguf` → `9e765db22fb92fdb1b2275987759714f2490e6f5fd1e9f0520ad751db48c93cb`
- `LFM2.5-2.6B-heretic-Q4_K_M.gguf` → `c1a8e875880cbb9262d37139a7f98b45dd7e41eec19c4ae819e6c782ddf61006`
- `LFM2.5-2.6B-heretic-Q4_0.gguf` → `8d19413eafe734db9e4f08d0b27d0c614a95203b68345c2764610da3165029b3`

## How to run

[llama.cpp](https://github.com/ggml-org/llama.cpp):

```bash
llama-cli -hf atakankutalp/LFM2.5-2.6B-heretic-GGUF:Q4_K_M --conversation --temp 0.1 --top-k 50 --repeat-penalty 1.1
```

OpenAI-compatible server:

```bash
llama-server -hf atakankutalp/LFM2.5-2.6B-heretic-GGUF:Q4_K_M --host 0.0.0.0 --port 8080
```

Also works with [LM Studio](https://lmstudio.ai/), [Ollama](https://ollama.com/)
(convert the GGUF) and any other llama.cpp-compatible runtime.

## Reproducibility

| Step | Detail |
| :--- | :----- |
| **Abliteration** | Heretic v1.4.0, 200 trials, seed 3407, trial index 93 |
| **Source checkpoint** | [`atakankutalp/LFM2.5-2.6B-heretic`](https://huggingface.co/atakankutalp/LFM2.5-2.6B-heretic) |
| **Conversion** | `convert_hf_to_gguf.py --outtype f16` (llama.cpp `b10964`, arch `LFM2`) |
| **Quantization** | `llama-quantize` from the same llama.cpp build |
| **Verified** | all 6 files load and generate with `llama-cli`; sizes match the upstream `LiquidAI/LFM2.5-2.6B-GGUF` set |

> [!WARNING]
> **These weight files have been modified.**
>
> The source checkpoint is `LiquidAI/LFM2.5-2.6B` after **directional ablation
> ("abliteration")**, performed with [Heretic](https://github.com/p-e-w/heretic).
> A refusal direction was projected out of every attention out-projection and
> MLP down-projection across all 30 transformer layers, then merged into the
> base weights.
>
> **The model's safety alignment has been deliberately reduced.** Refusals on
> sensitive prompts are substantially lower than the original checkpoint, and
> outputs are **not** safety-filtered. Use accordingly.

## Attribution & license

- Base model: [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
  © Liquid AI, Inc.
- Abliteration tool: [p-e-w/heretic](https://github.com/p-e-w/heretic)
  © Philipp Emanuel Weidmann, AGPL-3.0
- Quantization: [llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT)

This derivative is distributed under the **LFM Open License v1.0** — see the
[LICENSE](./LICENSE) file, required by Section 4(a). Modified files carry the
notice above as required by Section 4(b); original copyright, trademark and
attribution notices are retained per Section 4(c).

## Provenance

Weights derive from the safetensors checkpoint, itself produced by Heretic from
`LiquidAI/LFM2.5-2.6B`. Full ablation parameters and settings are documented in
the source repository's README.
